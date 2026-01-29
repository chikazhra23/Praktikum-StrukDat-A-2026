#ex python strings
print("Fun")
print('Fun')

#ex2
print("It's alright")
print("She is called 'Jasmine'")
print('She is called "Jasmine"')

#ex3
a = "Fun"
print(a)

#ex4
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

#ex5
a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)

#ex slicing strings
b = "Hello, World!"
print(b[2:5])

#ex2
b = "Hello, World!"
print(b[:5])

#ex3
b = "Hello, World!"
print(b[2:])

#ex4
b = "Hello, World!"
print(b[-5:-2])

#ex modify strings
a = "Learning, is fun"
print(a.upper())

#ex2
a = "Hello, World!"
print(a.lower())

#ex3
a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"

#ex4
a = "Hello, World!"
print(a.replace("H", "J"))

#ex5
a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']

#ex concatenate strings
a = "Jasmine"
b = "Beautiful"
c = a + b
print(c)

#ex2
a = "Jasmine"
b = "Beautiful"
c = a + " " + b
print(c)

#ex format strings
age = 20
txt = f"My name is Jasmine, I am {age}"
print(txt)

#ex4
price = 59
txt = f"The price is {price} dollars"
print(txt)

#ex5
price = 59
txt = f"The price is {price:.2f} dollars"
print(txt)

#ex6
txt = f"The price is {20 * 59} dollars"
print(txt)

#ex escape characters
txt = "We are the so-called \"Vikings\" from the north."

#ex string methods
txt = "Learning Python"
print(txt.lower())
