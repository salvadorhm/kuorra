import application.controllers.users.config  as config
import hashlib
import app
import datetime


class Insert:
    
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

            session_user = app.session.user
            session_user = app.session.privilege  # get the session_privilege
            if session_user == 0: # admin user
                return self.GET_INSERT() # call GET_INSERT() function
            elif session_user == 1: # guess user
                raise config.web.seeother('/') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    def POST(self):
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
                return self.POST_INSERT() # call POST_EDIT function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    @staticmethod
    def GET_INSERT():
        return config.render.insert() # render insert.html

    @staticmethod
    def POST_INSERT():
        form = config.web.input()  # get form data
        #pwdhash = hashlib.md5(form.password + config.secret_key).hexdigest() # encrypt pwdhash
        user_hash = hashlib.md5(form.user + config.secret_key).hexdigest() # encrypt user_hash

        config.check_string(form['user'])
        config.check_integer(form['user'])

        # call model insert_users and try to insert new data
        config.model.insert_users(
            form['user'],
            form['privilege'],
            form['status'],
            form['username'],
            form['email'],
            form['other_data'],
            user_hash
        )
        raise config.web.seeother('/users') # render users index.html
