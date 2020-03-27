def lesserEven(*args):
    lesserEven = biggerOdd = None
    for number in args:
        if type(number) is not int:
            continue
        if biggerOdd is None:
            if number % 2 == 1:
                biggerOdd = number
            elif lesserEven is None:
                lesserEven = number
            elif lesserEven > number:
                lesserEven = number
        else:
            if number % 2 == 1 and number > biggerOdd:
                biggerOdd = number
    if biggerOdd is None:
        return lesserEven
    else:
        return biggerOdd
print(lesserEven(2,4,6,8,40))
print(lesserEven(40,4,6,2,8,40))
print(lesserEven(35,7,900,-805))
print(lesserEven("banana",5.5,2,5,9,4,8))
print()

# Animal Cracker
def animalCracker(stringCheck):
    splitString = stringCheck.lower().split()
    if len(splitString) < 2:
        return False
    letter = splitString[0][0]
    for word in splitString[1:]:
        if letter != word[0]:
            return False
    return True
stringToCheck = ""
print(stringToCheck + " " + str(animalCracker(stringToCheck)))
stringToCheck = "Banana"
print(stringToCheck + " " + str(animalCracker(stringToCheck)))
stringToCheck = " b b b b       b"
print(stringToCheck + " " + str(animalCracker(stringToCheck)))
stringToCheck = "joystick jockey"
print(stringToCheck + " " + str(animalCracker(stringToCheck)))
stringToCheck = "pneumonia  password physical pony"
print(stringToCheck + " " + str(animalCracker(stringToCheck)))
stringToCheck = "liver frog landowner"
print(stringToCheck + " " + str(animalCracker(stringToCheck)))
print()

def makes20(*args):
    print(args)
    if 20 in args or sum(args) == 20:
        return True
    return False
print(f"Result {makes20(20,10)}")
print(f"Result {makes20(2,3)}")
print(f"Result {makes20(2,-3,5,-5,7,4,4)}")
print(f"Result {makes20(2,3,5,-5,7,4,4)}")
print()

def oldMacDonald(name):
    if len(name) < 4:
        return name + " is too short"
    return name[0].upper() + name[1:3] + name[3].upper() + name[4:]
def oldCapItalize(name):
    if len(name) < 4:
        return name + " is too short"
    return name[:3].capitalize() + name[3:].capitalize()
print(oldMacDonald('macdonald'))
print(oldMacDonald('ullu'))
print(oldMacDonald('ul'))
print(oldMacDonald('ullullllllllll'))
print(oldCapItalize('macdonald'))
print(oldCapItalize('ullu'))
print(oldCapItalize('ul'))
print(oldCapItalize('ullullllllllll'))
print()

def masterYoda(stringToWork):
    convertedString = ""
    splitedWords = stringToWork.lower().split()
    convertedString = " ".join(splitedWords[::-1]).capitalize()
    return  convertedString

print(masterYoda('I am home'))
print(masterYoda('We are ready'))
print()

def almostThere(number):
    return abs(number - 100) <= 10 or abs(number - 200) <= 10
print(almostThere(104))
print(almostThere(150))
print(almostThere(209))
print()

def has33(nums):
    if nums.count(3) < 2:
        return False
    indexCheck = 0
    while True:
        arrayPart = nums[indexCheck:]
        indexCheck = arrayPart.index(3)
        if arrayPart[indexCheck+1] == 3:
            return True
        indexCheck+=2
        if indexCheck >= len(arrayPart)-1:
            break
    return False
print(has33([1, 3, 3]))
print(has33([1, 3, 1, 3]))
print(has33([3, 1, 3]))
print(has33([2, 1, 5]))
print(has33([3, 1, 3, 3, 1, 3, 3]))
print()

def paperDoll(text):
    newText = ""
    for letter in text.lower():
        if letter in 'aeiou':
            newText += letter * 2
        elif letter in ' +=-_/*!/,.;:(){}[]\'"':
            newText += ' '
        elif letter in 'qwrtypsdfghjklçzxcvbnm':
            newText += letter*3
        else:
            newText += letter
    return newText.capitalize()
