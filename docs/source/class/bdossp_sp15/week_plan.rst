===============================================================================
Weekly Plan
===============================================================================

.. sidebar:: Page Contents

   .. contents::
      :local:
	 
Overview of the schedule

.. list-table:: Schedule Section 2 (HPC-ABDS Technologies)
   :widths: 10 30 10 
   :header-rows: 1

   * - Week
     - Topic
     - Due
   * - Week 1
     - **Gaining Access to FutureSystems and Core Technologies**
     - 03/20
   * - Week 2
     - **The Basics of OpenStack**
     - 03/27
   * - Week 3
     - **Cloudmesh - Cloud Management Software**
     - 04/03
   * - Week 4
     - **IT Operations - Automation and Orchestration**
     - 04/10
   * - Week 5
     - **Virtual Clusters I (First Appearance of Hadoop)**
     - 04/17
   * - Week 6
     - **Virtual Clusters II (Composite Cluster with Sub-Clusters)**
     - 04/24
   * - Week 7
     - **Other Technologies**
     - 05/01
   * - Week 8
     - **Future**
     - N/A


Week 1
-------------------------------------------------------------------------------

Gaining Access to FutureSystems and Core Technologies
*******************************************************************************

In this week, you will learn how to gain access to the FutureSystems resources.
Some of the lessons have been prepared for the beginners to help understand the
basics of Linux operating systems and the collaboration tools i.e. GitHub,
Google hangout and remote desktop. Please watch video lessons and read online
materials on this page. It also covers Unix shell scripting, SSH and other
utilities with various exercises.

.. list-table:: Collaboration Tools
   :widths: 15 10 30 10 10 10
   :header-rows: 1

   * - Topic
     - Video
     - Text
     - Lab sessions
     - Study Material By
     - Lab Session Homework
   * - **Overview and Introduction**
     - `2 mins <https://www.youtube.com/watch?v=ZWzYGwnbZK4&list=PLLO4AVszo1SPYLypeUK0uPc4X6GXwWhcx&index=1>`_
     - `10 mins <../lesson/collaboration/overview.html>`_
     - 
     - 03/23
     - N/A
   * - **Google**
        - Google+, Hangout, Remote Desktop
     - `4 mins  <https://www.youtube.com/watch?v=kOrWm830vxQ&list=PLLO4AVszo1SPYLypeUK0uPc4X6GXwWhcx&index=2>`_
     - `15 mins  <../lesson/google.html>`_
     -
     - 03/23
     - N/A
   * - **Shell Access**                  
     - `3 mins <https://www.youtube.com/watch?v=aJDXfvOrzRE&index=3&list=PLLO4AVszo1SPYLypeUK0uPc4X6GXwWhcx>`_
     - `10 mins <../lesson/shell-access.html>`_
     - `5 mins <../lesson/shell-access.html#exercise>`_
     - 03/23
     - N/A
   * - **GitHub**
     - `18 mins <https://www.youtube.com/watch?v=KrAjal1a30w&list=PLLO4AVszo1SPYLypeUK0uPc4X6GXwWhcx&index=4>`_
     - `30 mins <../lesson/git.html>`_
     - `10 mins <../lesson/git.html#exercise>`_
     - 03/23
     - 03/27 



.. list-table:: System Access to FutureSystems                                                                              
   :widths: 15 10 30 10 10 10
   :header-rows: 1

   * - Topic
     - Video
     - Text
     - Lab sessions
     - Study Material By
     - Lab Session Homework
   * - **ssh-keygen**
     - `4 mins <https://www.youtube.com/watch?v=pQb2VV1zNIc&feature=em-upload_owner>`_
     - `10 mins <../../accounts/ssh.html#s-using-ssh>`_
     - see (a) below
     - 03/23
     - 03/27 see (a) below
   * - **Account Creation**
     - `12 mins <https://www.youtube.com/watch?v=X6zeVEALzTk>`_
     - `10 mins <../../accounts/accounts.html>`_
     - see (a) below
     - 03/23
     - 03/27 see (a) below
   * - **Remote Login**                                                                             
     - `6 mins <https://mix.office.com/watch/eddgjmovoty0>`_ 
     - `10 mins <../lesson/system/futuresystemsuse.html#remote-login>`_
     - see (a) below
     - 03/23
     - 03/27 see (a) below
   * - **Putty for Windows**
     - `11 mins <https://mix.office.com/watch/9z30n7rs67x0>`_
     - `10 mins <../lesson/system/futuresystemsuse.html#putty-under-preparation>`_
     - see (a) below
     - 03/23
     - 03/27 see (a) below

