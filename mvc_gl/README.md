# Kuorra login with Google API oauth 2.0

## Introduction

Kuorra is a Web.py Microframework Frontend, use kuorra to create a MVC skeleton for work with Web.py, MySQL and Heroku App.


## GOOGLE API OAUTH2.0

1. For use the google API oauth2.0 first is needed create a proyect in google developer console at next link

    - [Google Developer Console](https://console.developers.google.com)

2. Select the proyect created and create credencials in the next link

    - [Google Developer Credentials](https://console.developers.google.com/apis/credentials)

3. Create  ID client for OAuth

    - Choose Web Application.

    - Give a name to the Application.

    - URI redirection, choose:
        - For work in local:
            - http://localhost:8080/auth/google/callback
        - For work in the web:
            - http://yourwebserver.com:8080/auth/google/callback
            - or
            - http://proyect.herokuapp.com/auth/google/callback

    - GET tokens for use in **app.py**
        - app_id 
        - app_secret


## Content

This template have the next functions

### Functions

+ Script for create a **kuorra_login_google** DB
    - *users table*
    - *sessions table*
    - *logs table*
    - Create an DB user: 
        - **kuorra_google** 
    - Create an DB password:
        - **kuOrra.2018**

+ Config one DB conection.

+ Create a **users Controller**.

    - *index*
    - *view*
    - *edit*
    - *delete*
    - *insert*
    - *config*
    - *printer*
    - *import*


+ Create a **main Controller**

    - *auth*
    - *index*
    - *login*
    - *logout*
    - *config*

+ Create a **logs Controller**

    - *config*
    - *index*
    - *printer*
    - *view*
    - *url.md*

+ Create a **Logs Model**
    - *get_all_logs*
    - *insert_logs*

+ Create a **users Model**
    - *validate_user*
    - *get_all_users*
    - *get_users*
    - *delete_users*
    - *insert_users*
    - *edit_users*

+ Create a **users View**
    - *csv_import*
    - *delete*
    - *edit*
    - *index*
    - *insert*
    - *master*
    - *printer*
    - *view*

+ Create a **main View**
    - *admin*
    - *guess*
    - *index*
    - *login*
    - *master*

+ Create a **logs View**
    - *index*
    - *master*
    - *printer*
    - *view*
