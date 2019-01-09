import application.controllers.logs.config as config
import app
import datetime


class Index:

    def __init__(self):
        pass

    def GET(self):
        if app.session.loggedin is True:
            # get now time
            now = datetime.datetime.now()
            now_str = str(now).split('.')[0]

            expires = config.check_secure_val(app.session.expires)

            print "now    : " , now_str
            print "expires: " , expires

            if (now_str > expires): # compare now with time login
                raise config.web.seeother('/logout')

            # session_user = app.session.user
            session_privilege = app.session.privilege
            if session_privilege == 0:
                return self.GET_INDEX()
            elif session_privilege == 1:
                raise config.web.seeother('/')
        else:
            raise config.web.seeother('/login')

    @staticmethod
    def GET_INDEX():
        result = config.model.get_all_logs().list()
        for row in result:
            row.user = config.make_secure_val(str(row.user))
        return config.render.index(result)