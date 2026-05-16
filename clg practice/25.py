#Write a Python program to print sum of N numbers using UDF.
def print_sum_number(n):
    sum=0
    for i in range(1,n+1):
        print(i,end=" ")
        sum = sum + i
    
    print("Sum of n number: ",sum)

num=int(input("enter a nth number: "))
print_sum_number(num)