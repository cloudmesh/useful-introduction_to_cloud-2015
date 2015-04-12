.. _ref-class-lesson-devops-exercises:

SaltStack
======================================================================

Overview
----------------------------------------------------------------------

This lesson will introduce you to a very important topic to Salt (or
SaltStack), a configuration management system.

.. tip:: Duration: 1 hour

Prerequisite
----------------------------------------------------------------------

In order to conduct this lesson you should have knowledge of

* `Shell Access <../shell-access.html>`_
* `Package Managers <../linux/packagemanagement.html>`_

Description
----------------------------------------------------------------------

Salt or SaltStack is a open source software for managing configurations and
execution application. It is written in Python and runs with ZeroMQ which is an
asynchronous messaging library. Salt is similar to Puppet, Ansible and Chef.

For more introduction to Salt, see here:
http://docs.saltstack.com/en/latest/topics/index.html

Salt Installation
-------------------------------------------------------------------------------

Salt can be installed by package management tools or a simple installation
script. This lesson is based on FutureSystems which means you create a VM
instance on India OpenStack and install Salt on top of it. We assume you use a
OpenStack instance on FutureSystems.

.. note:: If don't know how to launch a new instance? `See here
    <../iaas/openstack.html#launching-a-new-instance>`_

Guideline on India FutureSystems
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

You *DON'T* install Salt on India. If you see the cursor like:

::

  [albert@i136 ~]$

You *should NOT* install any program.

You have to log into *your VM instance* to install Puppet. ``i136`` is a India
login node which is like a gateway.  You are supposed not to perform any tasks
on India, especially if you require ``root`` privileges. Please create a VM
instance on India OpenStack and SSH into your VM to run and install your
software. You will have a full access of your virtual machine instance.

Quick instructions
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

* Launch a VM instance is::

    nova boot --flavor m1.small --image futuresystems/ubuntu-14.04 --key_name $USER-key $USER-salt

* Once your VM instance is ready, try to login using SSH::

    ssh ubuntu@[IP ADDRESS]

``root`` Access
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

We will install Salt and other software using ``root`` account. Using ``root``
account means that you have a permission to use entire system resources without
any restriction. Since this lesson includes a couple of examples using Salt, we
recommend to use OpenStack VM instance on FutureSystems. DON'T try to
install Puppet on your local machine or on the ``india.futuresystems.org`` host.
Use a benefit of VM instance which you can easily delete and re-create a new
one.

On a VM instance, simply run a switch user command::

  ubuntu@salt:~$ sudo su -

If you see ``root`` label, you are in ``root`` account on your machine::

  root@salt:~#


Update Hostname
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If you see ``sudo: unable to resolve host``, try to add hostname with the
following command::

  echo -e "\n127.0.1.1 $HOSTNAME" >> /etc/hosts


Ubuntu
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

First, add the salt repository.

::

  sudo add-apt-repository ppa:saltstack/salt
  sudo apt-get update

Core components will be installed with the following commands. If you run Salt
in a local mode, install ``salt-minion`` only.  The master, minion, or syndic
will be installed.

::

  sudo apt-get install salt-master
  sudo apt-get install salt-minion
  sudo apt-get install salt-syndic

A few more components are also installed with the following commands.  The
salt-cloud, salt-ssh, and salt-api will be installed.

::

  sudo apt-get install salt-cloud
  sudo apt-get install salt-ssh
  sudo apt-get install salt-api

One-Line Installation Salt Minion
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

With a caution, one-line installation can be used to have a quick installation
on various operating systems.

::

  sudo sh ins://bootstrap.saltstack.com | sudo sh -s -- git develop

Or two lines will be used::

  curl -L https://bootstrap.saltstack.com -o install_salt.sh
  sudo sh install_salt.sh

SLS Files
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

SaLt State file (SLS) is instructions of tasks in which a system should be in,
and what applications should be installed and configured. SLS data is written
in a simple format, YAML file with a ``.sls`` file extension. This is often
called configuration management. We will create a few files to try a simple
example of starting a Apache web server so that you can understand basic flows
in the use case.

Salt State Tree
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Salt state tree is a collection of SLS files that live under the directory
specified in ``file_roots``. We use a default directory ``/srv/salt`` to store
sls files.

::

  sudo mkdir /srv/salt

Top File
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The top file (``top.sls``) is to map what **SLS modules** get loaded onto what
**minions** via the state system. For example **apache sls module** can be
loaded to install and run on the target machine using ``top.sls`` file.  The
top file creates a few general abstractions. First it maps what nodes should
pull from which environments, next it defines which matches systems should draw
from.

* Create ``top.sls`` file for ``webserver``::

  nano /srv/salt/top.sls

The ``base`` environment will be loaded. type the following three lines in the
``top.sls`` file::

 base:
   '*':
     - webserver

* Create ``webserver.sls`` file to install Apache::

  nano /srv/salt/webserver.sls

The ``webserver.sls`` content include ``apache2`` package installation::

  apache2:              # ID declaration
    pkg:                # state declaration
      - installed       # function declaration

.. note::  Use **httpd** for Fedora/RHEL, **apache** for others in the package
           name.

Salt Call
-------------------------------------------------------------------------------

We use ``salt-call`` command to try our example of running a Apache web server.
With ``--local`` option, we can simply run Salt wihtout communicating with a
Salt master. The ``--local`` option indicates that *salt-minion* reads the
state tree in a local file system and does not to connect to a Salt Master for
instructions. Optionally you can you ``-l`` option for generating debug
messages:

::
 
 salt-call --local state.highstate

It runs Salt in a local mode.

The expected output messages look like so::

        [INFO    ] Loading fresh modules for state activity
        [INFO    ] Fetching file from saltenv 'base', ** done ** 'top.sls'
        [INFO    ] Creating module dir '/var/cache/salt/minion/extmods/modules'

        ...(skip)...

        Summary
        ------------
        Succeeded: 1 (changed=1)
        Failed:    0
        ------------
        Total states run:     1


:ref:`Full output message <ref-class-lesson-devops-saltstack-ex1-output>`

Now, you have Apache up and running.

Test
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Check your Apache is running with ``nc`` command.

::

  nc -v -z salt 80

You have running Apache if you see the message like so::

  Connection to salt 80 port [tcp/http] succeeded!

How It Works
-------------------------------------------------------------------------------

The instructions we made are executed in the following order:

* The Salt minion reads the top.sls file and determines that it is a part of
  the group matched by * glob.

* It reads the webserver SLS and applies.

* ``webserver.sls`` file will be loaded and finds the apache state, which
  installs the Apache package.

* The Salt minion now have Apache web server installed.

.. Salt Configuration
.. -------------------------------------------------------------------------------

.. http://docs.saltstack.com/en/latest/ref/configuration/index.html

.. _ref-class-lesson-devops-saltstack-exercises:

Exercises
----------------------------------------------------------------------

Exercise I
^^^^^^^^^^^^^^^^^^

Next Step
-----------

In the next page, Puppet will be introduced.

:ref:`Puppet <ref-class-lesson-devops-puppet>`

