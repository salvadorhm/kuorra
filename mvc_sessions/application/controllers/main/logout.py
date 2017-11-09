import config
import app


class Logout:
    def __init__(self):
        pass

    @staticmethod
    def GET():
        app.session.username = 'anonymous'
        app.session.privilege = -1
        app.session.kill()
        raise config.web.seeother('/')
