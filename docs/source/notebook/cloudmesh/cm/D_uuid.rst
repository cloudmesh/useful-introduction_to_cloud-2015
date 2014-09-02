
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

    UUID('f040aaf5-3242-11e4-bd35-600308a5f9d2')



Random Uuid
-----------

.. code:: python

    uuid.uuid4()



.. parsed-literal::

    UUID('ac332de1-faef-4054-aae8-6f32eb15f982')



As in some cases we want to generate names that do not include special
characters such as - or . we avoid using the uuid function for now and
use the function get\_unique\_name instaed.

.. code:: python

    uuid.UUID(bytes=uuid.uuid4().bytes)



.. parsed-literal::

    UUID('e529ec9c-e40d-4e3b-b4db-4b46802bd4f6')



.. code:: python

    uuid.uuid4().int



.. parsed-literal::

    64005057163216856052777834181321712834L



Cloudmesh get\_unique\_name
---------------------------

Sometimes it is beneficial to create uuids without the - in it. For this
we have a convenience function in cloudmesh.

.. code:: python

    from cloudmesh_common.util import get_unique_name
.. code:: python

    print get_unique_name()

.. parsed-literal::

    f04729ee324211e49889600308a5f9d2


As you can see it is just like the uuid function (currently uuid1 with
the - removed.

In addition one can place a prefix into the uuid to make furher
distinctions. However this is rarely needed.

.. code:: python

    get_unique_name("gregor")



.. parsed-literal::

    'gregorf0487de3324211e4b177600308a5f9d2'


