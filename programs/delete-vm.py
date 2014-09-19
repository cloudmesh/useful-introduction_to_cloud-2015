'''
# from sh import nova 

from cloudmesh import vm_name

username = "gregor"

# simulator = False
simulator = True


if simulator:
    def nova (*args, **kwargs):
        return args
else:
    from sh import nova 


for index in range(1, n + 1):
    print "DELETE VM", index, vm_name.(username, index)
    print nova ("delete", vm_name(username, index))
'''    

#!/usr/bin/env python

import sys
import os

if len(sys.argv) != 2:
    print "VM ID or Name is required. 'nova list' will show the list of currently running VMs"
    sys.exit(1)
else:
    os.system("nova delete {0}".format(sys.argv[1]))
    
