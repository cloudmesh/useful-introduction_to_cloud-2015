Cloudmesh MOOC Shell
======================

`cm-mooc` provides an easy way to start a Cloudmesh VM on OpenStack India. 
You can start a virtual machine for Cloudmesh with a single command in `cm-mooc`.
You can also enable IPython Notebook on the virtual machine with `cm notebook`
commands.  You may read the following instructions to enable this program on
your terminal.

Tutorial Video Clip: http://youtu.be/kFWGPqHrBCA

.. |video-cm-mooc| replace:: |video-image| :youtube:`kFWGPqHrBCA`


Quickstart
------------

Create a FutureSystems portal ID (if you don't have)
  
- http://portal.futuregrid.org
    
.. note:: Need more help? see :ref:`s-accounts`

Login to India OpenStack
  
- ``ssh <username>@india.futuregrid.org`` 
     
.. note:: Need more help for ssh? see :ref:`s-using-ssh`

Activate `cm-mooc`::

     module load heatclient
     source ~/.futuregrid/openstack_havana/novarc
     source /share/project/FG455/MOOC/bin/activate
   
  .. note:: It maye be useful to add the module load and the source
     commands into your .bashrc_profile so you do not forget to
     activate them whnever you log in.


Create the 'cloudmesh' security group to add 5000, 8888 ports.

.. note:: If you already have `cloudmesh` in your security group, you
   can skip this step.

::

      source ~/.futuregrid/openstack_havana/novarc
      nova secgroup-create cloudmesh "cloudmesh ports 5000, 8888"
      nova secgroup-add-rule cloudmesh tcp 8888 8888 0.0.0.0/0
      nova secgroup-add-rule cloudmesh tcp 5000 5000 0.0.0.0/0
      nova secgroup-list-rules cloudmesh

Execute the following commands::

   india$ cm-mooc start      

.. warning:: Please wait approximately 5 minutes after this command.
   when you log into early the next command will fail.
	     
after you have waited for 5 minutes you can execute::

   india$ cm-mooc login       # SSH to VM

Now that you are looged into the VM please execute:: 

   vm$ cm notebook create # provide your password to IPython Notebook on the
  
Now you need to exit the virtual machine. You will now be back in
india. In india you execute::

   india$ cm-mooc notebook start

Now you can access the IPython Notebook via a web browser:
  `https://[ip address]:8888`

If you forgot the ip address you can use the command::

    india$ cm-mooc info
  
The class material is contained in two directories. Dependent on the
class please chose the directory suitable for you:

* **fg455**: directory containing ipython notebooks for the class fg455
* **cloudmesh**: directory containing cloudmesh ipython notebooks


To delete the services (dangerous)  use::

   india$ cm-mooc delete


Detailed Instructions
----------------------------------------------------------------------

`cm-mooc` Instruction
^^^^^^^^^^^^^^^^^^^^^^^

The following instrunctions explain `cm-mooc` command in detail. 
Start, login, stop of your virtual machine is really easy with `cm-mooc`
command. 

OpenStack Credential
^^^^^^^^^^^^^^^^^^^^

Once you logged in India OpenStack, you may load your OpenStack credential
first.

* novarc file
   - ``source ~/.futuregrid/openstack_havana/novarc``

OpenStack Heat   
^^^^^^^^^^^^^^^^^^

We use OpenStack Heat Orchestration to start Cloudmesh VM, so loading heat
libraries is required.

* heatclient
   - ``module load heatclient``
  
Enable `cm-mooc`
^^^^^^^^^^^^^^^^^

Now, we activate the `cm-mooc` tool.

* `cm-mooc`
   - ``source /share/project/FG455/MOOC/bin/activate``

Security Group
^^^^^^^^^^^^^^^^^^^^^

Cloudmesh, IPython Notebook requires to use 5000, 8888 port numbers. We need to
add rules for these port numbers.

* Create 'cloudmesh' secgroup to allow the access of 5000, 8888 ports
  
  ::

    nova secgroup-create cloudmesh "cloudmesh ports 5000, 8888"
    nova secgroup-add-rule cloudmesh tcp 8888 8888 0.0.0.0/0
    nova secgroup-add-rule cloudmesh tcp 5000 5000 0.0.0.0/0
    nova secgroup-list-rules cloudmesh
  
**If you already have `cloudmesh` in your security group, you can skip this
section.**

SSH Key Registration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If you have not registered your ssh key, you may need to do the following
steps::

  ssh $USER@india.futuresystems.org
  module load novaclient
  source ~/.futuregrid/openstack_havana/novarc
  
*$USER is your login id to FutureSystems*

If you do not have a ssh key, you can generate one::

  ssh-keygen -t rsa -C $USER-india-key

We assume your public key is `~/.ssh/id_rsa.pub`::

  nova keypair-add --pub-key ~/.ssh/id_rsa.pub $USER-india-key

Start Cloudmesh VM
^^^^^^^^^^^^^^^^^^

We can now start Cloudmesh VM on OpenStack India.

``cm-mooc start``

**It may take 5 minutes or so. You need to wait otherwise the environment is
not ready to use in the next step.**

.. note:: Try Cloudmesh Web Site at http://[ip address]:5000 Your
   default password is: *cloudmesh* To change the password, try the
   following commands::
  
     cm-mooc login
     cd ~/cloudmesh
     fab user.mongo # set your password
     fab server.start # restart the Cloudmesh server
    
List VM
^^^^^^^^

You can check the status of the VM by the following commanf.

``cm-mooc list``

Delete the Mooc Cloudmesh VM
^^^^^^^^^^^^^^^^^^^^^

If you have completed all of your work in the VM, you may stop the VM by the following command.

``cm-mooc delete``

Login Cloudmesh VM
^^^^^^^^^^^^^^^^^^^^^^^^^^

You can ssh to the VM by the following command.

``cm-mooc login``

Create IPython Notebook Profile on Cloudmesh VM (Set Password)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If you have waited more than 5 minutes, you can now create IPython Notebook
(ipynb) Profile with,

``cm-mooc notebook create``

This step requires your password input for IPython Notebook and information of
the self-assigned certificate to enable SSL.

You can also do the same thing with ssh login.

``cm-mooc login``

Once you logged in, try `cm` program.

``cm notebook create``

This command asks you the password of your IPython Notebook Server. You also
need to create self-signed certificate.  You can create the certificate by
providing some information.

``exit``

If you created the ipynb profile, you may exit from the VM. Let's get back to
India and use `cm-mooc` command.

  .. note:: `cm` is the Cloudmesh shell program. It allows you to create a
  IPython Notebook Profile.

Start IPython Notebook on Cloudmesh VM
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If you have already configured your IPython Notebook (ipynb), you can start
with,

``cm-mooc notebook start``

Once the server started, you can get access to the IPython Notebook via
https://[public ip address]:8888

Class Material (IPython Notebooks)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

IPython Notebook files for the class is in **fg455** directory in the main tree
of IPython Notebook.

* https://[public ip address]:8888/fg455
Original source is at https://github.com/cglmoocs/IPythonFiles

Cloudmesh Notebook files are also available.

*  https://[public ip address]:8888/cloudmesh
Original source is at
https://github.com/cloudmesh/introduction_to_cloud_computing

You can import or export more IPython Notebook files.

Stop IPython Notebook on Cloudmesh VM
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The simple command ``cm-mooc notebook stop`` kills the Ipython Notebook server.

Help Message
^^^^^^^^^^^^^

You can see available commands to `cm-mooc` program.

``cm-mooc -h``
