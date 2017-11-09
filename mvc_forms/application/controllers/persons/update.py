import config

class Update:

    def GET(self, id_person):
        persons = config.form_persons()
        result = config.model.get_persons(id_person)
        persons.fill(result)
        return config.render.update(persons)

    def POST(self, id_person):
        persons = config.form_persons()
        if persons.validates():
            config.model.update_persons(**persons.d)
            raise config.web.seeother('/')
        else:
            return config.render.update(persons)
