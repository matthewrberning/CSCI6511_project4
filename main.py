import model
from api import API
import numpy as np
import os

def epsilon_decay(epsilon, epoch, epochs):
    
    epsilon = epsilon*np.exp(-.01*epoch)
    
    print(epsilon)
    return epsilon


def main():

	mode = str(input("\n(default is train, world 0)\n") or "t")

	print("training on world 0")

	if mode == "t":

		epochs = 100

		epsilon = 0.9

		world = 0

		q_table = model.init_q_table()
		run_num = len([i for i in os.listdir("runs")])

		file_path = "./runs/attempt-{}/Q-table_world_{}_epoch_".format(run_num, world)

		good_term_states = []
		bad_term_states = []

		obstacles = []

		for epoch in range(epochs):
			print("EPOCH #"+str(epoch)+":\n\n")
			epsilon = epsilon_decay(epsilon, epoch, epochs)
			q_table, new_term_state, obstacles, is_good = model.learn(
				q_table, worldId=0, mode='train', learning_rate=0.001, gamma=0.7, epsilon=epsilon, good_term_states=good_term_states, bad_term_states=bad_term_states,
				epoch=epoch, obstacles=obstacles, run_num=run_num)

			if not(new_term_state in good_term_states) and not(new_term_state in bad_term_states):
				if is_good:
					good_term_states.append(new_term_state)
				else:
					bad_term_states.append(new_term_state)

			

			np.save(file_path+str(epoch)+".np", q_table) 




		

	# 	agent = Api()
	# 	user = Api("./api_key/mellon.json") #sorry

	# 	board_size = int(input("board size? (default is 3)\nsize: ") or "3")
		
	# 	target_size = int(input("how many to win? (must be less than or equal to board size -default is 3)\ntarget: ") or "3")

	# 	game = Game(agent, user, size=board_size, target=target_size)

	# 	print(f"Game created! $GME (1265) vs. MellonCap (1267) --> gameId: {game.gameId}")

	# 	game.play_game()


	# elif game_type == "c":

	# 	agent = Api()
	# 	user = Api("./api_key/mellon.json")

	# 	gameId = input("what's the gameId?\ngameId: ")

	# 	game = Game(agent, user, gameId=gameId)

	# 	game.play_game()



	else:
		print("that option doesn't exist yet :'(")
		# while true check for open games, create a new instance of game play
		# add instance to collection, list? update each sucessively? 
		# for instance in instances: instance.check_and_move/report?
		exit()



if __name__ == "__main__":
    main()