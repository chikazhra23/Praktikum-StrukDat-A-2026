print(10 + 5)

sum1 = 100 + 50      # 150 (100 + 50)
sum2 = sum1 + 250    # 400 (150 + 250)
sum3 = sum2 + sum2   # 800 (400 + 400)


x = 15
y = 4

print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(x % y)
print(x ** y)
print(x // y)

#Division always returns a float
x = 12
y = 5

print(x / y)

#It rounds DOWN to the nearest integer:

x = 12
y = 5

print(x // y)

#Assignment Operators
numbers = [1, 2, 3, 4, 5]

if (count := len(numbers)) > 3:
    print(f"List has {count} elements")

#Comparison Operators
x = 5
y = 3

print(x == y)
print(x != y)
print(x > y)
print(x < y)
print(x >= y)
print(x <= y)

#Chaining Comparison Operators
x = 5

print(x > 0 and x < 10)

#Logical Operators
x = 5

print(x < 5 or x > 10)

#Reverse the result with not
x = 5

print(not(x > 3 and x < 10))

#Identity Operators
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is z)
print(x is y)
print(x == y)

#Operator is notakan mengembalikan nilai Truejika kedua variabel tidak menunjuk ke objek yang sama
x = ["apple", "banana"]
y = ["apple", "banana"]

print(x is not y)

#Perbedaan Antara isdan==
x = [1, 2, 3]
y = [1, 2, 3]

print(x == y)
print(x is y)

#Membership Operators
fruits = ["apple", "banana", "cherry"]

print("banana" in fruits)

#perksa jika pineapple tidak didalam list
fruits = ["apple", "banana", "cherry"]

print("pineapple" not in fruits)

#Membership in Strings
text = "Hello World"

print("H" in text)
print("hello" in text)
print("z" not in text)

#Bitwise Operators
print(6 & 3)

print(6 | 3)

print(6 ^ 3)


#Operator Precedence
print((6 + 3) - (6 + 3))

print(100 + 5 * 3)

print(5 + 4 - 7 + 3)