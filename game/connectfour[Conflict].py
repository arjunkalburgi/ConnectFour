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
	if player is None: 
		player = 1
	elif player is 1: 
		player = 2
	elif player is 2: 
		player = 1
	else: 
		print("ERROR")

	if memo is None: 
		memo = {}

	if depth is 0: 
		return 0

	max = -100
	best_locn = board.available_cols()[0]
	for i in board.available_cols(): 
		value = board.move_value(player, i)
		board.add_piece(player, i)

		b = board.immutable()
		if b in memo: 
			other_val = memo[b]
			# print("from memo[curr_board]", other_val)
		else: 
			other_val = SBM(board, depth-1, player, memo)
			# print("from SBM[curr_board]", other_val)
			memo[b] = other_val
		
		print("memo type",type(memo)) 
		print("memo",memo)

		value = value + other_val
		board.rm_piece(i)
		if value > max: 
			max = value
			best_locn = i

	return best_locn, memo