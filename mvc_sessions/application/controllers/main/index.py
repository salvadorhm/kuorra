from . import config
import app


class Index:
    
    def __init__(self):
        pass

    @staticmethod
    def GET():
        if app.session.loggedin is True:
            username = app.session.username
            privilege = app.session.privilege
            params = {}
            params['username'] = username
            params['privilege'] = privilege
            if privilege == 0:
                return config.render.admin(params)
            elif privilege == 1:
                return config.render.guess(params)
        else:
            params = {}
            params['username'] = 'anonymous'
            params['privilege'] = '-1'
            return config.render.index(params)
