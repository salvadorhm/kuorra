from . import config
import hashlib
import app


class Edit:

    def __init__(self):
        pass

    def GET(self, username, **k):
        if app.session.loggedin is True:
            # session_username = app.session.username
            privilege = app.session.privilege
            if privilege == 0:
                return self.GET_EDIT(username)
            elif privilege == 1:
                raise config.web.seeother('/guess')
        else:
            raise config.web.seeother('/login')

    def POST(self, username, **k):
        if app.session.loggedin is True:
            # session_username = app.session.username
            privilege = app.session.privilege
            if privilege == 0:
                return self.POST_EDIT(username)
            elif privilege == 1:
                raise config.web.seeother('/guess')
        else:
            raise config.web.seeother('/login')

    @staticmethod
    def GET_EDIT(username, **k):
        message = None
        username = config.check_secure_val(str(username))
        result = config.model.get_users(username)
        result.username = config.make_secure_val(str(result.username))
        return config.render.edit(result, message)
    
    @staticmethod
    def POST_EDIT(username, **k):
        form = config.web.input()
        username = config.check_secure_val(str(username))
        user = config.model.get_users(username)
        print user
        pwd = user.password
        print pwd
        print form.password

        if pwd == form.password:
            pwdhash = pwd
        else:
            pwdhash = hashlib.md5(form.password + config.secret_key).hexdigest()

        user_hash = hashlib.md5(form.username + config.secret_key).hexdigest()

        form.username = config.check_secure_val(str(form.username))

        res = config.model.edit_users(
            form['username'],
            pwdhash,
            form['privilege'],
            form['status'],
            form['name'],
            form['email'],
            form['other_data'],
            user_hash,
            form['change_pwd']
        )
        if res == 0:
            username = config.check_secure_val(str(username))
            result = config.model.get_users(username)
            result.username = config.make_secure_val(str(result.username))
            message = "Error al editar el registro"
            return config.render.edit(result, message)
        else:
            raise config.web.seeother('/users')