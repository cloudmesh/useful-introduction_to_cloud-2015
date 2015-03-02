Use of FutureSystems (Under Preparation)
----------------------------------------------------------------------

.. sidebar:: Page Contents

   .. contents::
      :local:


Getting an Account
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

In order to use FutureSystems you will need to get an account.

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


Remote Login (Under preparation)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

In order to login into your account on FutureSystems you will need:

- an account on FutureSystems (see above)
- an SSH client

Login via ``india@futuresystems.org``.

.. tip:: Please see :doc:`../../../accounts/ssh` for instructions on
   configuring an SSH client.


Managing keys (Under Preparation)
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

Linux and OS X store the ssh identity files under ``~/.ssh``.
An invocation of ``ssh-keygen`` will by default choose to write
``~/.ssh/id_rsa``.
This generated key consists of a **public** key and a **private** key.
By providing your public key to FutureSystems you will be able to login
to ``india@futuresystems.org`` as described above.

.. warning::
   Never share your private key with an untrusted party.


There are a few usefull operations on ssh keys:

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

ssh (Under Preparation)
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""



