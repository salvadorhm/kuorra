import web
import config
import json

class Api_persons:
	def get(self, id_person):
		try:
			# http://0.0.0.0:8080/api_persons?user_hash=12345&action=get
			if id_person == None:
				result = config.model.get_all_persons()
				persons_json = []
				for row in result:
					tmp = dict(row)
					persons_json.append(tmp)
				web.header('Content-Type', 'application/json')
				return json.dumps(persons_json)
			else:
				# http://0.0.0.0:8080/api_persons?user_hash=12345&action=get&id_person=1
				result = config.model.get_persons(int(id_person))
				persons_json = []
				persons_json.append(dict(result))
				web.header('Content-Type', 'application/json')
				return json.dumps(persons_json)
		except Exception as e:
			print "GET Error {}".format(e.args)
			persons_json = '[]'
			web.header('Content-Type', 'application/json')
			return json.dumps(persons_json)

# https://0.0.0.0:8080/api_persons?user_hash=12345&action=put&id_person=1&name=new&telephone=12345&email=new@email.com
	def put(self, name,telephone,email):
		try:
			config.model.insert_persons(name,telephone,email)
			persons_json = '[{200}]'
			web.header('Content-Type', 'application/json')
			return json.dumps(persons_json)
		except Exception as e:
			print "PUT Error {}".format(e.args)
			return None

# http://0.0.0.0:8080/api_persons?user_hash=12345&action=get&id_person=1
	def delete(self, id_person):
		try:
			config.model.delete_persons(id_person)
			persons_json = '[{200}]'
			web.header('Content-Type', 'application/json')
			return json.dumps(persons_json)
		except Exception as e:
			print "DELETE Error {}".format(e.args)
			return None

# https://0.0.0.0:8080/api_persons?user_hash=12345&action=update&id_person=1&name=new&telephone=12345&email=new@email.com
	def update(self, id_person, name,telephone,email):
		try:
			config.model.update_persons(id_person,name,telephone,email)
			persons_json = '[{200}]'
			web.header('Content-Type', 'application/json')
			return json.dumps(persons_json)
		except Exception as e:
			print "GET Error {}".format(e.args)
			persons_json = '[]'
			web.header('Content-Type', 'application/json')
			return json.dumps(persons_json)

	def GET(self):
		user_data = web.input(
			user_hash=None,
			action=None,
			id_person=None,
			name=None,
			telephone=None,
			email=None,
		)
		try:
			user_hash = user_data.user_hash  # user validation
			action = user_data.action  # action GET, PUT, DELETE, UPDATE
			id_person=user_data.id_person
			name=user_data.name
			telephone=user_data.telephone
			email=user_data.email
			
			#change de user_hash 
			if user_hash == '12345':  # user_hash
				if action == None:
					raise web.seeother('/404')
				elif action == 'get':
					return self.get(id_person)
				elif action == 'put':
					return self.put(name,telephone,email)
				elif action == 'delete':
					return self.delete(id_person)
				elif action == 'update':
					return self.update(id_person, name,telephone,email)
			else:
				raise web.seeother('/404')
		except Exception as e:
			print "WEBSERVICE Error {}".format(e.args)
			raise web.seeother('/404')
