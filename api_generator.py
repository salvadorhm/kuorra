import web
import os


class Api_generator:

    db_host = 'localhost'
    db_name = 'acme_store'
    db_user = 'root'
    db_pw = 'toor'

    table_name = ''

    db = web.database(
            dbn='mysql',
            host=db_host,
            db=db_name,
            user=db_user,
            pw=db_pw
            )

    def conectar(self):
        try:
            new_db = web.database(
            dbn='mysql',
            host=self.db_host,
            db=self.db_name,
            user=self.db_user,
            pw=self.db_pw
            )
            self.db = new_db
            print 'Conectado'
        except Exception as e:
            print e.args
            print "Error en conexion {}".format(e.message)

    def get_tables(self):
        try:
            return self.db.query('show tables')
        except Exception as e:
            print e.args
            print "Error en get_tables {}".format(e.message)
            return None

    def describre_tables(self, table):
        try:
            sql = 'describe {}'.format(table)
            return self.db.query(sql, vars=locals())
        except Exception as e:
            print e.args
            print "Error  describe_tables {}".format(e.message)
            return None

    def get_fields(self, table):
        try:
            result = self.describre_tables(table)
            fields = []
            for i in result:
                r = [i.Field, i.Key]
                fields.append(r)
            return fields
        except Exception as e:
            print e.args
            print "Error get_fields {}".format(e.message)
            return None

    def get_primary_key(self, fields):
        primary_key = ''
        for field in fields:
            try:
                if field[1] == 'PRI':
                    primary_key = field[0]
                    exit
            except:
                primary_key = None
        return primary_key

    def super_cool(self, table_name):
        try:
            primary_key = self.get_primary_key(self.get_fields(table_name))

            script_path = os.path.abspath(__file__)
            script_dir = os.path.split(script_path)[0]
            rel_path = "plugin"
            abs_file_path = os.path.join(script_dir, rel_path)

            file = open(abs_file_path + '/api_master_cool.py', 'r')
            plantilla = ''
            for line in file:
                plantilla += line

            field_all = ""
            for field in self.get_fields(table_name):
                field_all += field[0] + ','
            field_all = field_all[:-1]

            field_none = ""
            for field in self.get_fields(table_name):
                field_none += '            ' + field[0] + '=None,\n'
            field_none = field_none[:-1]

            field_user_data = ""
            for field in self.get_fields(table_name):
                field_user_data += '            ' + field[0] + '=user_data.' + field[0] + '\r'
                field_user_data += '\n'
            field_user_data = field_user_data[:-1]

            fields = ""
            for field in self.get_fields(table_name)[1:]:
                fields += field[0] + ','
            fields = fields[:-1]

            plantilla = plantilla.replace('table_name', table_name)
            plantilla = plantilla.replace('primary_key', primary_key)
            plantilla = plantilla.replace('fields', fields)
            plantilla = plantilla.replace('field_all', field_all)
            plantilla = plantilla.replace('field_none', field_none)
            plantilla = plantilla.replace('field_user_data', field_user_data)

            api = plantilla
            self.new_folder(table_name)
            file = open(table_name+'/api_' + table_name + '.py', 'w')
            file.write(api)
            file.close()

            config = '''import web
import application.models.model_table_name
model = application.models.model_table_name
'''
            config = config.replace('table_name', table_name)

            file_config = open(table_name + '/config.py', 'w')
            file_config.write(config)
            file.close()

            #Api config

            api_md = "'/api_table_name/?', 'application.api.table_name.api_table_name.Api_table_name',"
            api_md = api_md.replace('table_name', table_name)
            file_api = open(table_name+'/api_' + table_name + '.md', 'w')
            file_api.write(api_md)
            file.close()

            file_init = open(table_name + '/__init__.py', 'w')
            file_init.write('')
            file_init.close()

        except Exception as e:
            print e.args
            print e.message
            print "Error en supercool {}".format(e.message)

    def new_folder(self, table_name):
        try:
            os.makedirs(table_name)
        except Exception as e:
            print "ERROR create dir {}".format(e.message)

    def generate(self):
        try:
            for i in self.get_tables():
                m = str(i.values())
                self.super_cool(m[3:-2])
        except Exception as e:
            print "Error en generate {}".format(e.message)

    def generate_one(self, table_name):
        try:
            self.super_cool(table_name)
        except Exception as e:
            print "Error al generar {}".format(e.message)
