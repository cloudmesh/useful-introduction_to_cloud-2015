
Cloudmesh Shell
===============

Initialization
--------------

.. code:: python

    import cloudmesh
Activating Clouds
-----------------

In order for cloudmesh to work with multiple coulds, we need to find out
first which clouds are available. Users can add their own clouds later
which we describe in the registration section.

Let us inspect what is already available by invoking the list command

.. code:: python

    print cloudmesh.shell("cloud list")

.. parsed-literal::

    +---------+----------+
    | cloud   | active   |
    +=========+==========+
    | alamo   |          |
    +---------+----------+
    | aws     |          |
    +---------+----------+
    | azure   |          |
    +---------+----------+
    | hp      |          |
    +---------+----------+
    | hp_east |          |
    +---------+----------+
    | india   |          |
    +---------+----------+
    | sierra  |          |
    +---------+----------+
    


As you see we have a number of clouds, but none of them is already
active. Thus we need to first activate a cloud. We assume that you have
an account on FutureGrid. Let us activate the cloud india

.. code:: python

    print cloudmesh.shell("cloud on india")

.. parsed-literal::

    * india
    Refreshing gvonlasz servers india ->
    Refresh time: 0.382435083389
    Store time: 0.00305485725403
    [92mcloud 'india' activated.[0m
    


We also have a conveniet interactive selector to select a cloud to work
with, that however does not work with ipython

::

    "cloud select"

or you may also input "cloud select india" to select a specific cloud
india

To check if the cloud was activated, simply use the list command again

.. code:: python

    print cloudmesh.shell("cloud list")

.. parsed-literal::

    +---------+----------+
    | cloud   | active   |
    +=========+==========+
    | alamo   |          |
    +---------+----------+
    | aws     |          |
    +---------+----------+
    | azure   |          |
    +---------+----------+
    | hp      |          |
    +---------+----------+
    | hp_east |          |
    +---------+----------+
    | india   | True     |
    +---------+----------+
    | sierra  |          |
    +---------+----------+
    


Starting VMs
------------

Now let us see how to start VMs on a cloud, here is how to start a VM on
cloud india

.. code:: python

    print cloudmesh.shell("vm start --cloud=india --image=futuregrid/ubuntu-14.04 --flavor=m1.small")
You may don't know what images or flavors are available on the cloud, or
you don't want to type a long command every time you start a VM, things
can get a lot easier by performing some setting up...

set default image
~~~~~~~~~~~~~~~~~

You can invoke command "cloud set image india" to set a image
interactively, however this does not work with ipython. Then we can use
the following commands to get a list of images first and set default
image by giving its image name or image id

.. code:: python

    print cloudmesh.shell("list image india --refresh")
.. code:: python

    print cloudmesh.shell("cloud set image india --image=futuregrid/ubuntu-14.04")
set default flavor
~~~~~~~~~~~~~~~~~~

Similar as setting default image, to set up default flavor
interactively, "cloud set flavor india", otherwise you may get a list of
flavors then set by giving flavor name or flavor id

.. code:: python

    print cloudmesh.shell("list flavor india --refresh")
.. code:: python

    print cloudmesh.shell("cloud set flavor india --flavorid=2")
set default cloud
~~~~~~~~~~~~~~~~~

If you want to make things even more convenient, you can set a default
cloud or select a cloud to work with so that you don't have to type in a
cloud everytime you need to specify a cloud, to set india as default
cloud

.. code:: python

    print cloudmesh.shell("cloud set default india")
to select a cloud

.. code:: python

    print cloudmesh.shell("cloud select india")
You can see a selected cloud as a temporarily default cloud to work
with.

For more details of using command cloud to set up a cloud

.. code:: python

    print cloudmesh.shell("cloud -h")
simple way to start a VM
~~~~~~~~~~~~~~~~~~~~~~~~

After all setting up above, now you can start a VM simply by typing in

.. code:: python

    print cloudmesh.shell("vm start")
set default VM name
~~~~~~~~~~~~~~~~~~~

If the user doesn't provide a name while starting VMs, cloudmesh will
generate labels for them. The default form to name VMs is prefix\_index,
where prefix is a string and index is an non-negative integer. If a
index is used, the index value will be automatically added by one
waiting to be used for next VM. To check your current prefix and index

.. code:: python

    print cloudmesh.shell("label")
To change the prefix and/or reset index(e.g. to abc and 3)

.. code:: python

    print cloudmesh.shell("label --prefix=abc --id=3")
Refreshing VM status
--------------------

After you have started or deleted VMs, you may want to check clouds' VMs
status. To refresh cloud india's VMs information

.. code:: python

    print cloudmesh.shell("list vm india --refresh")
Starting multiple VMs
---------------------

Sometimes we want to start more than one VM at the same time, we can
choose the option --count=int where int is the number of VMs you want to
start. For example, to start 5 VMs on india

.. code:: python

    print cloudmesh.shell("vm start --cloud=india --count=5")
Deleting VMs
------------

To delete one VM is easy, what if we want to delete 1000 VMs, we need a
more convenient way to do it. Cloudmesh shell provides several methods
to find the VMs and delete them, you may think there are two phases of
VM deletion, searching and deleting. Here are some examples:

to delete all VMs of cloud india

.. code:: python

    print cloudmesh.shell("vm delete --cloud=india --force")
Note here we use the option "--force", without it the shell will give
you a list of VMs to delete and ask for your confirmation.

to delete a VM by giving its name (you may always provide a cloud unless
you have specified a default cloud or have selected a cloud)

.. code:: python

    print cloudmesh.shell("vm delete --cloud=india abc_2 --force")
to delete a VM by group

.. code:: python

    print cloudmesh.shell("vm delete --cloud=india --goup=testgroup --force")
We can also narrow the search result by giving more search conditions.
For example, to delete VMs of cloud india that they are also in the
group 'testgroup' and they have the prefix name 'abc' and their indices'
range is no greater than 100

.. code:: python

    print cloudmesh.shell("vm delete --cloud=india --goup=testgroup --prefix=abc --range=,100 --force")
For more details for command vm

.. code:: python

    print cloudmesh.shell("vm -h")