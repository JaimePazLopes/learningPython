peopleFile = open("../supportFiles/people.txt")
print(peopleFile.read())
print(peopleFile.read())
peopleFile.seek(0)
print(peopleFile.read())
peopleFile.seek(0)
fileContent = peopleFile.read()
peopleFile.seek(0)
print(peopleFile.readlines())
peopleFile.seek(0)
peopleFile.close()
print()
with open("../supportFiles/people.txt", mode='r') as temporaryFile:
    print(temporaryFile.readline())
    print(temporaryFile.readline())
    print(temporaryFile.readline())
lines = 0
with open("../supportFiles/people.txt") as temporaryFile:
    for line in temporaryFile:
        lines = lines + 1
with open("../supportFiles/people.txt", mode='a') as temporaryFile:
    temporaryFile.write(f"\n{lines},Jaime,Lopes,Male,Brazil,31,19/05/1988,3333")
for line in open('../supportFiles/people.txt'):
    print(line)
print()
with open("../supportFiles/newFile.txt", mode='w+') as temporaryFile:
    temporaryFile.write("Lorem Ipsum")
    temporaryFile.seek(0)
    print(temporaryFile.read())