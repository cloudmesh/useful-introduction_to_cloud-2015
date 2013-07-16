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
    print "DELETE VM", index, name.format("dmoney4454", index)
    print nova ("delete",
                name.format("dmoney4454", index))
