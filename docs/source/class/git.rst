Topic
======================================================================

Overview
----------------------------------------------------------------------

This lesson show you how to submit and work on homework assignments.
Assignments are to be worked on the
`GitHub FutureSystems organization`_.

.. _GitHub FutureSystems organization: https://github.com/futuresystems

Contact
----------------------------------------------------------------------

* `Badi' Abdul-Wahid <badonald@iu.edu>`_
* `Hyungro Lee <lee212@iu.edu>`_

Preliminary Setup
----------------------------------------------------------------------

Prerequisite: a GitHub account
^^^^^^^^^^^^^^^^^^

Go to `GitHub <https://github.com>`_ and signup for an account.

This prerequisite is satisfied if you are able to

* go to `https://github.com`
* sign in

Prerequisite: form a group to work with
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

You need to form a group with other students.

This prerequisite is satisfied if you and other students have formed
a group.

Prerequisite: a FutureSystems account
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

You need a FutureSystems account to do your work.
Go to the `FutureSystems portal <https://portal.futuresystems.org>`_
and request an account if you do not yet have one.
Additionally, see `further documentation`_ on aquiring an account.

.. _further documentation:  http://cloudmesh.github.io/introduction_to_cloud_computing/accounts/index.html

This prerequisite is satisfied if you are able to accomplish the following

* ``ssh $USER@india.futuresystems.org``

Prerequisite: an SSH key
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

You will need an SSH key to use both GitHub and FutureSystems.
If you have followed the documentation for creating a FutureSystems
account you should have created an SSH key in the process.

The prerequisite is satisfied if:

* You can log onto ``india.futuresystems.org``

On **Mac OS X** you will have

* The ``~/.ssh/id_rsa` and ``~/.ssh/id_rsa.pub`` files exists

On **Windows** using PuTTY:

* **In Preparation**

If you have not satisifed this section, please the the `documentation`_.

.. _documentation: http://cloudmesh.github.io/introduction_to_cloud_computing/accounts/ssh.html#s-using-ssh

Getting access to repository
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Send an email to `Badi' Abdul-Wahid <badonald@iu.edu>`_ and include the
following information:

* your github username
* the course number you registered for
* a description of your project

A repository will then be created for your group and you will be
email the link.
All members of a group will have access to this repository.

This prerequisite is satisfied if are able to

* go to `https://github.com/futuresystems`
* see you repository (for example: ``class-bigdata-technology-spring-2015-ABCDE``)
* are in the ``students`` team

Initializing the Repository
----------------------------------------------------------------------

Once you have access to a repository you should use it to work on
assignments.
You must do so from your FutureSystems account by logging into
``india.futuresystems.org`` with ssh.::

  ssh $USER@india.futuresystems.org

Given your repository url in ``URL``
(for example: ``URL=git@github.com:futuresystems/my-repo.git``)
you can download the repository like so::

  git clone $URL

Using the Repository
----------------------------------------------------------------------

Now that you have an initialized repository you may use it for
your assignments.

There are several concepts to understand in order to submit assignments

``git add``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

``git commit``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


``git push``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


``git pull``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


