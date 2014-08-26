
Initialization
==============

To use th emany useful functions available in cloudmesh, we need to
import the basic cloudmesh module.

.. code:: python

    import cloudmesh
Version
=======

Cloudmesh has a version number that can be retrived with the version
function

.. code:: python

    print cloudmesh.version()

.. parsed-literal::

    1.0


Generating Names
================

Cloudmesh has a number of helper functions. One of them is to create a
name for a virtual machine. This will come in handy when we need to
start multile virtual machines and distinguish them with a different
name

.. code:: python

    print cloudmesh.vm_name("gregor", 1)

.. parsed-literal::

    gregor-00001

