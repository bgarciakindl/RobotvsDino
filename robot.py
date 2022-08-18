from weapon import Weapon


class Robot:

    def __init__(self,name):
        self.name = name
        self.health = 100
        self.active_weapon = Weapon()

    attack_weapon = Weapon("LaserSword", 35)
    
    def attack_dino(self,dinosuar):
        dinosuar -= self.attack_weapon