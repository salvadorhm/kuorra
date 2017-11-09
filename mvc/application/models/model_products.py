import web
import config

db = config.db


def get_all_products():
    try:
        return db.select('products')
    except Exception as e:
        print "Model get all Error {}".format(e.args)
        print "Model get all Message {}".format(e.message)
        return None

def get_products(id_product):
    try:
        return db.select('products', where='id_product=$id_product', vars=locals())[0]
    except Exception as e:
        print "Model get Error {}".format(e.args)
        print "Model get aMessage {}".format(e.message)
        return None

def delete_products(id_product):
    try:
        return db.delete('products', where='id_product=$id_product', vars=locals())
    except Exception as e:
        print "Model delete Error {}".format(e.args)
        print "Model delete Message {}".format(e.message)
        return None

def insert_products(product, description, stock, purchase_price, price_sale, product_image):
    try:
        db.insert('products',
                  product=product,
                  description=description,
                  stock=stock,
                  purchase_price=purchase_price,
                  price_sale=price_sale,
                  product_image=product_image)
    except Exception as e:
        print "Model insert Error {}".format(e.args)
        print "Model insert Message {}".format(e.message)
        return None

def edit_products(id_product, product, description, stock, purchase_price, price_sale, product_image):
    try:
        db.update('products',
                  product=product,
                  description=description,
                  stock=stock,
                  purchase_price=purchase_price,
                  price_sale=price_sale,
                  product_image=product_image,
                  where='id_product=$id_product',
                  vars=locals())
    except Exception as e:
        print "Model update Error {}".format(e.args)
        print "Model update Message {}".format(e.message)
        return None
