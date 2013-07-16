import sys
from sh import nova
from sh import grep
from pprint import pprint

class cloud:

    def __init__(self):
        vms = {}
        vm_status = []
        
    def refresh(self):
        self.lines = grep (nova("list"), "|").split("\n)")
        self.vm_status = []
        for line in self.lines:
            print "LINE", line
            line = line[2:-2]
            (id, name, status, networks) = line.split("|")
            print "-%s-" % id
            print "-%s-" % name
            self.vms[id] = {"id": id.strip(),
                       "name":name.strip(),
                       "status":status.strip(),
                       "networks": networks.strip()}

    def status_list(self):
        self.vm_status = []
        for vm in vms:
            self.vm_status.append(vms[vm]["status"])

    def display_status(self):
        pprint(vms)

v = cloud ()
v.refresh()
v.status_list()
v.display_status()



