#!/usr/bin/python

#def nameOfFunction(param):
#    your code
#    return

def addition(ass, num2, num3):
        return ass + num2 + num3

def division(ass, num2):
    if num2 == 0:
        return "ERROR: Cannot divide by ZERO!"
    else:
        return ass/num2
shitbag = 10
var2 = 23
var4653 = 352

result = addition(shitbag, var2, var4653)
print("Result of addition:", result)

result = division(var4653, var2)
print("Result of division:", result)

