def main():
    # set this to any double
    doubleValue = 1.4

    # set this to any int
    intValue = 6

    # print out addition, subtraction, multiplication, and division of these two values
    print(doubleValue + intValue)
    print(intValue - doubleValue)
    print(doubleValue * intValue)
    print(intValue / doubleValue)

    # populate this list
    myFriends = ["Moira", "Riya", "Max", "Emma", "Hannah", "Luke"]

    # print out your friends at index 2 and index 3
    print(myFriends[2])
    print(myFriends[3])

    # populate this list with five numbers
    fiveNumbers = [1, 5, 82, 900, 64]

    # do each of the four equations with different numbers each time.
    print(fiveNumbers[0] + fiveNumbers[1])
    print(fiveNumbers[4] - fiveNumbers[3])
    print(fiveNumbers[2] * fiveNumbers[1])
    print(fiveNumbers[3] / fiveNumbers[0])

    # now replace two of the numbers in the list with a different number (using name of list[x] = ?, not rewriting the
    # fiveNumber list)
    fiveNumbers[1] = 13
    fiveNumbers[4] = 66

    # print out the list
    print(fiveNumbers)


main()
