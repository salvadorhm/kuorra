import web
import application.models.model_products

render = web.template.render('application/views/products/', base='master')
model = application.models.model_products
	