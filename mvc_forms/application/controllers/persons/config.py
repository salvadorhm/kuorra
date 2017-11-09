import web
from web import form
import application.models.model_persons

render = web.template.render('application/views/persons/', base='master')
model = application.models.model_persons

vemail = form.regexp(r".*@.*", "Must be a valid email address")
'''
Here we define the form fields for use in all the views
'''
form_persons = form.Form(
            form.Hidden('id_person',description="", value="0", class_="form-control", required=True),
            form.Textbox('name',description="name", class_="form-control", required=True),
            form.Textbox('telephone',description="telephone", class_="form-control", required=True),
            form.Textbox('email', vemail, description="Email", class_="form-control", required=True),
        )
        