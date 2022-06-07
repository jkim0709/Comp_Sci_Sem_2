length = int(input("Please enter line length: "))
hl = input("Do you want a horizontal or vertical line?")
if hl == "horizontal":
    for x in range(0, length):
        print("*", end= "")
if hl == "vertical":
    for x in range(0, length):
        print("*", end= "\n")
   