print(paperDoll('Hello'))
print(paperDoll('Mississippi'))
print(paperDoll('Mis!,#sis/*si     ppi'))
print()

def blackjack(card1, card2, card3):
    sumCards = card1 + card2 + card3
    if sumCards <= 21:
        return sumCards
    if 11 in [card1, card2, card3]:
        if sumCards - 10 <= 21:
            return sumCards - 10
    return "BUST"
print(blackjack(5,6,7))
print(blackjack(9,9,9))
print(blackjack(9,9,11))
print(blackjack(11,9,11))
print()

def summer69(numberList):
    sum69 = 0
    index69 = 0
    tempArgs = numberList
    while True:
        tempArgs = tempArgs[index69:]
        if not 6 in tempArgs:
            return sum69 + sum(tempArgs)
        index6 = tempArgs.index(6)
        sum69 += sum(tempArgs[:index6])
        if not 9 in tempArgs:
            return 'This sequence is missing a 9'
        index69 = tempArgs.index(9)+1
        if index69 >= len(tempArgs):
            return sum69

print(summer69([6, 9]))
print(summer69([1, 3, 5]))
print(summer69([4, 5, 6, 7, 8, 9]))
print(summer69([2, 1, 6, 9, 11]))
print(summer69([2, 1, 6, 11, 98]))
print(summer69([2, 1, 6, 9, 11, 4, 5, 6, 7, 8, 9, 1, 3, 5]))
print()

def spyGame(numberList):
    if 0 in numberList:
        subList = numberList[numberList.index(0)+1:]
        if 0 in subList:
            return 7 in subList[subList.index(0)+1:]
    return False
print(spyGame([1,2,4,0,0,7,5]))
print(spyGame([1,0,2,4,0,5,7]))
print(spyGame([1,7,2,0,4,5,0]))
print(spyGame([0]))
print()


def countPrimesVisual(num):
    countPrimes = 0
    dictOfNumbers = {i: True for i in list(range(num+1))}
    dictOfNumbers[0] = False
    dictOfNumbers[1] = False
    for index in range(0, num+1):
        if dictOfNumbers[index]:
            countPrimes += 1
            for indexB in range(index * 2, num + 1, index):
                dictOfNumbers[indexB] = False
    return countPrimes
def countPrimes(num):
    if num < 2:
        return 0
    primes = [2]
    x = 3
    while x <= num:
        for y in primes:
            if x%y == 0:
                break
        else:
            primes.append(x)
        x += 2
    return len(primes)

print(countPrimesVisual(100))
print(countPrimes(100))
print()

stringA ="""   *  
  * * 
 *****
 *   *
 *   *"""
stringE = """ *****
 *    
 *****
 *    
 *****"""
stringI = """ *****
   *  
   *  
   *  
 *****"""
stringO = """ *****
 *   *
 *   *
 *   *
 *****"""
stringU = """ *   *
 *   *
 *   *
 *   *
 *****"""

bigLetters = {"a": stringA, "e": stringE, "i": stringI, "o": stringO, "u": stringU}

def printBig(letters):
    stringToPrint = [' ']*5
    for letter in letters:
        splitLines = bigLetters[letter].split("\n")
        for lineNumber in range(len(stringToPrint)):
            stringToPrint[lineNumber] += splitLines[lineNumber]
    for line in stringToPrint:
        print(line)
printBig('aeiouaoai')
print()

def printBigAnswer(letter):
    patterns = {1:'  *  ',2:' * * ',3:'*   *',4:'*****',5:'**** ',6:'   * ',7:' *   ',8:'*   * ',9:'*    '}
    alphabet = {'A':[1,2,4,3,3],'B':[5,3,5,3,5],'C':[4,9,9,9,4],'D':[5,3,3,3,5],'E':[4,9,4,9,4]}
    for pattern in alphabet[letter.upper()]:
        print(patterns[pattern])
printBigAnswer("a")
