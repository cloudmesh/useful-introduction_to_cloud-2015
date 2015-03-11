OpenStack for Beginners (Under Preparation)
======================================================================

Overview
----------------------------------------------------------------------

This lesson will introduce you to a very important topic to OpenStack core
components.

.. tip:: Duration: 2 hours

Prerequisite
----------------------------------------------------------------------

In order to conduct this lesson you should have knowledge of

* `Overview OpenStack <overview_openstack.html>`_

Description
----------------------------------------------------------------------

OpenStack is an open source cloud IaaS platform which provides compute,
storage, and networking resources with service components.  We explore these
components with a few examples in this lesson to have a taste of OpenStack
cloud on FutureSystems.

OpenStack consists of the following set of core components:

Table 1. Core components of OpenStack

=============   ==============  ======================= ======================
Component       Project Name    Main task               Sample Command
=============   ==============  ======================= ======================
Compute         Nova            vm management           nova boot 
Storage         Swift           Data warehouse          swift post
Network         Neutron         Network management      neutron net-create
Account         Keystone        Identity/Authentication keystone tenant-create
Web Interface   Horizon         Web User Interface      
=============   ==============  ======================= ======================

There are many other important components in OpenStack, for example, OpenStack
Heat provides automated deployment service with AWS CloudFormation template,
and OpenStack Telemetry (previously Ceilometer) offers a billing service based
on the measured data. Block Storage service named Cinter and virtual machine
image service named Glance are also major components in OpenStack.

Nova Compute
------------------------------------------------------------------------------

Nova Compute engine manages computing resources on OpenStack. It starts a
virtual machine instance with a choice of a machine (i.e. small, medium, large,
or cpu-intensive) and an image (i.e. Ubuntu, CentOS, etc.), and updates or
terminates the instance.

To have your own virtual machine (vm) instance on OpenStack cloud, you need to
submit your request of a vm instance via a command line tool (Nova client) or
on a dashboard Horizon.

Let's explore a few examples to allocate vm instances. In FutureSystems, you
need to be on the India login node.  (India is a hostname for OpenStack on
FutureSystems)

::

  $ ssh india.futuresystems.org

Launching a new instance
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Starting a new instance is simple. The following command starts a new instance
named *tutorial1* with a Ubuntu 14.04 base image.  The size of the machine will
be **small**.

::

  $ nova boot --flavor m1.small --image futuresystems/ubuntu-14.04 --key_name albert-india-key tutorial1

Here are some explanations for the arguments.

* ``boot`` is a sub command to start a new server.
* ``--flavor`` is a name for your machine size. ``m1.small`` typically has 1 vCPU and 2GB memories.
* ``--image`` is a name for your base image. ``nova image-list`` displays all registered image.
* ``--key_name`` is a key name to use for SSH connection. This key should be
  registered on Nova Compute. Try ``nova keypair-list`` to see registered keys.
* ``tutorial1`` is a name for your vm instance.


Swift Storage 
------------------------------------------------------------------------------

Neutron Network
------------------------------------------------------------------------------

Glance Image Management
------------------------------------------------------------------------------

  
Exercises
----------------------------------------------------------------------

Exercise I
^^^^^^^^^^^^^^^^^^

* Launch a new large instance with a futuresystems/ubuntu-14.04 image.

Exercise II
^^^^^^^^^^^^^^^^^^

* Allocate a floating ip address to the instance that you just launched.

Next Step
-----------

In the next page, ...

`Link here <link>`_

