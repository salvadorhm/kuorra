import shutil
import errno
import sys
from subprocess import call
import os
from model_generator import Model_generator as model_generator
from api_generator import Api_generator as api_generator
from view_generator import View_generator as view_generator
from controller_generator import Controller_generator as controller_generator


version = '0.7.3.0'


def new_base(args):
    name = args[2]
    print 'Creating new project ....'
    print 'Project: {}'.format(name)
    script_path = os.path.abspath(__file__)
    script_dir = os.path.split(script_path)[0]
    rel_path = "mvc_base"
    abs_file_path = os.path.join(script_dir, rel_path)
    #call(['ls -l'], shell = True)
    copyanything(abs_file_path, name)
    print 'Project created succesful'

def new_mvc_gl(args):
    name = args[2]
    print 'Creating new project ....'
    print 'Project: {}'.format(name)
    script_path = os.path.abspath(__file__)
    script_dir = os.path.split(script_path)[0]
    rel_path = "mvc_gl"
    abs_file_path = os.path.join(script_dir, rel_path)
    #call(['ls -l'], shell = True)
    copyanything(abs_file_path, name)
    print 'Project created succesful'

def new_login(args):
    name = args[2]
    print 'Creating new login project ....'
    print 'Project: {}'.format(name)
    script_path = os.path.abspath(__file__)
    script_dir = os.path.split(script_path)[0]
    rel_path = "mvc_sessions"
    abs_file_path = os.path.join(script_dir, rel_path)
    #call(['ls -l'], shell = True)
    copyanything(abs_file_path, name)
    print 'Project created succesful'


def new_forms(args):
    name = args[2]
    print 'Creating new project ....'
    print 'Project: {}'.format(name)
    script_path = os.path.abspath(__file__)
    script_dir = os.path.split(script_path)[0]
    rel_path = "mvc_forms"
    abs_file_path = os.path.join(script_dir, rel_path)
    #call(['ls -l'], shell = True)
    copyanything(abs_file_path, name)
    print 'Project created succesful'


def copyanything(src, dst):
    try:
        shutil.copytree(src, dst)
    except OSError as exc:
        if exc.errno == errno.ENOTDIR:
            shutil.copy(src, dst)
        else:
            raise


def new(args):
    name = args[2]
    print 'Creating new project ....'
    print 'Project: {}'.format(name)
    script_path = os.path.abspath(__file__)
    script_dir = os.path.split(script_path)[0]
    rel_path = "mvc"
    abs_file_path = os.path.join(script_dir, rel_path)
    #call(['ls -l'], shell = True)
    copyanything(abs_file_path, name)
    print 'Project created succesful'


def info():
    print 'kuorra V {}'.format(version)
    print 'Author	: Salvador Hernandez Mendoza'
    print 'Email 	: salvadorhm@gmail.com'
    print 'Twiter 	: @salvadorhm'


def help():
    print ''
    print 'HELP'
    print ''
    print 'kuorra V {}'.format(version)
    print ''
    print 'project_name \t- Project name'
    print 'host \t- Database host'
    print 'db \t- Database name'
    print 'user \t- Database user'
    print 'password- Database password'
    print 'table \t- Database table name'
    print 'port \t- Database port number'
    print ''
    print 'COMMANDS'
    print ''
    print 'kuorra -n project_name -> NEW PROJECT'
    print 'kuorra -nb project_name -> NEW BLANK PROJECT'
    print 'kuorra -nf project_name -> NEW WEB.PY FORMS USE'
    print 'kuorra -nl project_name -> NEW WEB.PY LOGIN PROJECT'
    print 'kuorra -ngl project_name -> NEW WEB.PY GOOGLE LOGIN PROJECT'
    print 'kuorra -d -> DEPLOY PROJECT'
    print 'kuorra -i -> INFORMATION'
    print 'kuorra -am db host user password port-> CREATE ALL TABLES MODELS'
    print 'kuorra -m db table host user password port-> CREATE ONE TABLE MODEL'
    print 'kuorra -aa db host user password port-> CREATE ALL TABLES API'
    print 'kuorra -a db table host user password port-> CREATE ONE TABLE API'
    print 'kuorra -av db host user password port-> CREATE ALL TABLES VIEWS'
    print 'kuorra -v db table host user password port-> CREATE ONE TABLE VIEW'
    print 'kuorra -ac db host user password port-> CREATE ALL TABLES CONROLLERS'
    print 'kuorra -c db table host user password port-> CREATE ONE TABLE CONTROLLER'
    print ''


def deploy():
    try:
        call(['clear'], shell=False)
        print '*******************************************************'
        print '*kuorra V {}'.format(version)
        print '*  kuorra WebApp Deploy'
        print '*  For OPEN use Crtl + click in URL'
        print '*  For STOP use Crtl + C  '
        print '*******************************************************'
        print '*************    kuorra Console       *****************'
        print '*******************************************************\n'
        call(['python app.py'], shell=True)
    except (KeyboardInterrupt, SystemExit):
        print 'kuorra shutdown..'


