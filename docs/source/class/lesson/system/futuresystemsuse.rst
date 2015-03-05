Use of FutureSystems
----------------------------------------------------------------------

.. sidebar:: Page Contents

   .. contents::
      :local:


Getting an Account
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

In order to use FutureSystems you will need to get an account.

.. important::

   Make sure you have cookies enabled or you will not be able to log
   in to your account.


#. Navigate to `FutureSystems.org <https://portal.futuresystems.org/>`_.
#. Click on ``Register`` at the top near the search bar
#. Fill out the information. Asterisk-denoted (``*``) fields are required.
#. Please be patient after clicking the ``Create new account` button.
   It may take one or two business day for the account to be approved.
#. Once your account is approved you will receive an email.

.. important:: At this point you will not be able to use any
   FutureSystems resources.  You will need to join a project and
   enable remote login to do so.  Only when the status is all green in
   the ``My FutureGrid HPC account status`` of your `portal account`_
   information will you have access to resources.

.. tip::
   Please see :doc:`../../../accounts/accounts` for additional details.

.. _portal account: https://portal.futuresystems.org/my/fg-account


Join a Project
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Now that you have a FutureSystems account you will need to join a
project.

#. Navigate to `FutureSystems.org
   <https://portal.futuresystems.org/>`_ and log into your account.
#. Click on the appropriate project name
#. Click on the ``Join the project`` link on the right hand side.
#. Upon approval you will recieve an email.

.. tip::
   Please see :ref:`s-account-join-project` for further details.


Remote Login
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

In order to login into your account on FutureSystems you will need:

- an account on FutureSystems (see above)
- an SSH client

Login via ``$PORTALNAME@india.futuresystems.org``.

.. tip::
   On Mac OS X open a terminal via `Applications --> Utilities --> Terminal`

.. tip::
   On Windows you will need to install `PuTTY`_.


You will need to know your portal username (``$PORTALNAME``).
For instance, Albert has an account on FutureSystems and his username
is ``albert``:
The hostname will be ``india.futuresystems.org`` and he can log in
like so::

  ssh albert@india.futuresystems.org


.. tip:: Please see :doc:`../../../accounts/ssh` for details on
   configuring and using an SSH client.

.. _PuTTY: http://www.chiark.greenend.org.uk/~sgtatham/putty/download.html


Managing keys
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

This section describes how to generate secure keys for using
OpenStack.
You will need to log into ``india`` to follow.
You may also find additional details in
:doc:`../../../iaas/openstack`.

.. sidebar:: Page Contents

   .. contents::
      :local:


.. tip::
   Make sure you have loaded the approprate modules and setup your
   environment::

     $ module load openstack
     $ source ~/.cloudmesh/clouds/india/juno/openrc.sh

Create a key pair
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

In order to use OpenStack on ``india`` you will need an SSH key.
First, check that ``~/.ssh/$PORTALNAME-key`` does not exist::

  $ file ~/.ssh/albert-key

