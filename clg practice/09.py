'''Write a Python program that accepts input as marks of 3 subjects for each student. 
Display total marks, percentage and grade (if per > 70 then grade DIST, per > 60 
then grade FIRST, per > 50 then grade SECOND, per > 40 then grade PASS) of 
each student. '''
s1=int(input("Enter first subject marks : "))
s2=int(input("Enter Second subject marks : "))
s3=int(input("Enter Third subject marks : "))

total_marks=s1+s2+s3
print("Total marks of the student is : ",total_marks)
percentage=total_marks/300.0*100
print("percentage of the student is : ",percentage)
if(percentage>=70 and percentage<=100):
    print("Grade=Distinct")
elif(percentage>=60 and percentage<=70):
    print("Grade=First")
elif(percentage>=50 and percentage<=60):
    print("Grade=Second")
elif(percentage>=40 and percentage<=50):
    print("Grade=pass")
else:
    print("Fail")