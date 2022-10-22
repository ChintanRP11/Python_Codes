# Defining class variable.... here, class variable is vehicle()
class vehicle():
    domain = 'vehicle types'		#it is static field for class vehicle
    def setvname(self,name):
        self.name = name

# defining instance variable here, instances are ob1 and ob2
# class variable is shared by both instances (ob1, ob2)
# instance variables are unique to each other (ob1 and ob2 are unique to each other)
ob1 = vehicle()
ob2 = vehicle()

ob1.setvname('Truck')
ob2.setvname('Bus')

print(ob1.domain)
print(ob2.domain)

ob1.domain = 'Transport vehicles'
print(ob1.domain)
print(ob2.domain)

print(ob1.name)
print(ob2.name)