from fabric.api import run, local

def auth():
    USERNAME = raw_input("Username: ")
    PASSWORD = raw_input("Password: ")
    return (USERNAME, PASSWORD)

def banner(msg):
    print 70 * "#"
    print msg
    print 70 * "#"

def run():
    local("python ./manage.py runserver")

def install():
    loacl("python install -r requirements.txt")
          
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
