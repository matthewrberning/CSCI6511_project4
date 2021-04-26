# hello world
import numpy as np
import api

def num_to_move(num):
    if num == 0:
        return 'N'
    elif num == 1:
        return 'S'
    elif num == 2:
        return 'E'
    elif num == 3:
        return 'W'
    return 'ERROR!'

#TODO: actually update q table
def update_q_table(table):
    return table

def learn(q_table, worldId=0, mode='train'):
    #create the api instance
    a = api.API(worldId=worldId)
    a.enter_world()

    #init terminal state
    terminal_state = False

    #find out where we are
    loc_response = a.locate_me()
    #OK response looks like {"code":"OK","world":"0","state":"0:2"}
    if loc_response["code"] != "OK":
            print(f"something broke on locate_me call \nresponse lookes like: {loc_response}")
            return -1
    # convert JSON into a tuple
    location = int(loc_response["state"].split(':')[0]), int(loc_response["state"].split(':')[1]) #location is a tuple (x, y)

    while True:
    
        #in q-table, get index of best option for movement based on our current state in the world
        move_num = np.argmax(q_table[location[0]][location[1]])

        #make the move - transition into a new state
        move_response = a.make_move(move=num_to_move(move_num), worldId='0') 
        #OK response looks like {"code":"OK","worldId":0,"runId":"931","reward":-0.1000000000,"scoreIncrement":-0.0800000000,"newState":{"x":"0","y":3}}
        
        if move_response["code"] != "OK":
            print(f"something broke on make_move call \nresponse lookes like: {move_response}")
            break
        # convert new location JSON into tuple
        new_loc = int(move_response["newState"]["x"]), int(move_response["newState"]["y"]) #tuple (x,y) (PROBABLY DON'T NEED THIS!?)

        reward = move_response["reward"]

        #update the q-table for the state we were in before
        update_q_table(location, q_table)
        
        #update our current location var
        location = new_loc

        #TODO: compute the temporal difference... somehow?


        if terminal_state:
            break



    #close the api instance
    a.enter_world(worldId=-1)

    return q_table


def init_q_table():
    '''
    init q table (random initilizations [0 to -1])
    defines grid as 40x40, 4 possible actions (N, S, E, W)
    access grid as row, col, action
    ex: [0][0][0] gird 0:0, action 'N'
    '''
    return -1*(np.random.rand(40, 40, 4)) 


