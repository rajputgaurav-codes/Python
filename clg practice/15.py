#Write a Python program to sum all the items in a list
l1=[45,25,89,12,63,65,96,67,25]
total=sum(l1)
avg=total/len(l1)
print(avg)

#  using loop and also find average
sum=0
i=0
for i in l1:
    
    sum=sum+i
print(sum/len(l1))