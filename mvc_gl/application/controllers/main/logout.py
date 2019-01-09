import config
import app
import auth
import json
import web

class Logout:
    def __init__(self):
        pass

    def GET(self):
        app.session.loggedin = False
        app.session.user = 'anonymous'
        app.session.privilege = -1 #asignar privilegio solo para pagina de introduccion
        app.session.picture = None
        app.session.kill()#destruir la session de kuorra
        web.setcookie('_id', '', 0)#cierre de session en google 

        # raise config.web.seeother('https://accounts.google.com/Logout?&continue=http://www.kuorra.com/')
        raise config.web.seeother('https://accounts.google.com/Logout')
        # raise config.web.seeother('/')#redireccion al index

