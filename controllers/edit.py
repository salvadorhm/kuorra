import config


class Edit:

    def GET(self, primary_key, message=None):
        primary_key = config.check_secure_val(str(primary_key))
        result = config.model.get_table_name(int(primary_key))
        result.primary_key = config.make_secure_val(str(result.primary_key))
        return config.render.edit(result, message)

    def POST(self, primary_key, message=None):
        form = config.web.input()
        form['primary_key'] = config.check_secure_val(str(form['primary_key']))
        res = config.model.edit_table_name(
            fields
        )
        if res == None:
            primary_key = config.check_secure_val(str(primary_key))
            result = config.model.get_table_name(int(primary_key))
            result.primary_key = config.make_secure_val(str(result.primary_key))
            message = "Error al editar el registro"
            return config.render.edit(result, message)
        else:
            raise config.web.seeother('/table_name')
