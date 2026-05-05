from equipment import equipment
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
game.dialogue(f"----- Welcome to SUPER BRAWL, the battle of champions! -----")
playername = input("What's the name of your glorious champion?").capitalize()
player = Gladiator(playername)
opponent = Gladiator("John Enemy")
game.dialogue(f"\n----- Gladiator {player.name} has entered the arena! -----")
system('cls')

for i, obj in equipment.items():
    print(i)
    
    for y in obj:
        print(y + ':', obj[y])
    input()

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