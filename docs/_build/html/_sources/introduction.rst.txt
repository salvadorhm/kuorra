# kuorra

## Introduction


Kuorra is a WebApp Model, it's based on MVC Pattern, and use Web.py like Microframework.

Use Kuorra to create a MVC skeleton for work with Web.py, MySQL and Heroku App.

****

## Kuorra Model

![Alt text](images/kuorra.svg?raw=true "Kuorra model")

***

## Install Kuorra

+ In a terminal write **python -m pip install kuorra**, this download all requirements packages.

![Alt text](images/install_kuorra.png?raw=true "Kuorra model")

+ When finish you can use kuorra

![Alt text](images/kuorra_installed.png?raw=true "Kuorra model")


****

## Upgrade Kuorra

+ In a terminal write **python -m pip install kuorra ---upgrade**, this update all requirements packages.

![Alt text](images/kuorra_upgrade.png?raw=true "Kuorra model")

****

## Functions

+ Script for create a demo DB.

+ Config one DB conection.

+ Create a products **Controller**.

  - *Index* **[index.py]**
  - *View* **[view.py]**
  - *Edit* **[edit.py]**
  - *Delete* **[delete.py]**
  - *Insert* **[insert.py]**

+ Create a products **Model**. **[model_products.py]**

  - *get_all_products*
  - *get_products*
  - *delete_products*
  - *insert_products*
  - *edit_products*

+ Create a products **Views**:

  - *Index* **[index.html]**
  - *View* **[view.html]**
  - *Edit* **[edit.html]**
  - *Delete* **[delete.html]**
  - *Insert* **[insert.html]**
  - *Master* **[master.html]** Web Template

+ Create a products **API**. **[api_products.py]**

  - *GET all products* (GET)
  - *GET one product* (GET id)
  - *INSERT one product* (PUT id, fields)
  - *DELETE one product* (DELETE id)
  - *UPDATE one product* (UPDATE id, fields)

7. Active a SSL connection

****
# How to Use Kuorra

## Create new project

**kuorra new project_name**

![Alt text](images/kuorra_new.png?raw=true "kuorra new")

+ Acme Store MVC Skeleton

![Alt text](images/vs_code.png?raw=true "vs code")

****

## Config new project

+ The new project have a demo database  called **acme_store_mvc**, with a products table.

+ The database script is written in the file **data + schema.sql**.

![Alt text](images/schme.png?raw=true "schema")

+ Connect to MySQL server using *mysql cli*, *mysql workbench* or any other application.

![Alt text](images/mysql_0.png?raw=true "mysql cli")

+ Execute the script **schema.sql** for create the DB.

![Alt text](images/mysql_1.png?raw=true "source schema.sql")

+ Products table

![Alt text](images/products.png?raw=true "Products table")

+ In the file **application + models + model_products.py** modify the connection parameters

  - **db_host** = 'localhost'
  - **db_name** = 'acme_store_mvc'
  - **db_user** = 'your user name'
  - **db_pw** = 'your password'

![Alt text](images/config.png?raw=true "Config")

****

## Deploy project

+ Into de folder where is the **app.py** file execute **kuorra dep** for deploy de WebApp.

**kuorra dep**

![Alt text](images/kuorra_dep.png?raw=true "kuorra dep")

+ For stop de server press **Ctrl + C**.

![Alt text](images/kuorra_stop.png?raw=true "Stop")

****

## Acme store Demo

+ https://localhost:8080/

![Alt text](images/kuorra_index.png?raw=true "index.html")

****

+ https://localhost:8080/products/view/1

![Alt text](images/kuorra_view.png?raw=true "view.html")

****

+ https://localhost:8080/products/insert

![Alt text](images/kuorra_insert.png?raw=true "insert.html")

****

+ https://localhost:8080/products/delete/1

![Alt text](images/kuorra_delete.png?raw=true "delete.html")

****

+ https://localhost:8080/products/edit/1

![Alt text](images/kuorra_edit.png?raw=true "edit.html")

****

##### Author Salvador Hernández Mendoza
##### Email salvadorhm@gmail.com
##### Twitter @salvadorhm