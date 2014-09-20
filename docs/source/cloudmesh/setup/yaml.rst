Creating the yaml file
======================================================================

.. highlight:: bash

You must have installed cloudmesh as discussed in ??? and run::

 $ ./install/new


This will create a `~/.cloudmesh` directory with some basic yaml files
that you will need to modify.

Adding FutureGrid Openstack clouds on sierra and india to the yaml file
----------------------------------------------------------------------

For FutureGrid we have additionally provided a script that
automatically creates some yaml files from the installation. In future
FutureGrid will provide directly a yaml for cloudmesh so that this
step is unnecessary. Before you can execute this command you maust
make sure that you can log into india and sierra via ssh. Once you
have verified this for example with::

  $ ssh $PORTALNAME@india.futuregrid.org hostname
  $ ssh $PORTALNAME@sierra.futuregrid.org hostname

Now create the yaml file while fetching some information from the
remote machines::

  $ ./install rc fetch

First it will ask you which username you have on FutureGrid. The name
may be different from your current local machine name. Please enter
your name when you see::


  Please enter your portal user id [default: albert]: 

After this you can update the yaml files with the data fetched from
the india and sierra with the command::

  $ ./install rc fill

The reason why we have separated the commands and not just created one
command is to provide you with the ability to double check overwriting
possibly an existing rc file.

Adding FutureGrid OpenStack Clouds on alamo and hotel to the yaml file
--------------------------------------------------------------------------

We do not recommend adding these machines as they use the FG portal
and password. However if you do so, we have placeholders in the yaml
file for these clouds. In case you can not find them, simply copy the
one from india and make appropriate corrections.

Adding HP cloud to the yaml file
----------------------------------------------------------------------

The cloud offered from HP is an Openstack cloud and contains the
ability to conduct project and user based billing. As this cloud is
Openstack it behaves much the same as the once defined on India and
Sierra. There may be differences based on the version. 

HP provides an interface to their cloud through horizon. The
documentation for it can be found at:

* http://docs.hpcloud.com/hpcloudconsole

To use the cloud you have to first create an account with HP, which
will charge you real money for using their cloud. Make sure you
understand what costs will be charged before you request thousands of
virtual machines. Naturally this is valid for any other commercial
cloud also. The console for the HP cloud is available at:

* http://www.hpcloud.com/console

Which will bring you to their horizon interface:

* https://horizon.hpcloud.com

You can add your username and password into the cloudmesh.yaml in the
.cloudmesh directory. It is that simple. However, presently the data
is stored in cleartext which we will change in future. Thus if your
would like to run cloudmesh we currently recommend running it on your
own local machine. Make sure that the access to the yaml file is
properly secured.


Adding AWS to the yaml file
----------------------------------------------------------------------

Amazon EC2 Cloud requires Secret Access Keys to use Amazon Web Services (AWS).
To configure Amazon EC2 on Cloudmesh, you need to provide the Secret Access
Keys of your account. Amazon allows only to download the credentials via their
web page, you need to go to the `Security Credentials
<http://console.aws.amazon.com/iam/home?#security_credential>`_ page to get the
credentials. You may use your existing AWS account or create a new AWS account.
The Access Key is a pair of Access Key ID and Secret Access Key and these
values should be replaced with *EC2_ACCESS_KEY* and *EC2_SECRET_KEY* fields in
the yaml file. Cloudmesh identifies *cm_type: aws* as Amazon Web Services in
the yaml file, you update the *aws* section with your security credentials.
Note that Amazon offers commercial services, the access key identification and
the secret key should be kept in a safe place to avoid any unexpected usage
from someone who you didn't authorize. 

Adding Azure to the yaml file
----------------------------------------------------------------------

Microsoft Windows Azure offers security credentials per a valid
subscription on a user account. Based on the subscription id,
chargeable usage is going to be applied to your bill. To authenticate
requests to Azure, you need to configure your credentials for
Cloudmesh. The following step-by-step tutorial explains the
configuration of Azure credentials on Cloudmesh.

