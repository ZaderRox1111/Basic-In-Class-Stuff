# Just a bunch of operations to do onto lists of numbers

def sum(numList):
    newSum = 0
    for num in numList:
        newSum += num

    return newSum

# Takes a list as input still
def squareList(numbers):
    newList = []
    for number in numbers:
        newList.append(number**2)

    return newList

def destructiveSquareList(numbers):
    for number in numbers:
        number = number ** 2

def removeEvens(numbers):
    odds = []
    for number in numbers:
        if number % 2 == 1:
            odds.append(number)

    return odds

def destructiveRemoveEvens(numbers):
    for number in numbers:
        if number % 2 == 0:
            numbers.remove(number)
