import application.controllers.main.config as config
import app
import hashlib
import web
import auth
import json
import datetime


# Google API Token
app_id = app.app_id
app_secret = app.app_secret

# Valores asignados de id_cliente proporcionado por el proveedor en este caso google
# En caso de trabajar con otros provedores como Facebook se cambiaran los valores 
# En caso de trabajar con dos o mas provedores al mismo tiempo se tendran valores asiganados independientes por cada proveedor  
# auth.parameters['google']['app_id'] = '364672633912-hbhtatjd9kbkbeaocn0902pivum4t0cd.apps.googleusercontent.com'#ID_cliente
# auth.parameters['google']['app_secret'] = 'b_HGPbqiY-gBHSCBuS38fVau'#Secret_del_cliente  

auth.parameters['google']['app_id'] = app_id
auth.parameters['google']['app_secret'] = app_secret


class Login:
    def __init__(self):
        pass
    
 

     #@staticmethod
     #def GET(*a):
     #   message = None
     #   return config.render.login(message)

    #@staticmethod
    #def POST(*a):
         #i = config.web.input()
class handler(auth.handler):
  def callback_uri(self, provider):
    """Please return appropriate url according to your app setting.
    """
    return 'http://localhost:8080/auth/%s/callback' % provider
    # return 'http://salvadorhm.ddns.net:8080/auth/%s/callback' % provider
    # return 'http://' +  web.ctx.host + '/auth/%s/callback' % provider

  def on_signin(self, provider, profile):
    """Callback when the user successfully signs in the account of the provider
    (e.g., Google account or Facebook account).

    Arguments:
      provider: google or facebook
      profile: the user profile of Google or facebook account of the user who
               signs in.
    """
    user_id = '%s:%s' % (provider, profile['id'])

    # set '_id' in the cookie to sign-in the user in our webapp
    web.setcookie('_id', user_id)
    web.setcookie('_profile', json.dumps(profile))
    
    #redireccion a entorno de usuario de login 
    raise web.seeother('/login') 


class AuthPage(handler):
  def GET(self, provider):
    self.auth_init(provider)


class AuthCallbackPage(handler):
  def GET(self, provider):
    self.auth_callback(provider)


#clase principal 
class LoginPage:
  def GET(self):
    # check '_id' in the cookie to see if the user already sign in
    if web.cookies().get('_id'):
      # user already sign in, retrieve user profile
      #transformacion de archivo json para leer y obtener perfil de usuario
      profile = json.loads( web.cookies().get('_profile'))
      #Obtencion de valor email del archivo json 
      user = profile['email'] 
      picture = profile['picture']
      #emision de valor email de archivo json para ver html
      # obtencion_email = profile['email'], json.dumps(user)


     
      check = config.model_users.validate_user(user)
      if check:
            app.session.loggedin = True
            app.session.user = check['user']
            app.session.privilege = check['privilege']
            app.session.picture = picture

            # get time now and N minutes
            now = datetime.datetime.now()
            future = now + datetime.timedelta(minutes = app.expires)
            future_str = str(future).split('.')[0]
            app.session.expires = config.make_secure_val(future_str)

            ip = web.ctx['ip']

            config.model_logs.insert_logs(check['user'], ip)

            if check['status'] == 0:
                message = check['user'] + ": User account disabled!!!!"
                app.session.loggedin = False
                app.session.user = 'anonymous'
                app.session.privilege = -1 #asignar privilegio solo para pagina de introduccion
                app.session.picture = None
                app.session.kill()#destruir la session de kuorra
                web.setcookie('_id', '', 0)#cierre de session en google 
                print message
                return config.render.login(message)
            else:
                raise config.web.seeother('/')
      if check==None:
        message = user + ": User not found"
        app.session.loggedin = False
        app.session.user = 'anonymous'
        app.session.privilege = -1 #asignar privilegio solo para pagina de introduccion
        app.session.picture = None
        app.session.kill()#destruir la session de kuorra
        web.setcookie('_id', '', 0)#cierre de session en google 
        
        print  message
        return config.render.login(message)
        # raise config.web.seeother('/logout')
    
    else:
      raise web.seeother('/auth/google')
      #return  redirect('/auth/google')
