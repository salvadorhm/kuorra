import application.controllers.users.config  as config
import app
import datetime


class View:
    def __init__(self):
        pass

    def GET(self, user):
        if app.session.loggedin is True: # validate if the user is logged
            # get now time
            now = datetime.datetime.now()
            now_str = str(now).split('.')[0]

            expires = config.check_secure_val(app.session.expires)

            print "now    : " , now_str
            print "expires: " , expires

            if (now_str > expires): # compare now with time login
                raise config.web.seeother('/logout')

            # session_user = app.session.user
            session_privilege = app.session.privilege # get the session_privilege
            if session_privilege == 0: # admin user
                return self.GET_VIEW(user) # call GET_VIEW() function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    @staticmethod
    def GET_VIEW(user):
        user = config.check_secure_val(str(user)) # HMAC username validate
        result = config.model.get_users(user)  # search for the user data
        return config.render.view(result) # render view.html with user data
