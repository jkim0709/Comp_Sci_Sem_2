x = input("What is your favorite number? ")
y = int(input("How old are you?"))
c = 0
thislist = [x]
for i in range(0, 40):
    if x[c: c+2] == "42":
        d = int(x[c: c + 2])
        print(d)
        j = d * y
        print(j)
    c = c + 1
