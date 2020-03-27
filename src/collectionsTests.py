from collections import Counter
from collections import defaultdict
from collections import OrderedDict
from collections import namedtuple

listOfNumber = [1,1,2,21,21,3,3,4,43,3,5,56,6,4,45,3,4,4,56,7,5,6,5,6,8,5,9,4,8,9,4,9,7,8,8,77,7,6,5,66,2,6]
message = "njndfvshiduyhs8g76ds97fbhfapfioshdguiasdoihfsdhgpjsdhgjkshddjfhjfhf"
sentence = "qwert banana banana nana hello hi code hello banana anana qwert dog"
print(Counter(listOfNumber))
print(Counter(message))
print(Counter(sentence))
words = sentence.split()
wordsCounter = Counter(words)
print(wordsCounter)
print(wordsCounter.most_common(3))
print(wordsCounter.most_common()[:-3-1:-1])
for item in wordsCounter:
    print(item)
for item in wordsCounter.items():
    print(item)
print()

dict = defaultdict(lambda: "empty")
print(dict[0])
print(dict[1])
print(dict[2])
print(dict)
print()

normalDict = {}
normalDict["zero"] = 0
normalDict["one"] = 1
normalDict["two"] = 2
normalDict["three"] = 3
normalDict["four"] = 4
normalDict["five"] = 5
print(normalDict)
for key, value in normalDict.items():
    print(key, value)
orderedDict = OrderedDict()
orderedDict["zero"] = 0
orderedDict["one"] = 1
orderedDict["two"] = 2
orderedDict["three"] = 3
orderedDict["four"] = 4
orderedDict["five"] = 5
print(orderedDict)
for key, value in orderedDict.items():
    print(key, value)
dictA = {}
dictA['a'] = 1
dictA['b'] = 2
dictB = {}
dictB['b'] = 2
dictB['a'] = 1
print(dictA, dictB, dictA == dictB)
dictA = OrderedDict()
dictA['a'] = 1
dictA['b'] = 2
dictB = OrderedDict()
dictB['b'] = 2
dictB['a'] = 1
print(dictA, dictB, dictA == dictB)
print()

Person = namedtuple('Person', "name age city job kids")
sam = Person(name = "Samuel", age = 31, city = "New York", job = "Writer", kids = 3)
print(sam)
print(sam.name, sam.kids)


