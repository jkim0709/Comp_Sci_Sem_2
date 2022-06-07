x = input("Input your first name and last name? ")
y = 0
z = 1
for h in range(0,len(x)):
    letter = x[y:z]
    print(letter)
    y = y + 1
    z = z + 1
    if letter == " ":
        y-1,z-1
        d = y-1
        e = z-1
print(d, e)
print(x[e:len(x)] +" " + x[0:d])
    
        
