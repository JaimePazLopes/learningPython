import math
import string


def sphereVolume(radius):
    return 4/3 * math.pi * radius ** 3

print(sphereVolume(2))
print()

def checkRange(number, low, high):
    def isInRange(number, low, high):
        return number in range(low, high)
    if isInRange(number,low,high):
        print(f"{number} is in the range between {low} and {high}")
    else:
        print(f"{number} is not in the range between {low} and {high}")

checkRange(5,2,7)
checkRange(3,1,10)
checkRange(-3,-10,0)
checkRange(0,0,0)
checkRange(1,10,100)
print()

def countUpperLower(stringToCount):
    print(f"String: {stringToCount}")
    numberUpper = 0
    numberLower = 0

    for char in stringToCount:
        if char.islower():
            numberLower += 1
        elif char.isupper():
            numberUpper += 1

    print(f"Number of upper case: {numberUpper}")
    print(f"Number of lower case: {numberLower}")
countUpperLower("Hello Mr. Rogers, how are you this fine Tuesday?")
print()

def uniqueList(listToWork):
    return list(set(listToWork))
print(uniqueList([1,1,1,1,2,2,3,3,3,3,4,5]))
print(uniqueList([1,1,7,1,2,2,3,3,3,0,4,5]))
print()

def multiply(listToMultiply):
    multTotal = 1
    for number in listToMultiply:
        multTotal *= number
    return multTotal
print(multiply([1,2,3,-4]))

def isPalindrome(palindrome):
    palindrome = palindrome.replace(" ", "")
    return palindrome == palindrome[::-1]
palindromeString = "madam"
print(f"{palindromeString}: {isPalindrome(palindromeString)}")
palindromeString = "nurses run"
print(f"{palindromeString}: {isPalindrome(palindromeString)}")
palindromeString = "nurse run"
print(f"{palindromeString}: {isPalindrome(palindromeString)}")
print()

def isPangram(pangram):
    return set(string.ascii_lowercase) <= set(pangram.lower())
print(isPangram("The quick brown fox jumps over the lazy dog"))
print(isPangram("The quick brown fox jumps over the lay dog"))