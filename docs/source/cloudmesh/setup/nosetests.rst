nosetests
=========

If you would like to verify installation by nosetests, we provides couple of
examples. This basic examples perform several tests towards installation, cm
console, cm API, and cm shell.

What does the test involve?
----------------------------
For API, shell, and cm, the nosetests checks activation, list, refresh, start
, stop and other features of vm instances. With these tests, we can assure 
that Cloudmesh users can use and launch vm instances on any interfaces
including web gui. The nosetest for the installation does perform actual 
process of the installation so all the required packages and files will be 
re-installed and re-configured.

Installation
------------------

Try to run the following command:

$ nosetests -v --nocapture ~/cloudmesh/tests/test_cm.py


API
---

Try to run the following command:

$ nosetests -v --nocapture ~/cloudmesh/tests/test_cm_api.py

cm shell
--------

Try to run the following command:

$ nosetests -v --nocapture ~/cloudmesh/tests/test_cm_shell.py

cm console
----------

Try to run the following command:

$ nosetests -v --nocapture ~/cloudmesh/tests/test_cm_console.py
