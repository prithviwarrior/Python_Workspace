#import re

file = open('Input.txt', 'r') 
Lines = file.readlines() 
count = 0

# Strips the newline character 
L1 = []
for line in Lines:
	#S = (line.strip())
	#print("Line{}: {}".format(count, line.strip()))
	L1.append(line.strip('\n').split(','))
	#print(S)
file.close() 


S = set()
print(type(S))
for t in L1:
	sum = int(t[1])  + int(t[2]) + int(t[3])
	t.append(sum)
	S.add(sum)


S = sorted(S, reverse = True) #set is returned as a list

file = open("output.txt","w")

for record in L1:
	record.append(str(S.index(record[4])))
	line = "{},{},{},{},{},{}".format(record[0],record[1],record[2],record[3],record[4],record[5])
	file.write(line + "\n")

file.close()

'''
for t in L1:
	sum = int(t[1])  + int(t[2]) + int(t[3])
	t.append(sum)
	S.add(sum)	
'''


	
'''
len = len(L1)
print(len)
L2 = []
for i in L1:
	sub = i.split(', ')
	#print(type(sub))
	L2.append(sub)

print(type(L2[2]))
''' 	



