import config


class Insert():

    def __init__(self):
        pass

    def GET(self):
        return config.render.insert()

    def POST(self):
        form = config.web.input()

        config.model.insert_table_name(
            fields
        )
        raise config.web.seeother('/table_name')
