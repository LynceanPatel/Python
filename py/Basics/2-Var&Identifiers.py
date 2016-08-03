#2- Variable and operators
'''
A Python identifier is a name used to identify a variable, function,
class, module or other object. An identifier starts with a letter A to Z
or a to z or an underscore (_) followed by zero or more letters,
underscores and digits (0 to 9).

Python does not allow punctuation characters such as @, $, and % within
identifiers. Python is a case sensitive programming language. Thus,
Manpower and manpower are two different identifiers in Python.

Here are naming conventions for Python identifiers −

    *Class names start with an uppercase letter. All other identifiers start with a lowercase letter.

    *Starting an identifier with a single leading underscore indicates that the identifier is private.

    *Starting an identifier with two leading underscores indicates a strongly private identifier.

    *If the identifier also ends with two trailing underscores, the
    identifier is a language-defined special name.
'''

''' Python variables do not need explicit declaration to reserve memory
space. The declaration happens automatically when you assign a value to
a variable. The equal sign (=) is used to assign values to variables.
'''
#Assigning Values to Variables
name = 'Lyncean Patel'
age = 26
height = 5.7

print("Name:",name)
print("Age:", age)
print("Height:", height)

#Multiple Assignment
a=b=c=10
print("Output For Multiple Assignment",a,b,c)

# TO hold the result on command prompt
input("Press <<Enter>> to exit.")
