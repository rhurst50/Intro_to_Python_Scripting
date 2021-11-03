length = 10
astr = "*"
for i in range(length):
    for j in range(length-i):
        print(" ",end='')
    print(astr)
    astr += "**"

length = 11
count = 3
astr = "*"
for k in range(length):
    if k <=5:
        print(astr)
        astr +="***"
    else:
        count += 3
        print(astr[:-count])
        #count += 3
