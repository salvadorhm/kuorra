import config

class View:

    def GET(self, id_person):
        result = config.model.get_persons(id_person)
        return config.render.view(result)
