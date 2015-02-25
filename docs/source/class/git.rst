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


Prerequisite: Configuring your Git Identity (``git config``)
----------------------------------------------------------------------

Git needs to know your name and email address in order to track
changes you make to a repository.
This can be configured like so::

 $ git config --global user.name "Ada Lovelace"
 $ git config --global user.email lovelace@gmail.com

Once you have done so you should have a ``~/.gitconfig`` file.
You can check that this file exists and that it containts the correct
information::

 $ cat ~/.gitconfig
 [user]
     name = Ada Lovelace
     email = lovelace@gmail.com


Using the Repository
----------------------------------------------------------------------

Now that you have an initialized repository you may use it for
your assignments.

This section describes how to create and modify documents using git
to track and share the changes among collaborators.
Upon completion you will know how to do the following:

* ``add``-ing files to git
* ``commit``-ing changes
* ``push``-ing changes
* ``pull``-ing changes
* resolving conflicts


Adding content to git (``git add``, ``git commit``, ``git status``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Now that you have a repository in your account on ``india`` let us
create some content and notify git that changes to this content needs
to be tracked.
Tracking content makes it easy to share changes among collaborators,
track precisely who made a change, what was changed, when something
changed, and why a change was made.

The commands we are using in this section are:

* ``git add``
* ``git commit``
* ``git status``

The concepts are:

* untracked content
* staging area
* tracked content
* what a **change** means in git terminology

First let us create a file called ``fist.txt`` and write some lines::

  $ nano fish.txt # open the file in the "nano" editor
  $ cat fish.txt  # after saving, show the contents of the file
  One fish
  Two fish
  Red fish
  Blue fish

At this stage the file exists but git is not tracking changes made.
If it were to be deleted then it is gone for good.

We can inspect the status of git using the ``git status`` command::

  $ git status
  On branch master

  Initial commit

  Untracked files:
    (use "git add <file>..." to include in what will be committed)

          fish.txt

  nothing added to commit but untracked files present (use "git add" to track)

There is a lot of information here but the key pertinant point is the
``Untracked files`` heading which lists all files that git sees exist
but whose changes are not being tracked.
There is also the helpful hint ``use "git add <file>..."`` indicating
a possible next step.
Let us do so::

  $ git add fish.txt
  On branch master

  Initial commit

  Changes to be committed:
    (use "git rm --cached <file>..." to unstage)

          new file:    fish.txt

In order to understand what ``git add`` does, we need to know the
difference between each of the three states that content may be in:

* untracked
* staging
* tracked

When the ``fish.txt`` file was created the content was *untracked*.
That is, any modifications to ``fish.txt`` will not be logged.
If it is deleted it cannot be recovered, it cannot be shared using
git, and we cannot extract the "who", "what", "when", and "why"
metadata associated with a change.

By using ``git add`` content can be added to the staging area.
Multiple files can be staged.
Hypothetically, if two other files ``hello.txt`` and ``world.txt``
were to be created they could be staged::

  $ git status
  On branch master

  Initial commit

  Untracked files:
    (use "git add <file>..." to include in what will be committed)

        fish.txt
	hello.txt
	world.txt

  nothing added to commit but untracked files present (use "git add" to track)
  $ git add hello.txt
  $ git add hello.txt
  $ git status
  On branch master
  
  Initial commit
  
  Changes to be committed:
    (use "git rm --cached <file>..." to unstage)
  
          new file:   fish.txt
          new file:   hello.txt
          new file:   world.txt


By using the staging area multiple files can be commited to git as a
single **change**.
Meaning: a **change** is the addition, deletion, of modification of
content of one or more files.

At this point, ignoring the hypothetical ``hello.txt`` and ``world.txt``
files, we can now **commit** this change::

  $ git commit -m "added counting fish"

The ``git commit`` command recording everything in the **staging area**
as a single **change**.
When committing a change it is necessary to add a message describing
the change.
The change itself stores the **what** (what content changed), and
**when** (time and date of a change), but you must provide a
message that describes **why** a change was made.
This message is then stored with the change and can be viewed by
looking at the history of the repository.

You can now see for yourself that git no longer sees any untracked
content::

  $ git status
  On branch master
  nothing to commit, working directory clean


At this point you have used the ``git add``, ``git commit``, and
``git status`` commands and should know the difference between the
``untracked``, ``staging area``, and ``tracked`` states that content
may be in, and understand what is meant by a "change."



``git push``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


``git pull``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


Resolving Conflicts
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


Exercise
----------------------------------------------------------------------


