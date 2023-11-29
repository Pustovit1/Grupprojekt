from random import randint

class Door:
    def __init__(self,number):
        self.number = number

random_number = randint(0,2)
door = Door(random_number)
print(door.number)

if door.number == 0:
    print("Congratulations, you found a chest")
elif door.number == 1:
    print("")