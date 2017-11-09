from . import config
import hashlib
import app


class Change_pwd:
    def __init__(self):
        pass

    def GET(self):
        if app.session.loggedin is True:
            username = app.session.username
            privilege = app.session.privilege
            print username
            if privilege == 0 or privilege == 1:
                print username
                return self.GET_CHANGE_PWD(username)
        else:
            raise config.web.seeother('/login')

    def POST(self):
        if app.session.loggedin is True:
            username = app.session.username
            privilege = app.session.privilege
            if privilege == 0 or privilege == 1:
                return self.POST_CHANGE_PWD(username)
        else:
            raise config.web.seeother('/login')

    @staticmethod
    def GET_CHANGE_PWD(username):
        print username
        message = None
        result = config.model.get_users(username)
        result.username = config.make_secure_val(str(result.username))
        return config.render.change_pwd(result, message)

    @staticmethod
    def POST_CHANGE_PWD(username):
        form = config.web.input()
        password = hashlib.md5(form.password + config.secret_key).hexdigest()
        password2 = hashlib.md5(form.password2 + config.secret_key).hexdigest()

        if password == password2:
            config.model.update_password(
                username,
                password,
                0
            )

        raise config.web.seeother('/users')
