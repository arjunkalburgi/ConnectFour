def SBM2(board, depth, player=None):
	if player is None: 
		player = 1
	elif player is 1: 
		player = 2
	elif player is 2: 
		player = 1
	else: 
		print("ERROR")

	if depth is 0: 
		return 0

	max = -100
	best_locn = board.available_cols()[0]
	for i in board.available_cols(): 
		value = board.move_value(player, i)
		board.add_piece(player, i)
		value = value + SBM(board, depth-1, player)
		board.rm_piece(i)
		if value > max: 
			max = value
			best_locn = i

	return best_locn, memo

def SBM(board, depth, player=None, memo=None):
	# case of the player, switch player
	# upon entering function, or initialize
	# player to be the computer (1)
	if player is None: 
		player = 1
	elif player is 1: 
		player = 2
	elif player is 2: 
		player = 1
	else: 
		print("ERROR")

	# initialize memo!
	if memo is None: 
		memo = {}

	# base case for depth=0
	if depth is 0: 
		return 0

	# initializing max as a low number
	# just in case some weird computation occurs
	max = -100

	# initializing best_locn as the first 
	# available column in case it cannot be determined below
	best_locn = board.available_cols()[0]

	# For each available column, drop a piece into that column
	# and get the value of that move, add it to the value of the 
	# next possible move and so on 'depth' amount of times. 
	# In the end, the path with the highest value is returned.
	for i in board.available_cols(): 
		value = board.move_value(player, i)
		board.add_piece(player, i)

		b = board.immutable()
		if b in memo: 
			other_val = memo[b]
		else: 
			other_val = SBM(board, depth-1, player, memo)
			try:
				memo[b] = other_val[0]
				other_val = other_val[0]
			except TypeError:
				memo[b] = other_val

		value = value + other_val
		board.rm_piece(i)
		if value > max: 
			max = value
			best_locn = i

	return best_locn#, memo