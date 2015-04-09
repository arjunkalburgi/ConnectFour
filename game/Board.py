class board: 
	def __init__(self):
		'''
		define a board as having 7 columns, 7 rows 
		and a board that is a tuple of lists. 

		Initializing it as a tuple of lists means that
		we won't be able to change the tuple's elements by
		accident, but we can change the list's elements in
		order to manipulate the board.
		'''
		self.columns = 7
		self.rows = 7

		self.board = ([0,0,0,0,0,0,0],
					  [0,0,0,0,0,0,0],
					  [0,0,0,0,0,0,0],
					  [0,0,0,0,0,0,0],
					  [0,0,0,0,0,0,0],
					  [0,0,0,0,0,0,0],
					  [0,0,0,0,0,0,0])

	def print_board(self): 
		'''
		prints the board nicely
		'''
		i = 0
		for i in self.board:
			print(i)

	def add_piece(self, player, col): 
		'''
		Arguments: The player, and the column

		Function: add_piece puts the piece of the 
		player (in the game the computer is 1 and the 
		user is 2) at the lowest available spot in the column 
		'''
		for i, row in enumerate(self.board):
			if i+1 == 7: 
				row[col] = player
				break
			if self.board[i + 1][col] != 0: 
				row[col] = player
				break

	def rm_piece(self, col): 
		'''
		Takes the topmost piece of a column out
		'''
		for i in range(0,7): 
			if self.board[i][col] is not 0: 
				self.board[i][col] = 0
				break

	def available_cols(self): 
		'''
		Returns a list of all the columns that are 
		not full. The function only checks the top row 
		of the board.
		'''
		av_cols = list()
		for i,col in enumerate(self.board[0]): 
			if col is 0: 
				av_cols.append(i)

		return av_cols

	def check_win(self): 
		'''
		Function looks for a four in three possible scenarios:
		in a row, in a column and diagonally. To check diagonally, 
		it needs to look diagonally both ways (up to the left and 
		up to the right). However to avoid trying to access elements
		that don't exist, the function goes through the first 3 elements 
		in the columns and in the rows. This increases the number of cases
		by needing to check down to the left and and down to the right to
		make sure to get them all. 
		'''
		# check row
		for row in self.board: # rows
			for i in range(0,4): # columns
				if row[i] == row[i+1] == row[i+2] == row[i+3] != 0: 
					print("heyyyy player", row[i], "woooooonnnnn")
					return row[i]
		
		# check vertical
		for i in range(0,7): # columns
			for j in range(0,4):  # rows
				if self.board[j][i] == self.board[j+1][i] == self.board[j+2][i] == self.board[j+3][i] != 0: 
					print("heyyyy player", self.board[j][i], "woooooonnnnn")
					return self.board[j][i]
		
		# check diagonal
		for j in range(0,4): # rows
			for i in range(0,4): 
				# down right
				if self.board[j][i] == self.board[j+1][i+1] == self.board[j+2][i+2] == self.board[j+3][i+3] != 0: 
					print("heyyyy player", self.board[j][i], "woooooonnnnn")
					return self.board[j][i]
				# down left 
				if self.board[j][6-i] == self.board[j+1][5-i] == self.board[j+2][4-i] == self.board[j+3][3-i] != 0: 
					print("heyyyy player", self.board[j][6-i], "woooooonnnnn")
					return self.board[j][6-i]
				# up right
				if self.board[6-j][i] == self.board[5-j][i+1] == self.board[4-j][i+2] == self.board[3-j][i+3] != 0: 
					print("heyyyy player", self.board[6-j][i], "woooooonnnnn")
					return self.board[6-j][i]
				# up left
				if self.board[6-j][6-i] == self.board[5-j][5-i] == self.board[4-j][4-i] == self.board[3-j][3-i] != 0: 
					print("heyyyy player", self.board[6-j][6-i], "woooooonnnnn")
					return self.board[6-j][6-i]
		return False

	def move_value(self, p, col): 
		'''
		If player p moves to columns col, how many points is that value worth?
		This function is GREEEEEDY

		This Heuristic Function is set up on the logic that setting or breaking
		up a ConnectFour is highest priority. Next is setting up or breaking up 
		a three-in-a-row. Next is close to the previous players turn. 
		'''
		# get place of where piece would go. 
		for i, row in enumerate(self.board):
			if  i == 6 or self.board[i + 1][col] != 0: 
				break
				# row is the row of our spot
				# i is the index of the row

		# check for any three in a row
		h = checkthree2(row, col, i, self.board)
		if h: 
			# if playing as p2 and the connect line 
			# is a line for p2, then two will win.
			# this case should be marked low.
			if h == p == 2:
				return -8
			else: 
				return 8 

		return 0

	def clear_board(self): 
		'''
		simply resets the board to all 0's
		'''
		self.board = ([0,0,0,0,0,0,0],
					  [0,0,0,0,0,0,0],
					  [0,0,0,0,0,0,0],
					  [0,0,0,0,0,0,0],
					  [0,0,0,0,0,0,0],
					  [0,0,0,0,0,0,0],
					  [0,0,0,0,0,0,0])

	def immutable(self):
		'''
		returns the tuple of lists as a tuple of tuples. 
		'''
		return (tuple(self.board[0]), tuple(self.board[1]), tuple(self.board[2]), tuple(self.board[3]), \
			 tuple(self.board[4]), tuple(self.board[5]), tuple(self.board[6]))

	# overwriting equ
	def __eq__(self, other):
		if isinstance(other, self.__class__):
			return self.board == other.board
		else:
			return False

	def __ne__(self, other): 
		if __eq__(other): 
			return False
		else: 
			return True

	# overwriting greater/lesser
	def __gt__(self, other): 
		if self.get_value > other.get_value: 
			return True
		else: 
			return False

	def __lt__(self, other): 
		if __gt__(self, other): 
			return False
		else: 
			return True


