import random
import time
import numpy as np

# 1 - animatronic, 2 - player, 3 - wall, 4 - door, 0 - empty space

map = np.array([[0, 0, 1, 0, 0],
                [0, 3, 3, 3, 0],
                [0, 3, 3, 3, 0],
                [0, 3, 3, 3, 0],
                [0, 4, 2, 4, 0]])

ai_level = 1
ai_move = 0
canAttack = False;
animatronic_position = (0, 2)

def moveOpportunity():
    time.sleep(2)
    move = canAiMove()
    if move:
        print("AI moved")
    else:
        print("AI did not move")

def canAiMove():
    ai_move = random.randint(1, 20)
    if ai_move < ai_level:
        return True
    else:
        return False

def mapMove():
    x, y = animatronic_position
    if y > 0:
        y -= 1
        map[x][y] = 1
    elif x == 0 and y == 0:
        x += 1
        map[x][y] = 1
    elif x > 0:
        x += 1
        map[x][y] = 1
    if x == len(map):
        x = 0
        y = 0
        map[x][y] = 1
        

def game_loop():
    while True:
        mapMove()
        print(map)
        time.sleep(5000)

game_loop()