#!/usr/bin/python
length = 10
length2 = 9
count = 1
astr = "*"
subtract = 2

for i in range(length):
    for j in range(length-i):
        print(" ", end='')
    print(astr)
    astr += "**"
for a in range(length2):
    for b in range(count):
        print(" ", end='')
    print (astr[:-subtract])
    subtract += 2
    count += 1
