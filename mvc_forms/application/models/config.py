import web

db_host = 'localhost'
db_name = 'contacts_kuorra'
db_user = 'root'
db_pw = 'toor'

db = web.database(
    dbn='mysql',
    host=db_host,
    db=db_name,
    user=db_user,
    pw=db_pw
    )