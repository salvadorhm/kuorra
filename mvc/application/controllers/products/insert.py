import config

class Insert:
	
	def GET(self):
		return config.render.insert()

	def POST(self):
		form = config.web.input()
		image = config.web.input(product_image={})
		filedir = 'static/files'
		filepath = image.product_image.filename.replace('\\', '/')
		filename = filepath.split('/')[-1]
		fout = open(filedir + '/' + filename, 'w')
		fout.write(image.product_image.file.read())
		fout.close()
		product_image = filename

		config.model.insert_products(
			form['product'],
			form['description'],
			form['stock'],
			form['purchase_price'],
			form['price_sale'],
			product_image
		)
		raise config.web.seeother('/')