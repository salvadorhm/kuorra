import application.controllers.users.config  as config
import hashlib
import app
import csv
import os
import datetime


class CsvImport:

    def __init__(self):
        pass

    def GET(self, **k):
        if app.session.loggedin is True:
            # get now time
            now = datetime.datetime.now()
            now_str = str(now).split('.')[0]

            expires = config.check_secure_val(app.session.expires)

            print "now    : " , now_str
            print "expires: " , expires

            if (now_str > expires): # compare now with time login
                raise config.web.seeother('/logout')

            # session_user = app.session.user
            session_privilege = app.session.privilege  # get the session_privilege
            if session_privilege == 0: # admin user
                return self.GET_IMPORT() # call GET_INSERT() function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    def POST(self, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # get now time
            now = datetime.datetime.now()
            now_str = str(now).split('.')[0]

            expires = config.check_secure_val(app.session.expires)

            print "now    : " , now_str
            print "expires: " , expires

            if (now_str > expires): # compare now with time login
                raise config.web.seeother('/logout')

            # session_user = app.session.user
            session_privilege = app.session.privilege # get the session_privilege
            if session_privilege == 0: # admin user
                return self.POST_IMPORT() # call POST_EDIT function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    @staticmethod
    def GET_IMPORT(**k):
        message = None
        return config.render.csv_import(message) # render import.html

    @staticmethod
    def POST_IMPORT(**k):
        csv_file_import = ""
        form = config.web.input(csv_file={})
        filedir = 'static/files/' # change this to the directory you want to store the file in.
        if form.csv_file.filename == "":
            message= "Not selected file!!"
            return config.render.csv_import(message) # render import.html
        else: # to check if the file-object is created
            filepath = form.csv_file.filename.replace('\\','/') # replaces the windows-style slashes with linux ones.
            filename = filepath.split('/')[-1] # splits the and chooses the last part (the filename with extension)
            fout = open(filedir +'/'+ filename,'w') # creates the file where the uploaded file should be stored
            fout.write(form.csv_file.file.read()) # writes the uploaded file to the newly created file.
            csv_file_import = "static/files/"+ filename
            fout.close() # closes the file, upload complete.

        file = open(csv_file_import,"r")
        reader = csv.reader(file)

        for row in reader:
            try:
                user_hash = hashlib.md5(row[0] + config.secret_key).hexdigest() # encrypt user_hash
                config.model.insert_users(
                    row[0], 
                    row[1],  
                    row[2],
                    row[3],
                    row[4],
                    row[5],
                    user_hash
                )
            except Exception as e:
                file.close()
                os.remove(csv_file_import)
                message = "Wrong file format!!"
                print "Import error " + e.message
                return config.render.csv_import(message) # render import.html
        
        file.close()
        os.remove(csv_file_import)
        raise config.web.seeother('/users') # render users index.html
