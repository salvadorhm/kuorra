from . import config
import app


class Delete:

    def __init__(self):
        pass

    def GET(self, username, **k):
        if app.session.loggedin is True:
            # session_username = app.session.username
            privilege = app.session.privilege
            if privilege == 0:
                return self.GET_DELETE(username)
            elif privilege == 1:
                raise config.web.seeother('/guess')
        else:
            raise config.web.seeother('/login')

    def POST(self, username, **k):
        if app.session.loggedin is True:
            # session_username = app.session.username
            privilege = app.session.privilege
            if privilege == 0:
                return self.POST_DELETE(username)
            elif privilege == 1:
                raise config.web.seeother('/guess')
        else:
            raise config.web.seeother('/login')

    @staticmethod
    def GET_DELETE(username, **k):
        message = None
        username = config.check_secure_val(str(username))
        result = config.model.get_users(username)
        result.username = config.make_secure_val(str(result.username))
        return config.render.delete(result, message)


    @staticmethod
    def POST_DELETE(username, **k):
        form = config.web.input()
        username = config.check_secure_val(str(form['username']))
        session_username = app.session.username
        if username != session_username:
            res = config.model.delete_users(username)
            if res is None:
                message = "El registro no se puede borrar"
                result = config.model.get_users(username)
                result.username = config.make_secure_val(str(result.username))
                return config.render.delete(result, message)
            else:
                raise config.web.seeother('/users')
        else:
            message = "No se puede elimiar el usuario activo"
            result = config.model.get_users(username)
            result.username = config.make_secure_val(str(result.username))
            return config.render.delete(result, message)
