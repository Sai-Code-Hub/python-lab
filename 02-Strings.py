#Strings
#--------------#
'''
Strings are used in Python to record text information, such as names. Strings in Python are actually a sequence,
which basically means Python keeps track of every element in the string as a sequence.
For example, Python understands the string "hello' to be a sequence of letters in a specific order.
This means we will be able to use indexing to grab particular letters (like the first letter, or the last letter).
This idea of a sequence is an important one in Python and we will touch upon it later on in the future.
In this lecture we'll learn about the following:

1.) Creating Strings
2.) Printing Strings
3.) String Indexing and Slicing
4.) String Properties
5.) String Methods
6.) Print Formatting '''

# Creating strings
print('hello')
print("This is also a string")
print("String built with double quotes")
print('Hello /n World')
print('Hello /tWorld')

print(len("5"))

# Handling quotes inside strings
print("Now I'm ready to use the single quotes inside a string!")

# Indexing and Slicing
'''<----------------------------->'''
s = 'Hello World'
print(s[0])      # First letter: 'H'
print(s[1:])     # From index 1 onward: 'ello World'
print(s[:3])     # Up to index 3 (excluding): 'Hel'
print(s[-1])     # Last character: 'd'
print(s[:-1])    # Everything except last: 'Hello Worl', reverse Indexing
print(s[::2])    # Every second character: 'HloWrd'
print(s[::-1])   # Reversed string: 'dlroW olleH'

#string Immutability Example
'''<------------------------------->'''
s = 'Hello World'
# s[0] = 'x'  # ❌ This causes an error
# So instead, we create a new string
s = 'x' + s[1:]
print(s)        # Output: 'xello World'

#Concatination & Repetition
s = 'Hello'
s = s + ' World'
print(s)        # Output: 'Hello World'

letter = 'z'
print(letter * 10)  # Output: 'zzzzzzzzzz'

#String Methods
s = 'Hello World'
print(s.upper())         # 'HELLO WORLD'
print(s.lower())         # 'hello world'
print(len(s))            # 11
print(s.split())         # ['Hello', 'World']
print(s.split('W'))      # ['Hello ', 'orld']


#Print Formatting
print("Insert another string with curly brackets: {}".format("The inserted string"))

