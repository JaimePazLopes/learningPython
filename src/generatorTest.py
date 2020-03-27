import random

def generateSquare(size):
    for index in range(size):
        yield index**2
print(generateSquare(5))
for number in generateSquare(5):
    print(number)
print()

def randomNumber(low, high, size):
    for index in range(size):
        yield random.randint(low, high)
for number in randomNumber(4,10,7):
    print(number)
print()

message = "Hello"
iterMessage = iter(message)
for char in iterMessage:
    print(char)

def tooMuchForAFunction():
    for index in range(100): # range(100000):
        yield index**index
for number in tooMuchForAFunction():
    print(number)
print()

my_list = [1,2,3,4,5]
gencomp = (item for item in my_list if item > 3)
#print(list(gencomp))
for item in gencomp:
    print(item)
print(gencomp)

gencomp = [item for item in my_list if item > 3]
print(gencomp)
for item in gencomp:
    print(item)
