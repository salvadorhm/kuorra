import application.controllers.logs.config as config
import app
import datetime


class View:
    
    def __init__(self):
        pass

    def GET(self, user):
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
                return self.GET_VIEW(user)
            elif session_privilege == 1:
                raise config.web.seeother('/')
        else:
            raise config.web.seeother('/login')

    @staticmethod
    def GET_VIEW(user):
        user = config.check_secure_val(str(user))
        result = config.model_users.get_users(user)
        print result
        return config.render.view(result)
