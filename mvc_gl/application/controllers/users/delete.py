import application.controllers.users.config  as config
import app
import datetime


class Delete:

    def __init__(self):
        pass

    def GET(self, user, **k):
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
                return self.GET_DELETE(user) # call GET_DELETE function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    def POST(self, user, **k):
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
            session_privilege = app.session.privilege
            if session_privilege == 0: # admin user
                return self.POST_DELETE(user) # call POST_DELETE function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    @staticmethod
    def GET_DELETE(user, **k):
        message = None # Error message
        user = config.check_secure_val(str(user)) # HMAC user validate
        result = config.model.get_users(user) # search for the user
        result.user = config.make_secure_val(str(result.user)) # apply HMAC for username
        return config.render.delete(result, message) # render delete.html with user data


    @staticmethod
    def POST_DELETE(user, **k):
        form = config.web.input() # get form data
        user = config.check_secure_val(str(form['user'])) # HMAC user validate
        print "User " + str(user)
        session_user = app.session.user # get session_username
        if user != session_user: # compare username with sesion_username
            result = config.model.delete_users(user) # call model delelete
            print "Result delete " + str(result)
            if result is None: # delete error
                message = "The row can't be deleted!!" # Error messate
                result = config.model.get_users(user) # get username data
                result.user = config.make_secure_val(str(result.user)) # apply HMAC to username
                return config.render.delete(result, message) # render delete.html again
            else: # user delete correctly
                raise config.web.seeother('/users') # render index.html
        else: #  username and session_username its the same
            message = "The active user can't be deleted!!" # Error message
            result = config.model.get_users(user) # get username data
            result.user = config.make_secure_val(str(result.user)) # apply HMAC to username
            return config.render.delete(result, message) # render delete.html
