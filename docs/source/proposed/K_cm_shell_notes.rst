
Notes
=====

.. code:: python

    import cloudmesh
.. code:: python

    userename = cloudmesch.user("mongo")
Specifying a custom label
-------------------------

.. code:: python

    from sh import fgrep
.. code:: python

    d = cloudmesh.shell("cloud list --column=label --format=json")
.. code:: python

    assert d['alamo']['label'] == alamo