from fabric.api import run, local
import sys


if sys.platform == 'darwin':
    browser = "open"
else:
    browser = "firefox"    


def auth():
    USERNAME = raw_input("Username: ")
    PASSWORD = raw_input("Password: ")
    return (USERNAME, PASSWORD)

def view():
    local("{browser} http://127.0.0.1:8000/".format(browser=browser))
    
def doc():
    local("{browser} http://127.0.0.1:8000/docs".format(browser=browser))
    
def banner(msg):
    print 70 * "#"
    print msg
    print 70 * "#"

def run():
    local("python ./manage.py runserver")

def install():
    local("pip install -r requirements.txt")

def db():
    local("python manage.py syncdb")
          
def users(USERNAME, PASSWORD):    
    banner ("users")
    local("curl -H 'Accept: application/json; indent=4' -u {0}:{1} http://127.0.0.1:8000/users/".format(USERNAME,PASSWORD))

def groups(USERNAME, PASSWORD):    
    banner("groups")
    local("curl -H 'Accept: application/json; indent=4' -u {0}:{1} http://127.0.0.1:8000/groups/".format(USERNAME,PASSWORD))

def test():
    USERNAME, PASSWORD = auth()
    users(USERNAME, PASSWORD)
    groups(USERNAME, PASSWORD)

def clean():
    local("rm -f *.sqlite3")
    local("rm -f *.pyc */*.pyc")    
