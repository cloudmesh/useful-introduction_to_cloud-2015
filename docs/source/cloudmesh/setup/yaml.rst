Creating the yaml file
======================================================================

You must have installed cloudmesh as discussed in ??? and run::

 ./install/new


This will create a ~/.cloudmesh directory with some basic yaml files
that you will need to modify.

Adding FutureGrid Openstack clouds on sierra and india to the yaml file
----------------------------------------------------------------------

For FutureGrid we have additionally provided a script that
automatically creates some yaml files from the installation. In future
FutureGrid will provide directly a yaml for cloudmesh so that this
step is unnecessary. Before you can execute this command you maust
make sure that you can log into india and sierra via ssh. Once you
have verified this for example with::

  ssh USERNAME@india.futuregrid.org hostname
  ssh USERNAME@sierra.futuregrid.org hostname

Now create the yaml file while fetching some information from the
remote machines::

  ./install rc fetch

First it will ask you which username you have on FutureGrid. The name
may be different from your current local machine name. Please enter
your name when you see::


  Please enter your portal user id [default: flat]: 

After this you can update the yaml files with the data fetched from
the india and sierra with the command::

  ./install rc fill

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

To connect Azure Virtual Machines to Cloudmesh, you need to provide
Azure credentials to authenticate requrests in the yaml file. You can
find the credentials on `Azure Management Portal
<https://manage.windowsazure.com>`_ which is a web interface to manage
your account and Azure Virtual Machines.  Also, you can find
credentials by downloading the subscription file (.publishsettings)
here: `http://go.microsoft.com/fwlink/?LinkId=254432
<http://go.microsoft.com/fwlink/?LinkId=254432>`_. Once you download
the file, you may need to import your subscription Id and valid X.509
certificate from the file by Azure Cross-Platform Command-Line
Interface. About installing the interface, please see the manual here:
`Azure Cross-Platform Command-Line Interface
<http://azure.microsoft.com/en-us/documentation/articles/xplat-cli>`_. Not
like setting AWS to the yaml file, Azure credentials require that the
X.509 certificate stays in the .cloudmesh directory. The
*subscriptionid* field should be filled with your Azure
subscription id. The valid X.509 certificate file (.pem) is also
required to be stored with the filename
*$HOME/.cloudmesh/azure_managementCertificate.pem*. Cloudmesh
identifies *cm_type: azure* as Microsoft Windows Azure in the yaml
file, you update the *aws* section with your credentials. Note that
Azure also offers commercial services, your subscription should be
stored in a safe place to avoid any unexpected usage.

.. include:: setup_azure.rst

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

