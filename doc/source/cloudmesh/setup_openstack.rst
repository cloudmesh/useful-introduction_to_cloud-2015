Setup/Testing Cloudmesh in Cloud environment (vm in OpenStack)
==================================================
Setting up Cloudmesh on a VM is an especially convenient way during dev and testing. The following steps have been developped and tested on a VM running Ubuntu 14.01.1 on FutureGrid Sierra openstack.

- Get a working VM with public IP.
- sudo apt-get update
- sudo apt-get install git
- git clone https://github.com/cloudmesh/cloudmesh.git
- cd cloudmesh
- ./install system
- cd ~
- virtualenv  --no-site-packages ~/ENV
- source ~/ENV/bin/activate
- cd cloudmesh
- ./install requirements
- ./install new
- vi ~/.futuregrid/cloudmesh.yaml (Update your user profile, name, project data)

  Alternatively you can copy your local working yaml files over.
- vi ~/.futuregrid/cloudmesh_server.yaml

  In cloudmesh->server->webui, make the following changes:
  
  change host to: 0.0.0.0
  
  change browser to: False
    
- ./install cloudmesh
- fab mongo.boot
- fab mongo.boot (call mongo.boot twice so the tables and security settings can be done properly)
- fab user.mongo
- fab server.start

Then the service should be available via:
http://PUBLIC_IP_OF_THE_VM:5000

To access the server, you will also need to first enable port 5000 for the VM. By default, you will add the port 5000 to the 'default' security group. This only need to be done once for a project.

Essentially you can do this from horizon or nova CLI. We can do this using cloudmesh too. We should have a GUI for this later, but for now, you can do this from command line as following:

- First identify the index of the cloud the VM is running from the cloudmesh.yaml, and make proper change of the file

  tests/test_compute.py

In setup, change the line:

self.name = self.configuration.active()[IDX]

with proper IDX.

- And then run from within the tests directory:

  nosetests test_compute.py:Test.test_20_create_secgroup

This should open the port 5000 so it's accessible from outside.

NOTE:

1. As you might be copying your yaml files into the cloud please secure the VM, or shut it down after using.

2. As the server is not secured by HTTPS, remember not to use your real password to login.

3. This method intends for dev/tesing, and not recommended for real using.

Please refer to http://cloudmesh.futuregrid.org/cloudmesh/developer.html#install-the-requirements for more information.