* (a) Create an account on the FutureSystems Portal, upload your ssh
  key and log into india. Dependent on your OS you may or may not need
  to use putty. Please identify a location from where you can login
  via ssh. Maybe such a location exists outside of your office.

       
.. list-table:: Linux Basics
   :widths: 15 10 30 10 10 10
   :header-rows: 1

   * - Topic
     - Video
     - Text
     - Lab sessions
     - Study Material By
     - Lab Session Homework
   * - **Overview and Introduction** 
     - `4 mins <https://www.youtube.com/watch?v=2uVZrGPCNcY&list=PLLO4AVszo1SOZF0tvCxLfS4AwkAJ1QKyp&index=1>`_
     - `5 mins <../lesson/linux/overview.html>`_
     - 
     - 03/23
     - 
   * - **Shell Scripting**                                                         
     - `15 mins <https://www.youtube.com/watch?v=TBOG3wmU8ZA&list=PLLO4AVszo1SOZF0tvCxLfS4AwkAJ1QKyp&index=2>`_
     - `30 mins <../lesson/linux/shell.html>`_
     - `5 mins <../lesson/linux/shell.html#exercises>`_,
       `5 mins <../lesson/linux/shell.html#id7>`_,
       `10 mins <../lesson/linux/shell.html#id11>`_,
       `10 mins <../lesson/linux/shell.html#id14>`_
     - 03/23
     - 03/27 all 4 Labs 
   * - **Editors**                            
        - Emacs, vi, and nano                                           
     - `5 mins <https://www.youtube.com/watch?v=yHW_qzOzPa0&list=PLLO4AVszo1SOZF0tvCxLfS4AwkAJ1QKyp&index=3>`_
     - `30 mins <../lesson/linux/editors.html>`_
     - see (b) below
     - 03/23
     - 03/27 see (b) below
   * - **Python**                             
        - virtualenv, Pypi                                                                                
     - `27 mins <https://www.youtube.com/watch?v=e_RuGr1dL0c&index=7&list=PLLO4AVszo1SOZF0tvCxLfS4AwkAJ1QKyp>`_
     - `1 hour <../lesson/linux/python.html>`_
     - `30 mins <../lesson/linux/python.html#exercises>`_
     - 03/23
     - 03/27
   * - **Package Managers**                   
        - yum, apt-get, and brew                                                      
     - `3 mins <https://www.youtube.com/watch?v=Onn9SKdUDUc&list=PLLO4AVszo1SOZF0tvCxLfS4AwkAJ1QKyp&index=4>`_
     - `10 mins <../lesson/linux/packagemanagement.html>`_
     - see (c) below
     - 03/23
     - 03/27 see (c) below
   * - **Advanced SSH**
        - SSH Config and Tunnel
     - `3 mins <https://www.youtube.com/watch?v=eYanElmtqMo&index=6&list=PLLO4AVszo1SOZF0tvCxLfS4AwkAJ1QKyp>`_
     - `20 mins <../lesson/linux/advancedssh.html>`_
     - `5 mins <../lesson/linux/advancedssh.html#exercise-i>`_, 
       `5 mins <../lesson/linux/advancedssh.html#exercise-ii>`_
     - 03/23
     - 03/27 both Labs
   * - **Modules**
     - `3 mins <https://www.youtube.com/watch?v=0mBERd57pZ8&list=PLLO4AVszo1SOZF0tvCxLfS4AwkAJ1QKyp&index=6>`_
     - `10 mins <../ lesson/linux/modules.html>`_
     - `5 mins <../lesson/linux/modules.html#exercises>`_
     - 03/23
     - 03/27


