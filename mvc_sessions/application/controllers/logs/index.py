import config
import app


class Index:

    def __init__(self):
        pass

    def GET(self):
        if app.session.loggedin is True:
            # username = app.session.username
            privilege = app.session.privilege
            if privilege == 0:
                return self.GET_INDEX()
            elif privilege == 1:
                raise config.web.seeother('/guess')
        else:
            raise config.web.seeother('/login')

    def GET_INDEX(self):
        result = config.model.get_all_logs().list()
        for row in result:
            row.username = config.make_secure_val(str(row.username))
        return config.render.index(result)