import matplotlib.pyplot as plt
import numpy as np

'''
x = rd.randint(1,100,size=20)
y = rd.randint(1,100,size=20)

print(x,"\n",y)

plt.plot(x,y,marker="s", color="red", markersize="10", linestyle="dotted", markeredgecolor="blue", markerfacecolor="g") #matplotlib marker documentation
plt.show()
'''

'''
names = ["Name1","Name2", "Name3", "Name4", "Name5" ]
mark_m1 = [1,2,4,3,5]
mark_m2 = [3,5,2,7,4]

print(plt.style.available)
plt.style.use("seaborn-dark")

plt.scatter(names, mark_m1, marker="o", label="Marks1", s=80, color="Red")

#plt.plot(names,mark_m1,marker="s", color="red",label="M1", markersize="5", linestyle="dotted", markeredgecolor="blue", markerfacecolor="g") #matplotlib marker documentation
#plt.plot(names,mark_m2,marker="o", color="blue",label="M2", markersize="10", linestyle="solid", markeredgecolor="blue", markerfacecolor="y") #matplotlib marker documentation

plt.xlabel("StudentName")
plt.ylabel("Marks")
'''

'''
shares = [10,20,30,30,10]
names = ["LTTS", "INFOSYS", "WIPRO", "TCS","CTS"]
colors = ["red", "green", "yellow", "cyan", "black"]
explods =(0.01,0.02,0.03,0.04,0.05)

plt.pie(shares, labels=names, colors= colors, explode=explods, shadow="True", autopct="%0.0f%%")


plt.title("Marks Analysis", fontsize=10, fontweight="bold")
'''

'''
data = np.random.normal(size = 100)
print(data)
mark_m1 = [10,20,40,30,50]
plt.hist(data, histtype="step", color="Red", label="Histogram")
'''

'''
names = ["Name1","Name2", "Name3", "Name4", "Name5"]
mark_m1 = [1,2,4,3,5]
mark_m2 = [3,5,2,7,4]
colors = ["red", "green", "yellow", "cyan", "black"]

plt.subplot(2,2,3)

plt.bar(names, mark_m1, label="Marks1", width=[0.5, 0.2,0.3,0.6,0.11], color=colors)
plt.title("Marks 1 analysis")
#plt.show()
plt.xlabel("StudentName")
plt.ylabel("Marks")

plt.subplot(2,2,4)
plt.bar(names, mark_m2, label="Marks2", width=0.5, color="blue")
plt.title("Marks 2 analysis")
plt.xlabel("StudentName")
plt.ylabel("Marks")
'''

pre_marks = [10,20,20,40,60,90,70,50,30,80]
post_marks = [30,40,50,50,60,70,80,90,65,75]
label=["pre_marks","post_marks"]

box_plt = plt.boxplot([pre_marks, post_marks], labels= label, patch_artist= True)
plt.title("Marks Distribution")

patches = box_plt["boxes"]

colors = ["cyan","yellow"]
index = 0
for patch in patches:
	patch.set_facecolor(colors[index])
	index = index +1

plt.legend(loc="upper left") #show all the lable in the plot
#plt.savefig("Test.png")
plt.show()