* (b) Find an editor that you will be useing to do your programming
  with. For advanced Python programming we recommend PyCharm. However
  you can probably only use this on your local computer. The way you
  could use it is to edit python locally, check the code into github
  and check it out into your vm or your login on
  india.futuresystems.org. This is how many of us work.
* (c) locate a package that you install on your VM that you started
  with Openstack. Provide a verification that the package was
  installed (log). Do not forget to delete the VM after you are
  done. Which package manager is used on ubuntu?



Length of the lessons in Week 1
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* Total of video lessons: 2 hours
* Total of study materials: 4 hours and 30 minutes
* Total of lab sessions: 1 hour and 30 minutes

Week 2
-------------------------------------------------------------------------------

Introduction to OpenStack and Public Clouds
*******************************************************************************

OpenStack is a open-source cloud computing software platform and a
community-driven project. You can use OpenStack to build a cloud infrastructure
in your public or private network, or you can simply use cloud software for
your services. The lessons in this week are specifically prepared to try
OpenStack Software and give you the confidence and understanding of using IaaS
cloud platforms. There are tutorial lessons to explore OpenStack web dashboard
(Horizon) and compute engine (Nova) including Public Clouds e.g. Amazon EC2 or
Microsoft Azure.

.. list-table:: Basics of OpenStack
   :widths: 15 10 30 10 10 10
   :header-rows: 1

   * - Topic
     - Video
     - Text
     - Lab sessions
     - Study Material By
     - Lab Session Homework
   * - **Introduction and Overview**
     - `12 mins <https://mix.office.com/watch/u7uovy9i06jo>`_
     - `10 mins </introduction_to_cloud_computing/class/lesson/iaas/overview_openstack.html>`_
     - 
     - 03/30
     - 
   * - **OpenStack for Beginners**
     - `21 mins <https://mix.office.com/watch/qohooyyk3wa1>`_
     -
     -
     - 03/30
     - 
   * - -- Compute Engine (Nova)
     -
     - `1 hour </introduction_to_cloud_computing/class/lesson/iaas/openstack.html>`_
     - `30 mins </introduction_to_cloud_computing/class/lesson/iaas/openstack.html#exercises>`_
     - 03/30
     - 04/03
   * - -- Web Dashboard (Horizon)
     - 
     - `15 mins </introduction_to_cloud_computing/class/lesson/iaas/openstack_horizon.html>`_
     - `15 mins </introduction_to_cloud_computing/class/lesson/iaas/openstack_horizon.html#exercises>`_
     - 03/30
     - 04/03
   * - **Storage (Swift)**
     - `3 mins <https://mix.office.com/watch/w3rko4itecgc>`_
     - `10 mins </introduction_to_cloud_computing/class/lesson/iaas/openstack.html#swift-storage>`_
     -
     - 03/30
     - 
   * - **Network (Neutron)**
     - `3 mins <https://mix.office.com/watch/1dt5hp0e2grov>`_
     - `10 mins </introduction_to_cloud_computing/class/lesson/iaas/openstack.html#neutron-network>`_
     -
     - 03/30
     - 
   * - **Introduction to OpenStack Juno Release**
     - `2 mins <https://mix.office.com/watch/cz6xehrs9xor>`_
     - `10 mins </introduction_to_cloud_computing/class/lesson/iaas/openstack_juno.html>`_
     - 
     - 03/30
     - 

