The documentation is available at

* http://cloudmesh.github.io/introduction_to_cloud_computing.

Introdution to Cloud Computing
================================

This directory contains code and documentation to learn elementary cloud computing concepts. 
We focus on the following topics:

1. Shell Tools to Conduct Elementary Distributed Computing
2. Essential Python for Cloud Computing
3. Essential iPython for Cloud Computing

Obtaining the documentation
==============================

To check out the code you can use one of two methods. 
If you do not have full access to the repository (which is for most the case):
You can do::

  git clone https://github.com/cloudmesh/introduction_to_cloud_computing.git

Otherwise, if you are a developer you can use::

  git clone git@github.com:cloudmesh/introduction_to_python.git

Prior to you being able to create the documentation, you do have to
install pandoc:

* http://johnmacfarlane.net/pandoc/installing.html

Quick setup for Ubuntu (tesetd for Ubuntu 14.04.1)

* sudo apt-get install python-dev git python-pip pandoc
* pip install -r requirements.txt

You can create the documentation as follows::

  make html

To view the result on OSX use::

  make view

On ubuntu say::

  make chrome
  

You can add new notebooks by adding them into the ipython notebooks::

  ./notbook 

folder. TO contribute your notebook, you can create a pull request. This is done as follows::

   TODO: please describe how to do that
 
