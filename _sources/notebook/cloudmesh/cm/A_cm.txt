
Calling **cm** in iPython or a shell
====================================

In this section we use one of the build in features of iPython. It
allows us to start command shell programs by putting the "!" at the
beginning of the line. This allows us to start the command shell easily
from iPython just as we would on a regular commandline.

We will demonstrate this and also showcase how to pass parameters from a
cm command to the cm shell.

Parameters
----------

.. code:: python

    !cm -h

.. parsed-literal::

    cm.
    
        Usage:
          cm [-q] help
          cm [-v] [-b] [--file=SCRIPT] [-i] [COMMAND ...]
    
        Arguments:
          COMMAND                  A command to be executed
    
        Options:
          --file=SCRIPT  -f  SCRIPT  Executes the scipt
          -i                 After start keep the shell interactive,
                             otherwise quit [default: False]
          -b                 surpress the printing of the banner [default: False]
        


Help
----

.. code:: python

    !cm help

.. parsed-literal::

    
    Documented commands (type help <topic>):
    ========================================
    EOF       edit      help       label   plugins  register        user   
    banner    exec      image      list    project  script          var    
    clear     exp       info       man     py       security_group  verbose
    cloud     flavor    init       metric  q        storm           version
    defaults  graphviz  inventory  open    quit     timer           vm     
    dot2      group     keys       pause   rain     use             web    
    
    Gui Commands
    ============
    web
    
    Cloud Commands
    ==============
    cloud     group  inventory  rain            storm  keys   
    defaults  image  list       register        user   project
    flavor    init   metric     security_group  vm   
    


An example command: cloud list
------------------------------

.. code:: python

    !cm cloud list

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


Let us inspect the parameters. To limit the output we just display the
first 10 lines of the help/man page. We see the --column option in the
list command.

.. code:: python

    !cm help cloud | head -n 10 

.. parsed-literal::

    
        ::
    
            Usage:
                cloud [list] [--column=COLUMN]
                cloud info [CLOUD|--all]
                cloud alias NAME [CLOUD]
                cloud select [CLOUD]
                cloud on [CLOUD]
                cloud off [CLOUD]


...

For more information, read the help page. It essentially allows us to
display some more useful information beyond to just document the active
clouds. Let us also display the label. This is done with the following
command.

.. code:: python

    !cm cloud list --column=active,label

.. parsed-literal::

    Usage:
          cm [-q] help
          cm [-v] [-b] [--file=SCRIPT] [-i] [COMMAND ...]


.. code:: python

    !cm "cloud list --column=active,label"

.. parsed-literal::

    +---------+----------+------------+
    | cloud   | active   | label      |
    +=========+==========+============+
    | alamo   |          | alamo      |
    +---------+----------+------------+
    | aws     |          | aws        |
    +---------+----------+------------+
    | azure   |          | waz        |
    +---------+----------+------------+
    | hp      |          | hpos       |
    +---------+----------+------------+
    | hp_east |          | hpeos      |
    +---------+----------+------------+
    | india   | True     | ios_havana |
    +---------+----------+------------+
    | sierra  |          | sos        |
    +---------+----------+------------+


Alternatively we can also say

!echo "cloud list --column=active,label" \| cm

iPython Alias and Rehash
------------------------

IPython provides the ability to ommit the ! by defining an alias to cm.
We will use this feature and define a cm alias in python as follows. If
you need debugging output you can also add the -v option fo the cm
command in the alsias specification.

.. code:: python

    alias cm (cm "%s")
.. code:: python

    cm version

.. parsed-literal::

    1.0.4


In addition to the direct spesification IPython has also a rehash
function, that loads the commands found in the $PATH variable so you can
aexecute the without !.

.. code:: python

    %rehashx
.. code:: python

    cm version

.. parsed-literal::

    1.0.4

