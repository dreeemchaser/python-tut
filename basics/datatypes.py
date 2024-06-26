# # String data type 

# # Literal Assignment: 
firstname = "Alex"
lastname = "draai"

# # print(type(firstname))
# # print(type(firstname == str))
# # print(isinstance(firstname, str))

# # Constructor Function: 

# # pizza  = str("bacon")
# # print(type(pizza))
# # print(type(pizza == str))
# # print(isinstance(pizza, str))

# # Concatenation 
# fullname = firstname + " " + lastname
# print(fullname)

# #Cast Number to string: 
# age = str(23) 
# print(type(age))
# print(age)

# statement = "I am " + age + " years old."
# print(statement)

# #Multiple Lines: 

multiline = ''' 
    Hello 
    How are you? 
      
'''
# print(multiline)

# #Escaping Special Characters:
# sentence = 'I\'m back at work!\t \n\nThanks for letting me know. Where are you \\locatated?'
# print(sentence)

#String Methods: (Functions called on the string class!)
# print(firstname)
# print(firstname.lower())
# print(firstname.upper())
# print(multiline.title())
# print(multiline.replace(" ", " "))
# print(len(multiline))

# multiline += "               "


# print(len(multiline.strip()))
# print(len(multiline.lstrip()))
# print(len(multiline.rstrip()))

# Build A Menu
# print("_______________________")
# title = "menu".upper()
# print(title.center(20, "="))

coffe = ("Coffee".ljust(16, ".") + "$1".rjust(4))
tea = ("Tea".ljust(16, ".") + "$4".rjust(4))
muffin = ("Muffin".ljust(16, ".") + "$2".rjust(4))
         
        
# print(coffe)
# print(tea)
# print(muffin)



# String Index Values: 
print(firstname[0].center(20, "-"))
print(firstname[-1].center(20, "-")) # Last Value
print(firstname[1:2].center(20, "-")) # You can get a specific range

# Methods return boolean data: 
print(firstname.startswith("a"))
print(firstname.endswith("x"))

my_val = True # Has to be capital.
x = bool(False) # Constructor function
print(type(x))
print(type(my_val))

# Numberic Datatypes: 
# -> int type:
price = 100 
best_price = int(80)
print(type(price))
print(isinstance(best_price, int))

# -> float type: 

discount = 3.28
y = float(1.14)
print(type(discount))

# -> Complex Type:
comp_value = 5+3j
print(type(comp_value))
print(comp_value.real)
print(comp_value.imag)


# Built in fucntion for numbers: 

print(abs(discount))
print(abs(discount * -1 ))
print(round(discount))
print(round(discount,1))
