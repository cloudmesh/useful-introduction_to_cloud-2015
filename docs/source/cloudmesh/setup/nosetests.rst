nosetests
=========

If you would like to verify installation by nosetests, we provides couple of
examples. This basic examples perform several tests towards installation, cm
console, cm API, and cm shell.

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
