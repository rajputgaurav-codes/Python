'''Write a python program to calculate net salary where net salary = basic salary + hra 
+ da - pf, hra is 10% of basic salary, da is 50% of basic salary and pf is 20% of 
basic salary. '''
name=input("enter the name of employee : ")
basicsalary=int(input("enter the basic salary of the employee : "))
hra=0.10*basicsalary
da=0.50*basicsalary
pf=0.20*basicsalary
netsalary=basicsalary+hra+da-pf
print("The net salary of the employee is: ",netsalary)