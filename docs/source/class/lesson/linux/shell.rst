Shell
======================================================================

.. sidebar:: Page Contents

   .. contents::
      :local:


Overview
----------------------------------------------------------------------


This lesson will introduce you to using the shell, which is required
for using FutureSystems resources.

Acknowledgements
----------------------------------------------------------------------

Parts of this lesson were adapted from the `Software Carpentry
lesson`_ on using the Shell, which is distributed under a `Creative
Commons Attribution licence v4`_ and is copywrite `Software Carpentry`_.

.. _Software Carpentry lesson: http://swcarpentry.github.io/shell-novice/
.. _Creative Commons Attribution licence v4: https://creativecommons.org/licenses/by/4.0/
.. _Software Carpentry: http://software-carpentry.org/


Description
----------------------------------------------------------------------

A "shell" is a program that facilitates interaction between human and
computer.
By providing this level of abstraction certain tasks which may be
otherwise cumbersome of time-consuming are relatively simple to
accomplish.
There are numerous types of shells.
If you have ever used a computer you have used a shell.
For instance, Windows and Mac OS X use a shell based on graphical
representations with a mouse and keyboard for interaction.
Touch-screen phones and tables also use another type of shell whose
mode of interaction is through touch.
In addition to these which you might be familiar with, we will be using
a command shell to interact with the computer primarily through the
keyboard.

.. tip::

   Command line shell is often called a Command Line Interface, or CLI
   for short.

.. note:: Adventerous readers may be interested to know that both
   Windows and Mac OS X provide a command shell.  On Windows you can
   run ``cmd.exe`` from `Start --> Run`.  On OS X open `Applications
   --> Utilities --> Terminal`. Be aware that the Windows and OS X CLI
   may be different than on FutureSystems.

.. tip::
   If you wish to follow along please log into your FutureSystems
   account (see :doc:`../system/futuresystemsuse`).


Introduction
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: shell-intro.rst


Prompts and Commands
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Shell Concepts Introduced
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- ``whoami``: display user id

Prompt
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Once you log into the appropriate machine you will be presented with
the **prompt**, typically represented as the following::

  $

Command
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

At the **prompt** you enter a **command** to run a program.
For instance, the ``whoami`` program indicates the username
you logged in under.
To see this type ``whoami`` and press enter (the result will be different
but you should recognize your username)::

  $ whoami
  nelle


.. tip::
 
   On Windows you start a program by double-clicking an icon to going
   to `Start --> <Program>` to launch it (the commands described here
   are Unix commands and are unlikely to work on Windows).  On OS X
   you might go to the dock at the bottom of the screen.  In a
   commandline shell you type the name of the program.


When you execute the ``whoami`` command the shell:

#. finds the program called ``whoami``
#. runs that program
#. displays the program's output
#. displays a new shell prompt (ready for more commands)


Files and Directories
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Shell Concepts Introduced
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- ``pwd``: print working directory
- ``ls``: list directory contents
- ``cd``: change directory
- ``TAB``: using tab-completion

.. include:: shell-filedir.rst


Creating and Deleting
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Shell Concepts Introduced
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- ``mkdir``: make a directory
- ``nano``: a text editor
- ``rm``: remove directory entries
- ``rmdir``: remove directories
- ``cp``: copy files
- ``mv``: move files

.. include:: shell-create.rst

Pipes and Filters
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Shell Concepts Introduced
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- ``wc``: word count
- ``*``: globbing
- ``>``: redirection to file
  ``stdout``: standard output stream
- ``cat``: concatenate
- ``sort``: sorting
- ``|``: pipe
- ``head``: get first few lines
- ``uniq``: remove duplicate adjacent lines
- ``cut``: cut selected portions of text

.. include:: shell-pipefilter.rst

Loops
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Shell Concepts Introduced
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- ``for``: starts a **for loop**
- ``$name``: a variable called ``name``
- ``echo``: display text

.. include:: shell-loop.rst

Finding Things
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Shell Concepts Introduced
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- ``grep``: file pattern searcher
- ``find``: walk a file hierarchy
- ``man``: display manual pages
- ``$()``: execute in a subshell

.. include:: shell-find.rst


Conclusion
----------------------------------------------------------------------

The Unix shell is older than most of the people who use it. It has
survived so long because it is one of the most productive
programming environments ever created --- maybe even *the* most
productive. Its syntax may be cryptic, but people who have mastered
it can experiment with different commands interactively, then use
what they have learned to automate their work. Graphical user
interfaces may be better at the first, but the shell is still
unbeaten at the second. And as Alfred North Whitehead wrote in 1911,
"Civilization advances by extending the number of important
operations which we can perform without thinking about them."

Cheatsheet
----------------------------------------------------------------------

.. include:: shell-cheatsheet.rst


Further Reading
----------------------------------------------------------------------

What is covered here is a small overview of using the commandline
shell.
For further reading please consult the `Bash Guide for Beginners`_
Additionally, there are numerous shell summaries `a Google Search away`_

.. _Bash Guide for Beginners: http://www.tldp.org/LDP/Bash-Beginners-Guide/html/
.. _a Google Search away: https://www.google.com/search?q=linux+shell+cheat+sheet


Next Step
----------------------------------------------------------------------

In the next page, ...

`Link here <link>`_
