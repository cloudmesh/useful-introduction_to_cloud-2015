Quickstart for an Openstack VM 
======================================================================

.. note:: This setup is primarily used for testing, but it can also be
	  useful for classes using OpenStack, when the call
	  participants have access to an OpenStack cloud. 

Setting up Cloudmesh on a VM is an especially convenient way during
development and testing. To do so, you can follow the steps to run
cloudmesh in a VM running Ubuntu 14.04 on FutureSystems `India`
OpenStack. The instructions have been tested on a small instance 
and the whole process could take about half an hour before you 
can access the running server.

Requirements
----------------------------------------------------------------------

We assume that you have set up an account on FutureSystems and are
able to log into the machine with the name india.


If you use a different cloud, you can adapt the instructions
accordingly.

Starting the VM
----------------------------------------------------------------------

First, you have to start a VM on the cloud and assign it a public IP. 

This can be done in multiple ways, using the command line, vagrant, or
the horizon GUI. Let us assume you have set it up via the horizon
GUI or the novaclient commandline. This is described in the following document:

More information about horizon on FutureSystems is available at `our
manual page <../../iaas/openstack.html#horizon-gui.html>`_.

We summarize the following steps, however like to point out that the
best source for this is our previously pointed out document.::

  ssh <portalname>@india.futuresystems.org
 
  india$ source ~/.futuregrid/openstack_havana/novarc
  india$ nova keypair-add --pub-key ~/.ssh/id_rsa.pub $USER-india-key

  india$ nova secgroup-add-rule default icmp -1 -1 0.0.0.0/0
  india$ nova secgroup-add-rule default tcp 22 22 0.0.0.0/0
  india$ nova secgroup-add-rule default tcp 8888 8888 0.0.0.0/0
  india$ nova secgroup-add-rule default tcp 5000 5000 0.0.0.0/0
  india$ nova secgroup-list-rules default

  india$ nova boot --flavor m1.small --image "futuregrid/ubuntu-14.04" --key_name $USER-india-key $USER-001


  india$ nova floating-ip-create

  india$ export MYIP=`nova floating-ip-list |fgrep "None" | cut -d '|' -f2`
  india$ nova add-floating-ip $USER-001 $MYIP
  india$ nova show $USER-001

You should see a table similare like this::

  +--------------------------------------+----------------------------------------------------------------+
  | Property                             | Value                                                          |
  +--------------------------------------+----------------------------------------------------------------+
  | status                               | ACTIVE                                                         |
  | updated                              | 2014-09-12T19:27:30Z                                           |
  | OS-EXT-STS:task_state                | None                                                           |
  | private network                      | 168.39.1.34, 192.165.159.40                                    |
  | key_name                             | USER-key                                                       |
  | image                                | futuregrid/ubuntu-14.04 (02cf1545-dd83-493a-986e-583d53ee3728) |
  | hostId                               | hsakjfhsdlkjfhsdlkjhflskjdhflkjsdhflkjshfpoeuiyrewuohfkljsdkjk |
  | OS-EXT-STS:vm_state                  | active                                                         |
  | OS-SRV-USG:launched_at               | 2014-09-12T19:27:30.000000                                     |
  | flavor                               | m1.small (2)                                                   |
  | id                                   | 7e458cbd-d37d-443a-aa76-adc7fcad52ea                           |
  | security_groups                      | [{u'name': u'default'}]                                        |
  | OS-SRV-USG:terminated_at             | None                                                           |
  | user_id                              | sjhkjsahflkjashfkljshfkdjsahfkjh                               |
  | name                                 | USER-001                                                       |
  | created                              | 2014-09-12T19:27:23Z                                           |
  | tenant_id                            | abcd01234hfslkjhfdskjfhkjdshfkjs                               |
  | OS-DCF:diskConfig                    | MANUAL                                                         |
  | metadata                             | {}                                                             |
  | os-extended-volumes:volumes_attached | []                                                             |
  | accessIPv4                           |                                                                |
  | accessIPv6                           |                                                                |
  | progress                             | 0                                                              |
  | OS-EXT-STS:power_state               | 1                                                              |
  | OS-EXT-AZ:availability_zone          | nova                                                           |
  | config_drive                         |                                                                |
  +--------------------------------------+----------------------------------------------------------------+

Looking at the status you will see if the VM is in ACTIVE state. Once this is the case you can login to it with::

  india$ ssh -i ~/.ssh/id_rsa.pub ubuntu@$MYIP



Preparation of the VM
----------------------------------------------------------------------

Next you have to update the operating system while logging into
the VM::

  sudo apt-get update
  sudo apt-get install git

To obtain cloudmesh you need to clone it from git hub and change to
the cloudmesh directory::

  cd ~
  git clone https://github.com/cloudmesh/cloudmesh.git
  cd cloudmesh

The first thing you have to do is to fix some ip addresses on india
with the command::

  ./bin/fix-india-routing.sh 

Instalation
----------------------------------------------------------------------

To start the installation of cloudmesh we first need to install a
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

The last command will create a number of yaml files in a folder::

  ~.cloudmesh
    
Next, install the cloudmesh server anad API with:: 

  ./install cloudmesh

Now we need to populate the cloudmesh.yaml file with your actual
information. You can edit the file ``~/.cloudmesh/cloudmesh.yaml` 
either with emacs or vi::

  emacs ~/.cloudmesh/cloudmesh.yaml

or::

  vi ~/.cloudmesh/cloudmesh.yaml

In this file, update your user profile, name, project
data. Alternatively, if you already have yaml files on for example
india.FutureSystems.org you can copy your local working yaml files from
that machine to th virtual machine.

Yet another alternative is to use the functionality provided by cloudmesh::

  cm-iu user fetch
  cm-iu user create

This will fetch your cloud credentials from FutureSystems and populate them 
into the yaml config file. BEFORE you can do this, make sure you can log into 
the FutureSystems resources, e.g. india. You will need a private key present 
in the VM that the matching public ssh key had been registered to the FutureSystems. 
Additionally you may need to excetue the following beforehand to add your 
password protected key into the session::

  eval `ssh-agent -s`
  ssh-add
  
To run cloudmesh you will need to start a number of services that you
can do with::

  fab mongo.boot

In some cases you may see connection problems in the later step. In that case 
please execute this command one again so the tables and security settings 
are done properly.

Once the mongo is initiated properly it's time to update the user data with::

  fab user.mongo

Before you start the server, you need to execute this so the server
would be accessible from outside::
  
  fab india.configure
    
And then start the server::

  fab server.start

Then the cloudmesh service should be available via::

   http://PUBLIC_IP_OF_THE_VM:5000


NOTE:

#. As you might be copying your yaml files into the cloud please
   secure the VM (following good security practice, including but 
   not limited to proper ssh settings disallowing password authentication, 
   securing the location of your private key as well as setting a 
   passphrase, etc.). As this method targets the scenario for rapid 
   dev and testing, it will be a good idea that shutting the vm down 
   after using.

#. As the server is not secured by HTTPS, remember not to use your
   favorite password when you are asked to set a password for portal login.

#. This method is only intended for development and testing, and not
   recommended for real production use.

More information about more sophisticated install instructions are
provided at 

* http://cloudmesh.futuregrid.org/cloudmesh/developer.html#install-the-requirements


Install IPython
----------------------------------------------------------------------

::
  
   fab ipython.create


::
  
   fab ipython.start


