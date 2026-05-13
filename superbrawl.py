from equipment import headgear, bodgear, leggear, weapon
from Gladiator import Gladiator
import random
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

    def gearprint(self, itemlist):
        for item in itemlist:
            if item["weight"] == 0: prefix = "[NONE]"
            elif item["weight"] == 5: prefix = "[LIGHT]"
            elif item["weight"] == 10: prefix = "[MEDIUM]"
            else: prefix = "[HEAVY]"
            if itemlist == weapon:
                print(f"{prefix} - {item["name"].capitalize()} - Weight: {item["weight"]}, Defence: {item["attack"]}")
            else:
                print(f"{prefix} - {item["name"].capitalize()} - Weight: {item["weight"]}, Defence: {item["defence"]}")
system('cls')
game = Game()


# INTRO
game.dialogue(f"----- Welcome to SUPER BRAWL, the battle of champions! -----")
player = Gladiator(input("What's the name of your glorious champion?\n").capitalize())
opponent = Gladiator("John Enemy")
game.dialogue(f"\n----- Gladiator {player.name} and Gladiator {opponent.name} has entered the arena! -----")
system('cls')

game.dialogue("----- A cart of weapons and armor has rolled up in front of you! ------")
game.dialogue("----- You get to choose one piece of equipment for every bodypart, with each one having different stats which will affect your coming fight. -----")
system('cls')
game.dialogue("\n----- Three paths await you: LIGHT gear for speed and precision, HEAVY for an impenetrable defense, or BALANCED for versatility. -----")
game.dialogue("----- Choose wisely! Weight drains your stamina more when you make an attack and you strike more certainly with light armor, but risk taking more hits. Defence is your shield against enemy blades. Attack determines how much pain you deal when your blows connect. -----")
system('cls')

#forloop för varje equipmentlist där man kan välja en equipment
while True:
    print("----- Choose your headgear! -----")
    game.gearprint(headgear)
    headgear_choice = input("\n")
    selected_item = [item for item in headgear if item["name"] == headgear_choice]
    if selected_item:
        player.defence += selected_item[0]["defence"] 
        player.weight += selected_item[0]["weight"]
        system('cls')
        break
    else:
        system('cls')
        game.dialogue("----- Equipment not found, try again. Type only name. -----")
    system('cls')

while True:
    print("----- Choose your bodygear! -----")
    game.gearprint(bodgear)
    bodgear_choice = input("\n")
    selected_item = [item for item in bodgear if item["name"] == bodgear_choice]
    if selected_item:
        player.defence += selected_item[0]["defence"]
        player.weight += selected_item[0]["weight"] 
        system('cls')
        break
    else:
        system('cls')
        game.dialogue("----- Equipment not found, try again. Type only name. -----")
    system('cls')

while True:
    print("----- Choose your leggear! -----")
    game.gearprint(leggear)
    leggear_choice = input("\n")
    selected_item = [item for item in leggear if item["name"] == leggear_choice]
    if selected_item:
        player.defence += selected_item[0]["defence"]
        player.weight += selected_item[0]["weight"] 
        system('cls')
        break
    else:
        system('cls')
        game.dialogue("----- Equipment not found, try again. Type only name. -----")
    system('cls')

while True:
    print("----- Choose your weapon! -----")
    game.gearprint(weapon)
    weapon_choice = input("\n")
    selected_item = [item for item in weapon if item["name"] == weapon_choice]
    if selected_item:
        player.attack += selected_item[0]["attack"]
        player.weight += selected_item[0]["weight"] 
        system('cls')
        break
    else:
        system('cls')
        game.dialogue("----- Equipment not found, try again. Type only name. -----")
    system('cls')

# enemy equipment
enemy_headgear = random.choice(headgear) 
enemy_bodgear = random.choice(bodgear)
enemy_leggear = random.choice(leggear)
enemy_weapon = random.choice(weapon)
opponent.defence += enemy_headgear["defence"] + enemy_bodgear["defence"] + enemy_leggear["defence"]
opponent.weight += enemy_headgear["weight"] + enemy_bodgear["weight"] + enemy_leggear["weight"] + enemy_weapon["weight"]
opponent.attack += enemy_weapon["attack"]
game.dialogue(f"----- {opponent.name} chooses {enemy_headgear["name"]} as headgear, {enemy_bodgear["name"]} as bodygear,\n{enemy_leggear["name"]} as leggear and {enemy_weapon["name"]} as their weapon! -----")
system('cls')
# GAME
faces = ["(˙ʟ˙)", "(ಠ_ಠ)", "(¬_¬)", "(o.o)", "(T_T)", "(<_<)", "(p_o)", "(D_D)"]
playerstamina = 100
enemystamina = 100
turn = "player_turn"
actions = ["[1] Attack", "[2] Defend", "[3] Do nothing"]
score = 0
while game.active == True:
    enemyface = random.choice(faces)
    while True:
        if opponent.health <= 0 or player.health <= 0:
            break
    game.endgame()
    
# END
c = input("'y' to insert score")
if c == 'y' or 'Y':
    game.inputscores()
game.printscores(highscore)
highscore.close()
cnx.close()