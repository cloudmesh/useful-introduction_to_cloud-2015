import sys
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

n = 3

for index in range(1, n + 1):
    print "START VM", index
    try: 
        print nova ("boot",
                    "--flavor", "m1.small",
                    "--image", "futuregrid/ubuntu-12.04",
                    "--key_name", "~/.ssh/id_rsa.pub",
                    vm_name(username, index))
    except:
        print "machine could not be started because of an error", name.format(username, index)

for index in range(1, n + 1):
    print "DELETE VM", index
    print nova ("delete", vm_name(username, index))
