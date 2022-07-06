# -- PRIMITIVE DATA TYPES --


# - Boolean values --
# -Assesses the truth value of something. Only has two values true and false

is_hungry = True
has_freckles = False


# - Numbers -
# -integers (whole numbers), floating point numbers (commanly known as decimal numbers), and comples numbers

age = 35  # storing an int
weight = 160.57  # storing a float


# String - literal text

name = "Joe Blue"


# --------------------------------------------------------------------


# -- COMPOSTIE TYPES --

# - Tuples -
# - a type of data that is immutable (cant be modified after its creation)
# and can hold a group of values. Tuples can contain mixed data types.

dog = ('Bruce', 'cocker spaniel', 19, False)
print(dog[0])
# dog[1] = 'dachshund'  # ERROR: cannot be modified ('tuple object does not support item assignment)


# - List -
# - a type of data that is mutable and can hold a group of values.
# Ususally meant to store a collection of related data.

empty_list = []
ninjas = ['Rozen', 'KB', 'Oliver']
print(ninjas[2])  # output oliver
ninjas[0] = 'Francis'  # changes 'Rozen' to 'Francis' due to [0]
ninjas.append('Micheal')  # .append adds micheal to end
ninjas.insert(1, 'Bernard')  # adds "Bernard" to 1 slot
print(ninjas)  # output: ['Francis', 'Bernard', 'KB', 'Oliver', 'Micheal']
ninjas.pop()  # .pop removes last item in list
print(ninjas)  # output: ['Francis', 'Bernard', 'KB', 'Oliver']
ninjas.pop(1)  # removes item in [1]
print(ninjas)  # output: ['Francis', 'KB', 'Oliver']


# - Dictionaries -
# - a group of keys-values pairs. Dictionary elements are indexed by
# unique keys which are used to access values.

empty_dict = {}
new_person = {'name': 'John', 'age': 38, 'weight': 160.2, 'has_glasses': False}
# updates if the key exists, adds a key-value pair if it dosen't
new_person['name'] = 'Jack'
new_person['hobbies'] = ['climbing', 'coding']
print(new_person)
# output : {'name': 'Jack', 'age': 38, 'weight': 160.2, 'has_glasses': False, 'hobbies': ['climbing', 'coding']}
# removes the specific key(weight) and return the value(160.2)
w = new_person.pop('weight')
print(w)
print(new_person)
# out put:{'name': 'Jack', 'age': 38, 'has_glasses': False, 'hobbies': ['climbing', 'coding']}


# - Common Functions -
print(type(2.63))  # output: <class 'float'>
print(type(new_person))  # output: <class 'dict'>

print(len('new_person'))  # output: 10 (the number of key-value pairs)
print(len("Coding Dojo"))  # output: 11


# --------------------------------------------------------------------


# -- NUMBERS --
# - 3 types of numbers -
# - int - whole numbers, postivie or negative ex. 35
# - float - decimal numbers, positive or negative ex. 4.2
# - complex - are a part of the real number system and are often referenced with the letter j. ex 1 + 3j.

num = 25  # int
dec = 4.2  # float
print(num)  # logs (num) - output: 25
print(dec)  # logs (dec) - output: 4.2
print(type(dec))  # types check - output: <class 'float'>


# - Type -
print(type(24))  # output - "int"
print(type(3.9))  # output - "float"
print(type(3j))  # output - "complex"


# - Conversion -
int_to_float = float(35)  # converts in to a float - output: "35.0"
float_to_int = int(44.2)  # converts float to int - ouptut: "44"
int_to_complex = complex(35)  # converts int to complex - output "(35 + 0j)"
print(int_to_float)
print(float_to_int)
print(int_to_complex)
print(type(int_to_float))  # output <class 'float'>
print(type(float_to_int))  # output <class 'int'>
print(type(int_to_complex))  # output <class: 'complex'>


# --------------------------------------------------------------------


# -- STRINGS --


# - String Literals -
# Strings are any sequence of characters (letters, numerals, 1($/}#, etc)) enclosed by '' or " "

print("this is a sample string")  # example of string


# - Conatentating Strings and Variables with the print function

name1 = "Zen"
print("My name is", name1)
# the print() function inserts a space between elements separated by a comma


name2 = "Zen"
print("My name is" + name2)
# this will concatenat the contents in a new string with the help of +

# examples of concatenating with iteger

name1 = "zen"
