import application.controllers.users.config  as config
import hashlib
import app
import datetime

class Edit:

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
                return self.GET_EDIT(user) # call GET_EDIT function
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
            session_privilege = app.session.privilege # get the session_privilege
            if session_privilege == 0: # admin user
                return self.POST_EDIT(user) # call POST_EDIT function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/logout') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    @staticmethod
    def GET_EDIT(user, **k):
        message = None # Error message
        user = config.check_secure_val(str(user)) # HMAC user validate
        result = config.model.get_users(user) # search for the user
        result.user = config.make_secure_val(str(result.user)) # apply HMAC for username
        return config.render.edit(result, message) # render edit.html
    
    @staticmethod
    def POST_EDIT(user, **k):
        form = config.web.input() # get form data
        user = config.check_secure_val(str(user)) # HMAC user validate
        user_hash = hashlib.md5(form.user + config.secret_key).hexdigest() # create a new user_hash
        form.user = config.check_secure_val(str(form.user)) # validate HMAC username
        session_user = app.session.user # get session_username
        message = None
        if user != session_user: # compare username with sesion_username
            # edit user with new data
            result = config.model.edit_users(
                form['user'],
                form['privilege'],
                form['status'],
                form['username'],
                form['email'],
                form['other_data'],
                user_hash
            )
            if result == None: # Error on udpate values
                user = config.check_secure_val(str(user)) # validate HMAC username
                result = config.model.get_users(user) # search for username data
                result.user = config.make_secure_val(str(result.user)) # apply HMAC to username
                message = "Error in Update" # Error message
                return config.render.edit(result, message) # render edit.html again
            else: # update user data succefully
                raise config.web.seeother('/users') # render users index.html

        elif user == session_user:
            if form['status'] == '0':
                message = "Can't change logged user to disabled user" # Error message
                result = config.model.get_users(user) # get username data
                result.user = config.make_secure_val(str(result.user)) # apply HMAC to username
                return config.render.edit(result, message) # render edit.html

            elif form['privilege'] == '1': 
                message = "Can't change logged user to guess privilge user" # Error message
                result = config.model.get_users(user) # get username data
                result.user = config.make_secure_val(str(result.user)) # apply HMAC to username
                return config.render.edit(result, message) # render edit.html

            else:
                # edit user with new data
                result = config.model.edit_users(
                    form['user'],
                    0,
                    1,
                    form['username'],
                    form['email'],
                    form['other_data'],
                    user_hash
                )
                if result == None: # Error on udpate values
                    user = config.check_secure_val(str(user)) # validate HMAC username
                    result = config.model.get_users(user) # search for username data
                    result.user = config.make_secure_val(str(result.user)) # apply HMAC to username
                    message = "Error in Update" # Error message
                    return config.render.edit(result, message) # render edit.html again
                else: # update user data succefully
                    raise config.web.seeother('/users') # render users index.html
