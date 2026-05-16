#Write a Python to print N number using UDF
def print_number(n):
    for i in range(1,n+1):
        print(i,end=" ")

num=int(input("enter a n number:"))
print_number(num)