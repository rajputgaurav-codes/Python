'''Write a python program that accept a line of text from user and perform following 
operation on it. 
1. Toggle case 
2. Title case 
3. Sentence case 
4. Exit 
Note: Menu will be repeated until user select Exit option.'''
name="Hello Evereone Happy holi"
while True:
    print("----menu----\n")
    print("1.Toggle case")
    print("2.Title case")
    print("3.Sentence case")
    print("4.Exit")

    choice=int(input("enter number between(1-4)"))

    if choice==1:
        print("Toggle case: ",name.swapcase())
    elif choice==2:
        print("Title case: ",name.title())
    elif choice==3:
        print("Sentence case: ",name.capitalize())
    elif choice==4:
        print("Exit")
        break
    else:
        print("Invalid choice")