"""
    Class for show a users list for print
"""
from . import config
import app


class Printer:
    def __init__(self):
        pass

    def GET(self):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege # get the session_privilege
            if session_privilege == 0: # admin user
                return self.GET_PRINTER() # call GET_PRINTER() function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else:# the user dont have logged
            raise config.web.seeother('/login')

    @staticmethod
    def GET_PRINTER():
        result = config.model.get_all_users().list() # get all users data
        for row in result: 
            row.username = config.make_secure_val(str(row.username)) # apply HMAC to username
        return config.render.printer(result) # render printer.html
