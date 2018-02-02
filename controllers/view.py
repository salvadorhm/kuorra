import config
import hashlib
import app


class View:

    def __init__(self):
        pass

    '''
    def GET(self, primary_key):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege # get the session_privilege
            if session_privilege == 0: # admin user
                return self.GET_VIEW(primary_key) # call GET_VIEW() function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    @staticmethod
    def GET_VIEW(primary_key):
    '''

    def GET(self, primary_key):
        primary_key = config.check_secure_val(str(primary_key)) # HMAC primary_key validate
        result = config.model.get_table_name(primary_key) # search for the primary_key data
        return config.render.view(result) # render view.html with primary_key data
