import random
import time
import numpy as np

# 1 - animatronic, 2 - player, 3 - wall, 4 - door, 0 - empty space

map = [[0, 0, 1, 0, 0],
       [0, 3, 3, 3, 0],
       [0, 3, 3, 3, 0],
       [0, 3, 3, 3, 0],
       [0, 4, 2, 4, 0]]

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