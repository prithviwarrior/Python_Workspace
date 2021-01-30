s = "AlPhabET__123"
s2 = ""

for i in s:
	if(i.isupper):
		s2.join(i.lower)
	else:
		s2.join(i.upper)
		
print(s2)