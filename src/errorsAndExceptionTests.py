def addNumber(number1, number2):
    sumNumber = 0
    try:
        sumNumber = number1 + number2
    except TypeError:
        print("I need two numbers to add")
        sumNumber = "Invalid"
    except:
        print("Some unexpected error happened")
        sumNumber = "Invalid"
    else:
        print("I can sum this numbers")
    finally:
        print(f"The sum is: {sumNumber}")
        print()
    return sumNumber

addNumber(3,5)
addNumber(3,"banana")
print()

def typeInteger():
    integer = ""
    while True:
        try:
            integer = int(input("Type an integer: "))
        except ValueError:
            print("You didnt type and integer")
            continue
        except:
            print("An unexpected error happened")
            continue
        else:
            print("You type an integer")
            break
        finally:
            if type(integer) is int:
                print(f"Your integer is {integer} and my integer is {integer + 1}, so I won!!")

typeInteger()