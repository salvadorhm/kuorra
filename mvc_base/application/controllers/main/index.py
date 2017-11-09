import config

class Index:

    def GET(self):
        #result = config.model.get_all_table_name()
        #return config.render.index(result)
        return config.render.index()
