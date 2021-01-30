class Student():
	def show(self): #self => s1, i=10
		print("Stu:show")
		self.i = 10
		
s1 = Student()
s1.show() #s1.show(s1) this
print("i in s1", s1.i)

s2 = Student()
s2.show() #s1.show(s1) 
print("i in s2", s1.i)


