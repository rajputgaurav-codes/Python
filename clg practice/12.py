'''Write a python program to create choice based menu for calculator operations.'''
n1=int(input("enter a first number:"))
n2=int(input("enter a second number:"))

choise=int(input("Enter a number between(1-4):"))
if choise==1:
    print("Addition of both number is: ",n1+n2)
elif choise==2:
    print("Subtraction of both number is: ",n1-n2)
elif choise==3:
    print("Multiplication of both number is: ",n1*n2)
elif choise==4:
    print("Division of both number is: ",n1/n2)
else:
    print("Invalid choice")
    