If you get an error message like::

  $ file ~/.ssh/albert-key
  ~/albert-key: cannot open `~/.ssh/albert-key' (No such file or directory)

then the file does not exist and you will need to create it (see below).
If the file does exist you will see something like::

  $ file ~/.ssh/albert-key
  ~/.ssh/albert-key: ASCII text

In order to create a key for OpenStack use the ``nova keypair-add``
command and set the appropriate permissions::

  $ nova keypair-add $PORTALNAME-key >~/.ssh/$PORTALNAME-key
  $ chmod 600 ~/.ssh/$PORTALNAME-key

.. tip:: Replace ``albert`` with whatever your ``$PORTALNAME`` is.

.. caution::
   This ``nova keypair-add`` command will overwrite any preexisting
   file in ``~/.ssh/$PORTALNAME-key`` so make sure it does not exist
   before executing this command.
   

Import a key pair
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

If you already have a key pair that you wish to use it can be
imported into the cloud.
For example, Albert has created a key whose public key is located at
``~/.ssh/id_rsa.pub`` and he can import it using and naming it
using his ``PORTALNAME`` ``albert``::

  $ nova keypair-add --pub_key ~/.ssh/id_rsa.pub $PORTALNAME-key


List added keys
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

You can query OpenStack to see what keys you have added and uploaded::

  $ nova keypair-list
  +-----------------+-------------------------------------------------+
  | Name            | Fingerprint                                     |
  +-----------------+-------------------------------------------------+
  | $PORTALNAME-key | ab:a6:63:82:dd:08:d3:bc:c0:21:56:4c:e2:bb:22:ac |
  +-----------------+-------------------------------------------------+

Usefull SSH commands
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

The following is a short list of usefull SSH commands.

Change the password
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

You can change the password for the key by using the  the ``-p`` flag.
For example::

  $ ssh-keygen -p

Change the comment
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

You can change the comment of an key by modifying the public key file.
For example, Ada Lovelace wishes to replace an unimformative comment
with her email address.
She would execute the following::

  $ cat ~/.ssh/id_rsa.pub
  ssh-rsa  AAAAB3N.... this is not informative
  $ nano ~/.ssh/id_rsa.pub
  $ cat ~/.ssh/id_rsa.pub
  ssh-rsa  AAAAB3N.... lovelace@gmail.com


Show fingerprint
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

The fingerprint of a key can be used to authenticate the validity of
the key.
For example, if Ada were to share his public key with Albert Einstein,
she would transmit the key.
Albert could then compute the fingerprint and ensure that it matches.
To do so, Albert would save the key to ``~/.ssh/ada.pub`` and execute::

  $ ssh-keygen -l -f ~/.ssh/ada.pub
  2048 6c:52:54:20:b9:85:04:d4:30:46:48:c7:c4:bc:fe:c7  lovelace@gmail.com (RSA)

FutureSystems, for instance, uses fingerprints to identify keys once they have been uploaded.
You may see this fingerprint on the `FutureSystems portal
<https://portal.futuresystems.org/my/ssh-keys>`_.


Delete a known host
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

Whenever you log into a new machine via SSH, the host key of the
destination machine is added to ``~/.ssh/known_hosts``.
The next time you try to log in this key will be checked.
If it has changed you will need to remove the entry before attempting
to log back in.

.. note::
   The host key may change if the machine undergoes a major upgrade or
   change.
   Another reason may be that a third party is performing a
   `man-in-the-middle attack`_.


To remove a key for ``india.futuresystems.org`` from ``~/.ssh/known_hosts``::

  $ ssh-keygen -R india.futuresystems.org


.. _man-in-the-middle attack: http://en.wikipedia.org/wiki/Man-in-the-middle_attack


Windows (Under preparation)


Putty (Under Preparation)
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

SSH
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

Secure Shell, or SSH, is a protocol for securely connecting to a Shell
on a remote computer.

.. tip::

   See :doc:`../linux/shell` for more details on what a shell is and
   how to use it.

This security is accomplished by encrypting the data that is sent
between the two endpoints.  In order for this communication to be
considered "safe", the machines need to identify each other.  The
identity is usually accomplished through the use of a **key** file,
which usually comes in pairs: a **public** key and a **private** key.
This is usually called a **key pair**.  On Mac OS X and Linux a key
pair can be created using the ``ssh-keygen`` command. You can test this out by opening a terminal and entering the following:

.. code:: bash

   $ ssh-keygen -f ~/test_identity

What this does is actually create two file:

- ``~/test_identity``
- ``~/test_identity.pub``

The second file, ending in ``.pub``, is the public key and needs to be
shared with the machines you wish to access.  In the case of
FutureSystems, you add the public key to your `SSH Keys
<https://portal.futuresystems.org/my/ssh-keys>`_.  In the case of
GitHub (see :doc:`../git`) you add it to your account.

.. caution::

   **Never** share the private key with anyone.  This is used to
   identify you and can be used to completely regenerate the public
   key. Try it for yourself with:

   .. code:: bash

      $ ssh-keygen -y -f ~/test_identity

   and compare the output with ``~/test_identity.pub``

.. tip::

   A good practice for managing SSH keys is to create a key pair on
   each machine you use and to add a comment indicating your contact
   information and the machine this key belongs to.::

     $ ssh-keygen -C 'host:relativity contact:albert@gmail.com'

   In the above the comment is specified with the ``-C`` flag and the
   body of the comment is within the single quotes.

   The contact information is useful when sharing the key with others
   as it helps them understand who you are.

   The host information is useful for you if you have multiple
   machines.
