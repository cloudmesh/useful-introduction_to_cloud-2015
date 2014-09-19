Quick Start on your desktop
============================

.. warning:: this tutorial is for the new FutureSystems
	  infrastructure. However at this time we still use
	  FutureGrid. Please replace all occurrences of FutureSystems
	  with FutureGrid. 

This quickstart is designed for Ubuntu 14.04 and OSX.

We recommend that you use virtualenv to provide an isolated environment 
for cloudmesh. We assume you create one called ENV and activate it::

  virtualenv ~/ENV
  $ source ~/ENV/bin/activate

First you need to download the code from github. We assume you have
git installed::
   
  $ git clone https://github.com/cloudmesh/cloudmesh.git

Next, you need to install a number of required packages with the
following commands::


  $ cd cloudmesh
  $ sudo ./install system
  $ ./install requirements

.. note:: on OSX you can omit the sudo. 

To get access to IaaS cloud platforms, you need to create locally a
new user that has access to various clouds. This can be done with::

  $ ./install new

The next steps will deploy the cloudmesh code into the virtualenv
library path::

  $ ./install cloudmesh


.. note:: This step is optional but highly recommended for users.

   In case you have accounts on the IU machines you can also obtain
   pre-configured cloud rc files from them. To test if you have an account
   and have set it up correctly, please login to the machine india::

     $ ssh [username]@india.futuresystems.org

   If this does not work, you may not have uploaded your public key to
   FutureSystems portal at

   * https://portal.futuresystems.org/my/ssh-keys

   Once this step is completed, you can
   create the configuration files as follows::

     $ cm-iu user fetch
     $ cm-iu user create

At this time we like you to edit some information about yourself in
the cloudmesh.yaml file. Choose your favorite editor::

  $ emacs ~/.cloudmesh/cloudmesh.yaml

Change the values TBD that you find here with values that describe
you. 

.. .. todo:: Hyungro: cm "default username=username <portalname>"

.. .. todo:: Hyungro: cm "project fg101"  101 is just a placeholder use your real
	  project id
	  
As you will need at one point to login into virtual machines you will
need a key that cloudmesh can use do to so. We assume you have a
public key generated in your .ssh directory in the file::

  ~/.ssh/id_rsa.pub

If you do not have such a key, you can generate it with::

 ssh-keygen -t rsa -C portalname-key

The next steps will deploy the cloudmesh database::

  $ fab mongo.reset

We add the key to the database with::

   $ cm "key add --keyname=portalname-key ~/.ssh/id_rsa.pub"

where portal name is your name for the FutuerSystems portal.

You may next need to specify your default project if you have not yet
done so::
   
     $ cm project default [project id]
     
   *[project id]* is your default project id from FutureSystems e.g. fg455 as an example
   
To start Cloudmesh use::

  $ fab server.start

Now you can test the service by visiting the web interface at
http://127.0.0.1:5000. We have a convenient shortcut for this by
typing:: 

  $ fab server.view

Alternatively you can use the cloudmesh shell by invoking the cm
command via a terminal::

  $ cm
  
  ======================================================
  / ___| | ___  _   _  __| |_ __ ___   ___  ___| |__
  | |   | |/ _ \| | | |/ _` | '_ ` _ \ / _ \/ __| '_ \
  | |___| | (_) | |_| | (_| | | | | | |  __/\__ \ | | |
  \____|_|\___/ \__,_|\__,_|_| |_| |_|\___||___/_| |_|
  ======================================================
  Cloudmesh Shell
  
  cm> cloud
  +--------------------------+----------+
  | cloud                    | active   |
  +==========================+==========+
  | alamo                    |          |
  +--------------------------+----------+
  | aws                      |          |
  +--------------------------+----------+
  | azure                    |          |
  +--------------------------+----------+
  | dreamhost                |          |
  +--------------------------+----------+
  | hp                       |          |
  +--------------------------+----------+
  | hp_east                  |          |
  +--------------------------+----------+
  | india_eucalyptus         |          |
  +--------------------------+----------+
  | india                    |          |
  +--------------------------+----------+
  | sierra_eucalyptus        |          |
  +--------------------------+----------+
  | sierra                   |          |
  +--------------------------+----------+

  cm> cloud on india
  ...
  cloud 'india' activated.

  cm> flavor india --refresh
  ...
  Refresh time: 0.190665006638
  Store time: 0.0578060150146
  +--------+------+--------------+---------+-------+--------+----------------------+
  | CLOUD  |   id | name         |   vcpus |   ram |   disk | cm_refresh           |
  |--------+------+--------------+---------+-------+--------+----------------------|
  | india |    1 | m1.tiny      |       1 |   512 |      0 | 2014-08-26T01-15-20Z |
  | india |    3 | m1.medium    |       2 |  4096 |     40 | 2014-08-26T01-15-20Z |
  | india |    2 | m1.small     |       1 |  2048 |     20 | 2014-08-26T01-15-20Z |
  | india |    4 | m1.large     |       4 |  8192 |     40 | 2014-08-26T01-15-20Z |
  | india |    7 | m1.memmedium |       1 |  4096 |     20 | 2014-08-26T01-15-20Z |
  | india |    6 | m1.memlarge  |       1 |  8192 |     20 | 2014-08-26T01-15-20Z |
  +--------+------+--------------+---------+-------+--------+----------------------+


Commands without description
----------------------------------------------------------------------


This script assumes that you have a key in::

  ~/.ssh/id_rsa.pub

Which will be used to log into the VMs and the machines. This key must
be uploaded to the FutureSystems portal.

First, please set the PORTALNAME in your shell::

   export PORTALNAME=[name of your user account in FutureSystem]

For ubuntu use
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

::

  git clone https://github.com/cloudmesh/cloudmesh.git
  virtualenv ~/ENV
  source ~/ENV/bin/activate
  cd cloudmesh
  sudo ./install system

Next execute::

  ./install requirements
  ./install new
  ./install cloudmesh
  cm-iu user fetch --username=$PORTALNAME
  cm-iu user create
  fab mongo.reset

Next execute::

  fab server.start
  cm cloud list
  cm cloud on india
  cm flavor india --refresh


For OSX use
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

::

  git clone https://github.com/cloudmesh/cloudmesh.git
  virtualenv ~/ENV
  source ~/ENV/bin/activate
  cd cloudmesh
  ./install system

Next execute::

  ./install requirements
  ./install new
  ./install cloudmesh
  cm-iu user fetch --username=$PORTALNAME
  cm-iu user create
  fab mongo.reset

Next execute::

  fab server.start
  cm cloud list
  cm cloud on india
  cm flavor india --refresh


One line install with curl
----------------------------------------------------------------------

.. .. error:: this method does not yet work 

.. .. todo:: correct the documentation and the install script

.. development:: It may not work properly in some platforms. Please do step-by-step installation above in that case.

This script can also be executed while getting it from our convenient
instalation script repository. For ubuntu you can use::

  $ curl -sSL https://cloudmesh.github.io/get/ubuntu/ | username=[your FutureSystems portal id] sh

It will install cloudmesh in the directory where you started it from
and place it in the directory::

  cloudmesh

It creates also a directory called `./github/cloudmesh` and then cds
into this directory to conduct the installation from
there. Furthermore, as you can see this script also creates a virtual
env under the name ~/ENV

If you do not like these names or have a conflict with the names,
please download the script and modify accordingly.

After you have installed cloudmesh it is important to set a different
password for the local cloudmesh user. This is done with::

   cd fab user.mongo


Tips
----------------------------------------------------------------------

If you lost the cursor on your terminal, you can use the command::

   reset 

to bring the terminal in its default settings.

