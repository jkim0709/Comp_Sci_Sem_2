mynumbers = [6,9,32,28,15,22,3,18]
y = -1
for x in range(0, 8):
    if mynumbers[x] > y:
         y = mynumbers[x]
print(str(y) + " is the max number")

z = 1000
for x in range(0, 8):
    if mynumbers[x] < z:
        z = mynumbers[x]
print(str(z) + " is the min number")

w = mynumbers[0] + mynumbers[1] + mynumbers[2] + mynumbers[3] + mynumbers[4] + mynumbers[5] + mynumbers[6] + mynumbers[7]
i = w/8
print(str(i) + " is the average")

    
    
    