'''Write a python program that store characters of a word as List elements and 
removes vowels from the list.'''

old_list=["p","r","o","g","r","a","m"]

result="aeiou"
for ch in old_list:
    if result==ch:
        old_list.remove(result)
print(old_list)
