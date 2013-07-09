import webbrowser
import random
import math


class table:

    # self.filname

	def __init__(self, filename):
	    self.filename = filename

    def display (self, cols, list):
        table = "<table border=1>\n"
        rows = int(math.ceil(len(list)/float(cols)))
        item = 0
        for row in range(0,10):
            table = table + "  <tr>"
        for col in range(0,10):
            value = ""
        if item < len(list):
            value = list[item]
            table = table + "<td>{0}</td>".format(value)
            item = item + 1
            table = table + "</tr>\n"
            table = table + "</table>" + "%i" % item
        
    def read(self,filename, table):
        f = open ('abc.html', 'w')
        print >>f, table

    def write(self,filename):
        handle = webbrowser.get()
        handle.open('abc.html')
        
print 

n=91
list = record()
r.input()
r.output()

for i in range(0,n):
    list.append(random.randint(1,10))
print len(list), list
filename = "abc.html"
r = record(10,list)
r.input(filename, table)
r.output(filename)
