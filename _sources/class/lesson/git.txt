
Git
======================================================================
  
Git is a [[http://en.wikipedia.org/wiki/Revision_control][Version
Control]] system (VCS).  The purpose of version is to track changes to
a set of files and facilitate collaboration among individuals.  This
provides users the ability to, given a *repository* of files

- track exactly what changes were made to a file
- who made the changes
- when a change was made
- undo changes that are later deemed unwanted
- collaborate with other people

There are many implementation of version control systems, dating back
to the 1970's.  Some examples include
[[http://en.wikipedia.org/wiki/Concurrent_Versions_System][Concurrent
Versions System (CSV)]],
[[http://en.wikipedia.org/wiki/Apache_Subversion][Subversion (SVN)]],
[[http://en.wikipedia.org/wiki/Mercurial][Mercurial (Hg)]], and
[[http://en.wikipedia.org/wiki/Git_(software)][Git]].  CSV and SVN are
example of Client-Server version control managers, meaning that any
changes made to a clients' repository is reflected on the server.  Hg
and Git are known as Distributed version control systems: each copy of
a repository and changes are share by explicitely *pushing* or
*pulling* to and from other git repositories.  Additionally, a
disributed VCS can mimic the behavior of a client-server VCS -- by
configuring a reference, original (the *origin*), repository -- but
the converse is not possible.

This document describe how to use the basic git operations to track
and share files (*clone*, *add*, *commit*, *push*, *pull*), describes
how to *conflicts*, and provides resources for further learning.

To follow a much more detailed description please refer the
[[http://git-scm.com/book/en/v2][Git Pro]] book by Scott Chacon and
Ben Straub.
  

Responsibilities
----------------------------------------------------------------------

- upload documentation in .rst format
- documentation in IEEE format (MS Word) is acceptable
- make sure all students in group check in code

Basic Git
----------------------------------------------------------------------

This section how to accomplish an operation with Git.  Using and
example workflow, you will learn how to:

- set up a git repository using =init= or =clone=
- inform git to track content using =add= and =commit=
- view the state of the git repository using =status=
- synchronize with a remote repository using =pull= and =push=.

Getting a Repository
----------------------------------------------------------------------
:init:clone:

There are two ways to get a repository.
The first is to start a new one from scratch.
To do so, create an empty directory, go into it, and initialize an empty repository.::

  $ mkdir my_repo
  $ cd my_repo
  $ git init

The alternative method is to copy a preexisting repository, to *clone*
in git parlance.  Take for example the git source code, which is
itself managed by git.  First a url is need, so head over to
[[https://github.com/git/git][git's GitHub page]], and look to the
right to get the url.  It looks like this:
=https://github.com/git/git=.  Now you can tell git to clone this
repository, and then go into the resultant directory::

  $ git clone https://github.com/git/git
  $ cd git

Making Changes
----------------------------------------------------------------------
:status:add:commit:
	
 Now that we have a repository to work with we can start adding files.
Let's say I want to write a book and track the changes in git.
First create a text file called =words.txt= and add some content.::

  $ nano words.txt # open and write some text
  $ cat words.txt  # show the contents of the file
  1 Fish
  2 Fish
  Red Fish
  Blue Fish

Now let's see the state of the git repository::

  $ git status

On branch master

Initial commit

Untracked files:
(use "git add <file>..." to include in what will be committed)::

  words.txt

nothing added to commit but untracked files present (use "git add" to
track)

Now we have a file which we would like to track, but git does not know
about it yet.  We can tell because =words.txt= is listed as an
=untracked file= and helpfully how to track it.  Thus we need to
inform git to *add* the file to the set of files it should monitor for
changes.  Do so::

  $ git add words.txt
  $ git status

On branch master

Initial commit

Changes to be committed:
(use "git rm --cached <file>..." to unstage)

new file:   words.txt

At this point the content is in a *staging area*.  The staging area is
like telling git of content we /wish/ to track, but since we have not
yet /finished/ telling git what to track, it has not yet been
recorded.  Since we are in fact done adding to git, *commit* the
changes::

  $ git commit -m "counting fish"

Upon committing content to git we need specify a message to go along
with the changes.  In this case the message is simple: "counting
fish".  A helpful commit message summarizes clearly what has changed.
In this case, the newly tracked content counts fish, so the message is
straighforward.  These messages are very useful when looking through a
list of changes to identify what has happened.

The Staging Area
----------------------------------------------------------------------

At this point you may wonder why the *add* and *commit* operations are
separate steps.  The short answer is that git views content as being
in one of three states: *untracked*, *staging*, or *tracked*.  This is
shown in the figure [[fig:states]] and is explained in further detail
later.
   

#+CAPTION: Content is seen by git as either *untracked*, *staging*, or *tracked*. Use the git subcommands =add= and =commit= to move content between states.
#+LABEL: fig:states
[[./images/states.png]]



Summary of Commands
----------------------------------------------------------------------

| Operation                                                                | command                                        |
|--------------------------------------------------------------------------+----------------------------------------------|
| Make a local copy of an existing repository                              | =git clone <repo url>=                         |
| Tell git to track changes made to a local path                           | =git add <path>=                               |
| Notify git of all changes made to a local path                           | =git commit -m <msg> <path>=                   |
| Get the current status of the git repository                             | =git status=                                   |
| List the commit messages of the entire repository                        | =git log=                                      |
| List the commit messages of a file or directory                          | =git log <path>=                               |
| Pull any changes made to the original remote repository (named *origin*) | =git pull origin=                              |
| Push any local changes to the remote                                     | =git push origin <branch>=                     |
| Tell git your name                                                       | =git config --global user.name First\ Last=    |
| Tell git your email address                                              | =git config --global user.email name@provider= |


Git Concepts
----------------------------------------------------------------------

This section describes the main concepts behind git.
Understanding these concepts will make it easer to use git, and diagnose and fix any issues that arise.

Blob
Tree
HEAD
Staging area


Fixing Problems
----------------------------------------------------------------------

Using Git on Futuresystems
----------------------------------------------------------------------

GVL: the next section may not be needed.

* Git Hosting

** GitHub
** Bitbucket
** Sourceforge
** Gitorious

Resources
----------------------------------------------------------------------

- [[http://git-scm.com/docs/gittutorial][Git]]
- [[https://www.atlassian.com/git/tutorials/][Atlassian]]
- [[http://rogerdudler.github.io/git-guide/][Roger Dudler]]
- [[http://www.vogella.com/tutorials/Git/article.html][Lars Vogel]]
