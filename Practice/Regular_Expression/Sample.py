import re


#print(re.match("he?ll+o","hellllllo"))
print(re.match("[123abc]","123nh")) #matches 1 return 1
print(re.match("[123abc]+","123nh"))
print(re.match("[a-z123]+","abvh123"))
print(re.match("[a-jpq23]+","abp2345"))
print(re.match("[a-z]+|[1-9]+","145jisdfg")) #matches numbers and doesnt go back to char
print(re.match("","adhitnpo"))

