import sys
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

n = 3

for index in range(1, n + 1):
    print "START VM", index
    try: 
        print nova ("boot",
                    "--flavor", "m1.small",
                    "--image", "futuregrid/ubuntu-12.04",
                    "--key_name", "~/.ssh/idrsa.pub",
                    vm_name(username, index))
    except:
        print "machine could not be started because of an error", name.format("dmoney4454", index)

for index in range(1, n + 1):
    print "DELETE VM", index
    print nova ("delete", vm_name("username", index))
