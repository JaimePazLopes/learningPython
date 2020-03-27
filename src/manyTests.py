print("Grocery list: \n\t{}, \n\t{}, \n\t{}".format('banana', 'house', "pickles"))
print()
print("Cities list: \n\t{2}, \n\t{0}, \n\t{1}".format('New York', 'France', "Africa"))
print()
print("Movies list: \n\t{a}, \n\t{c}, \n\t{b}".format(a='IT', b='Star Trek Piccard', c="Ugly Betty"))
print()
print("Float printing: {value:1.5}".format(value=10/3))
print()
person1, person2, person3 = 'Di Caprio', "Pitt", 'Kleber'
print(f"Friends list: \n"
      f"\t{person1},\n"
      f"\t{person2},\n"
      f"\t{person3}")
print()
car1, car2, car3 = "Enterprise", 'Mustang', "Red October"
print(f"""Car list:
    {car1},
    {car2},
    {car3}""")
print()

listInt = [2, 5, 3, 76, 32, -9, -2324, 445, 0, 0, 0, 23, 4, 2]
listInt.sort()
print(listInt)
listInt = ['', "0123", "~~~~~~", "banana", "a", "zzz", "A", "a", "666", " "]
listInt.sort()
print(listInt)
listInt.reverse()
print(listInt)
print()

listInt = [5, 1, 0, 2, 1, -1, 1, 3, 2, 0]
print(listInt)
listToSet = set(listInt)
print(listToSet)
print()

for _ in listInt:
      print("Cool feature")

tupleList = [(2, "banana"), (3, "Man"), (1,"TV")]
for number, object in tupleList:
      print(f"There is {number} {object} in this room")

generatedList1 = list(range(10))
print(generatedList1)
generatedList2 = list(range(-1,7))
print(generatedList2)
generatedList3 = list(range(0,101,10))
print(generatedList3)
generatedList4 = list(range(0,-33,-4))
print(generatedList4)

randomWord = "upbuilding"
for item in enumerate(randomWord):
      print(item)
for index,letter in enumerate(randomWord):
      print(f"{index}: {letter}")

zip1 = [1,2,3,4]
zip2 = ["a", "b", "c", "d", "e", "f"]
zip3 = ["*", "/", "-", "+", "="]
for item in zip(zip1, zip2):
      print(item)
for one, two in zip(zip2, zip3):
      print(one + two)
for item in zip(zip1, zip2, zip3):
      print(item)
zipList = zip(zip1, zip3)
for item in zipList:
      print(item)

minMaxIn = list(range(20))
print(max(minMaxIn))
print(min(minMaxIn))
print(3 in minMaxIn)
print(20 in minMaxIn)

from random import shuffle
shuffle(minMaxIn)
print(minMaxIn)
from random import randint
randomInt = randint(0,30)
print(randomInt, randomInt in minMaxIn)

stringToList = [letter for letter in "Oslo, Kiev, Quito"]
print(stringToList)
squareList = [number ** 0.5 for number in range(0,100,4)]
print(squareList)
numberList = list(range(-10,11))
shuffle(numberList)
negativeList = [number for number in numberList if number < 0]
print(negativeList)
negativeList = [number if number < 0 else number * -1.0 for number in numberList]
print(negativeList)

soccerTeam = ["New York City FC", "Tigres", "Manchester City"]
games = [club1 + " vs " + club2 for club1 in soccerTeam for club2 in soccerTeam if club1 != club2]
print(games)
print()

insertList = ["lemur", "ground hog", "otter"]
help(insertList.insert)
insertList.insert(1, "capybara")
print(insertList)
print()


def testHelp():
      '''
      This function is just a help test
      :return:
      '''
      pass
help(testHelp)
print()


def favoriteColor(color="Black"):
    print(f"My favorite Power Ranger is {color}")
favoriteColor()
favoriteColor("Green")
print()

# pig latin
sentence = "The quick brown fox jumps over the lazy dog"
newSentence = ""
for word in sentence.lower().split():
      if word[0] in "aeiou":
            newSentence += word + "ay"
      else:
            newSentence += word[1:] + word[0] + "ay"
      newSentence += " "
newSentence = newSentence[0].title() + newSentence[1:]
print(sentence)
print(newSentence)
print()

def sumAll(*args):
      print(sum(args))
sumAll(1)
sumAll(10,8)
sumAll(1,2,3,4,5,-4,40)
print()

def lookForCountry(**kwargs):
      if 'country' in kwargs:
            print(f"The country is {kwargs['country']}")
      else:
            print("There is no country here")
lookForCountry(fruit = 'banana', person = 'Pope', musician = "Paul")
lookForCountry(fruit = 'banana', person = 'Pope', country = 'Panama', musician = "Paul")
print()

integer = 1024
binary = bin(integer)
hexadecimal = hex(integer)
print(integer, binary, hexadecimal, "\n")

print(f"5.23222 rounded to two decimal places is: {round(5.23222, 2)}\n")

s = 'hello how are you Mary, are you feeling okay?'
print(s.islower())
s = 'hello how are you mary, are you feeling okay?'
print(s.islower())
s = 'twywywtwywbwhsjhwuwshshwuwwwjdjdid'
print(s.count('w'))
print()

set1 = {2,3,1,5,6,8}
set2 = {3,1,7,5,6,8}
uniqueSet1 = set1 - set2
print(uniqueSet1)
print(set1.intersection(set2))
print()

# {0: 0, 1: 1, 2: 8, 3: 27, 4: 64}
dictCube = {value: value**3 for value in range(5)}
print(dictCube)
print()

list1 = [1,2,3,4]
list1.reverse()
print(list1)
list2 = [3,4,2,5,1]
list2.sort()
print(list2)




