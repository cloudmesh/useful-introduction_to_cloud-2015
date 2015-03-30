Setup Cloudmesh in an VirtualBox VM with Vagrant for Testing
==============================================================

.. highlight:: bash

This tutorial provides as how to deploy Cloudmesh with Vagrant and VirtualBox.
Official Ubuntu 14.04 Server LTS 64 bit and 32 bit are supported as base images
of Vagrant.

Download cloudmesh
--------------------------

::

  $ git clone https://github.com/cloudmesh/cloudmesh.git
  $ cd cloudmesh

Install Vagrant and VirtualBox
--------------------------------

This instructions are tested on Ubuntu 14.04.

::

  $ sudo apt-get install vagrant
  $ sudo add-apt-repository multiverse 
  $ sudo apt-get update
  $ sudo apt-get install virtualbox


Install Vagrant on OSX
-------------------

Download and install vagrant from https://www.vagrantup.com/downloads.html

::
   
  curl -L https://dl.bintray.com/mitchellh/vagrant/vagrant_1.7.2.dmg > vagrant_1.7.2.dmg
  open vagrant_1.7.2.dmg

Click on the vagrant.pkg and follow the install instructions

Verify that vagrant is installed with::

  vagrant -h


which should give you the vagrant help message

Install virtualbox from

https://www.virtualbox.org/wiki/Downloads

once downloaded and you clock on the dmg, follow the instalation instructions.
  
Install Veewee (Optional)
-------------------------

There are `requirements <veewee-requirement.html>`_ prior installing Veewee.

::
  
   $ gem install veewee

* On OS X Yosemite::

   
   $ sudo ARCHFLAGS=-Wno-error=unused-command-line-argument-hard-error-in-future gem install veewee


Vagrant up
----------

::

  $ cd ~/cloudmesh/vagrant/example1
  $ ./run.sh

FutureGrid Portal ID
^^^^^^^^^^^^^^^^^^^^^

Provide your portal ID::

  ==================================
  Futuregrid portal id? (def: )

  ==================================

Base Image
^^^^^^^^^^^

Select one of the base images::

  ==================================
  Select base image to launch
  ==================================
  1) Ubuntu Server 14.04 64bit
  2) Ubuntu Server 14.04 32bit
  Please choose an option: 
  
  Ubuntu Server 14.04 xxbit selected
  Bringing machine 'default' up with 'virtualbox' provider...
  ==> default: Checking if box 'ubuntu/trustyxx' is up to date...

Vagrant will be loaded.

Vagrant ssh
-----------

Cloudmesh installed on a root account. You need to switch user account to a
root once you ssh to the VM.

::
 
   $ vagrant ssh
   $ sudo su -

Virtualenv and cm
-----------------

Cloudmesh installed on Virtualenv. You need to enable the environment. ``cm``
Cloudmesh interactive shell is ready to use.

::

   $ source ~/ENV/bin/activate
   $ cd cloudmesh
   $ cm
