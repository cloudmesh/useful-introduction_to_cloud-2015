.. _s-cloudmesh-vm-quickstart:

Quickstart for an Openstack VM 
======================================================================


A video about the contents of this page is available on |video-cm-openstack-setup|.

.. |video-image| image:: /images/glyphicons_402_youtube.png 
.. |video-cm-openstack-setup| replace:: |video-image| :youtube:`rcecpgm-47g`


.. highlight:: bash

.. role:: pink

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
the horizon GUI. Let us assume you have set it up via the horizon GUI
or the nova command line. 

To set up a machine you could use the either of the following methods:

* **Horizon**: see `our manual page
  <../../iaas/openstack.html#horizon-gui.html>`_.

* **nova**: see the :ref:`s-openstack`

* **cloudmsh**: see :ref:`s-cloudmesh-quickstart` and the cloudmesh
  shell found elsewhere.


.. note:: FutureSystems Portalname and Project ID
          For this example we assume you have set the shell variable
	  PORTALNAME to your FutureSystems portal username. This can
	  be done as follows. Let us assume your portal name is
	  `albert`. Than you can set it with::

              export PORTALNAME=albert

         We also assume that you have a project id that you set to::

              export PROJECTID=fg101
 
         if it is the number 101.

.. note:: Please note that in the following document we use the
	  :pink:`$USER` and :pink:`$PORTALNAME` are the same values
	  and the portalname needs to be replaced with the portal name
	  you obtained for FutureSystems. As the subsequent steps are
	  all executed on india we can simply use the default
	  :pink:`$USER` shell variable.

However, we use here a commandline approach and use the tools already
installed on india. Thus you do not have to install anything on your
machine. We assume however that you have uploaded the public key of
your machine to the FutureSystems portal so you can log into india.

We summarize the following steps::

  $ ssh $PORTALNAME@india.futuresystems.org
  india$ module load openstack
  india$ source ~/.cloudmesh/clouds/india/juno/openrc.sh

.. important::

   If you are following this as part of a class, make sure you source
   the appropriate ``rc`` file **after** to the ``openrc.sh``.
   Check for the available files like so::

     $ ls .cloudmesh/clouds/india/juno/
     cacert.pem  fg455  fg465  fg82  openrc.sh

   If you are in the ``FG465`` course, load the appropriate settings::

     $ source .cloudmesh/clouds/india/juno/fg465


In order to log into the machine (once we start it up later),
OpenStack needs to have an ssh keypair associated.  You can either
have OpenStack create a key for you or import your current key.

To **import** a pre-existing key, such as ``~/.ssh/id_rsa.pub``, do the following::

  $ nova keypair-add --pub-key ~/.ssh/id_rsa.pub $USER-india-key

This will associate your ``~/.ssh/id_rsa.pub`` key with the name ``$USER-india-key``.

**Alternatively**, to have OpenStack create a key for you, execute the following::

  $ nova keypair-add $USER-india-key >~/.ssh/$USER-india-key
  $ chmod 600 ~/.ssh/$USER-india-key

This will generate the key, import it into OpenStack, and ``chmod``
will fix permissions on the file.

.. warning:: Remember to set a passphrase once prompted to secure your private key.

             You must not use a passphrase less key! Please specify a
	     strong passphrase.

Next step is to open the necessary ports of the VM to be started::

  india$ nova secgroup-add-rule default icmp -1 -1 0.0.0.0/0
  india$ nova secgroup-add-rule default tcp 22 22 0.0.0.0/0
  india$ nova secgroup-add-rule default tcp 8888 8888 0.0.0.0/0
  india$ nova secgroup-add-rule default tcp 5000 5000 0.0.0.0/0
  india$ nova secgroup-list-rules default

Now you can boot a VM and set public ip for external access::

  india$ nova boot --flavor m1.small --image "futuresystems/ubuntu-14.04" --key_name $USER-india-key $USER-001

  india$ nova floating-ip-create ext-net

  india$ export MYIP=`nova floating-ip-list | grep "| -" | cut -d '|' -f3 | head -1`
  india$ nova add-floating-ip $USER-001 $MYIP
  india$ nova show $USER-001

