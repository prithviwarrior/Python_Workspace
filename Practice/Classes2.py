class Student():
	def show(self, i): #self => s1, i=10
		print("Stu:show")
		self.i = i
		
s1 = Student()
s1.show(10) #s1.show(s1) this
print("i in s1", s1.i)
print(s1.__dir__())
s2 = Student()
s2.show(20) #s1.show(s1) 
print("i in s2", s2.i)