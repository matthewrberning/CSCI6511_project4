import numpy as np
import api
import random
import movement_viz as v
from matplotlib import pyplot

import utils

def init_q_table():
    '''
    init q table (initilizations are all [0])
    defines grid as 40x40, 4 possible actions (N, S, E, W)
    access grid as row, col, action
    ex of indexing: q-tab[0][0][0] gird 0:0, action 'N'
    '''

    return (np.zeros((40, 40, 4)))

def num_to_move(num):
    '''
    translates the index returned from np.argmax()
    when accessing our representation of the q-table
    structure into the expexted value that the API 
    can understand
    '''
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


def learn(q_table, worldId=0, mode='train', learning_rate=0.001, gamma=0.9, epsilon=0.9, good_term_states=[], bad_term_states=[], epoch=0, obstacles=[], run_num=0, verbose=True):
    '''
    ~MAIN LEARNING FUNCTION~
    takes in:
    -the Q-table data structure (numpy 3-dimensional array)
    -worldID (for api and plotting)
    -mode (train or exploit)
    -learning rate (affects q-table calculation)
    -gamma (weighting of the rewards)
    -epsilon (determines the amount of random exploration the agen does)
    -good_term_states
    -bad_term_states
    -eposh
    -run number
    -verbosity

    returns: q_table [NumPy Array], good_term_states [list], bad_term_states [list], obstacles [list]


    '''

    #create the api instance
    a = api.API(worldId=worldId)
    w_res = a.enter_world()


    if verbose: print("w_res: ",w_res)


    #init terminal state reached
    terminal_state = False

    #create a var to track the type of terminal state
    good = False

    #accumulate the rewards so far for plotting reward over step
    rewards_acquired = []

    #find out where we are
    loc_response = a.locate_me()

    #create a list of everywhere we've been for the viz
    visited = []

    if verbose: print("loc_response",loc_response)
    
    #OK response looks like {"code":"OK","world":"0","state":"0:2"}
    if loc_response["code"] != "OK":
            print(f"something broke on locate_me call \nresponse lookes like: {loc_response}")
            return -1
    
    # convert JSON into a tuple (x,y)
    location = int(loc_response["state"].split(':')[0]), int(loc_response["state"].split(':')[1]) #location is a tuple (x, y)
    
    # SET UP FIGURE FOR VISUALIZATION.
    pyplot.figure(1, figsize=(10,10))
    curr_board = [[float('-inf')] * 40 for temp in range(40)]
    
    #keep track of where we've been for the visualization
    visited.append(location)
    while True:
        #////////////////// CODE FOR VISUALIZATION
        curr_board[location[1]][location[0]] = 1
        for i in range (len(curr_board)):
            for j in range(len(curr_board)):
                if (curr_board[i][j] != 0):
                    curr_board[i][j] -= .1
        for obstacle in obstacles:
            if obstacle in visited:
                obstacles.remove(obstacle)
        v.update_grid(curr_board, good_term_states, bad_term_states, obstacles, run_num, epoch, worldId, location, verbose)
        #//////////////// END CODE FOR VISUALIZATION

        #in q-table, get index of best option for movement based on our current state in the world
        if mode == 'train':
            #use an episolon greedy approach to randomly explore or exploit
            if np.random.uniform() < epsilon:
                move_num = random.randint(0,3) 
            else:
                move_num = np.argmax(q_table[location[0]][location[1]])

        else:
            #mode is exploit -we'll use what we already have in the q-table to decide on our moves
            move_num = np.argmax(q_table[location[0]][location[1]])

        #make the move - transition into a new state
        move_response = a.make_move(move=num_to_move(move_num), worldId=str(worldId)) 

        if verbose: print("move_response", move_response)
        #OK response looks like {"code":"OK","worldId":0,"runId":"931","reward":-0.1000000000,"scoreIncrement":-0.0800000000,"newState":{"x":"0","y":3}}
        

        if move_response["code"] != "OK":
            #handel the unexpected
            print(f"something broke on make_move call \nresponse lookes like: {move_response}")

            move_failed = True
            while move_failed:
                move_response = a.make_move(move=num_to_move(move_num), worldId=str(worldId))

                print("\n\ntrying move again!!\n\n")

                if move_response["code"] == 'OK':
                    move_failed = False
        
        # check that we're not in a terminal state, and if not convert new location JSON into tuple
        if move_response["newState"] is not None:
            #we're now in new_loc, which will be a tuple of where we are according to the API
            #KEEP IN MIND the movment of our agent is apparently STOCHASTIC
            new_loc = int(move_response["newState"]["x"]), int(move_response["newState"]["y"]) #tuple (x,y)
            
            # keep track of if we hit any obstacles
            expected_loc = list(location)

            #convert the move we tried to make into an expected location where we think we'll end up (expected_loc) 
            recent_move = num_to_move(move_num)
            if recent_move == "N":
                expected_loc[1]-=1
            elif recent_move == "S":
                expected_loc[1]+=1
            elif recent_move == "E":
                expected_loc[0]+=1
            else:
                expected_loc[0]-=1
            expected_loc = tuple(expected_loc)

            if verbose: print(f"New Loc: {new_loc} (where we actually are now):")
            if verbose: print(f"Expected Loc: {expected_loc} (where we thought we were going to be):")

            if (mode == "train"):
                obstacles.append(expected_loc)

            #continue to track where we have been
            visited.append(new_loc)

            #if we placed an obstacle there in the vis, remove it
            for obstacle in obstacles:
                if obstacle in visited:
                    obstacles.remove(obstacle)
            
            
        else:
            #we hit a terminal state
            terminal_state = True
            print("\n\n--------------------------\nTERMINAL STATE ENCOUNTERED\n--------------------------\n\n")
       
        #get the reward for the most recent move we made
        reward = float(move_response["reward"])


        #add reward to plot
        rewards_acquired.append(reward) 

        #if we are training the model then update the q-table for the state we were in before
        #using the bellman-human algorithim
        if mode == "train":
            update_q_table(location, q_table, reward, gamma, new_loc, learning_rate, move_num)
        
        #update our current location variable to our now current location
        location = new_loc


        #if we are in a terminal state then we need to collect the information for our visualization
        #and we need to end our current training epoch
        if terminal_state:
            print(f"Terminal State REWARD: {reward}")

            if reward > 0:
                #we hit a positive reward so keep track of it as a good reward terminal-state
                good = True
            if not(location in good_term_states) and not(location in bad_term_states):
                #update our accounting of good and bad terminal states for the visualization
                if good:
                    good_term_states.append(location)
                else:
                    bad_term_states.append(location)

            #update our visualization a last time before moving onto the next epoch
            v.update_grid(curr_board, good_term_states, bad_term_states, obstacles, run_num, epoch, worldId, location, verbose)
            break

    #possibly not needed but this seperates out the plot
    pyplot.figure(2, figsize=(5,5))
    #cumulative average for plotting reward by step over time purposes
    cumulative_average = np.cumsum(rewards_acquired) / (np.arange(len(rewards_acquired)) + 1)
    # plot reward over each step of the agent
    utils.plot_learning(worldId, epoch, cumulative_average, run_num)

    return q_table, good_term_states, bad_term_states, obstacles

