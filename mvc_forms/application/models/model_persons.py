import web
import config

db = config.db

def get_all_persons():
    try:
        return db.select('persons')
    except Exception as e:
        print "Model get all Error {}".format(e.args)
        print "Model get all Message {}".format(e.message)
        return None

def get_persons(id_person):
    try:
        return db.select('persons', where='id_person=$id_person', vars=locals())[0]
    except Exception as e:
        print "Model get Error {}".format(e.args)
        print "Model get Message {}".format(e.message)
        return None

def delete_persons(id_person):
    try:
        return db.delete('persons', where='id_person=$id_person', vars=locals())
    except Exception as e:
        print "Model delete Error {}".format(e.args)
        print "Model delete Message {}".format(e.message)
        return None

def insert_persons(id_person,name,telephone,email):
    try:
        db.insert('persons',id_person=id_person,
name=name,
telephone=telephone,
email=email)
    except Exception as e:
        print "Model insert Error {}".format(e.args)
        print "Model insert Message {}".format(e.message)
        return None

def update_persons(id_person,name,telephone,email):
    try:
        db.update('persons',id_person=id_person,
name=name,
telephone=telephone,
email=email,
                  where='id_person=$id_person',
                  vars=locals())
    except Exception as e:
        print "Model update Error {}".format(e.args)
        print "Model updateMessage {}".format(e.message)
        return None
