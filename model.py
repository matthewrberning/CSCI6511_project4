# hello world
import numpy as np
import api
import random

def update_viz():
    x = 5

def init_q_table():
    '''
    init q table (random initilizations [0 to -1])
    defines grid as 40x40, 4 possible actions (N, S, E, W)
    access grid as row, col, action
    ex: [0][0][0] gird 0:0, action 'N'
    '''
    # return -1*(np.random.rand(40, 40, 4)) 

    return (np.zeros(40, 40, 4))

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

def update_q_table(location, q_table, reward, gamma, new_loc, learning_rate, move_num):
    '''
    bellman eq: NEW Q(s,a) = Q(s,a) + learning_rate * [R(s,a) + gamma * maxQ'(s',a') - Q(s,a)]
    '''

    #collecting the current understanding of the best q value based upon our new location, weight it by gamma and add reward
    right_side = reward + gamma * q_table[new_loc[0], new_loc[1], :].max() - q_table[location[0], location[1], move_num]

    #use the previous location to 
    new_q = q_table[location[0], location[1], move_num] + learning_rate * right_side

    #update q_table with new value
    q_table[location[0], location[1], move_num] = new_q


def learn(q_table, worldId=0, mode='train', learning_rate=0.0001, gamma=0.9, epsilon=0.9):
    #create the api instance
    a = api.API(worldId=worldId)
    w_res = a.enter_world()
    print("w_res",w_res)

    # if w_res["code"] != "OK":

    #init terminal state
    terminal_state = False

    #find out where we are
    loc_response = a.locate_me()
    print("loc_response",loc_response)
    #OK response looks like {"code":"OK","world":"0","state":"0:2"}
    if loc_response["code"] != "OK":
            print(f"something broke on locate_me call \nresponse lookes like: {loc_response}")
            return -1
    # convert JSON into a tuple (x,y)
    location = int(loc_response["state"].split(':')[0]), int(loc_response["state"].split(':')[1]) #location is a tuple (x, y)

    while True:
    
        #in q-table, get index of best option for movement based on our current state in the world
        if mode == 'train':
            #use an episolon greedy approach to randomly explore or exploit
            if np.random.uniform() < epsilon:
                move_num = np.argmax(q_table[location[0]][location[1]])
            else:
                move_num = random.randint(0,3) 

        else:
            #mode is exploit
            move_num = np.argmax(q_table[location[0]][location[1]])

        #make the move - transition into a new state
        move_response = a.make_move(move=num_to_move(move_num), worldId='0') 
        print("move_response", move_response)
        #OK response looks like {"code":"OK","worldId":0,"runId":"931","reward":-0.1000000000,"scoreIncrement":-0.0800000000,"newState":{"x":"0","y":3}}
        
        if move_response["code"] != "OK":
            print(f"something broke on make_move call \nresponse lookes like: {move_response}")
            break
        # convert new location JSON into tuple
        if move_response["newState"] is not None:
            new_loc = int(move_response["newState"]["x"]), int(move_response["newState"]["y"]) #tuple (x,y) (PROBABLY DON'T NEED THIS!?)

        else:
            terminal_state = True
            print("TERMINAL STATE ENCOUNTERED?!!?!??")
       
        reward = move_response["reward"]

        #update the q-table for the state we were in before
        update_q_table(location, q_table, reward, gamma, new_loc, learning_rate, move_num)
        
        #update our current location var
        location = new_loc

        if terminal_state:
            break



    # #close the api instance
    # a.enter_world(worldId=-1)

    return q_table




