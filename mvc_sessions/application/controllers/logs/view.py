from . import config
import app


class View:
    
    def __init__(self):
        pass

    def GET(self, username):
        if app.session.loggedin is True:
            # username = app.session.username
            privilege = app.session.privilege
            if privilege == 0:
                return self.GET_VIEW(username)
            elif privilege == 1:
                raise config.web.seeother('/guess')
        else:
            raise config.web.seeother('/login')

    @staticmethod
    def GET_VIEW(username):
        username = config.check_secure_val(str(username))
        result = config.model_users.get_users(username)
        print result
        return config.render.view(result)
