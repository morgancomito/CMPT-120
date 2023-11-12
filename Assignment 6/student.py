# oo scary
"""
Instructions:
We're now experts at classes, right?
Yeah?
mkay so do me a favor
Create the class student
every student has these traits:
name
student id (you can pick this number arbitrarily)
year (f/s/j/s)
major
gpa

create a function to see if the student is eligible for the honors program
to be eligible they need to have a gpa above 3.5
return true if they can and false if they cant, and print it out

create a function because this college is a wacky one- every day they generate a student id and if the student id
matches a student, that student gets free food that day.
1. generate a random number the length of however long you choose to make the id number
2. compare if the random number matches your student's id
3. if it matches print out "winner! student (name) gets free lunch!"
4. if not, print "Loser!"
(disclosure: obviously there's a very small chance of your generated number matching the student id number. I just want
to see that you're generating and comparing properly)
"""
from random import randint


class student:
    def __init__(self, name, studentID, year, major, gpa):
        self.name = name
        self.studentID = studentID
        self.year = year
        self.major = major
        self.gpa = gpa

    def honors(self):
        if self.gpa > 3.5:
            return True
        else:
            return False

    def dailyGiveaway(self):
        randomID = randint(10000000, 99999999)
        if randomID == self.studentID:
            return "Winner! Student {self.name} gets free lunch!"
        else:
            return "Loser!"


def main():
    # create three students and check if they get free lunch and if they qualify for honors
    Student1 = student("Morgan", 20127343, "junior", "math", 3.6)
    Student2 = student("Dustin", 20141886, "sophomore", "sports comm", 2.9)
    Student3 = student("Moira", 20129465, "junior", "poli sci", 3.4)

    print(Student1.honors())
    print(Student2.honors())
    print(Student3.honors())

    print(Student1.dailyGiveaway())
    print(Student2.dailyGiveaway())
    print(Student3.dailyGiveaway())


main()
