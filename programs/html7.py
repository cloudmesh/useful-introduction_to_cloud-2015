import webbrowser
import random
import math
import os

class table:

    # self.filname
    # self.alist
    # self.cols
    # self.table
    # self.n
    def __init__(self, filename, cols, n):
        self.filename = filename
        self.cols = cols
        self.alist = []
        self.table = ""
        self.n = n  
        
    def generate (self):
        self.table = "<table border=1>\n"
        rows = int(math.ceil(len(self.alist) / float(self.cols)))
        item = 0
        for row in range(0, 10):
            self.table = self.table + "  <tr>"
            for col in range(0, 10):
                value = ""
                if item < len(self.alist):
                    value = self.alist[item]
                    self.table = self.table + "<td>{0}</td>".format(value)
                    item = item + 1
            self.table = self.table + "</tr>\n"
        self.table = self.table + "</table>" + "%i" % item

    def write(self):
        f = open (self.filename, "a")
        print >> f, self.table
        f.close() 
        
    

    def display(self):
        handle = webbrowser.get()
        handle.open(self.filename)

    def random(self):
         
        self.alist = []
        for i in range(0, self.n):
            self.alist.append(random.randint(1, 10))
filename = 't.html'
os.remove(filename)

t = table(filename, 10, 91)

t.random()
t.generate()
t.write()
t.display()

w = table(filename, 7, 20)

w.random()
w.generate()
w.write()
w.display()



