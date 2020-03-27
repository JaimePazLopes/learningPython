
def createCubes(size):
    result = []
    for number in range(size):
        result.append(number**3)
    return result

def yieldCubes(size):
    for number in range(size):
        yield number**3

print(createCubes(3))
for number in createCubes(3):
    print(number)

print(yieldCubes(3))
for number in yieldCubes(3):
    print(number)
print(list(yieldCubes(3)))
print()

def generateFibonati(size):
    a = b = 1
    # result = []
    for _ in range(size):
        # result.append(a)
        yield a
        a, b = b, a + b
    # return result
for number in generateFibonati(10):
    print(number)
print()

def simpleGenerator():
    for number in range(5):
        yield number
for number in simpleGenerator():
    print(number)
generator = simpleGenerator()
print(generator)
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print()

message = "Hello!!"
for char in message:
    print(char)
stringIterator = iter(message)
print(stringIterator)
print(next(stringIterator))
print(next(stringIterator))
print(next(stringIterator))
print(next(stringIterator))
print(next(stringIterator))
print(next(stringIterator))






