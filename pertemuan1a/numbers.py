#ex number python
x = 5    # int
y = 3.5  # float
z = 1j   # complex

#ex2
print(type(x))
print(type(y))
print(type(z))

#ex3
x = 5
y = 45666778211
z = -3222456

print(type(x))
print(type(y))
print(type(z))

#ex4
x = 3.20
y = 2.0
z = -40.30

print(type(x))
print(type(y))
print(type(z))

#ex5
x = 35e3
y = 12E4
z = -87.7e100

print(type(x))
print(type(y))
print(type(z))

#ex6
x = 2+4j
y = 4j
z = -4j

print(type(x))
print(type(y))
print(type(z))

#ex7
x = 1    # int
y = 2.8  # float
z = 1j   # complex

#convert from int to float:
a = float(x)

#convert from float to int:
b = int(y)

#convert from int to complex:
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))

#ex8
import random

print(random.randrange(1, 10))