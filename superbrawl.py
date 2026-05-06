from equipment import headgear, bodgear, leggear, weapon
from Gladiator import Gladiator
from random import randint
import sqlite3
from os import system

# DATABASE
DB_FILE = "database.db"

try:
    cnx = sqlite3.connect(DB_FILE)
except sqlite3.Error as err:
    print(f"Failed to connect to database: {err}")
    raise SystemExit(1)

highscore = cnx.cursor()
query = ("SELECT Highscores.*, Highscores.name as username FROM Highscores")
highscore.execute(query)

# SETUP
class Game:
    def __init__(self):
        self.round = 0
        self.active = True
        self.score = 0
        self.event = "null"
    
    def next_round(self):
        self.round += 1 
        return self.round
    
    def dialogue(self, prompt):
        print(f"{prompt}")
        input()

    def endgame(self):
        print("----- GAME OVER -----")
        self.active = False

    def printscores(self, highscore):
        for row in highscore:
            print(row)

    def inputscores(self):
        username = input("Input name")
        score = input("Input score")
        sql = "INSERT INTO Highscores (name, score) VALUES (?,?)";
        data = (username, score)
        cnx.execute(sql, data)
        cnx.commit()

system('cls')
game = Game()

# INTRO
game.dialogue(f"\n----- Welcome to SUPER BRAWL, the battle of champions! -----")
player = Gladiator(input("What's the name of your glorious champion?\n").capitalize())
opponent = Gladiator("John Enemy")
game.dialogue(f"\n----- Gladiator {player.name} and Gladiator {opponent.name} has entered the arena! -----")
system('cls')

game.dialogue("\n----- A cart of weapons and armor has rolled up in front of you! ------")
game.dialogue("----- You get to choose one piece of equipment for every bodypart, with each one having different stats which will affect your coming fight. -----")
system('cls')
game.dialogue("\n----- There is light equipment, focusing on manouverability other than defence, heavy equipment focusing on the complete opposite, and medium equipment being a good middleground. -----")
game.dialogue("----- The Weight-stat affects how well you can attack, a higher value decreases your chance of successfull attacks late fight, and defence directly decreasing the amount of damage you take, a higher value makes you harder to kill. -----")
game.dialogue("----- There is also the attack-stat, which increases your damage on successfull hits the higher it is. -----")
system('cls')

#forloop för varje equipmentlist där man kan välja en equipment
while True:
    for item in headgear:
        print(f"{item["name"]}")
    selected_items = [item for item in headgear if item["name"] == input("----- Choose equipment -----\n")]
    for item in selected_items:
            print(item)

    
                
        

# GAME
while game.active == True: 
    game.endgame()
    
# END
c = input("'y' to insert score")
if c == 'y':
    game.inputscores()
game.printscores(highscore)
highscore.close()
cnx.close()