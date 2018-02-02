import config
import hashlib
import app

class Delete:
    
    def __init__(self):
        pass

    '''
    def GET(self, primary_key, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege # get the session_privilege
            if session_privilege == 0: # admin user
                return self.GET_DELETE(primary_key) # call GET_DELETE function
            elif privsession_privilegeilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    def POST(self, primary_key, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege
            if session_privilege == 0: # admin user
                return self.POST_DELETE(primary_key) # call POST_DELETE function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    @staticmethod
    def GET_DELETE(primary_key, **k):

    @staticmethod
    def POST_DELETE(primary_key, **k):
    '''

    def GET(self, primary_key, **k):
        message = None # Error message
        primary_key = config.check_secure_val(str(primary_key)) # HMAC primary_key validate
        result = config.model.get_table_name(int(primary_key)) # search  primary_key
        result.primary_key = config.make_secure_val(str(result.primary_key)) # apply HMAC for primary_key
        return config.render.delete(result, message) # render delete.html with user data

    def POST(self, primary_key, **k):
        form = config.web.input() # get form data
        form['primary_key'] = config.check_secure_val(str(form['primary_key'])) # HMAC primary_key validate
        result = config.model.delete_table_name(form['primary_key']) # get table_name data
        if result is None: # delete error
            message = "El registro no se puede borrar" # Error messate
            primary_key = config.check_secure_val(str(primary_key))  # HMAC user validate
            primary_key = config.check_secure_val(str(primary_key))  # HMAC user validate
            result = config.model.get_table_name(int(primary_key)) # get primary_key data
            result.primary_key = config.make_secure_val(str(result.primary_key)) # apply HMAC to primary_key
            return config.render.delete(result, message) # render delete.html again
        else:
            raise config.web.seeother('/table_name') # render table_name delete.html 
