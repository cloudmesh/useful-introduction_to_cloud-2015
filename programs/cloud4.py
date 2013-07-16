from pprint import pprint
from sh import grep, nova
import json
import sys

class cloud:

    def __init__(self):
        self.vms = {}
        
    def refresh(self):
        lines = grep (nova("list"), "|").split("\n")[1:-1]        
        for line in lines:
            line = line[2:-2]
            (id, name, status, networks) = line.split("|")
            self.vms[id] = {"id": id.strip(),
                       "name":name.strip(),
                       "status":status.strip(),
                       "networks": networks.strip()}
    def table(self):
        table_s = ""
        table_s += "<table>\n"
        table_s += "<tr><th>"
        table_s += "<th></th>".join(self.vms[self.vms.keys()[0]].keys())
        table_s += "</th></tr>\n"
        for vm in self.vms:
            table_s += "<tr><td>"
            table_s += "<td></td>".join(self.vms[vm].values())
            table_s += "</td></tr>\n"
        table_s += "</table>\n"
        return table_s
    
    def status(self):
        status_list = []
        for vm in self.vms:
            status_list.append(self.vms[vm]["status"])
        return status_list

    def __str__(self):
        return json.dumps(self.vms, indent=4)
    
if  __name__ == '__main__':

    c = cloud ()
    c.refresh()

    print c.status()
    print c
    print c.table()

