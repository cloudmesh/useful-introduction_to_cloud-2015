
IPython
=======

IPython is a python command shell with notebook features that can be
accessed through a browser. Throughout the material presented here we
will be using IPython to present some of the demonstrations. This also
allows you to try out the various excersises easily. We present here
just a small set of features and recommend you to visit the IPython
manaul for more information

Command Execution
-----------------

To execute a shell command you can specify the ! at the beginning of a
line

.. code:: python

    !echo "hallo"

.. parsed-literal::

    hallo


Environment Variables
---------------------

Environment variables can be accessed with $$

.. code:: python

    !echo "$$EDITOR"

.. parsed-literal::

    emacs


Variables can be accessed by assigning values with = and by using them
in { }

Variables
---------

.. code:: python

    a="Hallo"
.. code:: python

    !echo "{a}"

.. parsed-literal::

    Hallo


Surpressing output
------------------

Output can be surpressed while using the %%capture command. These
commands are called magic functions in IPython. Many more magic
functions are documented in the IPython manual

.. code:: python

    %%capture
    !echo "You can not see me"
.. code:: python

    !echo "You can see me"

.. parsed-literal::

    You can see me

