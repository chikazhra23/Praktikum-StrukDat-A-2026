#ex python boolean
print(8 > 5)
print(5 == 9)
print(8 < 5)

#ex2
x = 50
y = 20

if x > y:
  print("y is greater than x")
else:
  print("y is not greater than x")

#ex3
print(bool("Hello"))
print(bool(15))

#ex4
a = "Hello"
b = 15

print(bool(a))
print(bool(b))

#ex5
bool("abc")
bool(123)
bool(["apple", "grape", "lemon"])

#ex6
bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})

#ex7
class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj))

#ex8
def myFunction() :
  return True

print(myFunction())

#ex9
def myFunction() :
  return True

if myFunction():
  print("YES!")
else:
  print("NO!")

#ex10
x = 50
print(isinstance(x, int))
