Shell Access
======================================================================

This lesson describes how to provide access to your account on
FutureSystems to a Teaching Assitant.


Prerequisites
----------------------------------------------------------------------

You will need:

* an account on FutureSystems (see `Creating FutureSystems Accounts and Projects`_)
* upload an SSH key (see `Using SSH Keys`_)

These prerequisites are satisfied if

* your FutureSystems status is all green in your "Portal Account" tab on https://portal.futuresystems.org/
* log into ``india.futuresystems.org`` using SSH.

You may wish to view a `Detailed discussion about SSH`_.

.. _Creating FutureSystems Accounts and Projects: http://cloudmesh.github.io/introduction_to_cloud_computing/accounts/accounts.html
.. _Using SSH Keys: http://cloudmesh.github.io/introduction_to_cloud_computing/accounts/accounts.html
.. _Detailed discussion about SSH: http://cloudmesh.github.io/introduction_to_cloud_computing/class/lesson/linux/advancedssh.html


Providing Access
----------------------------------------------------------------------

First log into ``india.futuresystems.org``.
You will need to have the public key of the person you are giving access to.
Here is an example public key::

 ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDsalgoFkAbLCkFVoZE5PLdlZB9fFGmqLX7mnhu6HRCdBGVdA5Z+683p5nD8rq8cOq5ZrHPxsoN1wfsN9yNKVdy2uYZnVfe4oROwYraHfYKZz/SpxsR+1NyzjBw/QOOUJoNLJ0v1X/9WwWWqopeTOsUOqDLQVV8ueyyy7yfWyBvMxNXbGGNzjZHS3II5qB8iY3A5dKLa+bzNM6Aq/7Bj3Ut8ZUn7AOmfohjfRaAwyGEH5mIPY/AlHZ9JRB7EetKYtA3OVobhaHdQlFiiS5zYx41sHeNaaMlH13FbvdLb8C2YhHhWpF+7dKF/Ickr1yFMeA3yvDZ154LRE+jFSteeQw7 example key

You need to modify the ``~/.ssh/authorized_keys`` file and add the public key::

 $ cd .ssh
 $ nano authorized_keys
 # now past the public key to the bottom of the file

Now the Teaching Assistant can log into your account.


.. caution::
   Be aware that this procedure allows someone to log into your account as you.
   Once this session is over, you should remove their public key from your ``~/.ssh/authorized_keys`` file.
