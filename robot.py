from weapon import Weapon


class Robot:

    def __init__(self):
        self.name = ''
        self.health = 0
        self.active_weapon = Weapon()
        