def checkthree2(row, col, i, b): 
	if col == 0: 
		# check for three flat in the row. 
		if row[col+1] == row[col+2]!=0:
			return row[col+1]
		# check for three diagonal
		if i > 2 and twoupright2(b, i, col):
			return twoupright2(b, i, col)
		if i < 4 and twodownright2(b, i, col): 
			return twodownright2(b, i, col)
	if col == 1: 
		# check for three flat in the row. 
		if row[col+1] == row[col+2]!=0:
			return row[col+1]
		if row[col-1] == row[col+1]!=0:
			return row[col+1]
		# check for three diagonal
		if i > 1 and twoupright2(b, i, col):
			return twoupright2(b, i, col)
		if i < 5 and twodownright2(b, i, col): 
			return twodownright2(b, i, col)
		if i > 0 and i < 5 and leftuprightdown2(b,i,col): 
			return leftuprightdown2(b,i,col)
		if i < 6 and i > 1 and rightupleftdown2(b,i,col): 
			return rightupleftdown2(b,i,col)
	if col == 2: 
		# check for three flat in the row. 
		if row[col+1] == row[col+2]!=0:
			return row[col+1]
		if row[col-1] == row[col+1]!=0:
			return row[col-1]
		if row[col-2] == row[col-1]!=0: 
			return row[col-2]
		# check for three diagonal
		if i > 1 and i < 5 and twoupleft2(b, i, col): 
			return twoupleft2(b, i, col)
		if i < 5 and i > 1 and twodownleft2(b, i, col): 
			return twodownleft2(b, i, col)
		if i > 1 and twoupright2(b, i, col):
			return twoupright2(b, i, col)
		if i < 5 and twodownright2(b, i, col): 
			return twodownright2(b, i, col)
		if i > 0 and i < 6 and leftuprightdown2(b,i,col): 
			return leftuprightdown2(b,i,col)
		if i > 0 and i < 6 and rightupleftdown2(b,i,col): 
			return rightupleftdown2(b,i,col)
	if col == 3:
		# check for three flat in the row. 
		if row[col+1] == row[col+2]!=0:
			return row[col+1]
		if row[col-1] == row[col+1]!=0:
			return row[col+1]
		if row[col-2] == row[col-1]!=0:
			return row[col-1]
		if row[col-3] == row[col-2]!=0: 
			return row[col-2]
		# check for three diagonal
		if i > 1 and twoupleft2(b, i, col):
			return twoupleft2(b, i, col)
		if i > 1 and twoupright2(b, i, col): 
			return twoupright2(b, i, col)
		if i < 5 and twodownleft2(b, i, col):
			return twodownleft2(b, i, col)
		if i < 5 and twodownright2(b, i, col): 
			return twodownright2(b, i, col)
		if i > 0 and i < 6 and leftuprightdown2(b,i,col): 
			return leftuprightdown2(b,i,col)
		if i > 0 and i < 6 and rightupleftdown2(b,i,col): 
			return rightupleftdown2(b,i,col)
	if col == 4: 
		# check for three flat in the row. 
		if row[col-1] == row[col-2]!=0:
			return row[col-1]
		if row[col+1] == row[col-1]!=0:
			return row[col-1]
		if row[col+2] == row[col+1]!=0: 
			return row[col+1]
		# check for three diagonal
		if i > 1 and i < 5 and twoupright2(b, i, col): 
			return twoupright2(b, i, col)
		if i < 5 and i > 1 and twodownright2(b, i, col): 
			return twodownright2(b, i, col)
		if i > 1 and twoupleft2(b, i, col):
			return twoupleft2(b, i, col)
		if i < 5 and twodownleft2(b, i, col): 
			return twodownleft2(b, i, col)
		if i > 0 and i < 6 and rightupleftdown2(b,i,col): 
			return rightupleftdown2(b,i,col)
		if i > 0 and i < 6 and leftuprightdown2(b,i,col): 
			return leftuprightdown2(b,i,col)
	if col == 5: 
		# check for three flat in the row. 
		if row[col-1] == row[col-2]!=0:
			return row[col-1]
		if row[col+1] == row[col-1]!=0:
			return row[col+1]
		# check for three diagonal
		if i > 1 and twoupleft2(b, i, col):
			return twoupleft2(b, i, col)
		if i < 5 and twodownleft2(b, i, col):
			return twodownleft2(b, i, col)
		if i > 0 and i < 5 and rightupleftdown2(b,i,col): 
			return rightupleftdown2(b,i,col)
		if i < 6 and i > 1 and leftuprightdown2(b,i,col): 
			return leftuprightdown2(b,i,col)
	if col == 6: 
		# check for three flat in the row. 
		if row[col-1] == row[col-2]!=0:
			return row[col-1]
		# check for three diagonal 
		if i > 2 and twoupleft2(b, i, col):
			return twoupleft2(b, i, col)
		if i < 4 and twodownleft2(b, i, col): 
			return twodownleft2(b, i, col)
	
	# check for three vertical 
	if i < 4: 
		if b[i+1][col] == b[i+2][col]!=0: 
			return b[i+1][col] 

	return False

def twoupright2(b, i, col): 
	if b[i-1][col+1] == b[i-2][col+2]!=0: 
		return b[i-1][col+1]

def twodownright2(b, i, col): 
	if b[i+1][col+1] == b[i+2][col+2]!=0: 
		return b[i+1][col+1]

def twoupleft2(b, i, col): 
	if b[i-1][col-1] == b[i-2][col-2]!=0: 
		return b[i-1][col-1]

def twodownleft2(b, i, col): 
	if b[i+1][col-1] == b[i+2][col-2]!=0:
		return b[i+1][col-1]

def leftuprightdown2(b,i,col): 
	if b[i+1][col+1] == b[i-1][col-1]!=0: 
		return b[i+1][col+1]

def rightupleftdown2(b,i,col): 
	if b[i+1][col-1] == b[i-1][col+1]!=0: 
		return b[i+1][col-1]
