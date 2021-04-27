import model
from api import API

def epsilon_decay(epsilon, epoch, epochs):
    
    epsilon = epsilon*np.exp(-.01*epoch)
    
    print(epsilon)
    return epsilon


def main():



	mode = str(input("\n(default is train, world 0)\n") or "t")

	print("training on world 0")

	if mode == "t":

		epochs = 100

		world = 0

		q_table = model.init_q_table()

		file_path = f"./runs/Q-table_world_{world}_epoch_"

		for epoch in epochs:

			q_table = model.learn(q_table, worldId=0, mode='train', learning_rate=0.0001, gamma=0.9, epsilon=0.9)

			epsilon = epsilon_decay(epsilon, epoch, epochs)

			numpy.save(file_path+epoch+".np", q_table) 




		

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