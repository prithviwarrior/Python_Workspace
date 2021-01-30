class Base():

	def __init__(self): #self-> d
		print("Self type in base", type(self))
		self.i = 10
		print("Base __init__")
		

	def display(self): 
		print ("base display")
		
		
class Derived(Base):
	pass
	
'''
d = Derived() #d.__init__(d)
d.display()
print("i in d:", d.i)
'''


	
