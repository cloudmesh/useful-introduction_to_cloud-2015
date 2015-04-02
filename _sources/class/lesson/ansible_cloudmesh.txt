.. Writing Ansible Playbook for Cloudmesh on FutureSystems
Writing Ansible Playbooks on FutureSystems
===============================================================

Ansible Playbooks are automated scripts written in YAML data format.  Instead
of using manual commands to setup multiple remote machines, you can utilize
Ansible Playbooks to configure your entire systems. YAML syntax is easy to read
and express the data structure of certain Ansible functions. You simply write
some tasks, for example, installing software, configuring default settings, and
starting the software, in a Ansible Playbook.  With a few examples in this
tutorial, you will understand how it works and how to write your own Playbooks.

 There are also several examples of using Ansible `Playbooks
 <http://docs.ansible.com/playbooks.html>`_ from the official site. It covers
 from basic usage of Ansible Playbooks to advanced usage such as applying
 patches and updates with different roles and groups. 

Tutorial: Writing Ansible Playbook 
--------------------------------------------------------------------

.. tip:: approximate time 45 minutes

In this tutorial, we are going to write a basic playbook of Ansible software.
Keep in mind that ``Ansible`` is a main program and ``playbook`` is a template
that you would like to use. You may have several playbooks in your Ansible.

First playbook for MongoDB Installation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

As a first example, we are going to write a playbook which installs MongoDB
server.  It includes the following tasks:

* Import the public key used by the package management system
* Create a list file for MongoDB
* Reload local package database
* Install the MongoDB packages
* Start MongoDB

*This tutorial is based on the manual installation of MongoDB from the official
site: http://docs.mongodb.org/manual/tutorial/install-mongodb-on-ubuntu/*

*We also assume that we install MongoDB on Ubuntu OS.*

Hosts and Users
^^^^^^^^^^^^^^^^

First step is choosing hosts to install MongoDB and a user account to run
commands (tasks).  We start with the following lines in the example filename of
``mongodb.yaml``

::

  ---
  - hosts: local 
    remote_user: root

In a previous tutorial, we setup two machines with ``local`` group name. This
tutorial uses that two machines for MongoDB installation.  Also, we use
``root`` account to complete Ansible tasks.

.. note:: Indentation is important in YAML format. Do not ignore spaces start
          with in each line.

Tasks
^^^^^^^^^

A list of tasks contains commands or configurations to be executed on remote
machines in a sequential order.  Each task comes with a ``name`` and a
``module`` to run your command or configuration.  You provide a description of
your task in ``name`` section and choose a ``module`` for your task.  There are
several modules that you can use, for example, ``shell`` module simply executes
a command without considering a return value.  You may use ``apt`` or ``yum``
module which is one of the packaging modules to install software. You can find
an entire list of modules here:
http://docs.ansible.com/list_of_all_modules.html

Step 1: Import the public key used by the package management system
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

We need to import the MongoDB public GPG Key. This is going to be a first task
in our playbook.

::

  tasks:
    - name: Import the public key used by the package management system
      shell: apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 7F0CEB10


Step 2: Create a list file for MongoDB
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Add a list of MongoDB URL with the following task:

::

   - name: Create a list file for MongoDB
     shell: echo 'deb http://downloads-distro.mongodb.org/repo/ubuntu-upstart dist 10gen' | tee /etc/apt/sources.list.d/mongodb.list

Step 3: Reload local package database
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

::

  - name: Reload local package database
    shell: apt-get update

Step 4: Install the MongoDB packages
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

We use ``apt`` module to install ``mongodb-org`` package.
``notify`` action is added to start ``mongod`` after the completion of this task.

::
  - name: install mongodb
    apt: pkg=mongodb-org state=latest
    notify:
    - start mongodb

Step 5: Start MongoDB
^^^^^^^^^^^^^^^^^^^^^^^

We use ``handlers`` here to start or restart services. It is similar to ``tasks`` but will run only once.

::

   handlers:
     - name: start mongodb
       service: name=mongod state=started

A playbook for Mongodb
~~~~~~~~~~~~~~~~~~~~~~~~~

Our first playbook looks like this:

:: 

   cat mongodb.yaml

   ---
   - hosts: local
     remote_user: root
     tasks:
     - name: Import the public key used by the package management system
       shell: apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 7F0CEB10
     - name: Create a list file for MongoDB
       shell: echo 'deb http://downloads-distro.mongodb.org/repo/ubuntu-upstart dist 10gen' | tee /etc/apt/sources.list.d/mongodb.list
     - name: Reload local package database
       shell: apt-get update
     - name: install mongodb
       apt: pkg=mongodb-org state=latest
       notify:
       - start mongodb
     handlers:
       - name: start mongodb
         service: name=mongod state=started

Run Playbook
~~~~~~~~~~~~~~~~~

We use ``ansible-playbook`` command to run our playbook.

::

  ansible-playbook mongodb.yaml


Test Mongodb
~~~~~~~~~~~~

Let's try to run 'mongo' to enter mongodb shell.

::

  $ mongo
  MongoDB shell version: 2.6.7
  connecting to: test
  >

Terms
~~~~~

* Module: Ansible library to run or manage services, packages, files or commands.
* Handler: A task for notifier.
* Task: Ansible job to run a command, check files, or update configurations.
* Playbook: a list of tasks for Ansible nodes. YAML format used.
* YAML: Human readable generic data serialization.

Reference
~~~~~~~~~~

The main tutorial from Ansible is here: http://docs.ansible.com/playbooks_intro.html

Next Step
---------

In the next page, we learn Basic Docker on FutureSystems.

`Basic Docker On FutureSystems <docker.html>`_
