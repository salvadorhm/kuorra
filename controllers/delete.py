import config


class Delete:

    def GET(self, primary_key, message=None):
        primary_key = config.check_secure_val(str(primary_key))
        result = config.model.get_table_name(int(primary_key))
        result.primary_key = config.make_secure_val(str(result.primary_key))
        return config.render.delete(result, message)

    def POST(self, primary_key, message=None):
        form = config.web.input()
        form['primary_key'] = config.check_secure_val(str(form['primary_key']))
        res = config.model.delete_table_name(form['primary_key'])
        if res is None:
            message = "El registro no se puede borrar"
            primary_key = config.check_secure_val(str(primary_key))
            result = config.model.get_table_name(int(primary_key))
            result.primary_key = config.make_secure_val(str(result.primary_key))
            return config.render.delete(result, message)
        else:
            raise config.web.seeother('/table_name')
