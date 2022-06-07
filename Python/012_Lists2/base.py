import random
x = int(input("How many random numbers would you like? "))
thislist = []
for i in range(0,x):
    y = random.randrange(1,11)
    thislist.append(y)
print(thislist)
