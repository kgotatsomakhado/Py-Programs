import math

print("*******************************************************")
print("")
print("         Welcome to the hypotenuse program")
print("")
print("*******************************************************")
print("")
print("Formula- [c = √a\u00b2 + b\u00b2]")
print("")
a = float(input("Enter the value of 'a': "))
b = float(input("Enter the value of 'b': "))

c = math.sqrt(pow(a, 2) + pow(b, 2))

print("")
print(f"The size of your hypotenuse is: {c} units")
print("")
print("*******************************************************")