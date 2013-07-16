import sys
import json
from sh import nova
from sh import grep
from pprint import pprint

class cloud:

    def __init__(self):
        self.vms = {}
        self.status = []
        
    def refresh(self):
        lines = grep (nova("list"), "|").split("\n")[1:-1]
        self.status = []
        
        for line in lines:
            line = line[2:-2]
            (id, name, status, networks) = line.split("|")
            self.vms[id] = {"id": id.strip(),
                       "name":name.strip(),
                       "status":status.strip(),
                       "networks": networks.strip()}

    def get_status(self):
        self.status = []
        for vm in self.vms:
            self.status.append(self.vms[vm]["status"])
        return self.status

    def __str__(self):
        return json.dumps(self.vms,indent=4)

def main():
    c = cloud ()
    c.refresh()

    pprint(c.get_status())
    pprint(c)

if  __name__ =='__main__':
    main()

