"""
    Class for update users
"""
from . import config
import hashlib
import app


class Edit:

    def __init__(self):
        pass

    def GET(self, username, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege # get the session_privilege
            if session_privilege == 0: # admin user
                return self.GET_EDIT(username) # call GET_EDIT function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    def POST(self, username, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege # get the session_privilege
            if session_privilege == 0: # admin user
                return self.POST_EDIT(username) # call POST_EDIT function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    @staticmethod
    def GET_EDIT(username, **k):
        message = None # Error message
        username = config.check_secure_val(str(username)) # HMAC user validate
        result = config.model.get_users(username) # search for the user
        result.username = config.make_secure_val(str(result.username)) # apply HMAC for username
        return config.render.edit(result, message) # render edit.html
    
    @staticmethod
    def POST_EDIT(username, **k):
        form = config.web.input() # get form data
        username = config.check_secure_val(str(username)) # HMAC user validate
        user = config.model.get_users(username)  # search for the user
        pwd = user.password # get database user password

        if pwd == form.password: # compare the database user password with form new password
            pwdhash = pwd # its the same password
        else: # has a new password
            pwdhash = hashlib.md5(form.password + config.secret_key).hexdigest() # encrypt the new password

        user_hash = hashlib.md5(form.username + config.secret_key).hexdigest() # create a new user_hash

        form.username = config.check_secure_val(str(form.username)) # validate HMAC username

        # edit user with new data
        result = config.model.edit_users(
            form['username'],
            pwdhash,
            form['privilege'],
            form['status'],
            form['name'],
            form['email'],
            form['other_data'],
            user_hash,
            form['change_pwd']
        )
        if result == None: # Error on udpate values
            username = config.check_secure_val(str(username)) # validate HMAC username
            result = config.model.get_users(username) # search for username data
            result.username = config.make_secure_val(str(result.username)) # apply HMAC to username
            message = "Error al editar el registro" # Error message
            return config.render.edit(result, message) # render edit.html again
        else: # update user data succefully
            raise config.web.seeother('/users') # render users index.html