Overview and Introduction
======================================================================

.. sidebar:: Page Contents

   .. contents::
      :local:

Overview
----------------------------------------------------------------------

This lesson will introduce you to the basics of Linux usage.
The topics covered will be :

- :doc:`shell`
- :doc:`editors`
- :doc:`python`
- :doc:`packagemanagement`
- :doc:`advancedssh`
- :doc:`modules`

Prerequisite
----------------------------------------------------------------------

In order to conduct this lesson you should have an account on
FutureSystems, as descibred in :doc:`../system/futuresystemsuse`.
You should start by logging into you FutureSystems account.


Description
----------------------------------------------------------------------


Shell
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


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


Editing Files
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Programming and scripting requires the use of a text editor, which is
different than a word processor such as Microsoft Word. Common editors
used on Linux include nano, vi, or emacs. There are many others, but
most examples will use nano and interested students can investigate vi
or emacs as they wish. The principal difference between a text editor
like nano and a word processor like MS Word is how text is saved to
disk. A text editor saves its contents as plain text ("what you type
is what you save"). A word processor supports formatting, such as
bold- or italicized-face and different fonts. A text editor is
appropriate for writing Python code, shell scripts, or
reStructuredText documents but a word processor should not be used.


Python Programming
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Python is an interpreted, dynamic, high-level programming language and
is suitable for a wide range of applications.

The ideals of Python are expressed in `The Zen of Python`_, of which
several statements are:

- Explicit is better than implicit
- Simple is better than complex
- Complex is better than complicated
- Readability counts

The main features of Python are:

- Use of indentation whitespace to indicate blocks
- Object orient paradigm
- Dynamic typing
- Interpreted runtime
- Garbage collected memory management
- a large standard library
- a large repository of third-party libraries

Python is used by many companies (such as Google, Yahoo!, CERN, NASA)
and is applied for web development, scientific computing, embedded
applications, artificial intelligence, software development, and
information security, to name a few.

.. _The Zen of Python: https://www.python.org/dev/peps/pep-0020/


Package Management
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Package Manager: is a tool to install, update or remove software on
the system. A pre-defined set of files also called a package will be
used to setup software. It also manages dependencies such as a certain
library or an other required program to be installed. If program A
requires program B and library C, installing B and C should be done
prior to program. The package manager easily handles packages which
are compiled sets of software. With different types of Linux
distributions, there are several package managers i.e. yum, apt-get or
brew.

Advanced SSH
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This lesson will introduce you to advanced SSH configuration and
tunneling. You can have a shortcut to your SSH connection with a
``ssh`` configuration file or you can create a secure connection
between local and remote machines using SSH tunneling. You will find
out as how to define ssh options in the ``ssh`` config and what
commands you need to establish SSH tunneling with a few examples.


Software Modules
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Modules (Software Environment Management): is a dynamic shell
management tool. Environment variable settings can be loaded, unloaded
or switched on the fly while users are using the shell. Working on
different versions of software is possible using the Module package
while it manages environment variables i.e. PATH, MANPATH, etc by
reading modulefiles.

Cheatsheet
----------------------------------------------------------------------

.. toctree::
   :glob:

   cheatsheet-shell
   cheatsheet-editor
   cheatsheet-python
   cheatsheet-ssh
   cheatsheet-modules

Next Step
-----------

Next: :doc:`shell`
