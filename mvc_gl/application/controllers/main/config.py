import web
import hmac
import application.models.model_users as model_users
import application.models.model_logs as model_logs
import app

render = web.template.render('application/views/main/', base='master')

# app secret_key
secret_key = app.secret_key


def validate_https():
    if app.web.ctx.protocol == "http":
            dom = app.web.ctx.homedomain
            dom = dom.replace("http","https")
            dom += app.web.ctx.path
            raise app.web.seeother(dom)


def hash_str(s):
    return hmac.new(secret_key, s).hexdigest()


def make_secure_val(s):
    return "%s!%s" % (s, hash_str(s))


def check_secure_val(h):
    val = h.split('!')[0]
    if h == make_secure_val(val):
        return val