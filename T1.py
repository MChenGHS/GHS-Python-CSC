name = input("What's your name? ")
age = int(input("How old are you? "))
address = input("Where do you live? ")
car = input("Do you have a car? ")

if car == "True" or car == "Yes":
    car = True
elif car == "False" or car == "No":
    car = False

#print(car)
#print(type(car))

if car:
    print(name, " is a ", age, "year old car owner")
else:
    print(name, " is a ", age, "year person who doesn't have a car")