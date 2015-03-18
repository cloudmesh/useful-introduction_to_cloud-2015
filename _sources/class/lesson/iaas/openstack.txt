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

You should now load the ``openstack`` module to gain access to the
necessary commands.::

  $ module load openstack

Next, you need to set up your environment correctly to use some
OpenStack commands. This has been configured for you so you just need
to source the appropriate files::

  $ source ~/.cloudmesh/clouds/india/juno/openrc.sh
  $ source ~/.cloudmesh/clouds/india/juno/fg465

Launching a New Instance
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Starting a new instance is simple. The following command starts a new
instance named *tutorial1* with a Ubuntu 14.04 base image.  The size
of the machine will be **small**.

.. note::

   Make sure you have a ``~/.ssh`` directory and created a key for
   OpenStack to use.
   Create the directory if necessary::

     $ test -d ~/.ssh || mkdir ~/.ssh

   Generate a key for OpenStack::

     $ nova keypair-add openstack-key >~/.ssh/openstack-key

   Ensure the permissions are set correctly::

     $ chmod 600 ~/.ssh/openstack-key

   You can now see that your key is visible to OpenStack::

     $ nova keypair-list
     +---------------+-------------------------------------------------+
     | Name          | Fingerprint                                     |
     +---------------+-------------------------------------------------+
     | openstack-key | 35:74:ee:be:14:4b:43:dd:ed:d8:cf:8e:de:13:ea:ce |
     +---------------+-------------------------------------------------+


Boot the instance using the following command:

::

  $ nova boot --flavor m1.small --image futuresystems/ubuntu-14.04 --key_name openstack-key tutorial1

Here are some explanations for the arguments.

* ``boot`` is a sub command to start a new server.
* ``--flavor`` is a name for your machine size. ``m1.small`` typically
  has 1 vCPU and 2GB memories.
* ``--image`` is a name for your base image. ``nova image-list``
  displays all registered image.
* ``--key_name`` is a key name to use for SSH connection. This key
  should be registered on Nova Compute. Try ``nova keypair-list`` to
  see registered keys.
* ``tutorial1`` is a name for your vm instance.

.. _lab-openstack-1:

Lab - OpenStack - Launch an Instance
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

* Launch a new medium instance with a CentOS image using a different
  key (call it ``openstack-ex1-key``). Name the CentOS instance
  ``tutorial1-ex1`` and make sure both instances are running using the
  ``nova list`` command.
* Allocate a floating ip address to the instance that you just launched.

Glance Image Management
------------------------------------------------------------------------------

OpenStack Glance is a virtual machine (VM) image management tool which
registers, manages, shares or deletes machine images. The registered VM image
can be used to launch a compute instance from users if it is open to public.
Typically various operating systems are provided as basic VM images and users
can add a variation to the images for saving their work on a VM instance.
The following sub commands tell what you can do:

* image-create: Create a new image
* image-delete: Delete specified image(s)
* image-download: Download a specific image
* image-list: List images you can access
* image-show: Describe a specific image
* image-update: Update a specific image
* member-create: Share a specific image with a tenant
* member-delete: Remove a shared image from a tenant
* member-list: Describe sharing permissions by image or tenant
* bash-completion: Prints all of the commands and options to stdout

These commands are available in glance version 0.15.0.

Creating a New Image
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The following command will register Ubuntu 14.04 image to OpenStack cloud. You
can download cloud images from Ubuntu Cloud.

::

  $ glance image-create \
  --name $PROJECT/$USER/myimages/ubuntu-14.04 \
  --disk-format qcow2 \
  --container-format bare \
  --file trusty-server-cloudimg-amd64-disk1.img

If your image registered successfully, you will see ACTIVE status in the image-list command.

::

  $ glance image-list
  
Keystone Account and Authenticaion
-------------------------------------------------------------------------------

OpenStack Keystone manages user accounts and provides authentication service
using tokens. If you need to add a new user or a group, you may use keystone
client tool to register. As a developer, you use Keystone for user
authentication with tokens when you send a service request via OpenStack API.
The token is a convinient method to deal with authenticaion instead of a pair
of username and password. Let's explore a few basic commands of OpenStack
Keystone.

