'''Write a python program to converts all the characters of a Lower Case to Upper 
Case and Upper Case to Lower Case. '''
name="My name is Gaurav"
# print(name.swapcase())
result=""
for ch in name:
    if ch.islower():
        result= result + ch.upper()
    else:
        result= result + ch.lower()
print("converting string:",result)




