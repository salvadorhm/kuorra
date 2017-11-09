import config

class Delete:

    def GET(self, id_person):
        persons = config.form_persons()
        result = config.model.get_persons(id_person)
        persons.fill(result)
        return config.render.delete(persons)

    def POST(self, id_person):
        config.model.delete_persons(id_person)
        raise config.web.seeother('/')
