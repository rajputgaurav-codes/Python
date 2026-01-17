#write a program to write a letter and print
name="Gaurav"
date="22-05-2007"
print(f''' 
          Dear <|{name}|>,
          You are Selected !
          <|{date}|>
          ''')

#use string function
letter= '''Dear <|Name|>,
          You are Selected !
          <|Date|>'''
print(letter.replace("<|Name|>","Amit").replace("<|Date|>","22-september"))