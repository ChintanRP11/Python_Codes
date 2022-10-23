#Polymorphism

#Simple polymorphism
def sum(x,y,z=0):
	return x+y+z

print(sum(1,2))
print(sum(1,2,3))


#polymorphism using class methods
class Flight:
	def __init__(self,engine):
		self.engine=engine
	def startEngine(self):
		self.engine.start()

class AirbusEngine:
	def start(self):
		print("Starting Airbus Engine")

class BoingEngine:
	def start(self):
		print("Starting Boing Engine")
	
ae = AirbusEngine()
f = Flight(ae)
# run start method using parent class.
f.startEngine()

be = BoingEngine()
f1 = Flight(be)
f1.startEngine()