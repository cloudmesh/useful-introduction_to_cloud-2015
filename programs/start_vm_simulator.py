import sys
# from sh import nova 

simulator = False
# simulator = True


if simulator:
    def nova (*args, **kwargs):
        return args
else:
    from sh import nova 



n = 10000
length = len (str(n))
print length

name = "{0}-{1:0" + str(length) + "d}"


for index in range(1, n + 1):
    print "START VM", index
    try: 
        print nova ("boot",
                    "--flavor", "m1.small",
                    "--image", "futuregrid/ubuntu-12.04",
                    "--key_name", "dmoney4454-key",
                    name.format("dmoney4454", index))
    except:
        print "machine could not be started because of an error", name.format("dmoney4454", index)

for index in range(1, n + 1):
    print "DELETE VM", index
    print nova ("delete",
                name.format("dmoney4454", index))