You should see a table similar to this::

    +--------------------------------------+-------------------------------------------------------------------+
    | Property                             | Value                                                             |
    +--------------------------------------+-------------------------------------------------------------------+
    | OS-DCF:diskConfig                    | MANUAL                                                            |
    | OS-EXT-AZ:availability_zone          | nova                                                              |
    | OS-EXT-STS:power_state               | 1                                                                 |
    | OS-EXT-STS:task_state                | -                                                                 |
    | OS-EXT-STS:vm_state                  | active                                                            |
    | OS-SRV-USG:launched_at               | 2015-03-26T18:17:45.000000                                        |
    | OS-SRV-USG:terminated_at             | -                                                                 |
    | accessIPv4                           |                                                                   |
    | accessIPv6                           |                                                                   |
    | config_drive                         |                                                                   |
    | created                              | 2015-03-26T18:17:39Z                                              |
    | flavor                               | m1.small (2)                                                      |
    | hostId                               | 1094ef059b959406822d0a0517873b8cb03363d700019913ebd9f636          |
    | id                                   | ad81e08f-9827-4a37-b029-xxxxxxxx                                  |
    | image                                | futuresystems/ubuntu-14.04 (6a6a3474-8194-44ac-9f56-70cb93207f21) |
    | int-net network                      | 10.23.1.xxx, 149.165.xxx.xxx                                      |
    | key_name                             | xxx-india-key                                                     |
    | metadata                             | {}                                                                |
    | name                                 | xxx-001                                                           |
    | os-extended-volumes:volumes_attached | []                                                                |
    | progress                             | 0                                                                 |
    | security_groups                      | default                                                           |
    | status                               | ACTIVE                                                            |
    | tenant_id                            | c7e8f17828fb48309e38axxxxxxxxxxxx                                 |
    | updated                              | 2015-03-26T18:17:45Z                                              |
    | user_id                              | 433181ac60be4115a51axxxxxxxxxxxx                                  |
    +--------------------------------------+-------------------------------------------------------------------+


Looking at the status you will see if the VM is in ACTIVE
state. Repeat the command::

    india$ nova show $USER-001

if necessary. Once this is the case you can login to it with::

  india$ ssh -i ~/.ssh/id_rsa -l ubuntu $MYIP



Cloudmesh Installation
----------------------------------------------------------------------

Systems Dependencies
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Installation of cloudmesh can be complicated. We provide a oneline
script to install::

  $ curl https://raw.githubusercontent.com/cloudmesh/get/master/cloudmesh/ubuntu/14.04.sh | venv=$HOME/ENV bash

.. note:: This may take several minutes.

Please see :ref:`ref-cloudmesh-quickstart-system-install-curl` for
details on what this does.

You now need to activate the virtualenv created::

  $ source $HOME/ENV/bin/activate


Cloudmesh Setup
----------------------------------------------------------------------

As part of its installation, cloudmesh create a ``~/.cloudmesh``
directory with several yaml files. Now we need to populate the
cloudmesh.yaml file with your actual cloud credentials.  Cloudmesh
provides tools for you to retrieve your futuresystems cloud credential
and configure the cloudmesh.yaml file properly. Before we can use it
however we have to create a key that we upload to the FutureSystems
portal::

 $ export PORTALNAME=<put your portal name here>
 $ ssh-keygen -t rsa -C $PORTALNAME-ubuntu-vm-key

Than lets add the key to the ssh agent::

  $ eval `ssh-agent -s`
  $ ssh-add
  
Then you need to add the key to your FutureSystems portal account. 
Please visit the portal and paste the content of the public
key in the appropriate field. You can get the content of the key by ::

  $ cat ~/.ssh/id_rsa.pub

At this point you should be able to connect to india from this VM which is 
required by the following commands.

Now you can fetch the information you need to acces openstack form india::

  $ cm-iu user fetch
  $ cm-iu user create
  
It's also recommended you manually edit the file `~/.cloudmesh/cloudmesh.yaml` 
either with emacs or vi::

  $ emacs ~/.cloudmesh/cloudmesh.yaml

or::

  $ vi ~/.cloudmesh/cloudmesh.yaml

In this file, update your user profile, name, project data, etc.


In order to start the cloudmesh web server that is accessible to outside,
we also need to undertake some changes for the india OpenStack cloud 
configuration with ::
  
  $ fab india.configure
    
To run cloudmesh you will need to start a number of services. The first
is to create and initialize the cloudmesh database. Here we will use the command::

  $ fab mongo.reset

Please note that this command will erase the previous database and you
should be carefully considering its use. When you initialize the
cloudmesh server first this is the best method.  

.. note:: Also note that this command will take a long time on
	  machines that do not have SSD's due to the way mongo sets up
	  the database. Be patient and do not interrupt the program
	  although it may run multiple minutes.


Now you are ready to start all services for cloudmesh with::

  $ fab server.start

Then the cloudmesh service should be available via::

   http://PUBLIC_IP_OF_THE_VM:5000

If you forgot your IP, use the command::

  $ echo $MYIP


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
   recommended for real production use. If you have that intention,
   you can configure the system to use nginx+uwsgi to put cloudmesh
   user secure SSL channel.
