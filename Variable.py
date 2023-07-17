# variable is a named location in the computer's memory where data can be stored.
# It acts as a container to hold a value or reference to an object. 
# Variables are an essential concept in Python and are used extensively in all kinds of programs.
    #    Variable Assignment:
# To assign a value to a variable, use the assignment operator =. 

        #  syntax is:

    #  variable_name = value
x = 10
print(x)

y = 3
z = x + y
# the above shows that variable maybe add
print(z)

# Variable Names:

# A variable name must start with a letter (a-z, A-Z) or an underscore (_).
# It can be followed by letters, digits (0-9), or underscores.
# Variable names are case-sensitive, meaning name and Name are different variables.
# Avoid using Python reserved keywords like if, for, while, etc., as variable names.
# Dynamic Typing:

d = 5  
d = "this is for a string"

# Type() Function:
# You can check the type of a variable using the type() function:
t = 6
print(type(t))
# output is class 'int'
# This line of code likely printed the type of a variable that holds an integer value. 
# The output <class 'int'> indicates that the variable's type is an integer.

r = True
print(type(r))
# output is class 'bool'
# <class 'bool'>
# This line of code likely printed the type of a variable that holds a boolean value (True or False).
# The output <class 'bool'> indicates that the variable's type is a boolean.

Name = "Mobisa frankline"
print(type(Name))
# output is class 'str
# class 'str'>
# This line of code likely printed the type of a variable that holds a string value.
# The output <class 'str'> indicates that the variable's type is a string.
# The format <class 'type'> indicates that the type of the variable is 'type'. 

# Multiple Assignments:
# You can assign multiple variables in a single line using commas:

a, b, c = 1, 2, 3
print(b)

# output is 2

# Swapping Variables:
# Python allows you to swap the values of two variables without using a temporary variable:
f_name = "Frankline"
l_name = "Mobisa"
# the code below is for swapping
f_name , l_name = l_name , f_name