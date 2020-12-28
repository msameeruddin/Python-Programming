from time import sleep
from random import choice

time_range = list(range(2, 8))

class WashingMachine():
    def __init__(self, clothes):
        self.clothes = clothes
    
    def begin_stage(self):
        machine_desc = "This machine has python os 😊 which detects clothes to wash."
        print(machine_desc)
        print("Clothes provided to the machine - {}".format(self.clothes))
        sleep(3)
        return "{} is yet to be washed.".format(self.clothes)

class SpinningMachine(WashingMachine):
    def __init__(self, clothes):
        self.clothes = clothes
    
    def sping_stage(self):
        print(self.begin_stage())
        print('\n--------\n')
        motor_desc = "The battery of this machine has python components 😋 that help spin the clothes."
        print(motor_desc)
        time_requires = choice(time_range)
        print("\t Total time required : {} secs".format(time_requires))
        sleep(time_requires)
        return "{} is getting spun to clean the dirt.".format(self.clothes)

class DryingMachine(SpinningMachine):
    def __init__(self, clothes):
        self.clothes = clothes
    
    def dry_stage(self):
        print(self.sping_stage())
        print('\n--------\n')
        dry_desc = "This machine has mini-sun of python version to dry all the clothes 😍."
        print(dry_desc)
        time_requires = choice(time_range)
        print("\t Total time required : {} secs".format(time_requires))
        sleep(time_requires)
        return "{} is getting dried.".format(self.clothes)

my_clothes = ["T-shirt", "Jeans", "Towel"]
cloth = choice(my_clothes)
machine = DryingMachine(clothes=cloth)
print(machine.dry_stage())
print("\n\n{} washed 🐣 successfully.".format(cloth))