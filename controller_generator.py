import web
import os


class Controller_generator:

    db_host = ''
    db_name = ''
    db_user = ''
    db_pw = ''

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
            print "Error en describre_tables {}".format(e.message)
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
            print "Error en get_fields {}".format(e.message)
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

            fields = ""
            for field in self.get_fields(table_name)[1:]:
                fields += field[0] + ','
            fields = fields[:-1]

            first_field = fields[0]

            values = ""
            for field in self.get_fields(table_name)[1:]:
                values += field[0] + '=' + field[0] + ',\n'
            values = values[:-2]

            field_all = ""
            for field in self.get_fields(table_name):
                field_all += field[0] + ','
            field_all = field_all[:-1]

            value_all = ""
            for field in self.get_fields(table_name):
                value_all += field[0] + '=' + field[0] + ',\n'
            value_all = value_all[:-2]

            script_path = os.path.abspath(__file__)
            script_dir = os.path.split(script_path)[0]
            rel_path = "controllers"
            new_file_path = os.path.join(script_dir, table_name)
            abs_file_path = os.path.join(script_dir, rel_path)

            os.mkdir(os.path.expanduser(table_name))
            file = open(table_name + '/__init__.py', 'w')
            file.write("")
            file.close()

            #config.py

            index_file = open(abs_file_path + '/config.py','r')
            plantilla = ''
            for line in index_file:
                plantilla += line

            plantilla = plantilla.replace('table_name', table_name)
            plantilla = plantilla.replace('primary_key', primary_key)
            plantilla = plantilla.replace('first_field', first_field)
            plantilla = plantilla.replace('fields', fields)
            plantilla = plantilla.replace('values', values)
            plantilla = plantilla.replace('field_all', field_all)
            plantilla = plantilla.replace('value_all', value_all)

            view_master = plantilla

            file = open(table_name + '/config.py', 'w')
            file.write(view_master)
            file.close()

            #url.md

            index_file = open(abs_file_path + '/url.md','r')
            plantilla = ''
            for line in index_file:
                plantilla += line

            plantilla = plantilla.replace('table_name', table_name)

            view_master = plantilla

            file = open(table_name + '/url.md', 'w')
            file.write(view_master)
            file.close()

            #delete.py

            index_file = open(abs_file_path + '/delete.py','r')
            plantilla = ''
            for line in index_file:
                plantilla += line

            plantilla = plantilla.replace('table_name', table_name)
            plantilla = plantilla.replace('primary_key', primary_key)
            plantilla = plantilla.replace('first_field', first_field)
            plantilla = plantilla.replace('fields', fields)
            plantilla = plantilla.replace('values', values)
            plantilla = plantilla.replace('field_all', field_all)
            plantilla = plantilla.replace('value_all', value_all)

            view_master = plantilla

            file = open(table_name + '/delete.py', 'w')
            file.write(view_master)
            file.close()

            #index.py

            index_file = open(abs_file_path + '/index.py', 'r')
            plantilla = ''
            for line in index_file:
                plantilla += line

            plantilla = plantilla.replace('table_name', table_name)
            plantilla = plantilla.replace('primary_key', primary_key)
            plantilla = plantilla.replace('first_field', first_field)
            plantilla = plantilla.replace('fields', fields)
            plantilla = plantilla.replace('values', values)
            plantilla = plantilla.replace('field_all', field_all)
            plantilla = plantilla.replace('value_all', value_all)

            view_master = plantilla

            file = open(table_name + '/index.py', 'w')
            file.write(view_master)
            file.close()

            #view.py

            index_file = open(abs_file_path + '/view.py', 'r')
            plantilla = ''
            for line in index_file:
                plantilla += line

            plantilla = plantilla.replace('table_name', table_name)
            plantilla = plantilla.replace('primary_key', primary_key)
            plantilla = plantilla.replace('first_field', first_field)
            plantilla = plantilla.replace('fields', fields)
            plantilla = plantilla.replace('values', values)
            plantilla = plantilla.replace('field_all', field_all)
            plantilla = plantilla.replace('value_all', value_all)

            view_master = plantilla

            file = open(table_name + '/view.py', 'w')
            file.write(view_master)
            file.close()

            #edit.py
            edit_file = open(abs_file_path + '/edit.py', 'r')
            field_file = "form['field'],"

            plantilla = "form['" + primary_key + "'],"
            for field in self.get_fields(table_name)[1:]:
                plantilla += field_file
                plantilla = plantilla.replace('field', field[0])

            edit = ''
            for t in edit_file:
                edit += t

            edit = edit.replace('fields', plantilla)

            edit = edit.replace('table_name', table_name)
            edit = edit.replace('primary_key', primary_key)
            edit = edit.replace('first_field', first_field)
            edit = edit.replace('fields', fields)
            edit = edit.replace('values', values)
            edit = edit.replace('field_all', field_all)
            edit = edit.replace('value_all', value_all)

            file = open(table_name + '/edit.py', 'w')
            file.write(edit)
            file.close()

            #insert.py
            insert_file = open(abs_file_path + '/insert.py', 'r')
            field_file = "form['field'],"

            plantilla = ''
            for field in self.get_fields(table_name)[1:]:
                plantilla += field_file
                plantilla = plantilla.replace('field', field[0])

            insert = ''
            for t in insert_file:
                insert += t

            insert = insert.replace('fields', plantilla)
            insert = insert.replace('table_name', table_name)
            insert = insert.replace('primary_key', primary_key)
            insert = insert.replace('first_field', first_field)
            insert = insert.replace('fields', fields)
            insert = insert.replace('values', values)
            insert = insert.replace('field_all', field_all)
            insert = insert.replace('value_all', value_all)

            file = open(table_name + '/insert.py', 'w')
            file.write(insert)
            file.close()

        except Exception as e:
            print e.args
            print "Error en supercool {}".format(e.message)
            print "Error en supercool {}".format(e)

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