To connect Azure Virtual Machines to Cloudmesh, you need to provide
Azure credentials to authenticate requrests in the yaml file. You can
find the credentials in the 

* `Azure Management Portal <https://manage.windowsazure.com>`_ 

which is a web interface to manage your account and Azure Virtual
Machines.  Also, you can find credentials by downloading the
subscription file (.publishsettings) here:

* `http://go.microsoft.com/fwlink/?LinkId=254432 <http://go.microsoft.com/fwlink/?LinkId=254432>`_.

Once you download the file, you may need to import your subscription
Id and valid X.509 certificate from the file with the help of the  Azure cross-platform
command line interface. More information about the Azure CLI can be
found in the Manual/article about the

* `Azure Cross-Platform Command-Line Interface <http://azure.microsoft.com/en-us/documentation/articles/xplat-cli>`_. 

The Azure credentials require that the X.509 certificate is placed in
the `.cloudmesh` directory. The *subscriptionid* field should be filled
with your Azure subscription id. The valid X.509 certificate file
(.pem) must also be stored in the `.cloudmesh` directory. We store it
under the name::

  $HOME/.cloudmesh/azure_managementCertificate.pem

Cloudmesh yaml file has an example invalid entry that you can change
with your settings. It can be easily identified while looking for the
keyword azure in the `cloudmesh.yaml` file.
As Azure is a commercial service it is important that you properly
secure the .cloudmesh directory and its yaml files. 

.. note:: Recommended files and directory permissions for Secured Cloudmesh
   To protect the yaml files against any access from other users, we recommend
   to use `chmod` command. Try `chmod -R o+rwx,go-rwx ~/.cloudmesh` to make
   any file in the *.cloudmesh* directory a private file to your user account.
   This way allows you have a full access to the files and the directory but
   not others.

Azure Quickstart
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Azure account
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

If you do not have an Azure account you can obtain one from Microsoft.
Microsoft provides a free-trial for new account applicants. The
Windows Azure site is located at 

* `https://manage.windowsazure.com <https://manage.windowsazure.com>`_

Download credentials
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

Form ther you can download the::

  .publishsettings


Install Azure CLI
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

Next you will need to install the Azure CLI. This is documented at 

* http://azure.microsoft.com/en-us/documentation/articles/xplat-cli/

Here you find install instructions fror Linux but also a link to an
OSX installer.

Once the client is installed you can download the credentials

Import Credentials via Azure CLI
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

::

   $ azure account download
   $ azure account import <.publishsettings file path>

Download Subscription File (.publishsettings)
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
 
* http://go.microsoft.com/fwlink/?LinkId=254432

Place X.509 certificate on Cloudmesh
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

::

  $ cp -p ~/.azure/managementCertificate.pem ~/.cloudmesh/azure_managementCertificate.pem

 Only the owner with read and write permission e.g. -rw-------

.. note:: Recommended files and directory permissions for Secured Cloudmesh
   To protect the yaml files against any access from other users, we recommend
   to use `chmod` command. Try 
   `chmod o+rwx,go-rwx ~/azure_managementCertificate.pem` to make the file a 
   private file to your user account. This way allows you have a full access to
   the file but not others.

Replace Subscription ID
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

::

  $ azure service cert list

provides your subscription id that just imported from the .publishsettings file.

Now, you are ready to use Azure Virtual Machines on Cloudmesh.

Test Azure Virtual Machine
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

TBD


Adding devstack to the yaml file (TBD)
----------------------------------------------------------------------

DevStack offers an easy method to try out Openstack on your machine or
in a virtual machine (VM). `DevStack <http://devstack.org>`_ provides
a setup guide and configuration here: `Configuration
<http://devstack.org/configuration.html>`_.


Adding dreamhost to the yaml file
----------------------------------------------------------------------

Dreamhost provides an Openstack cloud that can be accessed through the
dreamhost panel at:

* https://panel.dreamhost.com/index.cgi

The Horizon interface is located at

* https://dashboard.dreamcompute.com

If you are a customer of dreamhost, use your username and password
that was send to you.

To use cloudmesh, please add this username and password in the
placeholder for dreamhost.

