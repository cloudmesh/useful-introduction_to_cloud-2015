Quick Start on your desktop
============================

This quickstart is designed for Ubuntu 14.04 and OSX.

We recommend that you use virtualenv to provide an isolated environmen
t for cloudmesh. We assume you create one called ENV and activate it::

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



To get access to IaaS cloud platforms, you need to create loaclly a
new user that has access to various clouds. In our case we assume you
have an account on FutureGrid.  Please make sure you can login to
india and sierrs::

  $ ssh [username]@india.futuregrid.org
  $ ssh [username]@sierra.futuregrid.org

If this does not work, you may not have uploaded your public key to
FutureGrid. Please do so now. Once this step is completed, you can
create the configuration files as follows::

  $ ./install new
  $ ./install rc fetch
  $ ./install rc fill

The next steps will deploy the futurgrid code prepare the databases::

  $ ./install cloudmesh
  $ fab mongo.start
  $ fab mongo.boot
  $ fab user.mongo
  $ fab mongo.simple

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

.. error:: this method does not yet work 

.. todo:: correct the documentation and the install script

This script can also be executed while getting it from our convenient
instalation script repository. For ubuntu you can use::

  $ curl -sSL https://cloudmesh.github.io/get/ubuntu/ | sh

It will install cloudmesh in the directory where you started it from
and place it in the directory::

  cloudmesh

It creates also a directory called ~/github/cloudmesh and than cds
into this directory to conduct the installation from
there. Furthermore, as you can see this script also creates a virtual
env under the name ~/ENV

If you co not like these names or have a conflict with the names,
please download the script and modify accordingly.

