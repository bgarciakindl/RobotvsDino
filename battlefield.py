from email.base64mime import header_length
from os import F_OK
from sys import displayhook
from dinosaur import Dinosaur
from robot import Robot


class Battlefield:
    def __init__(self):
        self.robot = Robot('frank')
        self.dinosaur = Dinosaur()

    def run_games(self):
        self.display_welcome()

        self.battle_phase()
        pass

    def display_welcome(self):
        print ("Welcome to the Field of Battle!")
        print ("Only one can win!")
        

    def battle_phase(self):
        while self.robot.health>0 and self.dinosaur.health>0:
            if self.robot.health == 0:
                self.display_winner()
            elif self.dinosaur.health == 0:
                self.display_winner()
            else:
                self.dinosaur.attack_robot(self.robot)
                self.robot.attack_dino(self.dinosaur)
         

         

    def display_winner(self):
        
        pass
