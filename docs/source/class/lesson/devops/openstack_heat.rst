OpenStack Heat
======================================================================

Overview
----------------------------------------------------------------------

This lesson will introduce you to a very important topic of OpenStack Heat, a
software provisioning tool on the cloud.

.. tip:: Duration: 40 minutes

Prerequisite
----------------------------------------------------------------------

In order to conduct this lesson you should have knowledge of

* `OpenStack for Beginners <../iaas/openstack.html>`_

Description
----------------------------------------------------------------------

OpenStack Heat is an open source software to deploy services within OpenStack
clouds. Heat launches VM instances, installs cloud applications and manages
required resources such as security groups or floating ip addresses. If you
describe your cloud services in Heat Template, OpenStack Heat provision your
service with your instruction. AWS CloudFormation template format is compatible
with OpenStack Heat Orchestration Template (HOT).

This lesson covers:

* Basic use of Heat Client Tool
* How to write Heat Template
* Example of deploying Hadoop Cluster with Heat
 
Use of OpenStack Heat on FutureSystems
-------------------------------------------------------------------------------

OpenStack Heat is available on Futuresystems. To use Heat Client Tool (heat CLI),
you simply run the following commands::

  module load openstack
  source $HOME/.cloudmesh/clouds/india/juno/openrc.sh

.. note:: If you run OpenStack Havana, try the following commands:
   module load openstack-havana
   module load heatclient
   source $HOME/.cloudmesh/clouds/india/havana/novarc

Try Heat Command Line Tool
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If you are able to use a heat client tool, you can see running stacks with the
following command:

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

