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
'''
fp = Data()
data2 = pickle.dump(fp)
data2 = Data()

data2 = pickle.load(fp)
fp.close()
data2.display()

'''

L = [1,2,3,4,5,6,7]
'''
fp = open("L.dat", "wb")

L_B = pickle.dump(L, fp)

fp.close
'''
fp = open("L.dat","rb")

L2 = pickle.load(fp)

print(L2)





