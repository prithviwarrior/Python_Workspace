#Error because derived has init and it get executed and closed so the object i will not be created

class Base():

	def __init__(self): #self-> d
		print("Self type in base", type(self))
		self.i = 10
		print("Base __init__")
		

	def display(self): 
		print ("base display")
		
		
class Derived(Base):
	def __init__(self):
		print("Derived __init__")
	

d = Derived() #d.__init__(d)
print(d.__dict__)
print("i in d:", d.i)


	
