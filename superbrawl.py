import champion

class Game:
    def __init__(self):
        self.round = 0
        self.game_over = False
    
    def next_round(self):
        self.round += 1 
        return self.round

p = Game()
while True:
    print(p.next_round())