from sh import nova
from sh import grep
from pprint import pprint
import webbrowser
import random
import math
import os

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
    

class table:

    #self.filname
    #self.alist
    #self.cols
    #self.table
    #self.n
    #self.css

    def __init__(self, filename, cols,n,css):
        self.filename = filename
        self.cols = cols
        self.alist = []
        self.table = ""
        self.n = n 
        self.css= css

    def assign(self,alist):
        self.alist = alist

    def generate (self):
        self.table = "<table border=1>\n"
        rows = int(math.ceil(len(self.alist)/float(self.cols)))
        item = 0
        for row in range(0,10):
            self.table = self.table + ""
            for col in range(0,10):
                value = ""
                if item < len(self.alist):
                    value =self.alist[item]
                    self.table = self.table + '<td class="{0}">{1}</td>'.format(value,value)
                    item = item + 1
            self.table = self.table + "</tr>\n"
        self.table = self.table + "</table>" 


    def write(self):
        f = open (self.filename, "w")
        print >>f, self.css
        print >>f, self.table
        f.close() 
    

    
    def display(self):
        handle = webbrowser.get()
        handle.open(self.filename)

    def random(self):
        states =['active', 'build', 'error']
        self.alist = []
        for i in range(0,self.n):
            value = random.randint(0,2)
            print value
            self.alist.append(states[value])

filename = 't.html'
css = """<style>
    .build {
    	background-color:red;
    
    }	
    .active {
        background-color:blue;
    }
    
    .error {
        background-color:green;
       
    }     
</style> """

#os.remove(filename)


nelem = len(alist)
t = table(filename, 10,nelem,css)
t.assign(alist)

#t.random() 
t.generate()
t.write()
t.display()



#w = table(filename, 7,20)

#w.random()
#w.generate()
#w.write()
#w.display()



