
Shell command vm startup and deletion examples
==============================================

Part1: Preparation
------------------

.. code:: python

    import cloudmesh
select a cloud to work with
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: python

    print cloudmesh.shell("cloud list")
.. code:: python

    print cloudmesh.shell("cloud select india")
activate the cloud
~~~~~~~~~~~~~~~~~~

.. code:: python

    print cloudmesh.shell("cloud on")
set default image
~~~~~~~~~~~~~~~~~

.. code:: python

    print cloudmesh.shell("list image --refresh")
.. code:: python

    print cloudmesh.shell("cloud set image --image=futuregrid/ubuntu-14.04")
set default flavor
~~~~~~~~~~~~~~~~~~

.. code:: python

    print cloudmesh.shell("list flavor --refresh")
.. code:: python

    print cloudmesh.shell("cloud set flavor --flavorid=2")
Part2: Start VM
---------------

start one vm on the selected or default cloud using its default image and default flavor
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: python

    print cloudmesh.shell("vm start")
check realtime vm status of the cloud
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: python

    print cloudmesh.shell("list vm --refresh")
delete the vm (--cloud=india: delete all vms of cloud india, --force: no user confirmation)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: python

    print cloudmesh.shell("vm delete --cloud=india --force")
.. code:: python

    print cloudmesh.shell("list vm --refresh")
Part3: Start multiple VMs
-------------------------

using option --count=count
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: python

    print cloudmesh.shell("vm start --count=3")
.. code:: python

    print cloudmesh.shell("list vm --refresh")
.. code:: python

    print cloudmesh.shell("vm delete --cloud=india --force")
.. code:: python

    print cloudmesh.shell("list vm --refresh")
Part4: Start VMs on different clouds
------------------------------------

activate another cloud
~~~~~~~~~~~~~~~~~~~~~~

.. code:: python

    print cloudmesh.shell("cloud on sierra")
start VMs on two clouds separately (users may specify a VM group by using option --group=group)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: python

    print cloudmesh.shell("vm start --cloud=sierra --image=futuregrid/ubuntu-14.04 --flavor=m1.small --group=test")
.. code:: python

    print cloudmesh.shell("vm start --group=test")
check realtime vm status of all active clouds
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: python

    print cloudmesh.shell("list vm --all --refresh")
delete VMs by group
~~~~~~~~~~~~~~~~~~~

.. code:: python

    print cloudmesh.shell("vm delete --cloud=sierra --group=test --force")
.. code:: python

    print cloudmesh.shell("vm delete --group=test --force")
.. code:: python

    print cloudmesh.shell("list vm --all --refresh")