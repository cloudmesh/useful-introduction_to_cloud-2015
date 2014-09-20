Preface
======================================================================

Conventions
----------------------------------------------------------------------

.. role:: pink

.. highlight:: bash

:pink:`$`
    When showing examples of commands, the :pink:`$` symbol precedes the
    actual command. So, the other lines are the output obtained after
    executing the command. An example invoking the ls command
    follows::

       $ ls

:pink:`PORTALNAME`
    In some examples we refer to your portal name as the :pink:`PORTALNAME`
    you have on FutureSystems.

:pink:`USERNAME`
    In some examples we refer to your local computers name as
    :pink:`USERNAME`. Your portal name and your local name may be
    different.

Menu selections:
    :menuselection:`Start --> Programs`

Man page:
    :manpage:`ls(1)`

Blocks
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. hint:: This is an important hint.

	   |info-image| Hints are represented in simple blocks that are
	   distinguished from the main text


.. |info-image| image:: images/glyphicons_195_circle_info.png 

Using the Notebooks
----------------------------------------------------------------------

The material provided in this documentation contains a number of
IPython notebooks. These notebooks can be executed or accessed through
te IPython notebook. We recommend that you set up the cloudmesh server
software on the machine where you run the iPython notebooks on. If it
is your desktop or Laptop, you can follow the instructions given in
the quickstart setup guide.

You need to run the notebook server from the directory that contains this
material. This can be easily checked out from git hub in the following
way::

  $ git clone git@github.com:cloudmesh/introduction_to_cloud_computing.git

One you have downloaded the learning documentation form github, you
need to cd into the directory with::

  $ cd introduction_to_cloud_computing 

Next you have to compile the information with::

   $ fab doc.html

Now you can start the notebook server with::

  $ fab doc.notebook

The lit of notebooks will be provided in the sidebar menu. You can ow
visit them and execute them. Howler, we like to remind you that this
requires that you have previously setup cloudmesh.

To view the information locally you can say::

  $ fab doc.html

