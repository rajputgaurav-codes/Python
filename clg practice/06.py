#Write a Python program to check if the number is an Armstrong number or not. 
num=int(input("Enter a number: "))
sum=0
temp=num
while temp > 0:
    digit=temp%10
    sum=sum+digit**3
    temp=temp//10

if(sum==num):
    print("It is the Armstrong number")
else:
    print("It is not the Armstrong number")