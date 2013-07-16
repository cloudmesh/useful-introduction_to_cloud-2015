from sh import nova
from sh import grep
from pprint import pprint



class virtual_machine:

 

    def __init__(self, lines):
        self.lines= grep (nova("list"),"|").split("\n)"

    def display(self):
        alist = []
        for line in self.lines:
            print "LINE", line
            line = line[2:-2]
            (id, name, status, networks) = line.split("|")
            print "-%s-" % id
            print "-%s-" % name
            vms[id] = {"id": id.strip(), "name":name.strip(), "status":status.strip(), "networks": networks.strip()}
    alist.append(status.strip())
            pprint(vms)

v= virtual_machine ()
v.display

print 70 * "-"
a = nova("list")
print a
print 70 * "-"
b = grep(a,"|")
print b
print 70 * "-"
c = b.split("\n")
print c
print 70 * "-"

lines = grep (nova("list"), "|").split("\n")

pprint (lines)
print " I am there"

lines = lines[1:-1]

pprint (lines)

print " I am here"
vms = {}



print 70 * "="
pprint(lines)
print 70 * "="
alist = []
for line in lines:
    print "LINE", line
    line = line[2:-2]
    (id, name, status, networks) = line.split("|")
    print "-%s-" % id
    print "-%s-" % name
    vms[id] = {"id": id.strip(), "name":name.strip(), "status":status.strip(), "networks": networks.strip()}
    alist.append(status.strip())
pprint(vms)
