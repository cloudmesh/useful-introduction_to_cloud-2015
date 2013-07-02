import webbrowser
import random
import math

class table:

	
    def make_table(cols, list):

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
        
return table

def write_table(filename, table):
    f = open ('abc.html', 'w')
    print >>f, table

def display_table(filename):
    handle = webbrowser.get()
    handle.open('abc.html')

n = 91
list = []
for i in range(0,n):
    list.append(random.randint(1,10))
print len(list), list
filename = "abc.html"
table = make_table(10,list)
write_table(filename, table)
display_table(filename)
