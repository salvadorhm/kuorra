import config

class View:

    def __init__(self):
        pass

    def GET(self, id_person):
        result = config.model.get_persons(id_person)
        return config.render.view(result)
