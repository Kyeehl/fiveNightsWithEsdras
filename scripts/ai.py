import random
import time
import numpy as np
import os

# 1 - animatronic, 2 - player, 3 - wall, 4 - door, 0 - empty space

map = np.array([[0, 0, 1, 0, 0],
                [0, 3, 3, 3, 0],
                [0, 3, 3, 3, 0],
                [0, 3, 3, 3, 0],
                [0, 4, 2, 4, 0]])

ai_level = 10
ai_move = 0
canAttack = False
animatronic_position = (0, 2)
isAtEndMap = False

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def moveOpportunity():
    time.sleep(2)
    move = canAiMove()
    if move:
        return True
    else:
        return False

def canAiMove():
    ai_move = random.randint(1, 20)
    if ai_move < ai_level:
        return True
    else:
        return False

def mapMove(canMove):
    global isAtEndMap
    global animatronic_position
    x, y = animatronic_position
    if x == map.shape[0] - 1:
        isAtEndMap = True
    if canMove:
        print("move opportunity: True")
        if x != map.shape[0] - 1:
            lastX, lastY = animatronic_position
            map[lastX][lastY] = 0
            if y > 0:
                y -= 1
                map[x][y] = 1
            elif y == 0:
                x += 1
                map[x][y] = 1
                if x > 0:
                    map[x][y] = 1
            isAtEndMap = False
    else:
        print("move opportunity: False")
    animatronic_position = (x, y)
    print("Animatronic position:",x, y)
    print("Is at end of map:", isAtEndMap)

def checkDoor():
    global animatronic_position
    x, y = animatronic_position
    if y + 1 < map.shape[1] and map[x][y + 1] == 4:
        print("AI at the door: True")
    else:
        print("AI at the door: False")

def Full_movement():
    canMove = moveOpportunity()
    mapMove(canMove)
    checkDoor()

def game_loop():
    while True:
        time.sleep(3)
        clear_screen()
        Full_movement()
        print(map)
print(map.shape)
game_loop()