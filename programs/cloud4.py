import time
import webbrowser
from pprint import pprint
from sh import grep, nova
import json
import sys

simulator = False
#simulator = True


if simulator:
    def nova (*args, **kwargs):
        return args
else:
    from sh import nova 


class cloud:

    
    def __init__(self):
        self.vms = {}

    def set (self,vms):
        self.vms = vms

    def refresh(self):
        self.vms = {}
        lines = grep (nova("list"), "|").split("\n")[1:-1]        
        for line in lines:
            line = line[2:-2]
            (id, name, status, networks) = line.split("|")
            self.vms[id] = {"id": id.strip(),
                       "name":name.strip(),
                       "status":status.strip(),
                       "networks": networks.strip()}

    def table(self, columns, name="__undefined__"):
        #columns = ["status", "name"]
        table_s = "<hr>\n"
        table_s += "<h1> My Cloud </1>"
        table_s += "<hr>\n"
        table_s += '<table border="1" cellpadding="10">\n'
        table_s += "\t<tr>\n\t\t<th>"
        table_s += "</th>\n\t\t<th>".join(columns)
        table_s += "</th>\n\t</tr>\n"
        for vm in self.vms:
            table_s += "\t<tr>\n"
            attribute_list = []
            for attribute in columns:
                value = self.vms[vm][attribute]
                
                if attribute == "status":
                    if value == "ACTIVE":
                        color = 'style="background-color:green"'
                    elif value == "ERROR":
                        color = 'style="background-color:red"'
                    else:
                        color = 'style="background-color:blue"'

                elif attribute == "name":
                    if value.startswith(name):
                        color = 'style="background-color:green"'
                    else:
                        color = ''

                else:
                    color = ""

                table_s += "\t\t<td {0}>{1}</td>\n".format(color,value)
            table_s += "\n\t</tr>\n"
        table_s += "</table>\n"
        return table_s
    
    def status(self):
        status_list = []
        for vm in self.vms:
            status_list.append(self.vms[vm]["status"])
        return status_list

    def __str__(self):
        return json.dumps(self.vms, indent=4)
    
    def display(self, columns=None,name="__undefined__"):
        filename = "table.html"
        f = open (filename, "w")
        print >> f, self.table(columns,name)
        f.close() 
        handle = webbrowser.get()
        handle.open(filename)

    def start(self, name):
        result = nova ("boot", 
                       "--flavor", "m1.small", 
                       "--image", "futuregrid/ubuntu-12.04", 
                       "--key_name", "~/.ssh/id_rsa.pub", 
                       name)
        return result

    def delete(self,name):
        results = nova ("delete", name)
        return results

    def  start_n (self, name, n):
       """fill this out"""
       length = len (str(n))
       name_format = "{0}-{1:0" + str(length) + "d}"

       print "start", n, "vm(s) with name", name
       for index in range(1, n + 1):
           print "START VM", index
           try: 
               print nova ("boot",
                           "--flavor", "m1.small",
                           "--image", "futuregrid/ubuntu-12.04",
                           "--key_name", "~/.ssh/id_rsa.pub",
                           name_format.format(name, index))
           except:
               print "machine could not be started because of an error", name.format(username, index)

    def delete_n(self,name,n):
       length = len (str(n))
       name_format = "{0}-{1:0" + str(length) + "d}"
       
       for index in range(1, n + 1):
           print "DELETE VM", index
           print nova ("delete",
                       name_format.format(name, index))

    def commandline(self):
        
        # write out the commands
        # commnd:
        # s 1  starts vm with index 1
        # s 3  starts vm with index 3
        # d 1 dletes vm with indes 1
        # d 3 dletes vm with indes 1
        # v updates the browser window and displays the curren t status

        # bonus

        # s 2 10  starts 10 vms starting from index 2
        # d 2 10  starts 10 vms starting from index 2

        while True:
            line = raw_input("cloud> ")
            if line =="q":
                break
            else:
                print "you typed", line
                ##### do all the programming here
                if line.startswith("v"):
                    self.refresh()
                    self.display(["status", "name", "id"], username)
                else:
                    command = line.split(" ")
                    print command
                    if command[0] == "d":
                        if len(command) == 2:
                            print "start", command
                            name = command[1]
                            result = self.delete(name)
                            print result

                        elif len(command) == 3:
                            print "delete", command
                            name = command[1]
                            n = int(command[2])
                            self.delete_n(name,n)

                        else:
                            print " wrong number of arguments"
                    elif command[0] == "s":
                        if len(command) == 2:
                            print "excute", command
                            name = command[1]
                            result = self.start(name)
                            print result
                        elif len(command) == 3:
                            print "bleep", command
                            name = command[1]
                            n = int(command[2])
                            self.start_n(name,n)
                        else:
                            print " wrong number of arguments"


        pass

if  __name__ == '__main__':

    cloud_dict = {
        "317aa10b-96e8-4705-a725-2b6deccd8535 ": {
            "status": "ACTIVE", 
            "networks": "private=10.35.23.96", 
            "id": "317aa10b-96e8-4705-a725-2b6deccd8535", 
            "name": "a2"
            }, 
        "59e5ee03-4e94-4265-8008-ba1d3b460ba7 ": {
            "status": "ERROR", 
            "networks": "private=10.35.23.52", 
            "id": "59e5ee03-4e94-4265-8008-ba1d3b460ba7", 
            "name": username + "001"
            }, 
        "e0926229-b252-4cac-93a8-2e614ef0a2cf ": {
            "status": "BUILDING", 
            "networks": "private=10.35.23.94", 
            "id": "e0926229-b252-4cac-93a8-2e614ef0a2cf", 
            "name": "a1"
            }
        }

    
    c = cloud ()
    c.commandline()
    sys.exit()
    name = "booh"

    c.start_n(name,2)
    c.refresh()
    c.display(["status", "name", "id"], username)
    time.sleep(3)
    c.refresh()
    c.display(["status", "name", "id"], username)


    c.delete_n(name,2)
    time.sleep(10)
    c.refresh()
    c.display(["status", "name", "id"], username)


#    


#    c.refresh()
#   c.display(["status", "name", "id"], username)
#    time.sleep(1)

#    c.refresh()
#    c.display(["status", "name", "id"], username)
#    time.sleep(1)

#    c.refresh()
#    c.display(["status", "name", "id"], username)
#    time.sleep(1)

#    c.delete(name)
#    time.sleep(5)
#    c.refresh()
#    c.display(["status", "name", "id"], username)

# c.display()


# print c.status()
# c.set(cloud_dict)
# print c
# print c.table(["status", "name"], username)
