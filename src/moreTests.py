def squareFunction(number):
    return number ** 2

numbersToSquare = [2, 3, 4.5, 6, 10]

for number in map(squareFunction, numbersToSquare):
    print(number)

listSquares = list(map(squareFunction, numbersToSquare))
print(listSquares)

def isEven(number):
    return number % 2 == 0
numbers = [1,2,3,4,5,6,7,8,9,10]
listEven = list(filter(isEven, numbers))
print(listEven)

for number in list(filter(isEven, numbers)):
    print(number)

square = lambda num: num ** 2
print(square(2))

for number in map(lambda num: num ** 2, numbersToSquare):
    print(number)
for number in list(filter(lambda num: num % 2 == 0, numbers)):
    print(number)

listString = ['string', "another", "last"]
for word in map(lambda word: word[::-1], listString):
    print(word)
