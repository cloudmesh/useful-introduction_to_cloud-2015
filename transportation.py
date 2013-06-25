class transportation:

	passengers = {}
        fleet = {}

	def add_vehicle (self,kind, noof):
            """ this function add a vihicle of a certain kind to the fleet"""
	    print "todo"

	def set_passengers(self,kind, amount):
        	self.fleet[kind] = amount

	
	

	def get_car(self, kind, passenger):
        	if self.fleet[kind] - self.passengers [passengers] >= 0  :
            		self.fleet[kind] -= self.passengers [passengers] 



 	def passengers(self):
        	return self.passengers

station = transportation()


station.set_passengers("truck",50)
station.set_passengers("convertible",25)
station.set_passengers("bus",80)

station.add_vehicle  ("truck",10)

station.add_vehicle ("convertible", 2)

station.add_vehicle ("bus", 5)


print station.fleet
