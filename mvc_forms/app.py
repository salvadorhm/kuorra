#Author : Salvador Hernandez Mendoza
#Email  : salvadorhm@gmail.com
#Twitter: @salvadorhm
import web
import application

ssl = False #activate ssl certificate 

if ssl == True:
    from web.wsgiserver import CherryPyWSGIServer
    CherryPyWSGIServer.ssl_certificate = "ssl/server.crt" 
    CherryPyWSGIServer.ssl_private_key = "ssl/server.key"

urls = (
    '/', 'application.controllers.persons.index.Index',
    '/insert', 'application.controllers.persons.insert.Insert',
    '/update/(.+)', 'application.controllers.persons.update.Update',
    '/view/(.+)', 'application.controllers.persons.view.View',
    '/delete/(.+)', 'application.controllers.persons.delete.Delete',
    '/api_persons/?', 'application.api.persons.api_persons.Api_persons'
)

if __name__ == "__main__":
    app = web.application(urls, globals())
    web.config.debug = False
    app.run()
