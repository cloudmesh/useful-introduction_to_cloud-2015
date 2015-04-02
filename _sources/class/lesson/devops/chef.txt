Chef 
======================================================================

Overview
----------------------------------------------------------------------

This lesson will introduce you to a very important topic to Chef, a
configuration management tool written in Ruby and Erlang. 

.. tip:: Duration: 1 hour

Prerequisite
----------------------------------------------------------------------

In order to conduct this lesson you should have knowledge of

* `OpenStack for Beginners <../iaas/openstack.html>`_

Description
----------------------------------------------------------------------

Chef is an open source infrastructure automation software that manages
installation and configuration of your software with its Ruby code ``Recipe``
and ``Cookbook``. ``Recipe`` is a description of how your servers should be set
up with your software and ``Cookbook`` is a set of recipes. If you install a
Apache web server or a MySQL database using Chef, you may download and use
existing recipes from the Chef server (SuperMarket). You can also write your
own recipes with your preference about configuration and installation. In most
cases, a single recipe is not enough to configure and install software.  Chef
provides a collection of related recipes named ``Cookbook``, and you use
Cookbooks to install software with relevant tools.

This lesson gives you an introduction of Chef including the following topics:

* Installation of Chef
* Example I: Apache2 Installation
* Write a first recipe

Installation Chef
-------------------------------------------------------------------------------

This lesson is based on FutureSystems which means you create a VM instance on
India OpenStack and installs Chef on top of it. If you prefer to use other
virtual environments, we recommend to use Vagrant and VirtualBox.

We assume you use a OpenStack instance on FutureSystems.

.. note:: If don't know how to launch a new instance? `See here
    <../iaas/openstack.html#launching-a-new-instance>`_


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

