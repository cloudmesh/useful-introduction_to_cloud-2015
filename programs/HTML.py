table = "<table border=1>\n"

item = 1

for row in range(0, 10):
    table = table + "  <tr>"

    for col in range(0, 10):
        table = table + "<td>"
        if item <= 97:
            table = table + "%i" % item
        item = item + 1
        table = table + "</td>"

    table = table + "</tr>\n"

table = table + "</table>"

f = open ('abc.html', 'w')
print >> f, table

import webbrowser
handle = webbrowser.get()
handle.open('abc.html')
