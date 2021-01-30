import pickle

L = [1,2,3,4,5]

L_B = pickle.dumps(L)

print(L_B)
print(type(L_B))
L_O = pickle.loads(L_B)
print(L_O)
print(type(L_O))

