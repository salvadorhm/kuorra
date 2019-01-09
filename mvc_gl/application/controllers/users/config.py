"""
    File for config the tables models and use HMAC
"""
import web
import hmac
import application.models.model_users
import app
import re 

render = web.template.render('application/views/users/', base='master')
model = application.models.model_users

secret_key = app.secret_key

def check_string(s):
    patron = re.compile('a-z')
    print patron.match(s)

def check_integer(i):
    patron = re.compile('0-9')
    print patron.match(i)  

def hash_str(s):
    return hmac.new(secret_key, s).hexdigest()


def make_secure_val(s):
    return "%s!%s" % (s, hash_str(s))


def check_secure_val(h):
    val = h.split('!')[0]
    if h == make_secure_val(val):
        return val
