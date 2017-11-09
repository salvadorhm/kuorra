import web
from . import config

db = config.db


def validate_user(username, password):
    try:
        return db.select('users',
        where='username=$username and password=$password', vars=locals())[0]
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


def get_users(username):
    try:
        return db.select('users', where='username=$username', vars=locals())[0]
    except Exception as e:
        print(("Model get Error {}".format(e.args)))
        print(("Model get Message {}".format(e.message)))
        return None


def delete_users(username):
    try:
        return db.delete('users', where='username=$username', vars=locals())
    except Exception as e:
        print(("Model delete Error {}".format(e.args)))
        print(("Model delete Message {}".format(e.message)))
        return False


def insert_users(username, password, privilege, status, name, email, other_data, user_hash, change_pwd):
    try:
        db.insert('users',
        username=username,
        password=password,
        privilege=privilege,
        status=status,
        name=name,
        email=email,
        other_data=other_data,
        user_hash=user_hash,
        change_pwd = change_pwd
                  )
    except Exception as e:
        print(("Model insert Error {}".format(e.args)))
        print(("Model insert Message {}".format(e.message)))
        return None


def edit_users(username, password, privilege, status, name, email, other_data, user_hash, change_pwd):
    try:
        return db.update('users',
            username=username,
            password=password,
            privilege=privilege,
            status=status,
            name=name,
            email=email,
            other_data=other_data,
            user_hash=user_hash,
            change_pwd = change_pwd,

            where='username=$username',
            vars=locals())
    except Exception as e:
        print("Model update Error {}".format(e.args))
        print("Model updateMessage {}".format(e.message))
        return None

def update_password(username, password, change_pwd):
    try:
        return db.update('users',
            username=username,
            password=password,
            change_pwd = change_pwd,

            where='username=$username',
            vars=locals())
    except Exception as e:
        print("Model update Error {}".format(e.args))
        print("Model updateMessage {}".format(e.message))
        return None