
Provider
========

Sometimes it may be useful to have access to the nova shell command from
within python. However, at times you may not actually want to use it but
rather print just jte arguments while simulating a call to the shell
command. To support these two functions, we are offering a simple
provider that returns either the real sh function, or a function that
just prints its arguments.

We start our program first with importing cloudmesh and the provider

.. code:: python

    import cloudmesh
.. code:: python

    from cloudmesh.sh.openstack import nova_provider
Next we decide to load one of the providors. The values are "sh" and
"simulator". We chose the simulator. we name the function to boot a vm
nova\_boot.

.. code:: python

    vm_boot = nova_provider("simulator")
Now we can boot a vm with the command

.. code:: python

    vm_boot("a", "b", h="k")

.. parsed-literal::

    ('a', 'b') {'h': 'k'}


To use a real submission we can switch the vm\_boot function with the
provider

.. code:: python

    vm_boot = nova_provider("sh")
.. code:: python

    vm_boot(TODO)