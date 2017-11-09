from . import config
import hashlib
import app


class Insert:
    def __init__(self):
        pass

    def GET(self):
        if app.session.loggedin is True:
            # username = app.session.username
            privilege = app.session.privilege
            if privilege == 0:
                return self.GET_INSERT()
            elif privilege == 1:
                raise config.web.seeother('/guess')
        else:
            raise config.web.seeother('/login')

    def POST(self):
        if app.session.loggedin is True:
            # username = app.session.username
            privilege = app.session.privilege
            if privilege == 0:
                return self.POST_INSERT()
            elif privilege == 1:
                raise config.web.seeother('/guess')
        else:
            raise config.web.seeother('/login')

    @staticmethod
    def GET_INSERT():
        return config.render.insert()

    @staticmethod
    def POST_INSERT():
        form = config.web.input()
        pwdhash = hashlib.md5(form.password + config.secret_key).hexdigest()
        user_hash = hashlib.md5(form.username + config.secret_key).hexdigest()

        config.model.insert_users(
            form['username'],
            pwdhash,
            form['privilege'],
            form['status'],
            form['name'],
            form['email'],
            form['other_data'],
            user_hash,
            1
        )
        raise config.web.seeother('/users')