.. list-table:: Other IaaS Platforms - Public Commercial Clouds
   :widths: 15 10 30 10 10 10
   :header-rows: 1

   * - Topic
     - Video
     - Text
     - Lab sessions
     - Study Material By
     - Lab Session Homework
   * - **Amazon Web Services (AWS)**
     - `16 mins <https://mix.office.com/watch/1351hz8j187i7>`_
     - `30 mins </introduction_to_cloud_computing/class/lesson/iaas/aws_tutorial.html>`_
     - `45 mins </introduction_to_cloud_computing/class/lesson/iaas/aws_tutorial.html#exercises>`_
     - 03/30
     - 04/03
   * - **Microsoft Azure**
     - `29 mins <https://mix.office.com/watch/kzh0nwvdw6tm>`_
     - `50 mins </introduction_to_cloud_computing/class/lesson/iaas/azure_tutorial.html>`_
     - `10 mins </introduction_to_cloud_computing/class/lesson/iaas/azure_tutorial.html#exercise1>`_
     - 03/30
     - 04/03

.. list-table:: Additional (optional) Further Study Materials
   :widths: 15 10 30 10 10 10
   :header-rows: 1

   * - Topic
     - Video
     - Text
     - Lab sessions
     - Study Material By
     - Lab Session Homework
   * - **OpenStack for Beginners**
         - Compute Engine (Nova)
     -
     - `2 hours </introduction_to_cloud_computing/iaas/index.html>`_
     - `50 mins </introduction_to_cloud_computing/iaas/openstack.html#exercises>`_
     - Not due
     - Not due
   * - **Other IaaS Platforms**
        - Public Commercial Clouds
             - Microsoft Azure
     -
     -
     - `50 mins </introduction_to_cloud_computing/class/lesson/iaas/azure_tutorial.html#exercise2>`_
     - Not due
     - Not due

Length of the lessons in Week 2
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* Total of video lessons: 1 hour and 30 minutes
* Total of study materials: 3 hours and 15 minutes
* Total of lab sessions: 1 hours 40 minutes


Week 3
-------------------------------------------------------------------------------


Cloudmesh - Cloud Management Software
*******************************************************************************

Cloudmesh is a cloud resource management software written in Python. It
automates launching multiple VM instances across different cloud platforms
including Amazon EC2, Microsoft Azure Virtual Machine, HP Cloud, OpenStack, and
Eucalyptus. The web interface of Cloudmesh helps users and administrators
manage entire cloud resources with the most cutting-edge technologies such as
Apache LibCloud, Celery, IPython, Flask, Fabric, Docopt, YAML, MongoDB, and
Sphinx. Command Line Tools and Rest APIs are also supported.

.. list-table:: Basics of Cloudmesh
   :widths: 15 10 30 10 10 10
   :header-rows: 1

   * - Topic
     - Video
     - Text
     - Lab sessions
     - Study Material By
     - Lab Session Homework
   * - **Introduction and Overview**
     - `29 mins <http://www.youtube.com/watch?v=njHHjRMb7V8>`_
     - `30 mins </introduction_to_cloud_computing/cloudmesh/overview.html>`_
     - 
     - 04/06
     - 04/10

.. list-table:: Cloudmesh for Beginners
   :widths: 15 10 30 10 10 10
   :header-rows: 1

   * - Topic
     - Video
     - Text
     - Lab sessions
     - Study Material By
     - Lab Session Homework
   * - **Installation on a local machine**
     - `18 mins <http://www.youtube.com/watch?v=lGiJifD0VgU>`_
     - `30 mins </introduction_to_cloud_computing/cloudmesh/setup/quickstart.html>`_
     -
     - 04/06
     - 04/10
   * - **Installation on a virtual machine OpenStack**
     - `33 mins <http://www.youtube.com/watch?v=rcecpgm-47g>`_
     - `30 mins </introduction_to_cloud_computing/cloudmesh/setup/setup_openstack.html>`_
     - 
     - 04/06
     - 04/10
   * - **Command Line Tools (CLI)**
     - `12 mins <http://www.youtube.com/watch?v=hdq-t-ggkXA>`_
     - `30 mins </introduction_to_cloud_computing/cloudmesh/shell/index.html>`_
     -
     - 04/06
     - 04/10
   * - **Web Interface (GUI)**
     - `16 mins <http://www.youtube.com/watch?v=l_P4G85rysA>`_
     - `30 mins </introduction_to_cloud_computing/cloudmesh/gui/index.html>`_
     -
     - 04/06
     - 04/10
   * - **Python APIs**
     - `15 mins <http://www.youtube.com/watch?v=xOL_-Sfh9MA>`_ 
     - `30 mins </introduction_to_cloud_computing/cloudmesh/api/index.html>`_
     -
     - 04/06
     - 04/10
   * - **IPython on Cloudmesh**
     - `15 mins <http://www.youtube.com/watch?v=1dn_av-zC00>`_
     - `20 mins </introduction_to_cloud_computing/cloudmesh/ipython.html>`_
     -
     - 04/06
     - 04/10
   * - **Using India OpenStack on Cloudmesh**
     - `5 mins <https://mix.office.com/watch/irhlsfq220zh>`_
     - Not yet available
     - 
     - 04/06
     - 04/10

