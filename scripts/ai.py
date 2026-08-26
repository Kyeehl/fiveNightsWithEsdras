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
    global animatronic_position
    x, y = animatronic_position
    print(x, y)
    if x == map.shape[0] - 1:
        print("End of the map reached")
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
    animatronic_position = (x, y)

def checkDoor():
    global animatronic_position
    x, y = animatronic_position
    if y + 1 < map.shape[1] and map[x][y + 1] == 4:
        print("AI is at the door")
        
def game_loop():
    cont = 0
    while cont <= 10:
        print(map)
        checkDoor()
        mapMove()
        time.sleep(2)
        cont += 1

print(map.shape)
game_loop()