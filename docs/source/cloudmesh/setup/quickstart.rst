Quick Start on your desktop
============================

This quickstart is designed for Ubuntu 14.04 and OSX.

We recommend that you use virtualenv to provide an isolated environment 
for cloudmesh. We assume you create one called ENV and activate it::

  virtualenv ~/ENV
  $ source ~/ENV/bin/activate

Firts you need to download the code from github. We assume you have
git installed::
   
  $ git clone https://github.com/cloudmesh/cloudmesh.git

Next, you need to install a number of required packages with the
following commands::


  $ cd cloudmesh
  $ sudo ./install system
  $ ./install requirements

.. note:: on OSX you can ommit the sudo. 


To get access to IaaS cloud platforms, you need to create loaclly a
new user that has access to various clouds. This can be done with::

  $ ./install new

The next steps will deploy the cloudmesh code into the virtualenv
library path::

  $ ./install cloudmesh


.. note:: This step is optional

   In case you have accounts on the IU machines yo ucan also obtain
   preconfigured cloud rc files from them. To test if you have an account
   and have set it up correctly, please login to the machine india::

     $ ssh [username]@india.futuregrid.org

   If this does not work, you may not have uploaded your public key to
   FutureGrid portal at

   * https://portal.futuregrid.org/my/ssh-keys

   Once this step is completed, you can
   create the configuration files as follows::

     $ cm-iu user fetch
     $ cm-iu user create

The next steps will deploy the cloudmesh databases::

  $ fab mongo.start
  $ fab mongo.boot
  $ fab user.mongo
  $ fab mongo.simple

Thes steps are conveniently wrapped into a single command::

  $ fab mongo.reset

To start the cloudmesh services use::

  $ fab server.start

Now you cen test the services by visiting the Web interface at
http://127.0.0.1:5000. We have a convenient shortcut for this by
typing:: 

  $ fab server.view

Alternatively you can use the cloudmesh shell by invoking the cm
command ina aterminal::

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
  | india_openstack_havana   |          |
  +--------------------------+----------+
  | sierra_eucalyptus        |          |
  +--------------------------+----------+
  | sierra                   |          |
  +--------------------------+----------+

  cm> cloud on sierra
  ...
  cloud 'sierra' activated.

  cm> flavor sierra --refresh
  ...
  Refresh time: 0.190665006638
  Store time: 0.0578060150146
  +--------+------+--------------+---------+-------+--------+----------------------+
  | CLOUD  |   id | name         |   vcpus |   ram |   disk | cm_refresh           |
  |--------+------+--------------+---------+-------+--------+----------------------|
  | sierra |    1 | m1.tiny      |       1 |   512 |      0 | 2014-08-26T01-15-20Z |
  | sierra |    3 | m1.medium    |       2 |  4096 |     40 | 2014-08-26T01-15-20Z |
  | sierra |    2 | m1.small     |       1 |  2048 |     20 | 2014-08-26T01-15-20Z |
  | sierra |    4 | m1.large     |       4 |  8192 |     40 | 2014-08-26T01-15-20Z |
  | sierra |    7 | m1.memmedium |       1 |  4096 |     20 | 2014-08-26T01-15-20Z |
  | sierra |    6 | m1.memlarge  |       1 |  8192 |     20 | 2014-08-26T01-15-20Z |
  +--------+------+--------------+---------+-------+--------+----------------------+


Commands without description
----------------------------------------------------------------------

::

  git clone https://github.com/cloudmesh/cloudmesh.git
  virtualenv ~/ENV
  source ~/ENV/bin/activate
  cd cloudmesh
  sudo ./install system
  ./install requirements
  ./install new
  ./install rc fetch
  ./install rc fill
  ./install cloudmesh
  fab mongo.start
  fab mongo.boot
  fab user.mongo
  fab mongo.simple
  fab server.start
  cm cloud list
  cm cloud on sierra
  cm flavor sierra --refresh

One line install with curl
----------------------------------------------------------------------

.. .. error:: this method does not yet work 

.. .. todo:: correct the documentation and the install script

.. development:: It may not work properly in some platforms. Please do step-by-step installation above in that case.

This script can also be executed while getting it from our convenient
instalation script repository. For ubuntu you can use::

  $ curl -sSL https://cloudmesh.github.io/get/ubuntu/ | username=[your Futuregrid portal id] sh

It will install cloudmesh in the directory where you started it from
and place it in the directory::

  cloudmesh

It creates also a directory called ~/github/cloudmesh and then cds
into this directory to conduct the installation from
there. Furthermore, as you can see this script also creates a virtual
env under the name ~/ENV

If you do not like these names or have a conflict with the names,
please download the script and modify accordingly.

