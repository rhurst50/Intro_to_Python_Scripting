
count = 10
while(count > 0):
    print("*" * count)
    count -= 1

for i in range(0,10):
    print("*" * i)

mystr = 'test'

for c in mystr:
    print(c)

mylist = ['hey there', 'how are you', 234, 'i am fine']
for s in mylist:
    print(s)

for i in range(0,10):
    if i == 8:
        break
        print("in IF:", i)
    print(i)
for i in range(0,11):
    if i == 8:
        continue
        print("in IF:", i)
    print(i)

for i in range(0,10):
    if i == 8:
        pass
        print("in IF:", i)
    print(i)
