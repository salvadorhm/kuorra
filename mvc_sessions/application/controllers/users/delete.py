"""
    Class for delete users
"""
from . import config
import app


class Delete:

    def __init__(self):
        pass

    def GET(self, username, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege # get the session_privilege
            if session_privilege == 0: # admin user
                return self.GET_DELETE(username) # call GET_DELETE function
            elif privsession_privilegeilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    def POST(self, username, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege
            if session_privilege == 0: # admin user
                return self.POST_DELETE(username) # call POST_DELETE function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    @staticmethod
    def GET_DELETE(username, **k):
        message = None # Error message
        username = config.check_secure_val(str(username)) # HMAC user validate
        result = config.model.get_users(username) # search for the user
        result.username = config.make_secure_val(str(result.username)) # apply HMAC for username
        return config.render.delete(result, message) # render delete.html with user data


    @staticmethod
    def POST_DELETE(username, **k):
        form = config.web.input() # get form data
        username = config.check_secure_val(str(form['username'])) # HMAC user validate
        session_username = app.session.username # get session_username
        if username != session_username: # compare username with sesion_username
            result = config.model.delete_users(username) # call model delelete
            if result is None: # delete error
                message = "El registro no se puede borrar" # Error messate
                result = config.model.get_users(username) # get username data
                result.username = config.make_secure_val(str(result.username)) # apply HMAC to username
                return config.render.delete(result, message) # render delete.html again
            else: # user delete correctly
                raise config.web.seeother('/users') # render index.html
        else: #  username and session_username its the same
            message = "No se puede elimiar el usuario activo" # Error message
            result = config.model.get_users(username) # get username data
            result.username = config.make_secure_val(str(result.username)) # apply HMAC to username
            return config.render.delete(result, message) # render delete.html
