Creating the yaml file
======================================================================

YOu must have installed cloudmesh as discussed in ???

and run 

 ./install/new


This will create a ~/.cloudmesh directory with some basic yaml files that you will need to modify.

For FutureGrid we have aditionally provided a script that automatically creates some yaml files from the instalation. In future FutureGrid will provide directly a yaml for cloudmesh so that this step is unnecessary. Before you can execute this command you maust make sure that you can log into india and siera via ssh. Once you have verified this for example with::

  ssh USERNAME@india.futuregrid.org hostname
  ssh USERNAME@sierra.futuregrid.org hostname

Now create the yaml file while fetching some information from the remote machines::

  ./install rc fetch

First it will ask you which username you have on futuregrid. The name may be different from your current local machine name. Please enter your name when you see::


  Please enter your portal user id [default: flat]: 

After this you can update the yaml files with the data fetched from the india and sierra with the command::

  ./install rc fill

The reason why we have separated the commands and not just created one command is to provide you with the ability to double check overwriting possibly an existing rc file.

Adding HP cloud to the yaml file
======================================================================

.. todo:: Gregor

Adding AWS to the yaml file
======================================================================

.. todo:: Hyungro

Adding Azaure to the yaml file
======================================================================

.. todo:: Hyungro

Adding devstack to the yaml file
======================================================================

.. todo:: Hyungro

Adding dreamhost to the yaml file
======================================================================

.. todo:: Gregor


Adding dreamhost to the yaml file
======================================================================

.. todo:: Gregor









































































