import web
import config

db = config.db


def get_all_table_name():
    try:
        return db.select('table_name')
    except Exception as e:
        print "Model get all Error {}".format(e.args)
        print "Model get all Message {}".format(e.message)
        return None


def get_table_name(primary_key):
    try:
        return db.select('table_name', where='primary_key=$primary_key', vars=locals())[0]
    except Exception as e:
        print "Model get Error {}".format(e.args)
        print "Model get Message {}".format(e.message)
        return None


def delete_table_name(primary_key):
    try:
        return db.delete('table_name', where='primary_key=$primary_key', vars=locals())
    except Exception as e:
        print "Model delete Error {}".format(e.args)
        print "Model delete Message {}".format(e.message)
        return None


def insert_table_name(fields):
    try:
        return db.insert('table_name',values)
    except Exception as e:
        print "Model insert Error {}".format(e.args)
        print "Model insert Message {}".format(e.message)
        return None


def edit_table_name(field_all):
    try:
        return db.update('table_name',value_all,
                  where='primary_key=$primary_key',
                  vars=locals())
    except Exception as e:
        print "Model update Error {}".format(e.args)
        print "Model updateMessage {}".format(e.message)
        return None
