class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Employee:
    def __init__(self, name, idNumber, department):
        self.name = name
        self.idNumber = idNumber
        self.department = department


class Cake:
    def __init__(self, flavor, frosting):
        # can you fill out the rest of this for me? im dumb
        # the cake needs to have the cake flavor and cake frosting stored
        self.flavor = flavor
        self.frosting = frosting


class Cat:
    def __init__(self, name, age, fur_length):
        self.name = name
        self.age = age
        self.fur_length = fur_length

    def breedGuess(self):
        if self.fur_length == "long":
            return "Domestic Longhair"
        else:
            return "Domestic Shorthair"


class Car:
    def __init__(self, model, year, color):
        self.model = model
        self.year = year
        self.color = color

    # create your own function! what do you want it to do?
    def morgansCar(self):
        if self.model == "Sentra" and self.year == 2010 and self.color == "gray":
            return "Morgan's car"
        else:
            return "Not Morgan's car"


def main():
    # fill this one out with a dog's name and age... can be your dog, friend's dog, etc
    newDog = Dog("Carly", 13)
    print(newDog.name, newDog.age)

    # and what about a new employee
    newEmployee = Employee("Morgan", 1, "clothing")
    # how would we print out each of the variables from newEmployee?
    print(newEmployee.name)
    print(newEmployee.idNumber)
    print(newEmployee.department)

    # now create and print out a cake you make
    cake1 = Cake("chocolate", "chocolate")
    print("The cake is", cake1.flavor, "with", cake1.frosting, "frosting")

    # and now create another cake and print it out
    cake2 = Cake("ice cream", "whipped cream")
    print("It is an", cake2.flavor, "cake with", cake2.frosting, "frosting")

    # create a cat!
    cat1 = Cat("Swiper", 10, "short")
    # create another cat!
    cat2 = Cat("Gabby", 20, "short")
    # What would we put here to print out the result of breedGuess for cat1?
    print(cat1.breedGuess())

    # create a car!
    car = Car("Sentra", 2010, "gray")
    # Now print out the function you made for car :)
    print(car.morgansCar())


main()
