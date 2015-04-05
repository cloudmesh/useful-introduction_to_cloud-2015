from fabric.api import task, local, settings
import sys
import os
import time
import subprocess



try:
    from cloudmesh_base.util import banner
except:
    os.system("pip install cloudmesh_base")

banner("import")
    
from cloudmesh_base.util import banner
from cloudmesh_base.Shell import Shell

if Shell.which("cm") is None:
    clone()
    local("cd ../cloudmesh; git checkout dev2.0")    
    local("cd ../cloudmesh; ./install system")
    local("cd ../cloudmesh; ./install requirements")
    local("cd ../cloudmesh; ./install cloudmesh")    

banner("compile doc")

browser = "firefox"

if sys.platform == 'darwin':
    browser = "open"


def cmd_exists(cmd):
    return subprocess.call("type " + cmd, shell=True, 
        stdout=subprocess.PIPE, stderr=subprocess.PIPE) == 0

for cmd in ['pandoc','ipython']:    
    if not cmd_exists(cmd):
        print "ERROR: {} is not installed.".format(cmd)
        sys.exit()
    else:
        print cmd, "found. ok."

    
@task
def all():
    html()
    pdf()
    epub()

    
@task
def clean():
    local("rm -rf docs/build/html/notebook/*")

@task
def notebook():
    local("ipython notebook &")
    time.sleep(1)
    local("{browser} docs/build/html/_index_notebooks.html".format(browser=browser))

    
@task
def convert():
    local("bin/convert")
    local("bin/videos.py")
    
@task
def view(kind='html'):
    if kind == 'html':
        """view the documentation in a browser"""
        local("{browser} docs/build/html/index.html".format(browser=browser))
    else:
        local("open docs/build/epub/myCloudmesh.epub")
        
def theme(name='readthedocs'):
    """set name to 'bootstrap' in case you want to use bootstrap.
    This also requires the template sto be in the main dir"""
    
    os.environ['SPHINX_THEME'] = name
    if os.environ['SPHINX_THEME'] == 'bootstrap':
        local('cp docs/source/_templates/layout_bootstrap.html docs/source/_templates/layout.html')
    elif name is 'readthedocs':
        return
    else:
        local('cp docs/source/_templates/layout_simple.html docs/source/_templates/layout.html')
    
@task
def html(theme_name='readthedocs'):
    # disable Flask RSTPAGES due to sphinx incompatibility
    os.environ['RSTPAGES'] = 'FALSE'
    theme(theme_name)
    clone()
    compile()
    api()
    # man()
    """build the doc locally and view"""
    #clean()
    convert()
    local("cd docs; make html")
    local("fab security.check")
    local("touch docs/build/html/.nojekyll")
    
@task
def pdf():
    theme('simple')
    with settings(warn_only=True):
        local("cd docs; echo 'r' | make latexpdf")
    local("cp docs/build/latex/myCloudmesh.pdf docs/build/html/myCloudmesh.pdf")
        
@task
def epub():
    theme('simple')
    with settings(warn_only=True):
        local("cd docs; make epub")
    local("cp docs/build/epub/myCloudmesh.epub docs/build/html/myCloudmesh.epub")
    
@task
def slides():
    # disable Flask RSTPAGES due to sphins incompatibility
    os.environ['RSTPAGES'] = 'FALSE'
    local("cd docs; make slides")

cloudmesh_dirs = ['cloudmesh',
                  'base',
                  'database',
                  'pbs',
                  'timestring',
                  'cmd3']                                            
        
@task
def clone():
    for package in cloudmesh_dirs:
        banner("Installing and Building: " + package)
        if not os.path.isdir("../{0}".format(package)):
            local("cd ..; git clone git@github.com:cloudmesh/{0}.git".format(package))
        else:
            local("cd ..; git pull")
        local ("cd ../{0}; git checkout dev2.0". format("cloudmesh"))
    
@task
def compile():
    for package in cloudmesh_dirs:
        banner("Installing and Building: " + package)
        if not os.path.isdir("../{0}".format(package)):
            local("cd ..; git clone git@github.com:cloudmesh/{0}.git".format(package))
        else:
            local("cd ..; git pull")
        local ("cd ../{0}; git checkout dev2.0; python setup.py install". format(package))
    
    
@task
def fast(theme_name='readthedocs'):
    theme(theme_name)
    local("cd docs; make html")


    
@task
def simple():
    local("cd docs; make html")
            
@task
def publish():
    """deploy the documentation on gh-pages"""
    local("ghp-import -p docs/build/html")
    #html()
    #local('cd docs/build/html && git add .  && git commit -m "site generated" && git push origin gh-pages')
    #local('git commit -a -m "build site"')
    #local("git push origin master")


@task
def man():
    """deploy the documentation on gh-pages"""
    #TODO: match on "Commands"
    local("cm man | grep -A10000 \"Commands\"  | sed \$d  > docs/source/man/man.rst")

@task
def api():
    for modulename in ["cloudmesh", "cmd3", "base", "pbs", "timestring"]:
        print 70 * "="
        print "Building API Doc:", modulename 
        print 70 * "="        
        local("sphinx-apidoc -f -o docs/source/modules/{0} ../{0}".format(modulename))



