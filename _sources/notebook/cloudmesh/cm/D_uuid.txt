
UUIDs
=====

                from uuid import uuid1
                
.. code:: python

    import uuid
Machine dependent uuid.
-----------------------

.. code:: python

    uuid.uuid1()



.. parsed-literal::

    UUID('7886b8f0-31db-11e4-951b-600308a5f9d2')



Random Uuid
-----------

.. code:: python

    uuid.uuid4()



.. parsed-literal::

    UUID('56de833b-e612-4223-a73f-0087163c0c83')



As in some cases we want to generate names that do not include special
characters such as - or . we avoid using the uuid function for now and
use the function get\_unique\_name instaed.

.. code:: python

    uuid.UUID(bytes=uuid.uuid4().bytes)



.. parsed-literal::

    UUID('5e1ebbfa-5d53-4099-9fa3-4c98fb83ce49')



.. code:: python

    uuid.uuid4().int



.. parsed-literal::

    174171799396821985787509117431189676732L



.. code:: python

    uuid.uuid4().int
Cloudmesh get\_unique\_name
---------------------------

Sometimes it is beneficial to create uuids without the - in it. For this
we have a convenience function in cloudmesh.

.. code:: python

    from cloudmesh_common.util import get_unique_name
.. code:: python

    print get_unique_name()

.. parsed-literal::

    028d7f3d31dc11e496d4600308a5f9d2


As you can see it is just like the uuid function (currently uuid1 with
the - removed.

In addition one can place a prefix into the uuid to make furher
distinctions. However this is rarely needed.

.. code:: python

    get_unique_name("gregor")



.. parsed-literal::

    'gregor26fd703331de11e495d1600308a5f9d2'


