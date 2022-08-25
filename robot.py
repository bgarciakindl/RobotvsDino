from weapon import Weapon


class Robot:

    def __init__(self,name):
        self.name = name
        self.health = 100
        self.active_weapon = Weapon ("Lasersword", 38)


    def attack_dino(self,dino):
        dino.health -= self.active_weapon.damage 
        print(f"{self.name} has attacked for {self.active_weapon.damage} , {dino.name} health is now {dino.health}")