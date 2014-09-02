
Mongo
=====

.. code:: python

    import cloudmesh
.. code:: python

    from cloudmesh.config.cm_config import cm_config_server

.. code:: python

    config = cm_config_server().get("cloudmesh.server.mongo")
.. code:: python

    print config
.. code:: python

    dbname = 'admin'
.. code:: python

       uri = "mongodb://{2}:{3}/{4}".format(cls.DBCONFIG["username"],
                                                                     cls.DBCONFIG["password"],
                                                                     cls.DBCONFIG["host"],
                                                                     cls.DBCONFIG["port"],
                                                                     dbname)
.. code:: python

    print uri
.. code:: python

     conn = MongoClient(uri)[dbname]