def all_models(args):
    try:
        name = args[2]
        db_host = args[3]
        db_name = name
        db_user = args[4]
        db_pw = args[5]
        db_port = args[6]

        model = model_generator()

        model.db_host = db_host
        model.db_name = db_name
        model.db_user = db_user
        model.db_pw = db_pw
        model.db_port = int(db_port)

        model.table_name = name

        model.conectar()
        model.generate()
    except Exception as e:
        print 'Error, 100'
        print e.message

def one_model(args):
    try:
        name = args[2]
        db_table = args[3]
        db_host = args[4]
        db_name = name
        db_user = args[5]
        db_pw = args[6]
        db_port = args[7]

        model = model_generator()

        model.db_host = db_host
        model.db_name = db_name
        model.db_user = db_user
        model.db_pw = db_pw
        model.table_name = db_table
        model.db_port = int(db_port)

        model.conectar()
        model.generate_one(db_table)
    except Exception as e:
        print 'Error, 101'
        print e.message


def all_apis(args):
    try:
        name = args[2]
        db_host = args[3]
        db_name = name
        db_user = args[4]
        db_pw = args[5]
        db_port = args[6]

        api = api_generator()

        api.db_host = db_host
        api.db_name = db_name
        api.db_user = db_user
        api.db_pw = db_pw
        api.db_port = dint(db_port)

        api.table_name = name

        api.conectar()
        api.generate()
    except Exception as e:
        print 'Error, 102'
        print e.message


def one_api(args):
    try:
        name = args[2]
        db_table = args[3]
        db_host = args[4]
        db_name = name
        db_user = args[5]
        db_pw = args[6]
        db_port = args[7]

        api = api_generator()

        api.db_host = db_host
        api.db_name = db_name
        api.db_user = db_user
        api.db_pw = db_pw
        api.table_name = db_table
        api.db_port = int(db_port)

        api.conectar()
        api.generate_one(db_table)
    except Exception as e:
        print 'Error, 103'
        print e.message


def all_views(args):
    try:
        name = args[2]
        db_host = args[3]
        db_name = name
        db_user = args[4]
        db_pw = args[5]
        db_port = args[6]

        view = view_generator()

        view.db_host = db_host
        view.db_name = db_name
        view.db_user = db_user
        view.db_pw = db_pw
        view.db_port = int(db_port)

        view.table_name = name

        view.conectar()
        view.generate()
    except Exception as e:
        print 'Error, 104'
        print e.message


def one_view(args):
    try:
        name = args[2]
        db_table = args[3]
        db_host = args[4]
        db_name = name
        db_user = args[5]
        db_pw = args[6]
        db_port = args[7]

        view = view_generator()

        view.db_host = db_host
        view.db_name = db_name
        view.db_user = db_user
        view.db_pw = db_pw
        view.table_name = db_table
        view.db_port = int(db_port)

        view.conectar()
        view.generate_one(db_table)
    except Exception as e:
        print 'Error, 105'
        print e.message


def all_controllers(args):
    try:
        name = args[2]
        db_host = args[3]
        db_name = name
        db_user = args[4]
        db_pw = args[5]
        db_port = args[6]

        controller = controller_generator()

        controller.db_host = db_host
        controller.db_name = db_name
        controller.db_user = db_user
        controller.db_pw = db_pw
        controller.db_port = int(db_port)

        controller.table_name = name

        controller.conectar()
        controller.generate()
    except Exception as e:
        print 'Error, 106'
        print e.message


def one_controller(args):
    try:
        name = args[2]
        db_table = args[3]
        db_host = args[4]
        db_name = name
        db_user = args[5]
        db_pw = args[6]
        db_port = args[7]

        controller = controller_generator()

        controller.db_host = db_host
        controller.db_name = db_name
        controller.db_user = db_user
        controller.db_pw = db_pw
        controller.table_name = db_table
        controller.db_port = int(db_port)

        controller.conectar()
        controller.generate_one(db_table)
    except Exception as e:
        print 'Error, 107'
        print e.message


def main():
    try:
        command = sys.argv[1]
        if command == 'new' or command == '-n':
            new(sys.argv)
        elif command == 'new_base' or command == '-nb':
            new_base(sys.argv)
        elif command == 'new_forms' or command == '-nf':
            new_forms(sys.argv)
        elif command == 'new_login' or command == '-nl':
            new_login(sys.argv)
        elif command == 'new_google_login' or command == '-ngl':
            new_mvc_gl(sys.argv)
        elif command == 'info' or command == '-i':
            info()
        elif command == 'dep' or command == '-d':
            deploy()
        elif command == 'help' or command == '-h':
            help()
        elif command == 'all_models' or command == '-am':
            all_models(sys.argv)
        elif command == 'model' or command == '-m':
            one_model(sys.argv)
        elif command == 'all_apis' or command == '-aa':
            all_apis(sys.argv)
        elif command == 'api' or command == '-a':
            one_api(sys.argv)
        if command == 'all_views' or command == '-av':
            all_views(sys.argv)
        elif command == 'view' or command == '-v':
            one_view(sys.argv)
        elif command == 'all_controllers' or command == '-ac':
            all_controllers(sys.argv)
        elif command == 'controller' or command == '-c':
            one_controller(sys.argv)
        else:
            help()
    except Exception as e:
        print 'Error, 108'
        print e.message

if __name__ == "__main__":
    main()