# variables is like a container where we stores value 

# examples 

name = "Ster"
age = 20

#Here name is a variables stores "Ster"
# Here age is a variables stores the number 20 


# How to create a variables 

variable_name = 'Value'

# Examples like 

x = 25    # This line stores an integer (Number)
y = 3.14  # This line stores an decimal(float)
z = "dok" # This line stores an string (Text)
is_happy = True # This line stores an Boolean(True or False)


# Names of Ruling Variables

#Must start with a letter or an underscore _

#Can only contain letters, numbers, and underscores

# Cannot start with a number

# Cannot use spaces or special symbols like @, $, %, etc.

# Should not be a Python keyword (like for, if, class)

# ✅ Valid: name, user_age, _count, x1

# ❌ Invalid: 1stname, user age, @data, if


# Types of Variables 

age = 23  # Integer
height = 2.2 # Float
Fruit = "mango" # String 
Answer = True # Boolean
Goal = ["lambo","ferrari","bugati"] # List/Arrays
Money = None # Nothing


# Using Variables 

a = 5 
b = 10 
sum = a+b
print(sum) # output 15

#Reassigning Variables

x = 30 
y = 30 
print(x) # output 30

# Multiple variables in one line 

x,y,z = 1,2,3 
a = x,y,z
print(x)

a = b = c = 100
print(a)

# Input from user (Dynamic Variables)

# name = input("What is your name? ")
# print("Hello,", name)


name = input ("What is your name?")

# age = input ("What is your age?")

print("Hello! My name is",name,)

# print("I am",age, "year old")

# Summary Tables 

# | Concept       Description                                 
#| Variable     | A name to store data                        |
#| Declaration  | `x = 5`                                     |
#| Types        | int, float, str, bool, list, etc.           |
#| Change Value | `x = 10` → `x = 20`                         |
#| User Input   | `input()` lets user type value              |
#| Check Type   | `type(x)` shows what kind of value it holds |


#Global variables 

x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()  