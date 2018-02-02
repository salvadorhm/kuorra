"""
    Class for show the users list
"""
from . import config
import app


class Index:
    def __init__(self):
        pass

    def GET(self):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege # get the session_privilege 
            if session_privilege == 0: # admin user
                return self.GET_INDEX() # call GET_INDEX() function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/guess') # rendner guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    @staticmethod
    def GET_INDEX():
        result = config.model.get_all_users().list() # get users table list
        for row in result: 
            row.username = config.make_secure_val(str(row.username)) # apply HMAC to username (primary key)
        return config.render.index(result) # render index.html
