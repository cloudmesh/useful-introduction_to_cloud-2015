# from sh import nova 

username = "gregor"

# simulator = False
simulator = True


if simulator:
    def nova (*args, **kwargs):
        return args
else:
    from sh import nova 

def vm_name(username, index, n=10000):
    length = len (str(n))
    name = "{0}-{1:0" + str(length) + "d}"
    return name.format(username, index)


for index in range(1, n + 1):
    print "DELETE VM", index, vm_name.(username, index)
    print nova ("delete", vm_name(username, index))
