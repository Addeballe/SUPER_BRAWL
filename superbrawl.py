from Gladiator import Gladiator
import sqlite3
import os

DB_FILE = "database.db"

try:
    cnx = sqlite3.connect(DB_FILE)
except sqlite3.Error as err:
    print(f"Failed to connect to database: {err}")
    raise SystemExit(1)

highscore = cnx.cursor()
query = ("SELECT Post.*, User.name as author FROM Post JOIN User ON Post.user_id = User.id")
highscore.execute(query)

class Game:
    def __init__(self):
        self.round = 0
        self.game_over = False
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
        self.game_over = True

os.system('cls')
game = Game()
game.dialogue(f"----- Welcome to SUPER BRAWL, the battle of champions! -----")
playername = input("What's the name of your glorious champion? ").capitalize()
player = Gladiator(playername)
opponent = Gladiator("John Enemy")
game.dialogue(f"\n----- Gladiator {player.name} has entered the arena! -----")
os.system('cls')

while game.game_over == False:
    game.endgame()

for row in highscore:
    print(row)

highscore.close()
cnx.close()