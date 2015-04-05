Puppet
======================================================================

Overview
----------------------------------------------------------------------

This lesson will introduce you to a very important topic to Puppet, an open
source configuration management tool.

.. tip:: Duration: 1 hour

Prerequisite
----------------------------------------------------------------------

In order to conduct this lesson you should have knowledge of

* `OpenStack for Beginners <../iaas/openstack.html>`_

Description
----------------------------------------------------------------------

Puppet is an open source configuration management software to configure systems
declaratively. If you describe system resources and configurations using
Puppet's declarative language (combination of JSON and Ruby) or Ruby DSL
(Domain Specific Language), Puppet discovers servers (nodes) and applies the
instructions that you described to the target machines. Puppet manages
configurations and installations with a client-server model like Chef.  You
need to use command line tools or web interfaces to communicate with a Puppet
server. There are many similar features and functionalities between Chef and
Puppet. Try to compare these two tools when you use their commands tools or
write the scripts. Chef calls the script as a ``Recipe``, and Puppet calls it
as a ``manifest``.

Open Source Puppet
-------------------------------------------------------------------------------

Puppet Labs supports Puppet software in two different versions. This lesson
uses an open source Puppet instead of Puppet Enterprise which is a commercial
version of Puppet. A few features are only available in the Enterprise version
but the core parts of Puppet are identical in both.

Installation Puppet
-------------------------------------------------------------------------------

This lesson is based on FutureSystems which means you create a VM instance on
India OpenStack and install Puppet on top of it. If you prefer to use other
virtual environments, we recommend to use Vagrant and VirtualBox.

We assume you use a OpenStack instance on FutureSystems.

.. note:: If don't know how to launch a new instance? `See here
    <../iaas/openstack.html#launching-a-new-instance>`_

Guideline on India FutureSystems
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

You *DON'T* install Puppet on India. If you see the cursor like:

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

    nova boot --flavor m1.small --image futuresystems/ubuntu-14.04 --key_name $USER-key $USER-puppet

* Once your VM instance is ready, try to login using SSH::

    ssh ubuntu@[IP ADDRESS]

Puppet on Ubuntu 14.04 (Standalone Mode)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Use a VM instance with a Ubuntu 14.04 image. The installation commands are::

        wget https://apt.puppetlabs.com/puppetlabs-release-trusty.deb
        sudo dpkg -i puppetlabs-release-trusty.deb
        sudo apt-get update
        sudo apt-get install puppet

.. info:: This is a client installation only. If you'd like to install Puppet
          Server, please read the instructions here:
          http://docs.puppetlabs.com/guides/install_puppet/install_debian_ubuntu.html

Check your installation::

  puppet --version

You expect to see 3.7.5 or higher version, otherwise your installation is incomplete.

``root`` Access
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

We will install Puppet and other software using ``root`` account. Using ``root``
account means that you have a permission to use entire system resources without
any restriction. Since this lesson includes a couple of examples using Puppet, we
strongly recommend to use OpenStack VM instance on FutureSystems. DON'T try to
install Puppet on your local machine or on the ``india.futuresystems.org`` host.
Use a benefit of VM instance which you can easily delete and re-create a new
one.

On a VM instance, simply run a switch user command::

  ubuntu@puppet:~$ sudo su -

If you see ``root`` label, you are in ``root`` account on your machine::

  root@puppet:~#

A Puppet Template - manifest
-------------------------------------------------------------------------------

You Puppet is ready to use on you VM instance. Let's create a Puppet
configuration file.  The installation process have created a Puppet directory
under ``/etc/``. (If it hasn't, create it with ``mkdir /etc/puppet``).

::
  cd /etc/puppet/;
  ls

You see files and directories like so::

  environments  manifests  modules  puppet.conf  templates

We're going to use ``manifests`` directory to create a Puppet configuration file.

.. note:: If you don't have one, run: ``mkdir /etc/puppet/manifests``


Exercises
----------------------------------------------------------------------

Exercise I
^^^^^^^^^^^^^^^^^^

Exercise II
^^^^^^^^^^^^^^^^^^

Next Step
-----------

In the next page, ...

`Link here <link>`_

