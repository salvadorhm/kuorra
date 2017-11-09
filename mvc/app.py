#Author : Salvador Hernandez Mendoza
#Email  : salvadorhm@gmail.com
#Twitter: @salvadorhm
import web
import application

ssl = True #activate ssl certificate 

if ssl == True:
    from web.wsgiserver import CherryPyWSGIServer
    '''
    Use OpenSSL to generate  keys

    user@host$ openssl genrsa -out server.key 1024
    user@host$ openssl req -new -key server.key -out server.csr
    user@host$ openssl x509 -req -days 365 -in server.csr -signkey server.key -out server.crt

    '''
    CherryPyWSGIServer.ssl_certificate = "ssl/server.crt" 
    CherryPyWSGIServer.ssl_private_key = "ssl/server.key"

urls = (
    '/', 'application.controllers.products.index.Index',
    '/products/view/(.+)', 'application.controllers.products.view.View',
    '/products/insert', 'application.controllers.products.insert.Insert',
    '/products/edit/(.+)', 'application.controllers.products.edit.Edit',
    '/products/delete/(.+)', 'application.controllers.products.delete.Delete',
    '/api_products/?', 'application.api.products.api_products.Api_products',
)

if __name__ == "__main__":
    app = web.application(urls, globals())
    web.config.debug = False
    app.run()
