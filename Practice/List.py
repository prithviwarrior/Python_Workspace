'''
L1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

L2 = []

for i in range (len(L1)):
	if(L1[i]%2 == 0 ):
		L2.append(L1[i])
		
print (L2)

'''

'''
L1 = [1,2,3,4,5]
L2 = [6,7,8,9,10]
L3 = []

for i in range (len(L1)):
	L3.append(L1[i] + L2[i])
print (L3)
'''

'''
s="12345"
x = int(s)
sum = 0
print(x)
print(type(x))
while (x != 0):
    sum = sum + x %10
    x   = x //10
    
print(sum)
'''

'''
s = "AbcDE__12a"
#print(swapcase(s))
print(s.swapcase())
'''

'''
L = [1,2,3,4,5,6,7,8,9]
L2 = []

for i in range (len(L)-1):
	for j in range (i+1, len(L)):
		if((L[i]+L[j])==9):
			t = (L[i], L[j])
			L2.append(t)
			
print(L2)
'''

'''
S = "PRATHVIRAJ"

for i in range (len(S)):
	count = 0
	S[i] not in S[i:0:-1]
	
	for j in range (i, len(S)):
		if(S[i] == S[j]):
			count+=1
			#S[j] = 0
	
	print(S[i], count)
'''
			

'''
S = "PRATHVIRAJ"
L = list(S)
for i in range (len(L)):
	count = 0
	for j in range (i+1, len(L)):
		if(L[i] == L[j]):
			count+=1
			L[j] = 0
	print(L[i], count+1)
'''

'''
def swap_case(s):
    input_list = list(s)
    return "".join(i.lower() if i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" else i.upper() for i in input_list)

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
'''

'''
L = [1,2,3,4,5,6,7,8,9]
L2 = []

for i in range (len(L)-1):
	for j in range (0, len(L)):
		if((i != j)and(L[i]+L[j])==9):
			t = (L[i], L[j])
			L2.append(t)
			
print(L2)
'''

'''
import re

s1 = "abCD45__"
s2 = ""

for ch in s1:
	if(re.match("[a-z]", ch)):
		s2 = s2 + ch.upper()
	elif(re.match("[A-Z]", ch)):
		s2 = s2 + ch.lower()
	else:
		s2 = s2 + ch

print(s2)
'''




