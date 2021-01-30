import pickle

class Data():
	def __init__(self):
		self.i = 10
		self.j = 20
		
	def display(self):
		print("i:{}, j: {}". format(self.i, self.j))
		
data = Data()
data.i = 100
data.j = 200
data.display()

data_b = pickle.dumps(data)

print(data_b)
print(type(data_b))

data_o = pickle.loads(data_b)
data.display()
print(data_o)
print(type(data_o))
