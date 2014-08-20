Setup Cloudmesh in an Openstack VM for Testing
======================================================================

Setting up Cloudmesh on a VM is an especially convenient way during
development and testing. To do so, you can follow the steps to run
cloudmesh in a VM running Ubuntu 14.01.1 on FutureGrid Sierra
openstack. If you use a different cloud, you can adapt the
instructions acordingly.

First, you have to start a VM on the cloud and assign it a public
IP. This can be done in multiple ways, using the commandline, vagrant,
or the horizon GUI. Let us assume you have set it up via the GUI. Next
you have to update the operating system while logging into the VM::

  sudo apt-get update
  sudo apt-get install git
  sudo apt-get install emacs  

To obtain cloudmesh you need to clone it from git hub and change to
the cloudmesh directory::

  cd ~
  git clone https://github.com/cloudmesh/cloudmesh.git
  cd cloudmesh

To start the instalation of cloudmesh we first need to install a
number of packages with::

  ./install system

We also recommend that you run virtualenv in python which you can
enable with::

  cd ~
  virtualenv  --no-site-packages ~/ENV
  source ~/ENV/bin/activate

Now let us install cloudmesh into this virtualenv::

  cd cloudmesh
  ./install requirements
  ./install new

The last command will create a number of yaml files in a folder
``.cloudmesh. 

.. todo::  Users: currently the code still installs into .futuregrid please
           change the name for .cloudmesh to .futuregrid for now.

           Developers: lets simply change the cloudmesh code to use
	   .cloudmesh instead of .futuregrid

Now edit the file ``~/.cloudmesh/cloudmesh.yaml` either with emacs or
vi::

  emacs ~/.cloudmesh/cloudmesh.yaml

or::

  vi ~/.cloudmesh/cloudmesh.yaml

In this file, update your user profile, name, project
data. Alternatively, if you already have yaml files on for example
india.yuturegrid.org you can copy your local working yaml files from
that machine to th virtual machine.

Next, edit the file `~/.futuregrid/cloudmesh_server.yaml`::

  vi ~/.futuregrid/cloudmesh_server.yaml

In the attribute cloudmesh->server->webui, make the following changes::
  
  host: 0.0.0.0
  browser: False
    
Next, install the cloudmesh server anad API with:: 

  ./install cloudmesh

To run cloudmesh you will need to start a number of services that you
can do with::

  fab mongo.boot
  fab mongo.boot 

Please make sure to call `fab mongo.boot` twice so the tables and
security settings are done properly. After this update the user data with::

  fab user.mongo
  fab server.start

Then the cloudmesh service should be available via::

   http://PUBLIC_IP_OF_THE_VM:5000

To access the server, you will also need to first open the port 5000
for the VM. By default, you will add the port 5000 to the 'default'
security group. This only need to be done once for a project. 


Essentially you can do this from horizon or nova CLI. We can do this
using cloudmesh too and use this method (We will simplify this step at
a later phase in the project, but for now, you can do this from
command line).

First identify the index of the cloud in which the VM is
running from the cloudmesh.yaml. The index is the sequential number
of the cloud from cloudmesh->active list, counting starting from 0.

Then make proper change of the file test_compute.py under tests. In 
the definition of the setup method in the above mentioned file, 
modify the line::

  self.name = self.configuration.active()[IDX]

with proper IDX. And then run from within the tests directory::

  nosetests test_compute.py:Test.test_20_create_secgroup

This will open the port 5000 so it is accessible from outside.

NOTE:

#. As you might be copying your yaml files into the cloud please
   secure the VM (following good security practice, including but 
   not limited to proper ssh settings disallowing password authentication, 
   securing the location of your private key as well as setting a 
   passphrase, etc.). As this method targets the scenario for rapid 
   dev and testing, it will be a good idea that shuting the vm down 
   after using.

#. As the server is not secured by HTTPS, remember not to use your
   real passwords that you use on other systems to login.

#. This method is only intended for development and tesing, and not
   recommended for real production use.

More information about more sophisticated install instructions are
provided at 

* http://cloudmesh.futuregrid.org/cloudmesh/developer.html#install-the-requirements