.. list-table:: Advanced Cloudmesh
   :widths: 15 10 30 10 10 10
   :header-rows: 1

   * - Topic
     - Video
     - Text
     - Lab sessions
     - Study Material By
     - Lab Session Homework
   * - **Introduction and Overview**
     - Not yet available
     - Not yet available
     - 
     - 04/06
     - 04/10
   * - **VM Management**
     - Not yet available
     - Not yet available
     - 
     - 04/06
     - 04/10
   * - **Adding new Commands via a Python Package**
     - `5 mins <https://www.youtube.com/watch?v=UFLyCVpDhgI&feature=em-upload_owner>`_
     - `5 mins <http://cloudmesh.github.io/cmd3/manual.html#generating-independent-packages>`_
     - 
     - 04/06 
     - 04/10 (see (cm.1) bellow
   * - **Virtual Clusters with Cloudmesh**
        - SSH Connections between nodes
        - Host Configuration
     - `5 mins <https://mix.office.com/watch/lk39mr08k0ox>`_
     - `20 mins </introduction_to_cloud_computing/cloudmesh/cm/_cm-cluster.html>`_
     - 
     - 04/06
     - 04/10

Homework cm.1
^^^^^^^^^^^^^^^^^^^^^^

(cm.1) This assignment will teach you how to add new commands to
cloudmesh while using the `cm-generate-command`. First read the
documentation and watch the video for an example to add a simple
command. After you successfully installed it, find a python package
that you like and can be installed with pip. Develop a new command
that has the following options (additional parameters may be used if
necessary). We use here the name your_command as a placeholder find a
better name for it::

  cm your_command deploy ...

      deploys the python package

  cm your_command start ...

      if the package has some services start them now

   cm your_command stop ...

       if the package has some services stop them  
   
   cm your_command run ...

       runs some useful command against the services

Alternatively, if you can not locate a good package, you can use 
shelve, while implementing the commands::

  cm shelve deploy
  cm shelve start --file=FILENAME     # filename of the shelve file
  cm shelve clear                                # removes the shelve file
  cm shelve set index data       # adds the data to the given index
  cm shelve delete index          # removes the data at the index
  cm shelve list                        # list the contents

Provide an extensive documentation while using docopts.

In a future task we will use what you have learned here to provide a
cm command that deploys and manages an advanced PaaS onto a virtual
cluster. For now we just do a simple version so you get familiar with
the concepts. Examples for such a bigger deployments are:

* pig
* zookeeper
* hadoop (already provided by cm)
* harp
* apache
* drupal
* others

You will sudo for many of them, thus india is not sufficient for the
more advanced PaaS. These are supposed to be done on a virtual cluster
while leveraging the `cm cluster` command.

          
Week 4
-------------------------------------------------------------------------------


IT Operations - Automation and Orchestration (under preparation)
*******************************************************************************

.. list-table:: IT Operations - Automation and Orchestration
   :widths: 15 10 30 10 10 10
   :header-rows: 1

   * - Topic
     - Video
     - Text
     - Lab sessions
     - Study Material By
     - Lab Session Homework
   * - **DevOps**
        - Ansible
        - SaltStack
        - Puppet
        - Chef
        - OpenStack Heat
        - Ubuntu Juju
     - Not yet available
     - Not yet available
     - 
     - 04/13
     - 04/17
   * - **Discussion**
        - Orchestration vs Collective DevOps
        - PaaS
        - Cloudmesh
     - Not yet available
     - Not yet available
     - 
     - 04/13
     - 04/17



Week 5 
-------------------------------------------------------------------------------


Virtual Clusters I (under preparation)
*******************************************************************************

**First Appearance of Hadoop in This Week**

.. list-table:: Virtual Clusters I
   :widths: 15 10 30 10 10 10
   :header-rows: 1

   * - Topic
     - Video
     - Text
     - Lab sessions
     - Study Material By
     - Lab Session Homework
   * - **Introduction and Overview**
     - Not yet available
     - Not yet available
     - 
     - 04/20
     - 04/24
   * - **Dynamic Deployment of Arbitrary X Software on Virtual Cluster**
     - Not yet available
     - Not yet available
     - 
     - 04/20
     - 04/24
   * - **Hadoop Virtual Cluster**
        - Cloudmesh
        - Discussion
        - Advanced Topics with Hadoop
             - Zookeeper and HBase
             - Yarn
             - OpenStack Havana
     - Not yet available
     - Not yet available
     - 
     - 04/20
     - 04/24

Week 6
-------------------------------------------------------------------------------


Virtual Cluster II: Composite Cluster with Sub-Clusters (under preparation)
*******************************************************************************

.. list-table:: Virtual Cluster II
   :widths: 15 10 30 10 10 10
   :header-rows: 1

   * - Topic
     - Video
     - Text
     - Lab sessions
     - Study Material By
     - Lab Session Homework
   * - **Composite Cluster with Sub-Clusters**
        - Introduction and Overview
        - Creating a Cross Resource Virtual Cluster
     - Not yet available
     - Not yet available
     - 
     - 04/27
     - 05/01
   * - **OpenMPI Virtual Cluster**
        - Introduction and Overview
        - HPC Stack - MPI
        - Cloudmesh HPC
     - Not yet available
     - Not yet available
     - 
     - 04/27
     - 05/01
   * - **MongoDB Virtual Cluster**
        - Introduction and Overview
        - Sharded MongoDB
     - Not yet available
     - Not yet available
     - 
     - 04/27
     - 05/01

Week 7
-------------------------------------------------------------------------------


Other Technologies (under preparation)
*******************************************************************************

.. list-table:: Other Technologies
   :widths: 15 10 30 10 10 10
   :header-rows: 1

   * - Topic
     - Video
     - Text
     - Lab sessions
     - Study Material By
     - Lab Session Homework
   * - **Virtualization Technologies**
         - Introduction and Overview
         - Hypervisors
             - KVM
             - Containers (LXC)
             - Docker
     - Not yet available
     - Not yet available
     - 
     - 05/04
     - 05/06
   * - **VM Software**
         - Vagrant
         - Oracle VirtualBox
         - VMWare
     - Not yet available
     - Not yet available
     - 
     - 05/04
     - 05/06
   * - **Apache Big Data Stack (ABDS)**
         - Apache Zookeeper
         - Apache Storm
         - Apache Mesos
         - Apache HBase
         - Apache Spark
         - Apache Pig
         - Apache Hive
     - Not yet available
     - Not yet available
     - 
     - 05/04
     - 05/06
   * - **Glossary**
     - Not yet available
     - Not yet available
     - 
     - 05/04
     - 05/06

Week 8
-------------------------------------------------------------------------------


Future (under preparation)
*******************************************************************************

.. list-table:: Future
   :widths: 15 10 30 10 10 10
   :header-rows: 1

   * - Topic
     - Video
     - Text
     - Lab sessions
     - Study Material By
     - Lab Session Homework
   * - **What will the Future Bring**
     - Not yet available
     - Not yet available
     - 
     - Not due
     - Not due
   * - **GE Industrial Internet of Things (IIoT)**
     - Not yet available
     - Not yet available
     - 
     - Not due
     - Not due

