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
