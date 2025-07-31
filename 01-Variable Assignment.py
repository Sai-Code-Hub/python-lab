# Variable Assignment and Dynamic Typing
#<<<<<<<<<<<<<------------------------------------------>>>>>>

# Rules for variable names
# names can not start with a number
# names can not contain spaces, use _ instead
# names can not contain any of these symbols:
# :'",<>/?|\!@#%^&*~-+
# it's considered best practice (PEP8) that names are lowercase with underscores
# avoid using Python built-in keywords like list and str
# avoid using the single characters l (lowercase letter el), O (uppercase letter oh) and I (uppercase letter eye) as they can be confused with 1 and 0



my_dogs = 2
print(my_dogs)

my_dogs = ['Sammy', 'Frankie']
print(my_dogs)

# Assigning Variables
a = 5
print(a)

a = 10
print(a)

print(a + a)

a = a + 10
print(a)

# Reassignment Shortcuts
a += 10
print(a)

a *= 2
print(a)

# Variable Type Checking
print(type(a))

a1=30.1
a= (1, 2)
print(type(a1))
print(type(a))
# Simple Exercise
my_income = 100
tax_rate = 0.1
my_taxes = my_income * tax_rate
print(my_taxes)