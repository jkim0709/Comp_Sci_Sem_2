items = int(input("How many items would you like to buy?:" ))
d=0
for x in range(0, items):
    input("What item are you buying? ")
    y = int(input("How much was the item? "))
    d = d + y
print("Your total is $" + str(d))
    