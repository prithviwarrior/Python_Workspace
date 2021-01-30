class Employee():
	def display(self, id, sal):
		self.id= id
		self.sal= sal


id = input()
sal = input()		
E1 = Employee()
E1.display(id, sal)
print("id: ", E1.id, "\nsal: ", E1.sal)
