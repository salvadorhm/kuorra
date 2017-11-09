import web
import config
import json


class Api_products:
    def get(self, id_product):
        try:
            # http://api_products?user_hash=12345&action=get
            if id_product == None:
                result = config.model.get_all_products()
                products_json = []
                for row in result:
                    tmp = str(dict(row))
                    products_json.append(tmp)
                web.header('Content-Type', 'application/json')
                return json.dumps(products_json)
            else:
                # http://api_products?user_hash=12345&action=get&id_product=1
                result = config.model.get_products(int(id_product))
                products_json = []
                products_json.append(str(dict(result)))
                web.header('Content-Type', 'application/json')
                return json.dumps(products_json)
        except Exception as e:
            print "GET Error {}".format(e.args)
            products_json = '[]'
            web.header('Content-Type', 'application/json')
            return json.dumps(products_json)

# https://0.0.0.0:8080/api_products?user_hash=12345&action=put&id_product=1&product=nuevo&description=nueva&stock=10&purchase_price=1&price_sale=3&product_image=0
    def put(self, product, description, stock, purchase_price, price_sale, product_image):
        try:
            config.model.insert_products(
                product, description, stock, purchase_price, price_sale, product_image)
            products_json = '[{200}]'
            web.header('Content-Type', 'application/json')
            return json.dumps(products_json)
        except Exception as e:
            print "PUT Error {}".format(e.args)
            return None
# http://api_products?user_hash=12345&action=get&id_product=1
    def delete(self, id_product):
        try:
            config.model.delete_products(id_product)
            products_json = '[{200}]'
            web.header('Content-Type', 'application/json')
            return json.dumps(products_json)
        except Exception as e:
            print "DELETE Error {}".format(e.args)
            return None
# https://0.0.0.0:8080/api_products?user_hash=12345&action=update&id_product=1&product=nuevo&description=nueva&stock=10&purchase_price=1&price_sale=3&product_image=default.jpg
    def update(self, id_product, product, description, stock, purchase_price, price_sale, product_image):
        try:
            config.model.edit_products(id_product,product, description, stock, purchase_price, price_sale, product_image)
            products_json = '[{200}]'
            web.header('Content-Type', 'application/json')
            return json.dumps(products_json)
        except Exception as e:
            print "GET Error {}".format(e.args)
            products_json = '[]'
            web.header('Content-Type', 'application/json')
            return json.dumps(products_json)

    def GET(self):
        user_data = web.input(
            user_hash=None,
            action=None,
            id_product=None,
            product=None,
            description=None,
            stock=None,
            purchase_price=None,
            price_sale=None,
            product_image=None
        )
        try:
            user_hash = user_data.user_hash  # user validation
            action = user_data.action  # action GET, PUT, DELETE, UPDATE
            id_product = user_data.id_product
            product = user_data.product
            description = user_data.description
            stock = user_data.stock
            purchase_price = user_data.purchase_price
            price_sale = user_data.price_sale
            product_image = user_data.product_image

            if user_hash == '12345':  # user_hash
                if action == None:
                    raise web.seeother('/404')
                elif action == 'get':
                    return self.get(id_product)
                elif action == 'put':
                    return self.put(product, description, stock, purchase_price, price_sale, product_image)
                elif action == 'delete':
                    return self.delete(id_product)
                elif action == 'update':
                    return self.update(id_product, product, description, stock, purchase_price, price_sale, product_image)
            else:
                raise web.seeother('/404')
        except Exception as e:
            print "WEBSERVICE Error {}".format(e.args)
            raise web.seeother('/404')
