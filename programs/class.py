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

