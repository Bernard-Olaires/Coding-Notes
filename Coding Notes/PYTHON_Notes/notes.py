# -- PRIMITIVE DATA TYPES --


# - Boolean values --
# -Assesses the truth value of something. Only has two values true and false

from hashlib import new


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

# - Type Casting or Explicit Type conversion -
# - in python you add two strings together. Python dosent know how to add string a number

# print("helo" + 42) #output error
print("Hello" + str(42))

# another example is receiving a string inout from a use that we want to treat as a number

total = 35
user_val = "26"
total = total + int(user_val)  # total will be 61


# -String Interpolation -
# we can ingject variable into our strings

# -F-Strings (literal String Interpilation)
""" To construct a f-string, place an f right before the open
quotation. Then within the string, place any variables within
curly brackets """

first_name = "Zen"
last_name = "Coder"
age = 27
print(f"My name is {first_name} {last_name} and I am {age} years old.")


# - string.format() -
""" rior to f-strings, string interpolation was accomplished with the .format() method. 
If you're searching online, you will likely find code snippets using this method. 
To use it, type out the full string, replacing any words that will get their values from variables with {}. 
Then call the format method on the string, passing in arguments in the order in which they should fill the {} placeholders"""

first_name = "Zen"
last_name = "coder"
age = 27
print("My name is {} {} and i am {} years old.".format(first_name, last_name, age))
# output: My name is Zen coder and i am 27 years old.
print("My name is {} {} and i am {} years old.".format(age, first_name, last_name))
# output: My name is 27 Zen and i am coder years old.

""" The two example print statements are provided to demonstrate that the format 
method reads the string from left to right, replacing the {} with the value of 
the arguments provided, in order. This means there should be the same number of 
sets of {} as there are arguments passed into the function. """


# %-formatting

hw = "Hello %s" % "world" 	# with literal values
py = "I love Python %d" % 3
print(hw, py)
# output: Hello world I love Python 3
name = "Zen"
age = 27
print("My name is %s and I'm %d" % (name, age))		# or with variables
# output: My name is Zen and I'm 27

# --------------------------------------------------------------------

# - LIST OVERVIEW -


"""  
        list are comparable to arryas from Javascript
        indexed starting at 0
        built in methods
        defined with []
        can store any data we want inside
        length can change
"""

# list are also known as an "array"
"""in python a list can me a mixture of data typles, including, typles, string
    numeric, and even a list itself (a list within a list) example:"""

ninjas = ['Rozen', 'KB', 'Oliver']
mylist = ['4', ['list', 'in', 'a', 'list'], 987]
empty_list = []


"""Another cool feature of lists in python is that you can combine them together
and duplicate values fairly easily, by using the + and * operators. 
If you 'add' lists together, it will create a new list that contains all the 
values of both of the arrays! Likewise, if you 'multiply' a list by a whole 
number it will copy all of the values that many times, and make a new list 
with all the copied values."""

fruits = ['apple', 'banana', 'orange', 'strawberry']
vegetables = ['lettuce', 'cucumber', 'carrots']
# combine fruits and vegtables with "+"
fruits_and_vegetables = fruits + vegetables
print(fruits_and_vegetables)
salad = 3 * vegetables  # will print vegetables 3 times
print(salad)

# --------------------------------------------------------------------

# - LIST MANIPULATION -

# - Acessing Values -

drawers = ["documents", "envelopes", "pens"]

# access the drawer with index of 0 and print value
print(drawers[0])  # prints documents
# access the drawer with index of 1 and print value
print(drawers[1])  # prints envelopes
# access the drawer with index of 2 and print value
print(drawers[2])  # prints pens

# replace "documents" with "tchotchkes"
drawers[0] = "tchotchkes"
print(drawers)  # prints ["tchotchkes", "envelopes", "pens"]

# stores the value "tchotchkes" in a temporary variable.
top_contents = drawers[0]

# Replaces the value at index 1
# with whatever value is stored at index 0
drawers[1] = drawers[0]
print(drawers)  # prints ["tchotchkes", "tchotchkes", "pens"]

# - Left-Hand-Side vs Right-Hand-Side -

"""
    left-hand side = LOCATION 
    right-hand side = RAW VALUE
"""

# - Appending Value to a list -

"""
    useful example of a method that we will use to manipulate list
    some_list.append(some_value)

    appends a new item onto the end of the given list
"""

nums = [1, 2, 3, 4, 5]
nums.append(99)  # adds 99 to the end
print(nums)
# the output would be [1,2,3,4,5,99]


# - Slicing -
"""
    It's also useful to know that Python uses the following syntax: [:] to return a copy of some portion of the list, constrained by specified indices. This is called slicing and it can be useful if you want to:

        1. Use a copy of the list so you don't have to change the original
        2. Only use a portion of a list.
    
    The starting index and ending index should be separated by the : character.
"""
# index =   0       1       2       3      4
words = ["start", "going", "till", "the", "end"]

