class Dinosaur:
    def __init__(self):
        self.name = "james"
        self.health = 100
        self.attack_power = 32


    def attack_robot(self,robot):
        robot.health -= self.attack_power
        print(f"{self.name} has attacked for {self.attack_power} , {robot.name} health is now {robot.health}")
        