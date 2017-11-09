import config

class Insert:

    def GET(self):
        persons = config.form_persons()
        return config.render.insert(persons)

    def POST(self):
        persons = config.form_persons()
        if persons.validates():
            config.model.insert_persons(**persons.d)
            raise config.web.seeother('/')
        else:
            return config.render.insert(persons)
