#Write a python program to display reverse number. 

# l1= input("enter the number : ")
# rev= l1[::-1]
# print("reverse number :",int(rev))

  #using formula/logic
num=int(input("enter the number : "))
reverse=0
while num > 0:
    digit=num%10
    reverse=reverse*10+digit
    num=num//10
print("reverse number is : ",reverse)

