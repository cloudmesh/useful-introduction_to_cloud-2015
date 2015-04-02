OpenStack Heat
======================================================================

Overview
----------------------------------------------------------------------

This lesson will introduce you to a very important topic of OpenStack Heat, a
software provisioning tool on a OpenStack platform.

.. tip:: Duration: 40 minutes

Prerequisite
----------------------------------------------------------------------

In order to conduct this lesson you should have knowledge of

* `OpenStack for Beginners <../iaas/openstack.html>`_

Description
----------------------------------------------------------------------

OpenStack Heat is an open source software to deploy services within OpenStack
clouds. Heat launches VM instances, installs cloud software and manages
required resources such as security groups or floating ip addresses within a
resource group, a stack. You just need to describe your cloud services and
resources in a Heat Template file, and OpenStack deploys your cloud services by
provisioning cloud infrastructure and installing/configuring software. Through
this lesson, you will learn how to write a Heat Template file and how to deploy
your cloud applications with a command line tool or a web interface. OpenStack
Heat Orchestration Template (HOT) is compatible with AWS CloudFormation
template format, there are some extensions of Heat Templates though. If you
have AWS templates, you can use them on OpenStack as well to start your cloud
services.

This lesson covers:

* Basic use of Heat Client Tool
* How to write Heat Template
* Example of deploying Hadoop Cluster with Heat
 
Use of OpenStack Heat on FutureSystems
-------------------------------------------------------------------------------

This lesson is based on FutureSystems. We start learning OpenStack Heat on
india.futuresystems.org. Heat is available on FutureSystems via a web interface
Horizon or a command line tool (Heat CLI). Resource topology is visible if you
use Horizon, and more command options and debugging messages are available on
command line tools.


Horizon on FutureSystems
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The Horizon on FutureSystems is at:
https://openstack-j.india.futuresystems.org/horizon/project/

For more details of Horizon:
`OpenStack Web Dashboard (Horizon) <../iaas/openstack_horizon.html>`_

Heat Client Tool
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If you'd like to use Heat Client Tool (heat CLI), you
simply run the following commands on india.futuresystems.org::

  module load openstack
  source $HOME/.cloudmesh/clouds/india/juno/openrc.sh

.. note:: If you run OpenStack Havana, try the following commands::
  
     module load openstack-havana;
     module load heatclient;
     source $HOME/.cloudmesh/clouds/india/havana/novarc;


``module load openstack`` enables Heat CLI on your shell.

Stack List
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

You can see running stacks with the following command:

::

   $ heat stack-list
   +----+------------+--------------+---------------+
   | id | stack_name | stack_status | creation_time |
   +----+------------+--------------+---------------+
   +----+------------+--------------+---------------+

A stack is cloud resources that you use with your selected Heat Template. If
you deployed 5 VM instances with 2 floating IP addresses and 1 security group,
all of these resources fall into a single stack on OpenStack.

Samples of Heat Templates
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

You can find examples of the Heat templates.

https://github.com/openstack/heat-templates/blob/master/hot/

Exercises
----------------------------------------------------------------------


Exercise I
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* Try to create a two VM instances with the following conditions:

  - futuresystems/ubuntu14.04
  - m1.small
  - Port 22, 80, and 443 opened

  - Save your OpenStack Heat template in ``$USERNAME_heat_ex1.yaml``


Next Step
-------------------------------------------------------------------------------

In the next page, Ubuntu Juju will be discussed.

`Ubuntu Juju <juju.html>`_

