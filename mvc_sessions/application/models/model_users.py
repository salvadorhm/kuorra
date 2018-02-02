import web
from . import config

db = config.db


def validate_user(username, password):
    try:
        # select * from users where username=$username and password=$password;
        return db.select('users',
            where='username=$username and password=$password', vars=locals())[0]
    except Exception as e:
        print(("Model get all Error {}".format(e.args)))
        print(("Model get all Message {}".format(e.message)))
        return None


def get_all_users():
    try:
        # select * from users;
        return db.select('users') 
    except Exception as e:
        print(("Model get all Error {}".format(e.args)))
        print(("Model get all Message {}".format(e.message)))
        return None


def get_users(username):
    try:
        # select * from users where username = $username;
        return db.select('users', where='username=$username', vars=locals())[0] 
    except Exception as e:
        print(("Model get Error {}".format(e.args)))
        print(("Model get Message {}".format(e.message)))
        return None


def delete_users(username):
    try:
        # delete * from users where username = $username;
        return db.delete('users', where='username=$username', vars=locals())
    except Exception as e:
        print(("Model delete Error {}".format(e.args)))
        print(("Model delete Message {}".format(e.message)))
        return None


def insert_users(username, password, privilege, status, name, email, other_data, user_hash, change_pwd):
    try:
        """
        insert into users (username, password, privilege, status, name, email, other_data, user_hash, change_pwd) 
        values ($username, $password, $privilege, $status, $name, $email, $other_data, $user_hash, $change_pwd);
        """
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
        """
        update users set password=$password, privilege=$privilege, status=$status, name=$name,
            email=$email, other_data=$other_data, user_hash=$user_hash, change_pwd=$change_pwd 
            where username=$username;
        """
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
        # update users set username=$username, password=$password, change_pwd=$change_pwd where username=$username;
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
