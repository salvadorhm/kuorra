import config

class View:
    
    def __init__(self):
        pass

    def GET(self, id_product):
        id_product = int(id_product)
        result = config.model.get_products(id_product)
        return config.render.view(result)
