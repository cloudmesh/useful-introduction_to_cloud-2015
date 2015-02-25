Using Git and GitHub for collaboration
======================================================================

Overview
----------------------------------------------------------------------

This lesson show you how to submit and work on homework assignments.
Assignments are to be worked on the
`GitHub FutureSystems organization`_.

Upon completion of this lession you will be able to use GitHub for
submitting assignments for your course

There are several prerequisites which are detailed below.
In summary, they are:

* a GitHub account
* forming a group with other students
* a FutureSystems account
* an SSH key

.. _GitHub FutureSystems organization: https://github.com/futuresystems

Contact
----------------------------------------------------------------------

The assistant instructors for the course are:

* `Badi' Abdul-Wahid <badonald@iu.edu>`_
* `Hyungro Lee <lee212@iu.edu>`_

For problems with FutureSystems please email `help@futuresystems.org`.
Be aware that the assistant instructors are not recipiants of these
emails so please carbon copy them so that they are aware of issue.

**IMPORTANT**
Please be aware that questions addressed to staff should be sent
between 9am and 4pm on business days.
Questions outside those hours may not be addressed until the
following business day.
Please keep this in mind and start working on your assignments early.

For advanced conceptual support please contact

* Gregor von Laszewski
* Fugang Wang

Preliminary Setup
----------------------------------------------------------------------

Prerequisite: a GitHub account
^^^^^^^^^^^^^^^^^^

Go to `GitHub <https://github.com>`_ and signup for an account.

This prerequisite is satisfied if you are able to

* go to `https://github.com`
* sign in

Prerequisite: form a group and identify a project
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

You need to form a group with other students and determine a project
to work on together.
If you have difficulty on deciding a project please contact the
instructors.
The instructors need to approve your project so please send them
a report detailing:

* the names and email address of group members
* a project title
* the goal of the project
* a list all deliverables
* assignments of tasks to group members

This prerequisite is satisfied if you and other students have formed
a group and your instructor has approved the project.

Prerequisite: a FutureSystems account
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

As all your work will be completed on FutureSystems, you will need
a FutureSystems account in order to access and user resources.
Go to the `FutureSystems portal <https://portal.futuresystems.org>`_
and request an account if you do not yet have one.
Then, you must request to be added to the course FutureSystems project.
Finally, you must upload an SSH key.
Please see the `FutureSystems documentation`_ for details on requesting
an account.
If you have trouble uploading an SSH Key please first consult
documentation on `how to upload an SSH Key`_ before contact support.

.. _further documentation:  http://cloudmesh.github.io/introduction_to_cloud_computing/accounts/index.html
.. _how to upload an SSH Key: http://cloudmesh.github.io/introduction_to_cloud_computing/accounts/ssh.html#s-using-ssh

This prerequisite is satisfied if you are able to accomplish the following:

* log into `https://portal.futuresystems.org
* go to the ``Portal Account`` tab
* the ``status`` row is all green in the ``My FutureGrid HPC account status`` section


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

If you have not satisifed this section, please the the `documentation`_
for details on how to do so.

.. _documentation: http://cloudmesh.github.io/introduction_to_cloud_computing/accounts/ssh.html#s-using-ssh

Getting access to repository
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Send an email to `Badi' Abdul-Wahid <badonald@iu.edu>`_ and include the
following information:

* the first and last name of each group member
* the email address of each group member
* the github username of each group member
* the course number registered for
* the project proposal approved by the instructor

Please adhere to the following template for this email::

  Subject: request futuresystems github project
  Body:
    <first name> <last name>, <email> <github username>
    <first name> <last name>, <email> <github username>
    ...
    <course number>
    
    <project proposal>

For example::

  Subject: request futuresystems github project
  Body:
    Ada Lovelace, adalovelace@gmail.com lovelace
    Albert Einstein, emc2@gmail.com albert
    SP15-BL-BUEX-V594-37186

    Development of a computer simulation of the Theory of General Relativity
    etc...

**IMPORTANT** please adhere to this format as improper formatting
may not be seen and processed.

A repository will then be created for your group and you will be
emailed the link.

**IMPORTANT** All members of a group will have access to this
repository and can make changes.
This means that anybody in your group can modify the work of of
everybody else in that group.

This prerequisite is satisfied if are able to

* go to `https://github.com/futuresystems`
* see your repository (for example: ``class-bigdata-technology-spring-2015-ABCDE``)
* are in the ``students`` team

Initializing the Repository with ``git clone``
----------------------------------------------------------------------

Once you have access to a repository you should use it to work on
assignments.
You must do so from your FutureSystems account by logging into
``india.futuresystems.org`` with ssh.
For instance, if your account name on FutureSystems is ``albert``::

  ssh albert@india.futuresystems.org

Once you have your repository url
(for example: ``git@github.com:futuresystems/class-bigdata-technology-spring-2015-ABCDE.git``)
you can download the repository like so::

  git clone git@github.com:futuresystems/class-bigdata-technology-spring-2015-ABCDE.git
  cd class-bigdata-technology-spring-2015-ABCDE

Using the Repository
----------------------------------------------------------------------

Now that you have an initialized repository you may use it for
your assignments.

There are several concepts to understand in order to submit assignments:

* ``add``-ing files to git
* ``commit``-ing changes
* ``push``-ing changes
* ``pull``-ing changes
* resolving conflicts

``git add``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


``git commit``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


``git push``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


``git pull``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


Resolving Conflicts
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


Exercise
----------------------------------------------------------------------


