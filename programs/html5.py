import webbrowser
import random
import math


class table:

    # self.filname


    #self.table

    def __init__(self, filename, cols, alist):
        self.filename = filename
        self.cols = cols
        self.alist = alist
        self.table = ""

    def generate (self):
        self.table = "<table border=1>\n"
        rows = int(math.ceil(len(self.alist)/float(self.cols)))
        item = 0
        for row in range(0,10):
            self.table = self.table + "  <tr>"
            for col in range(0,10):
                value = ""
                if item < len(alist):
                    value = alist[item]
                    self.table = self.table + "<td>{0}</td>".format(value)
                    item = item + 1
            self.table = self.table + "</tr>\n"
        self.table = self.table + "</table>" + "%i" % item

    def write(self):
        f = open (self.filename, 'w')
        print >>f, self.table
        f.close() 

    def display(self):
        handle = webbrowser.get()
        handle.open(self.filename)

    def random(self,n):
        self.random = ""
        print random
        
print 

n=91
alist = []
for i in range(0,n):
    alist.append(random.randint(1,10))

t = table('abc.html', 10,alist)

t.random(91)
t.generate()
t.write()
t.display()



