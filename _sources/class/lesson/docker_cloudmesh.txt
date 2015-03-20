Deploying Cloudmesh using Docker on FutureSystems
===============================================================

Docker is an image-based resource isolation software by using operating system
level virtualization.  Docker host runs software containers which deploy
applications with its environments. You can easily share your application using
Docker container across different platforms or operating systems.  This
section, we introduce basic commands of ``docker`` to introduce Docker software
on FutureSystems.  In the next section, we will explore advanced use of
``docker`` on FutureSystems.

.. note:: Need a basic tutorial for Docker? `Tutorial: Docker Basic commands <docker.html>`_

Tutorial: Deploying Cloudmesh using Docker 
--------------------------------------------------------------------

.. tip:: approximate time 10 minutes

In this tutorial, we are going to deploy Cloudmesh using Docker software.
Keep in mind that ``docker`` is a main program and ``container`` is an image
that you would like to use. We use Cloudmesh container to deploy.

Run Cloudmesh
~~~~~~~~~~~~~~~~~~~~~~~~

It's easy to deploy Cloudmesh using Docker. Please run the following
command: (sudo is supressed)

:: 

  docker run -d -p 80:8888 cloudmesh

It downloads Cloudmesh image from Docker Hub and connects 80 port to 8888 port.
So, if you open a web browser ``http://localhost`` or ``http://ip address of
host`` your connection forwards to the container 8888 port. ``-d`` option
daemonizes the container.

.. tip:: Did you see ``Unable to find image 'cloudmesh' locally``?
         Your Docker will find ``cloudmesh`` from Docker Hub and download it to
         your local.

Stop and Delete Container
~~~~~~~~~~~~~~~~~~~~~~~~~

Like stopping and terminating a virtual instance, docker stops and deletes its
container with two commands: ``stop`` and ``rm`` We use ``NAMES`` from ``docker
ps`` command. This example we use ``adoring_lalande`` for your tomcat:8.0
container.

::
  
  docker stop adoring_lalande

After stopping the container, you can delete it.

::

  docker rm adoring_lalande

Next Step
---------

In the next page, we explore [] on FutureSystems.

.. `Next Tutorial>> Deploying Cloudmesh using Docker <docker_cloudmesh.html>`_
