import web
import application.models.model_users
import application.models.model_logs

render = web.template.render('application/views/main/', base='master')
model = application.models.model_users
model_logs = application.models.model_logs

secret_key = "kuorra_key"