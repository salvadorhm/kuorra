import web
import app

db = app.db

def validate_user(user):
    try:
        return db.select('users', where='user=$user', vars=locals())[0]
    except Exception as e:
        print(("Model get all Error {}".format(e.args)))
        print(("Model get all Message {}".format(e.message)))
        return None



def get_all_users():
    try:
        return db.select('users') 
    except Exception as e:
        print(("Model get all Error {}".format(e.args)))
        print(("Model get all Message {}".format(e.message)))
        return None


def get_users(user):
    try:
        return db.select('users', where='user=$user', vars=locals())[0] 
    except Exception as e:
        print(("Model get Error {}".format(e.args)))
        print(("Model get Message {}".format(e.message)))
        return None


def delete_users(user):
    try:
        return db.delete('users', where='user=$user', vars=locals())
    except Exception as e:
        print(("Model delete Error {}".format(e.args)))
        print(("Model delete Message {}".format(e.message)))
        return None


def insert_users(user, privilege, status, username, email, other_data, user_hash):
    try:
        db.insert('users',
            user=user,
            privilege=privilege,
            status=status,
            username=username,
            email=email,
            other_data=other_data,
            user_hash=user_hash
            )
    except Exception as e:
        print(("Model insert Error {}".format(e.args)))
        print(("Model insert Message {}".format(e.message)))
        return None


def edit_users(user, privilege, status, username, email, other_data, user_hash):
    try:
        return db.update('users',
            user=user,
            privilege=privilege,
            status=status,
            username=username,
            email=email,
            other_data=other_data,
            user_hash=user_hash,
            where='user=$user',
            vars=locals())
            
    except Exception as e:
        print("Model update Error {}".format(e.args))
        print("Model updateMessage {}".format(e.message))
        return None
