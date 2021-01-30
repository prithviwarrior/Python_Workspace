class Base():

	def __init__(self): #self-> d
		print("Self type in base", type(self))
		self.i = 10
		print("Base __init__")
		

	def display(self): 
		print ("base display")
		
		
class Derived(Base):
	def __init__(self): #self->d
		self.i = 1111 #this will be overrided by base value
		super().__init__() #super().__init__(self) 
		print("Derived __init__")
	

d = Derived() #d.__init__(d)
print(d.__dict__)
print(Derived.mro())
print("i in d:", d.i)
