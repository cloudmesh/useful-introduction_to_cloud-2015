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
script.

Ubuntu
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

First, add the salt repository.

::

  sudo apt-get update
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

.. _ref-class-lesson-devops-saltstack-exercises:

One-Line Installation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

With a caution, one-line installation can be used to have a quick installation
on various operating systems.

::

  sudo sh ins://bootstrap.saltstack.com | sudo sh -s -- git develop

Or two lines will be used::

  curl -L https://bootstrap.saltstack.com -o install_salt.sh
  sudo sh install_salt.sh

Salt Configuration
-------------------------------------------------------------------------------

http://docs.saltstack.com/en/latest/ref/configuration/index.html

Exercises
----------------------------------------------------------------------

Exercise I
^^^^^^^^^^^^^^^^^^

Exercise II
^^^^^^^^^^^^^^^^^^

Next Step
-----------

In the next page, Puppet will be introduced.

:ref:`Puppet <ref-class-lesson-devops-puppet>`

