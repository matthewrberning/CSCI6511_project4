import model
from api import API
import numpy as np
import os

def epsilon_decay(epsilon, epoch, epochs):
    
    epsilon = epsilon*np.exp(-.01*epoch)
    
    print(epsilon)
    return epsilon


def main():

	mode = str(input("\noption t is train (default)\noption e is exploit\nENTER HERE: ") or "t")

	print("training on world 0")

	if mode == "t":

		epochs = 2

		epsilon = 0.9

		world = 0

		q_table = model.init_q_table()

		if not (os.path.exists(f"./runs/world_{world}/")):
			os.makedirs(f"./runs/world_{world}/")

		run_num = len([i for i in os.listdir(f"runs/world_{world}")])


		file_path = f"./runs/Q-table_world_{world}"

		good_term_states = []
		bad_term_states = []
		obstacles = []

		for epoch in range(epochs):
			print("EPOCH #"+str(epoch)+":\n\n")
			q_table, good_term_states, bad_term_states, obstacles = model.learn(
				q_table, worldId=world, mode='train', learning_rate=0.0001, gamma=0.9, epsilon=epsilon, good_term_states=good_term_states, bad_term_states=bad_term_states,
				epoch=epoch, obstacles=obstacles, run_num=run_num)

			epsilon = epsilon_decay(epsilon, epoch, epochs)

			np.save(file_path, q_table)
		np.save(f"./runs/obstacles_world_{world}", obstacles)
		np.save(f"./runs/good_term_states_world_{world}", good_term_states)
		np.save(f"./runs/bad_term_states_world_{world}", bad_term_states)

	elif mode == "e":
		epochs = 1
		world = 0
		file_path = f"./runs/Q-table_world_{world}"
		q_table = np.load(file_path+".npy")

		obstacles = np.load(f"./runs/obstacles_world_{world}"+".npy")
		good_term_states = np.load(f"./runs/good_term_states_world_{world}"+".npy")
		bad_term_states = np.load(f"./runs/bad_term_states_world_{world}"+".npy")

		obstacles = obstacles.tolist()
		good_term_states = good_term_states.tolist()
		bad_term_states = bad_term_states.tolist()

		epsilon = 0.9
		run_num = len([i for i in os.listdir(f"runs/world_{world}")])

		for epoch in range(epochs):
			print("EPOCH #"+str(epoch)+":\n\n")
			q_table, good_term_states, bad_term_states, obstacles = model.learn(
				q_table, worldId=world, mode='expl', learning_rate=0.0001, gamma=0.9, epsilon=epsilon, good_term_states=good_term_states, bad_term_states=bad_term_states,
				epoch=epoch, obstacles=obstacles, run_num=run_num)
	else:
		print("that option doesn't exist yet :'(")
		exit()



if __name__ == "__main__":
    main()