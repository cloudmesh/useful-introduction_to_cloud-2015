Shell (Under Preparation)
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

.. note:: Adventerous readers may be interested to know that both
   Windows and Mac OS X provide a command shell.  On Windows you can
   run ``cmd.exe`` from `Start --> Run`.  On OS X open `Applications
   --> Utilities --> Terminal`.

.. tip::
   If you wish to follow along please log into your FutureSystems
   account (see :doc:`../system/futuresystemsuse`).


Introduction
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: shell-intro.rst


Shell Usage
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Once you log into the appropriate machine you will be presented with
the **prompt**, typically represented as the following::

  $

At the **prompt** you enter a **command** to run a program.
For instance, the ``whoami`` program indicates the username
you logged in under.
To see this type ``whoami`` and press enter (the result will be different
but you should recognize your username)::

  $ whoami
  nelle


.. tip::
   On Windows you start a program by double-clicking an icon to
   going to `Start --> <Program>` to launch it.
   On OS X you might go to the dock at the bottom of the screen.
   In a commandline shell you type the name of the program.


When you execute the ``whoami`` command the shell:

#. finds the program called ``whoami``
#. runs that program
#. displays the program's output
#. displays a new shell prompt (ready for more commands)


Files and Directories
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: shell-filedir.rst


Creating Things
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: shell-create.rst

Pipes and Filters
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: shell-pipefilter.rst

Loops
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. include:: shell-loop.rst

Finding Things
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Cheatsheet
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Information
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

uname
head
date
uptime
whoami
man

Directory Operations
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

pwd
mkdir
cd
ls

``ls`` Options
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

-a
-R
-r
-t
-S
-l
-1
-m
-Q

Searching
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

grep
grep -i
grep -r
grep -v
grep -o
find dir -name
find dir -iname
whereis
locate

File Operations
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

touch
cat
less
file
cp
mv
rm
head
tail
chmod

Permissions
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

Process Management
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

ps
top
kill
pkill
killall




  
Exercises
----------------------------------------------------------------------

Exercise I
^^^^^^^^^^^^^^^^^^

Exercise II
^^^^^^^^^^^^^^^^^^

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