.. Note:: Keystone commands are only available to administrator

Project Creation (Tenant)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

OpenStack manages user accounts with a group. OpenStack represents a group as a
*project* or a *tenant* interchangeably. Each user should participate in at
least a single project, they can join multiple projects though. With a group of
users, it is convenient to manage different settings across multiple groups.
For example, you can set limits of 10 instances to project1 but project2 may
have higher or smaller size of vm instances.

::

  $ keystone tenant-create --name=project1 --description="futuresystems project 1"

User Creation 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To create a new user, you need a tenant (project) id, if you provide a
group-based cloud service.

::

  $ keystone user-create --name=albert \
    --pass=*** \
    --tenant_id=*** \
    --email=albert@futuresystems.org

List of Users or Projects
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Try ``user-list`` or ``tenant-list`` sub command to see a list of users or
projects.

::

  $ keystone user-list

  or

  $ keystone tenant-list

.. tip:: Try ``keystone`` command itself. The help message shows that available
        sub commands including tenant-create, user-create, user-list and
        tenant-list.

Role management
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Project members need to have different privileges to control allocated
resources to the project.  For example, *albert* needs an admin permission to
terminate or update other user's vm instances in a same project.  OpenStack
Keystone has a role management with a pair of a user and a project.

The following commands are useful to manage roles in a project:

* role-create: Create new role
* role-delete: Delete role
* role-get: Display role details
* user-role-add: Add role to user
* user-role-list: List roles granted to a user
* user-role-remove: Remove role from user

Swift Storage 
------------------------------------------------------------------------------

Swift is an object storage service on OpenStack like Amazon Simple Storage
Service (S3). If you are looking for a block storage, OpenStack Cinder is one
for you.

The following sub commands tell what you can do:

* delete: Delete a container or objects within a container
* download: Download objects from containers
* list: Lists the containers for the account or the objects for a container
* post: Updates meta information for the account, container, or object; creates
  containers if not present 
* stat: Displays information for the account,
  container, or object
* upload: Uploads files or directories to the given container
* capabilities: List cluster capabilities
* tempurl: Create a temporary URL

.. note:: Swift Storage is not available on FutureSystems.

.. tip:: Not to decide Swift or Cinder? If you need a large disk space mounted
        on your VM instance, Cinder is useful.  If you need to get access of a
        file across multiple servers using API? Swift is the answer.

Neutron Network
------------------------------------------------------------------------------

Neutron is a OpenStack Networking service to manage NAT, firewall, etc. This
type of tasks is for OpenStack cloud administrator. We briefly explore a few
commands available on Neutron to understand basic services on OpenStack
Networking.

* neutron net-list: List Current Neutron Networks
* neutron subnet-list: List Current Neutron Subnets
* neutron security-group-create <SEC-GROUP-NAME>: Create Neutron Security Group
* neutron security-group-rule-create --direction <ingress OR egress> --ethertype <IPv4 or IPv6> --protocol <PROTOCOL> --port-range-min <PORT-NUMBER> --port-range-max <PORT-NUMBER> <SEC-GROUP-NAME>: Add Rules to Neutron Security Group
* neutron floatingip-create <NET-NAME>: Create a Neutron Floating IP Pool
  - If you need N number of floating IP addresses, run this command N number of times:
* neutron port-create <NET-NAME> --fixed-ip ip_address=<IP-ADDRESS>: Create a Neutron Port with a Fixed IP Address

Example 1. add a rule to the default Neutron Security Group to allow SSH access to instances::

        neutron security-group-rule-create --direction ingress \
        --ethertype IPv4 --protocol tcp \
        --port-range-min 22 --port-range-max 22 default

Example 2. add a rule to the default Neutron Security Group to allow ICMP communication to instances::

        neutron security-group-rule-create --direction ingress \
        --ethertype IPv4 --protocol icmp default

 
Exercises
----------------------------------------------------------------------

Next Step
-----------

In the next page, ...

`Link here <link>`_

