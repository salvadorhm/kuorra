import web
import config
import json


class Api_table_name:
    def get(self, primary_key):
        try:
            # http://0.0.0.0:8080/api_table_name?user_hash=12345&action=get
            if primary_key is None:
                result = config.model.get_all_table_name()
                table_name_json = []
                for row in result:
                    tmp = dict(row)
                    table_name_json.append(tmp)
                web.header('Content-Type', 'application/json')
                return json.dumps(table_name_json)
            else:
                # http://http://0.0.0.0:8080/api_table_name?user_hash=12345&action=get&primary_key=1
                result = config.model.get_table_name(int(primary_key))
                table_name_json = []
                table_name_json.append(dict(result))
                web.header('Content-Type', 'application/json')
                return json.dumps(table_name_json)
        except Exception as e:
            print "GET Error {}".format(e.args)
            table_name_json = '[]'
            web.header('Content-Type', 'application/json')
            return json.dumps(table_name_json)

# https://0.0.0.0:8080/api_table_name?user_hash=12345&action=put&primary_key=1&product=nuevo&description=nueva&stock=10&purchase_price=1&price_sale=3&product_image=0
    def put(self, fields):
        try:
            config.model.insert_table_name(fields)
            table_name_json = '[{200}]'
            web.header('Content-Type', 'application/json')
            return json.dumps(table_name_json)
        except Exception as e:
            print "PUT Error {}".format(e.args)
            return None

# http://0.0.0.0:8080/api_table_name?user_hash=12345&action=get&primary_key=1
    def delete(self, primary_key):
        try:
            config.model.delete_table_name(primary_key)
            table_name_json = '[{200}]'
            web.header('Content-Type', 'application/json')
            return json.dumps(table_name_json)
        except Exception as e:
            print "DELETE Error {}".format(e.args)
            return None

# http://0.0.0.0:8080/api_table_name?user_hash=12345&action=update&primary_key=1&product=nuevo&description=nueva&stock=10&purchase_price=1&price_sale=3&product_image=default.jpg
    def update(self, primary_key, fields):
        try:
            config.model.edit_table_name(field_all)
            table_name_json = '[{200}]'
            web.header('Content-Type', 'application/json')
            return json.dumps(table_name_json)
        except Exception as e:
            print "GET Error {}".format(e.args)
            table_name_json = '[]'
            web.header('Content-Type', 'application/json')
            return json.dumps(table_name_json)

    def GET(self):
        user_data = web.input(
            user_hash=None,
            action=None,
field_none
        )
        try:
            user_hash = user_data.user_hash  # user validation
            action = user_data.action  # action GET, PUT, DELETE, UPDATE
field_user_data
            # user_hash
            if user_hash == '12345':
                if action is None:
                    raise web.seeother('/404')
                elif action == 'get':
                    return self.get(primary_key)
                elif action == 'put':
                    return self.put(fields)
                elif action == 'delete':
                    return self.delete(primary_key)
                elif action == 'update':
                    return self.update(primary_key, fields)
            else:
                raise web.seeother('/404')
        except Exception as e:
            print "WEBSERVICE Error {}".format(e.args)
            raise web.seeother('/404')
