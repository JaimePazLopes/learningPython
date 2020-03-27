try:
    for i in ['a','b','c']:
        print(i**2)
except TypeError:
    print("You cant do pow operation with strings")
print()

x = 5
y = 0
try:
    z = x/y
except ZeroDivisionError:
    print("You are executing a division by zero.")
    z = 0
finally:
    print(f"Z value is: {z}")
print()

def squareInteger():
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
                print(f"Your integer squared is {integer**2}.")

squareInteger()
