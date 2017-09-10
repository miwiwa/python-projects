from datetime import datetime

currentYear = datetime.now().year
print("Current year is: ", currentYear)

name = input("Please enter your name: ")
age = input("Please enter your age: ")

ageDiff = 100 - int(age)

newYear = currentYear + ageDiff

print("Hi " + name + " You will turn 100 in year ", newYear)
