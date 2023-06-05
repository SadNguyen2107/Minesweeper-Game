from minesweeper import Player, Map, Boom, SafeSpot

player1 = Player("Player")

# 1 Boom has created
booms = set()
for time in range(0, 1):
    boom = Boom()
    booms.add(boom)
    print(boom)

# 8 safe spots has created
# safeSpots = SafeSpot()

# # Create a map finished
mineMap = Map(player=player1, booms=booms)
mineMap.printMap()

# # Player Choose
while True:
    pos = player1.choosePos()
    mineMap.checkBoom(*pos)
