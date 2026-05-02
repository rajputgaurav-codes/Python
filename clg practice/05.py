#Write a Python program to find Fibonacci series up to n terms.
num=int(input("Enter a number: "))
a=0
b=1
c=0
for i in range(num):
    print(a,end=" ")
    c=a+b
    a=b
    b=c