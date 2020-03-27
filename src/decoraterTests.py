def decorator(function):
    def wrap():
        returnValue = "decorated " + function()
        returnValue += " is beautiful"
        return returnValue
    return wrap

@decorator
def function():
    return "function"

print(function())
decoratedFunction = decorator(function)
print(decoratedFunction())