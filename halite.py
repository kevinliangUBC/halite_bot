%%writefile submission.py

def xy(num):
    y = num // 21
    x = num % 21
    return x,y

def cord(x,y):
    return y*21 + x

def action_for_ship(action, ship_id, move):
    action[ship_id] = move



    

def getHalite(obs,x,y):
    return obs.halite[cord(x,y)]

def get_all_ships(obs):
    return list(obs.players[obs.player][2].keys())

def get_all_shipyards(obs):
    return list(obs.players[obs.player][1].keys())


        

def next_move(obs, ship_id):
    max = 0
    result = None
    x,y = xy(obs.players[obs.player][2][ship_id][0])
    halite = obs.players[obs.player][0]
    
    max = (getHalite(obs,x,y))
    if (max < getHalite(obs,x+1,y)):
        result="EAST"
        max = getHalite(obs,x+1,y)
    if (max < getHalite(obs,x,y+1)):
        result="SOUTH"
        max = getHalite(obs,x,y+1)
    if (max < getHalite(obs,x-1,y)):
        result="WEST"
        max = getHalite(obs,x-1,y)
    if (max < getHalite(obs,x,y-1)):
        result="NORTH"
        max = getHalite(obs,x,y-1)
    if halite >= 500:
        result = "CONVERT"
        print("converting!")
    
    
    return result

from random import choice
def my_agent(obs):
    action = {}
    
    
        
    
    for ship_id in get_all_ships(obs):
        move = next_move(obs, ship_id)
        if move is not None:
            action_for_ship(action, ship_id, move)
    
    for shipyard_id in get_all_shipyards(obs):
        halite = obs.players[obs.player][0]
        if  halite >= 500:
            action[shipyard_id] = "SPAWN"
            halite -= 500
   
    
   
    return action
