Try Ansible Basic on FutureSystems
===============================================================

Ansible is an IT automation tool which deploys software and configures systems
on multiple servers using SSH protocol. Python based Ansible stores information
about deployment and configuration in a yaml format file, named Ansible
Playbook. Tasks defined in the playbook allows you to have identical
configurations and software across multiple machines in your infrastructure.
This section, we introduce basic commands of ``ansible`` to introduce Ansible
software on FutureSystems.  In the next section, we will explore advanced use
of ``ansible`` on FutureSystems.

Tutorial: Ansible Basic commands
--------------------------------------------------------------------

.. tip:: approximate time 45 minutes

In this tutorial, we are going to learn basic commands of Ansible software.
Keep in mind that ``ansible`` is a main program and ``playbook`` is a template
that you would like to use. You may have several playbooks in your Ansible.

Install Ansible 
~~~~~~~~~~~~~~~~

Ansible has two types of servers: a control machine and a managed node.
Typically, a single control machine executes tasks over the one or more nodes.

Control machine
^^^^^^^^^^^^^^^^
Let's install Ansible from Git.

::

  sudo apt-get update
  sudo apt-get install git
  git clone git://github.com/ansible/ansible.git --recursive
  cd ./ansible
  source ./hacking/env-setup

.. tip:: You can also install ansible using apt-get:
        sudo apt-get install software-properties-common
        sudo apt-add-repository ppa:ansible/ansible
        sudo apt-get update
        sudo apt-get install ansible

Python PyPI
^^^^^^^^^^^^

You need to install python-pip:

::
 
  sudo apt-get install python-pip python-dev

Python Packages
^^^^^^^^^^^^^^^^

Four python packages are required:

* paramiko 
* PyYAML 
* Jinja2 
* httplib2

Install these packages::

  sudo pip install paramiko PyYAML Jinja2 httplib2

SSH Configuration
~~~~~~~~~~~~~~~~~

Since Ansible works with SSH, you need to make sure your node(s) are accessible by your control machine.

KeyPair Creation
^^^^^^^^^^^^^^^^^^^

With ``ssh-keygen`` command, we create a default key without a password.
:: 

  ssh-keygen -b 2048 -t rsa -f ~/.ssh/id_rsa -q -N ""

authorized_keys
^^^^^^^^^^^^^^^^^^^

Register the public key to ``authorized_keys``.

::

  cat ~/.ssh/id_rsa.pub >> ~/.ssh/authorized_keys

This public key will be registered on each node for your Ansible.

Node registration
^^^^^^^^^^^^^^^^^^

How many nodes do you have? In this section, we define hosts for Ansible.
The default location is in ``/etc/ansible/hosts``.

::

  sudo mkdir /etc/ansible

Now, register your hosts in the ``/etc/ansible/hosts`` default file. Your hosts
file looks like this:

::
  cat /etc/ansible/hosts

  [local]
  10.39.1.1
  10.39.1.2

.. note:: You need to make sure you can ssh to each of these nodes (i.e.
          10.39.1.1, 10.39.1.2)

We added two hosts (10.39.1.1, 10.39.1.2) in the ``local`` group.

Test Ansible
~~~~~~~~~~~~

Let's try to run 'echo Hello World' over the nodes.

::

  ansible all -a "echo Hello World"

You expect to see::

        10.39.1.1 | success | rc=0 >>
        Hello World

        10.39.1.2 | success | rc=0 >>
        Hello World

Run a simple command "ping".

::

  ansible all -m ping

You expect to see::

        10.39.1.1 | success >> {
            "changed": false,
            "ping": "pong"
        }

        10.39.1.2 | success >> {
            "changed": false,
            "ping": "pong"
        }


Terms
~~~~~

* Inventory: The hosts registered in the ``/etc/ansible/hosts`` file. Multiple
  inventories can be used.
* Group: A representation of a list of hosts. ``[group name]`` used in the
  inventory.  
* Playbook: a list of tasks for Ansible nodes. YAML format used.

More examples
~~~~~~~~~~~~~~

You can find more examples from here: https://github.com/ansible/ansible-examples

Reference
~~~~~~~~~~

The main tutorial from Ansible is here: https://docs.ansible.com/installation/ubuntulinux/

Next Step
---------

In the next page, we learn Ansible Playbook on FutureSystems.
