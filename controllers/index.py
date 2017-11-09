import config


class Index:

    def GET(self):
        result = config.model.get_all_table_name().list()
        for row in result:
            row.primary_key = config.make_secure_val(str(row.primary_key))
        return config.render.index(result)