words = ["start", "going", "till", "the", "end"]
# Sub-ranges (portions) of the list
print(words[1:])  # prints ['going', 'till', 'the', 'end']
print(words[:4])  # prints ['start', 'going', 'till', 'the']
print(words[2:4])  # prints ['till', 'the']

# Making a copy of a list
copy_of_words = words[0:]
copy_of_words.append("dojo")  # only appends to the copy
print(copy_of_words)  # prints ['start', 'going', 'till', 'the', 'end', 'dojo']
print(words)  # prints ['start', 'going', 'till', 'the', 'end']


# --------------------------------------------------------------------

# - BUILT-IN FUNCTIONS FOR LIST -

# - Built-in python functions for sequences
# The following functions can also be applied to all sequence types, including dictionaries, strings and tuples

my_list = [1, 'Zen', 'hi']
print(len(my_list))
# output 3

"""
    EXAMPLES OF FUNCTION LIST 
    len(sequence) returns the length (number of items) in a sequence.
    max(sequence) returns the highest value in a sequence.
    min(sequence) returns the lowest value in a sequence.
    sorted(sequence) returns a sorted sequence

refer to build in functions on python folder
"""

# - List-Specific Methods
"""
    In order to use a built-in list method, 
    you use dot-notation with an existing list, like so:
"""

my_list = [1, 5, 2, 8, 4]
my_list.pop()
print(my_list)
# output:
# [1,5,2,8]


# - The following are some commonly used list methods:

"""
list.append(value) appends a value to the end of the list.
list.pop(index) remove a value at given position. if no parameter is passed, it will remove the last value in the list.
list.index(value) returns the index (position) of the given value if it exists in the list and raises an error if it does not exist.
list.reverse() reverses the order of the elements, in place.*
list.sort() sorts the items in order of least to greatest, or alphabetically for strings, in place.*
"""


# --------------------------------------------------------------------

# - TUPLES -
"""
    Immutable list (they cannot be changed)
        -indexed starting at 0
        -Built in methods 
        -Defined with parenthesis ()
        -can store any data we want inside
        -Length is fixed
            -cant add or take away
"""
# Creating a tuple is as simple as declaring different comma-separated values.
# Optionally you can put these values between parentheses.
# example:

tuple_data = ('physics', 'chemistry', 1997, 2000)
tuple_num = (1, 2, 3, 4, 5)
tuple_letters = "a", "b", "c", "d"


# --------------------------------------------------------------------

# - CONDITIONALS -

"""
Conditional statements allow us to run certain lines of code depending on whether certain conditions are met.  
These statements control the flow of how our code is executed by the interpreter. 
In Python, the keywords for conditional statements are if, elif, and else.
"""

x = 12
if x > 50:
    print("bigger than 50")
else:
    print("smaller than 50")
# because x is not greater than 50, the second print statement is the only one that will execute

x = 55
if x > 10:
    print("bigger than 10")
elif x > 50:
    print("bigger than 50")
else:
    print("smaller than 10")
# even though x is greater than 10 and 50, the first true statement is the only one that will execute, so we will only see 'bigger than 10'

if x < 10:
    print("smaller than 10")
# nothing happens, because the statement is false

# !!! See Comparison and Logic Operators picture on file !!!


# --------------------------------------------------------------------

# - LOOPS -


# only one argument
range(5)  # this will loop start at 0 it will stop at 5
#output: [0 , 1, 2, 3, 4]

# two arguments
range(5, 10)  # this will loop start at 5 and will stop at 10
#output: [5,6, 7, 8, 9]

range(5, 10, 2)  # this will loop start at 5, stop at 10, and increment by 2
#output: [5,7,9]

# example using i :
for i in range(50):
    print(i)  # output: [0 all the way to 49]


for x in range(0, 10, 2):
    print(x)
# output: 0, 2, 4, 6, 8

# decrement a loop
for x in range(5, 1, -3):
    print(x)
# output: 5, 2

# --------------------------------------------------------------------

# - LOOPING OVER LISTS AND STRINGS -

# for loops through strings
    # Since a loop can be used on any sequence,
    # you can access each value of a string individual with loop.

for x in 'Hello':
    print(x)
# output: 'H', 'e', 'l', 'l', 'o'


# for loops through list
"""
If we want to iterate through a list, we could use the range function and send 
in the length of the list as the stopping value, but if we are not interested 
in the index values and want to just see the values of each item in the list in 
order, we can actually loop to get the values of the list directly!
"""

# logs with index values
my_list = ["abc", 123, "xyz"]
for i in range(0, len(my_list)):
    print(i, my_list[i])
# output: 0 abc, 1 123, 2 xyz

# OR

# logs without index values
for v in my_list:
    print(v)
# output: abc, 123, xyz


# - While Loops -
    # While loops are another way of looping while a certain condition is true

for count in range(0, 5):
    print("looping =", count)

# we can rewrite it as a while loop

