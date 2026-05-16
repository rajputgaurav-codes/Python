#print the reverse n number using udf
def print_reverse(n):
    for i in range(n,0,-1):
        print(i,end=" ")

num=int(input("enter a n number:"))
print_reverse(num)