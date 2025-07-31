# String Formatting
# #<<-------------------->>#
# String formatting lets you inject items into a string rather than trying to chain items together using commas or string concatenation.
# .foramt(), f-strings
from distutils.dep_util import newer

from setuptools.build_meta import get_requires_for_build_wheel

player = 'Thomas'
points = 33
print("Last night, %s scored %d points." %(player, points))

print('this is a string {}'.format('INSERTED'))

print('The {} {} {}'.format('fox','brown','quick'))

print('The {2} {1} {0}'.format('fox','brown','quick'))
print('The {0} {0} {0}'.format('fox','brown','quick'))
print('The {f} {b} {q}'.format(f='fox',b='brown',q='quick'))

#Float formatting follows "{value:width.precision f}"
result = 100/777
print(result)
print(type(result))
print("The result was {r}".format(r=result))
print("The result was {r:1.3f}".format(r=result))
#print("The result was {r:5.3f}".format(r=result))

result = 104.12345
print(result)
print(type(result))
print("The result was {r:1.3f}".format(r=result))

#Formatted String Literals (f-strings)

name = "Jose"
print(name)
print('Hello ,his name is {}'.format(name)) #.foramt() Method
print(f'Hello ,his name is {name}') #f-strings Method

name = 'Fred'
print(f"He said his name is {name}.")
#pass !r to get the string representation
print(f'He said his name is {name!r}.')

# Concatenation vs String Formatting
player = 'Thomas'
points = 33
print('Last night, ' + player + ' scored ' + str(points) + ' points.')
print(f'Last night, {player} scored {points} points.')

# Formatting with % placeholders
print("I'm going to inject %s here." % 'something')
print("I'm going to inject %s text here, and %s text here." % ('some', 'more'))
x, y = 'some', 'more'
print("I'm going to inject %s text here, and %s text here." % (x, y))

# %s vs %r conversion
print('He said his name was %s.' % 'Fred')
print('He said his name was %r.' % 'Fred')
print('I once caught a fish %s.' % 'this \tbig')
print('I once caught a fish %r.' % 'this \tbig')

# %s vs %d conversion with numbers
print('I wrote %s programs today.' % 3.75)
print('I wrote %d programs today.' % 3.75)

# Padding and Precision of Floating Point Numbers
print('Floating point numbers: %5.2f' % (13.144))
print('Floating point numbers: %1.0f' % (13.144))
print('Floating point numbers: %1.5f' % (13.144))
print('Floating point numbers: %10.2f' % (13.144))
print('Floating point numbers: %25.2f' % (13.144))

# Multiple formatting types
print('First: %s, Second: %5.2f, Third: %r' % ('hi!', 3.1415, 'bye!'))

# .format() method usage
print('This is a string with an {}'.format('insert'))
print('The {2} {1} {0}'.format('fox', 'brown', 'quick'))
print('First Object: {a}, Second Object: {b}, Third Object: {c}'.format(a=1, b='Two', c=12.3))
print('A {p} saved is a {p} earned.'.format(p='penny'))

# Alignment, padding and float precision with .format()
print('{0:8}  {1:9}'.format('Fruit', 'Quantity'))
print('{0:8}  {1:9}'.format('Apples', 3.))
print('{0:8}  {1:9}'.format('Oranges', 10))
print('{0:<8}  {1:^8}  {2:>8}'.format('Left', 'Center', 'Right'))
print('{0:<8}  {1:^8}  {2:>8}'.format(11, 22, 33))
print('{0:=<8}  {1:-8}  {2:.>8}'.format(11, 22, 33))

# Comparing % formatting and .format()
print('This is my ten-character, two-decimal number:%10.2f' % 13.579)
print('This is my ten-character, two-decimal number:{0:10.2f}'.format(13.579))

# f-strings examples
name = 'Fred'
print(f"He said his name is {name}.")
print(f"He said his name is {name!r}")

# Float formatting with f-strings
num = 23.45678
print("My 10 character, four decimal number is:{0:10.4f}".format(num))
print(f"My 10 character, four decimal number is:{num:{10}.{6}}")

num = 23.45
print("My 10 character, four decimal number is:{0:10.4f}".format(num))
print(f"My 10 character, four decimal number is:{num:{10}.{6}}")

# f-string using .format-style inside f-string
print(f"My 10 character, four decimal number is:{num:10.4f}")

name = "Sam"
age = 35
print(f"My name is {name!r}, and my age is {age}.")
print("My name is {!r}, and my age is {}.".format(name, age))

x = "few"
y= "new"
print("I have %s friends here and want to make %s ones." %(x,y))


value = 123.456789
print(f"Formatted value: {value:.2f}")

value = 123.4
print(f"Total padded: {value:1.2f}")

#Center, Left, Right Alignmen
text = "Python"
print(f"|{text:<10}|")  # Left
print(f"|{text:^10}|")  # Center
print(f"|{text:>10}|")  # Right

#exp:2
text1 = "Sai"
text2 = "Krishna"
text3 = "Kosuri"
print(f"|{text1:<10}|")  # Left
print(f"|{text2:^10}|")  # Center
print(f"|{text3:>10}|")  # Right

#Integers with Zero Padding
num = 42
print(f"|{num:<10}|")
print(f"ID: {num:05}")

name = "Saikrishna"
score = 98
print(f"Student: {name}, Score: {score}/100")


num = 13.144

print('Floating point numbers: %5.2f' % num)      # Width: 5, Precision: 2 → '13.14'
print('Floating point numbers: %1.0f' % num)      # Width: 1, Precision: 0 → '13'
print('Floating point numbers: %1.5f' % num)      # Width: 1, Precision: 5 → '13.14400'
print('Floating point numbers: %10.2f' % num)     # Width: 10, Precision: 2 → '      13.14'
print('Floating point numbers: %25.2f' % num)     # Width: 25, Precision: 2 → '                   13.14'

print('Floating point numbers: %5.2f' %(13.144))

# Using .format() to align text with fixed width
print('{0:8} | {1:9}'.format('Fruit', 'Quantity'))
print('{0:8} | {1:1}'.format('Apples', 3.0))
print('{0:8} | {1:1}'.format('Oranges', 10))


print('{0:=<8} | {1:-^8} | {2:.>8}'.format('Left','Center','Right'))
print('{0:=<8} | {1:-^8} | {2:.>8}'.format(11,22,33))