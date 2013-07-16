'''we will create an icecream machine that produces icecream in with tiny flavor, medium flavor and large flavor.in addition the icecream cone will be wrapped into some paper that has an image on it. Images will be Penguin, Apple,
'''

class icecream:
	number_of_icecream = 0
dave = icecream()
dave.number_of_icecream = 5
print "dave has %s icecream from the machine" % dave.number_of_icecream

class icecream:
	number_of_icecream = 0
	def flavor(self):
		print "Strawberry icecream"
dave = icecream()

dave.flavor()

class icecream:
	number_of_icecream = 0
	def flavor(self):
		print "Strawberry icecream"
dave = icecream()

dave.flavor()

print " _______________________________"

class icecream_machine:

    milk = 10
    flavor = {}

    def add_flavor(self, name, amount):
        self.flavor[name] = amount

    def remove_flavor(self, name):
        del self.flavor[name]

    def add_milk(self, amount):
        self.milk = self.milk + amount

    def get_icecream(self, flavor):
        if self.milk - self.flavor [flavor] >= 0  :
            self.milk = self.milk - self.flavor [flavor]  
        else:
            print "Sorry I have no more milk. Come back another time"
        
    def flavors(self):
        return self.flavor

machine = icecream_machine()
machine.add_milk(100)
# machine.milk = 1000

print machine.milk

machine.add_flavor("tiny", 10)
machine.add_flavor("large", 30)
machine.add_flavor("medium", 20)

print machine.flavors()

machine.get_icecream("large")
print machine.milk

machine.get_icecream("large")
print machine.milk

machine.get_icecream("large")
print machine.milk

machine.get_icecream("large")
print machine.milk

machine.get_icecream("large")
print machine.milk


machine.get_icecream("large")
print machine.milk
