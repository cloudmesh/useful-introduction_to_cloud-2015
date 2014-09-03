Adding Azure to the yaml file
================================

Microsoft Windows Azure offers security credentials per a valid subscription on
a user account. Based on the subscription id, chargeable usage is going to be
applied to your bill. To authenticate requests to Azure, you need to configure
your credentials on Cloudmesh.

The following step-by-step tutorial explains the configuration of Azure
credentials on Cloudmesh.

Azure account
-----------------------

You may sign in with your existing account or create a new Azure account.
Azure provides free-trial to a new account. The Windows Azure site is at:
`https://manage.windowsazure.com <https://manage.windowsazure.com>`_

Download credentials
------------------------

.publishsettings

Install Azure CLI
------------------

Linux
^^^^^
http://azure.microsoft.com/en-us/documentation/articles/xplat-cli/

OSX
^^^^^^

Import Credentials via Azure CLI
---------------------------------

$ azure account download
$ azure account import <.publishsettings file path>

Download Subscription File (.publishsettings)
---------------------------------------------
 
http://go.microsoft.com/fwlink/?LinkId=254432

[screenshot]

Place X.509 certificate on Cloudmesh
------------------------------------

$ cp -p ~/.azure/managementCertificate.pem ~/.cloudmesh/azure_managementCertificate.pem
( Only the owner with read and write permission e.g. -rw-------)

Replace Subscription ID
-------------------------

$ azure service cert list
provides your subscription id that just imported from the .publishsettings file.

Now, you are ready to use Azure Virtual Machines on Cloudmesh.

Test Azure Virtual Machine
--------------------------

TBD
