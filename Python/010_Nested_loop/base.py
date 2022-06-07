sym = input("What symbol woulld you like to use?")
wid = int(input("What's the width of your box?"))
hei = int(input("What's the height of your box?"))  
for y in range(0,hei):    
    for x in range(0, wid):
        print(sym, end="")
    print("")

    