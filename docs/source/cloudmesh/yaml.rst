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

.. todo:: Hyungro

Adding Azure to the yaml file
----------------------------------------------------------------------

.. todo:: Hyungro

Adding devstack to the yaml file
----------------------------------------------------------------------

.. todo:: Hyungro

Adding dreamhost to the yaml file
----------------------------------------------------------------------

Dreamhost provides an Openstack cloud that can be accessed through the
dreamhost panel at:

* https://panel.dreamhost.com/index.cgi

The Horizon interface is located at

* https://dashboard.dreamcompute.com

If you are a customer of dreamhost, use your username and
password that was send to you.

To use cloudmesh, please add this username and password in the
placeholder for dreamhost.

