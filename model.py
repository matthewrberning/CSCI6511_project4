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


def learn(q_table, worldId=0, mode='train'):

    #create the api instance
    a = api.API(worldId=worldId)
    a.enter_world()

    #init terminal state
    terminal_state = False


    while True:
        
        loc_response = a.locate_me()
        #OK response looks like {"code":"OK","world":"0","state":"0:2"}

        if loc_response["code"] != "OK":
            print(f"something broke on locate_me call \nresponse lookes like: {loc_response}")
            break

        location = loc_response["state"]

        x, y = int(location.split(':')[0]), int(location.split(':')[1])

        #in q-table, get index of best option for movement
        move_num = np.argmax(q_table[x][y])

        #make the move
        move_response = a.make_move(move=num_to_move(move_num), worldId='0') #TODO we might want to handle the worldId as a var inside the current api class instance i.e. api.world_ID
        
        if move_response["code"] != "OK":
            print(f"something broke on make_move call \nresponse lookes like: {move_response}")
            break

        if terminal_state:
            break
    # while true (breaks when we hit a terminal state)
    
        # make a call to the api to find where we are 
        x = 5
        # chose an action based on where we are

        # peform the action at the transition to the new state

        # receive the reward and compute the Temporal Difference

        # update the Q-Value for the previous state


    #close the api instance
    a.enter_world(worldId=-1)


def init_q_table():
    '''
    init q table (random initilizations [0 to -1])
    defines grid as 40x40, 4 possible actions (N, S, E, W)
    access grid as row, col, action
    ex: [0][0][0] gird 0:0, action 'N'
    '''
    return -1*(np.random.rand(40, 40, 4)) 


