from tire import Player, Map, Boom, SafeSpot

player1 = Player("Player")

# 1 Boom has created
booms = set()

# To change the amount of booms
# Change here
boom_amounts = 2         

for time in range(0, boom_amounts):
    boom = Boom()
    booms.add(boom)

# 8 safe spots has created
# safeSpots = SafeSpot()

print("---------WELCOME TO MY MINESWEEPER GAME RUN ON TERMINAL---------")
# # Create a map finished
mineMap = Map(player=player1, booms=booms)
mineMap.printMap()

# # Player Choose
while True:
    pos = player1.choosePos()
    mineMap.checkBoom(*pos)
