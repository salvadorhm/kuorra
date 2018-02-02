import config
import hashlib
import app

class Edit:
    
    def __init__(self):
        pass

    '''
    def GET(self, primary_key, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege # get the session_privilege
            if session_privilege == 0: # admin user
                return self.GET_EDIT(primary_key) # call GET_EDIT function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    def POST(self, primary_key, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege # get the session_privilege
            if session_privilege == 0: # admin user
                return self.POST_EDIT(primary_key) # call POST_EDIT function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    @staticmethod
    def GET_EDIT(primary_key, **k):

    @staticmethod
    def POST_EDIT(primary_key, **k):
        
    '''

    def GET(self, primary_key, **k):
        message = None # Error message
        primary_key = config.check_secure_val(str(primary_key)) # HMAC primary_key validate
        result = config.model.get_table_name(int(primary_key)) # search for the primary_key
        result.primary_key = config.make_secure_val(str(result.primary_key)) # apply HMAC for primary_key
        return config.render.edit(result, message) # render table_name edit.html

    def POST(self, primary_key, **k):
        form = config.web.input()  # get form data
        form['primary_key'] = config.check_secure_val(str(form['primary_key'])) # HMAC primary_key validate
        # edit user with new data
        result = config.model.edit_table_name(
            fields
        )
        if result == None: # Error on udpate data
            primary_key = config.check_secure_val(str(primary_key)) # validate HMAC primary_key
            result = config.model.get_table_name(int(primary_key)) # search for primary_key data
            result.primary_key = config.make_secure_val(str(result.primary_key)) # apply HMAC to primary_key
            message = "Error al editar el registro" # Error message
            return config.render.edit(result, message) # render edit.html again
        else: # update user data succefully
            raise config.web.seeother('/table_name') # render table_name index.html
