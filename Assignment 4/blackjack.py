# if you don't know how to play blackjack, tbh not super important but look it up anyway LOL
# this script is going to require some googling: I want you to practice using your resources with this one. But of
# course if you get stuck, reach out :)
""" instructions: randomly generate three values between 1 and 11. in the function bust: add these three numbers
together. if they add up to or less than 21, return the sum. If it's over 21, return 0. If it's over 21 BUT there's an
11 as one of the values, return the sum - 10. """
import random


def bust():
    num1 = random.randint(1, 11)
    num2 = random.randint(1, 11)
    num3 = random.randint(1, 11)
    total = num1 + num2 + num3
    if total <= 21:
        return total
    elif total > 21 and (11 in [num1, num2, num3]):
        return total - 10
    else:
        return 0


def main():
    print(bust())


main()
