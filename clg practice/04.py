#Write a Python program to find factorial of a number. 

num=int(input("Enter a number: "))

fact=1
i=1

while i<=num:
    fact=fact*i
    i+=1
    print("Factorial is: ",fact)

#using math build in function
import math
num=int(input("Enter a number: "))
print("Factorial is : ",math.factorial(num))

# using for loop
num=int(input("Enter a number: "))
fact=1
for i in range(1,num+1):
    fact=fact*i

print(f"factorial of {num} is {fact}")
