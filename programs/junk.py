#! /usr/bin/python

import sys

'''
her is the task i like you to do to reinforce the learning experience once you
are done with the tutorial.

a) write a program that uses loops over both x and y coordinates while x is in
1,2,3,4,5 and y is in 5,4,3,2,1 and prints the x and y coordinate

b) write a program that sums up all values in x and y

c) write a program just like a) but does not print values where x is equal to 2
and y is equal to 4

d) write a function that takes in a word and returns  it in reverse order

e) provide a program that uses dicts

f) read up on classes we will cover this in more detail  next week.

        we will create an icecream machine that produces icecream in with tiny
        flavor, medium flavor and large flavor. in addition the icecream cone
        will be wrapped into some paper that has an image on it. Images will be
        Penguin, Apple,

'''





xlist = [1, 2, 3, 4, 5]
ylist = [5, 4, 3, 2, 1]
zlist = [4, 5, 2, 1, 3]
print(xlist)
print(ylist)
print(zlist)




print "GREGORS TASK"

for x in xlist:
	for y in ylist:		
		print (x, y)


print ('Hello world')

print ("Task A")
# x and y cordinates
index = 1
for y in ylist:
	for x in xlist:
		print index, (x, y)
		index += 1


print ("Task B")
sum = 0
for y in ylist:
	for x in xlist:
		sum += y + x

print ("The sum is", sum)

print ("Task C")

for x in xlist:
	sum = (x, y)
print('\n\n The Sum of x and y cordinates is: + str(sum)')

for y in ylist:
	if y == 5 or y < 4:
		for x in xlist:
			if x >= 3 or x < 2:
				print (x, y)
print ("task D")
tim = {'cheese': xlist, 'burger': ylist}
tim['ham'] = zlist
for a in tim:
	print (a)
print ("task F")
class clown:
	number_of_noise = 1
jack = clown()

jack.number_of_noise = 3

print "Jack has %s noise." % jack.number_of_noise

class clown:
	number_of_noise = 1

	def nose(self):
		print "Big"
jack = clown()

jack.nose()