count = 0
while count <= 5:
    print("looping - ", count)
    count += 1

# basic syntax for a while loop:
# while <expression>:
    # do something, including progress towards making the expression False.
    # Otherwise we'll never get out of here!


# - Else -

"""
There are certain conditions that we give for every loop that we have, but what 
if the condition was not met and we still would like to do something if that 
happens? We can then use an else statement with our while loop.
"""

y = 3
while y > 0:
    print(y)
    y = y - 1
else:
    print("Final else statement")


# - Loop Control -

"""
Loops, breaks, and continues are all a part of control flow as well. 
Control flow is the cornerstone of most programming languages.
"""

# - Break -

"""
The break statement exits the current loop prematurely, resuming execution 
at the first post-loop statement. The break statement can be used in both while 
and for loops.
"""

for val in "string":
    if val == "i":
        break
    print(val)
# output: s, t, r

# when the loop entered "i" it stopped looping


# - Continue -

"""
The continue statement immediately returns control to the beginning of the loop. 
In other words, the continue statement rejects, or skips, all the remaining 
statements in the current iteration of the loop, and continues normal execution 
at the top of the loop
"""

for val in "string":
    if val == "i":
        continue
    print(val)
# output: s, t, r, n, g
# notice, no i in the output, but the loop continued after the i


y = 3
while y > 0:
    print(y)
    y = y - 1
    if y == 0:
        break
else:		# only executes on a clean exit from the while loop (i.e. not a break)
    print("Final else statement")
# output: 3, 2, 1

# --------------------------------------------------------------------

# - FUNCTIONS -
"""
    - a block of code tpo run at any point in the program
    - canbe defined and called anywhere in the file
    - takes in parameters
    - you give it arguments 
    - arguments become the parameters when you call or invoke the function
"""

"""
A function is a named block of code that we can execute to perform a specific task.
More simply, a function is a list of instructions that we can run at any time and as many times as we would like. 
If we find something that we seem to be using over and over again, it might be best to have a way to streamline the process. 
A function:

- has a name
- takes in parameters (parenthesis required, parameters optional)
- perform a series of instructions
- return something afterwards (will return None if there is no explicit return statement)
"""

# - Syntax -

"""
The def keyword signifies the declaration of a function. This indicates that 
the following code is a function and assigns a name to that function, so we can 
call it later. Parameters are inputs the function is expecting and appear inside 
the parenthesis that follow the function name.

ex. 

def add(a,b):	# function name: 'add', parameters: a and b
    x = a + b	# process
    return x	# return value: x

We have declared a function with the def keyword, named it add, and specified 
that it takes two inputs (parameters). If this is all we have in our file, 
nothing would actually appear to happen if we ran it. To actually run the 
function, we must execute it by invoking or calling it. This is done outside of 
the function using the function name followed by (). Inside the parenthesis are 
any values (arguments) the function is expecting as input.

new_val = add(3, 5)    # calling the add function, with arguments 3 and 5
print(new_val)    # the result of the add function gets sent back to and 
saved into new_val, so we will see 8
"""


# - Parameters and Arguments -

# we define functuons using parameter, functions can have as many parameters as we need


# here we defined say_hi with on parameter called "name"
def say_hi(name):
    print("Hi, " + name)


say_hi('Michael')
say_hi('Anna')
say_hi('Eli')


# - Returing Values -

# a function call is equal to whatever that function returns


def say_hi(name):
    return "Hi " + name


greeting = say_hi('Michael')
# the returned value from say_hi function gets assigned t the 'greeting' varriable
print(greeting)  # this will output 'Hi micheal'

# returning a value from a function allows us to store value in a variable
# above example we invoked the say_hi function with "Michael" and se it to the greeting variable
# we print greeting we that it contains the returned value of the say_hi function


def add(a, b):
    x = a + b
    return x


sum1 = add(4, 6)
sum2 = add(1, 4)
sum3 = sum1 + sum2

# -Default Parameters & Named Arguements


def be_cheerful(name="Mr. Nibbles", repeat=2):
    print(f"good morning {name}\n" * repeat)  # \n means new line


be_cheerful("Bernard")
be_cheerful()
be_cheerful(repeat=4, name="Benny Bob")


# set defaults when declaring the parameters
def be_cheerful(name='', repeat=2):
    print(f"good morning {name}\n" * repeat)


be_cheerful()  # output: good morning (repeated on 2 lines)
be_cheerful("tim")  # output: good morning tim (repeated on 2 lines)
be_cheerful(name="john")  # output: good morning john (repeated on 2 lines)
be_cheerful(repeat=6)  # output: good morning (repeated on 6 lines)
# output: good morning michael (repeated on 5 lines)
be_cheerful(name="michael", repeat=5)
# NOTE: argument order doesn't matter if we are explicit when sending in our arguments!
# output: good morning kb (repeated on 3 lines)
be_cheerful(repeat=3, name="kb")
