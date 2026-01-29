#ex python variables
x = 3
y = "Ain"
print(x)
print(y)

#ex2
x = 4      # x is of type int
x = "Deny" # x is now of type str
print(x)

#ex3
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0

#ex4
x = 3
y = "Ain"
print(type(x))
print(type(y))

#ex5
x = "Ain"
# is the same as
x = 'Ain'

#ex6
b = 4
B = "Deny"
#B will not overwrite b

#ex variables names
myvar = "Ain"
my_var = "Ain"
_my_var = "Ain"
myVar = "Ain"
MYVAR = "Ain"
myvar2 = "Ain"

#ex2
myVariableName = "Ain"
MyVariableName = "Ain"
my_variable_name = "Ain"

#ex assign multiple values
x, y, z = "Grape", "Apple", "Lemon"
print(x)
print(y)
print(z)

#ex2
x = y = z = "Apple"
print(x)
print(y)
print(z)

#ex3
fruits = ["Grape", "Apple", "Lemon"]
x, y, z = fruits
print(x)
print(y)
print(z)

#ex output variabel
x = "Learning python is fun"
print(x)

#ex2
x = "Learning"
y = "Python"
z = "is fun"
print(x, y, z)

#ex3
x = "Learning"
y = "Python"
z = "is fun"
print("x + y + z")

#ex4
x = 3
y = 5
print(x + y)

#ex5
X = 3
y = "Dani"
print(x, y)

#ex global variable
x = "fun"

def myfunc():
    print("Coding is" + x)

myfunc()

#ex2
x = "fun"

def myfunc():
  x = "amazing"
  print("Coding is " + x)

myfunc()

print("Coding is " + x)

#ex3
def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)

#ex4
x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)

#ex variable exercises
x = 20
y = 5
z = 3
print(x + y + z)