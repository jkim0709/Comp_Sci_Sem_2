import random
restlist = ["McDonalds", "Burger King", "Subways"]
print(restlist)
d = random.randrange(0, 3)
sugitem = ["tacos", "burritos", "fries"]
x = input("Pick from the list of restaurants ")
if x == "McDonalds":
    print("Your menu items are \n Chicken Nuggets \n Big Mac \n Coca Cola")
    print("The suggested menu item is " + sugitem[d])
if x == "Burger King":
    print("Your menu items are \n Whopper \n Cheese \n Coke")
    print("The suggested menu item is " + sugitem[d])
if x == "Subways":
    print("Your menu items are \n Meatball \n Italian Sub \n Cola")
    print("The suggested menu item is " + sugitem[d])
    