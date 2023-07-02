#write a program to find & calculate sqaure root program
#solution-1(using exponentiation)
#n1=64
# n1=int(input("enter a number is"))
# sr=n1**(1/2)
# print("the square root of the given numbef is", sr)

             #or

#solution 2(using math module)
import math
n=int(input("enter the number"))
sr = math.sqrt(n)
print("the square root of the number is:", sr)