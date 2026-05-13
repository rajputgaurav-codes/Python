#Write a Python program to find average of numbers in a list
l1=[45,12,78,85,35,45,36,45]
avg=sum(l1)/len(l1)
print(avg)

sum=0

for i in l1:
    sum=sum+i

print("average of the list is: ",sum/len(l1))