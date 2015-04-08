class board: 
	def __init__(self):
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
		i = 0
		for i in self.board:
			print(i)

	def add_piece(self, player, col): 
		for i, row in enumerate(self.board):
			if i+1 == 7: 
				row[col] = player
				break
			if self.board[i + 1][col] != 0: 
				row[col] = player
				break

	def rm_piece(self, col): 
		for i in range(0,7): 
			if self.board[i][col] is not 0: 
				self.board[i][col] = 0
				break

	def available_cols(self): 
		av_cols = list()
		for i,col in enumerate(self.board[0]): 
			if col is 0: 
				av_cols.append(i)

		return av_cols

	def move_value(self, p, col): 
		'''
		If player p moves to columns col, how many points is that value worth?
		This function is GREEEEEDY

		This Heuristic Function is set up on the logic that setting or breaking
		up a ConnectFour is highest priority. Next is setting up or breaking up 
		a three-ina-row. Next is close to the previous players turn. 
		'''
		# get place of where piece would go. 
		for i, row in enumerate(self.board):
			if  i == 6 or self.board[i + 1][col] != 0: 
				break
				# row is the row of our spot
				# i is the index of the row


		# # check for Connect Four
		# if checkfour(row, col, i, self.board): 
		# 	return 10

		# check for Connect Three
		if checkthree(row, col, i, self.board): 
			return 8

		return 0

	def check_win(self): 
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

	def clear_board(self): 
		self.board = ([0,0,0,0,0,0,0],
					  [0,0,0,0,0,0,0],
					  [0,0,0,0,0,0,0],
					  [0,0,0,0,0,0,0],
					  [0,0,0,0,0,0,0],
					  [0,0,0,0,0,0,0],
					  [0,0,0,0,0,0,0])

	def immutable(self):
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


def checkthree(row, col, i, b): 
	if col == 0: 
		# check for three flat in the row. 
		if row[col+1] == row[col+2]!=0:
			return True
		# check for three diagonal
		if i > 2 and twoupright(b, i, col):
			return True
		if i < 4 and twodownright(b, i, col): 
			return True
	if col == 1: 
		# check for three flat in the row. 
		if row[col+1] == row[col+2]!=0 or \
		 row[col-1] == row[col+1]!=0:
			return True
		# check for three diagonal
		if i > 1 and twoupright(b, i, col):
			return True
		if i < 5 and twodownright(b, i, col): 
			return True
		if i > 0 and i < 5 and leftuprightdown(b,i,col): 
			return True
		if i < 6 and i > 1 and rightupleftdown(b,i,col): 
			return True
	if col == 2: 
		# check for three flat in the row. 
		if row[col+1] == row[col+2]!=0 or \
		 row[col-1] == row[col+1]!=0 or \
		 row[col-2] == row[col-1]!=0: 
			return True
		# check for three diagonal
		if i > 1 and i < 5 and twoupleft(b, i, col): 
			return True
		if i < 5 and i > 1 and twodownleft(b, i, col): 
			return True
		if i > 1 and twoupright(b, i, col):
			return True
		if i < 5 and twodownright(b, i, col): 
			return True
		if i > 0 and i < 6 and (leftuprightdown(b,i,col) or rightupleftdown(b,i,col)): 
			return True
	if col == 3:
		# check for three flat in the row. 
		if row[col+1] == row[col+2]!=0 or \
		 row[col-1] == row[col+1]!=0 or \
		 row[col-2] == row[col-1]!=0 or \
		 row[col-3] == row[col-2]!=0: 
			return True
		# check for three diagonal
		if i > 1 and twoupleft(b, i, col) and twoupright(b, i, col): 
			return True
		if i < 5 and twodownleft(b, i, col) and twodownright(b, i, col): 
			return True
		if i > 0 and i < 6 and (leftuprightdown(b,i,col) or rightupleftdown(b,i,col)): 
			return True
	if col == 4: 
		# check for three flat in the row. 
		if row[col-1] == row[col-2]!=0 or \
		 row[col+1] == row[col-1]!=0 or \
		 row[col+2] == row[col+1]!=0: 
			return True
		# check for three diagonal
		if i > 1 and i < 5 and twoupright(b, i, col): 
			return True
		if i < 5 and i > 1 and twodownright(b, i, col): 
			return True
		if i > 1 and twoupleft(b, i, col):
			return True
		if i < 5 and twodownleft(b, i, col): 
			return True
		if i > 0 and i < 6 and (leftuprightdown(b,i,col) or rightupleftdown(b,i,col)): 
			return True
	if col == 5: 
		# check for three flat in the row. 
		if row[col-1] == row[col-2]!=0 or \
		 row[col+1] == row[col-1]!=0:
			return True
		# check for three diagonal
		if i > 1 and twoupleft(b, i, col):
			return True
		if i < 5 and twodownleft(b, i, col):
			return True
		if i > 0 and i < 5 and rightupleftdown(b,i,col): 
			return True
		if i < 6 and i > 1 and leftuprightdown(b,i,col): 
			return True
	if col == 6: 
		# check for three flat in the row. 
		if row[col-1] == row[col-2]!=0:
			return True
		# check for three diagonal 
		if i > 2 and twoupleft(b, i, col):
			return True
		if i < 4 and twodownleft(b, i, col): 
			return True
	
	# check for three vertical 
	if i < 4: 
		if b[i+1][col] == b[i+2][col]!=0: 
			return True 

	return False

def twoupright(b, i, col): 
	if b[i-1][col+1] == b[i-2][col+2]!=0: 
		return True

def twodownright(b, i, col): 
	if b[i+1][col+1] == b[i+2][col+2]!=0: 
		return True

def twoupleft(b, i, col): 
	if b[i-1][col-1] == b[i-2][col-2]!=0: 
		return True

def twodownleft(b, i, col): 
	if b[i+1][col-1] == b[i+2][col-2]!=0:
		return True

def leftuprightdown(b,i,col): 
	if b[i+1][col+1] == b[i-1][col-1]!=0: 
		return True

def rightupleftdown(b,i,col): 
	if b[i+1][col-1] == b[i-1][col+1]!=0: 
		return True



def checkfour(row, col, i, b): 
	# check for four vertical 	
	if i < 4: 
		if b[i+1][col] == b[i+2][col] and b[i+1][col] == b[i+3][col]!=0: 
			return True

	if col == 0: 
		# check for four flat in the row. 
		if row[col+1] == row[col+2] and row[col+2] == row[col+3]!=0:
			return True
		if i > 2 and dia1con1(i,b,col):
			return True
		if i < 4 and dia2con1(i,b,col):
			return True

	if col == 1: 
		# check for four flat in the row. 
		if row[col+1] == row[col+2] and row[col+2] == row[col+3]!=0 or \
		 row[col-1] == row[col+1] and row[col+1] == row[col+2]!=0:
			return True
		if i>2 and dia1con1(i,b,col):
			return True
		if i<4 and dia2con1(i,b,col):
			return True
		if i>1 and i<6 and dia1con2(i,b,col):
			return True
		if i>0 and i<5 and dia2con2(i,b,col):
			return True

	if col == 2: 
		# check for four flat in the row. 
		if row[col+1] == row[col+2] and row[col+2] == row[col+3]!=0 or \
		 row[col-1] == row[col+1] and row[col+1] == row[col+2]!=0 or \
		 row[col-2] == row[col-1] and row[col-1] == row[col+1]!=0: 
			return True
		if i>2 and dia1con1(i,b,col):
			return True
		if i<4 and dia2con1(i,b,col):
			return True
		if i>1 and i<6 and (dia1con2(i,b,col) or dia2con3(i,b,col)):
			return True
		if i>0 and i<5 and (dia2con2(i,b,col) or dia1con3(i,b,col)):
			return True

	if col == 3:
		# check for four flat in the row. 
		if row[col+1] == row[col+2] and row[col+2] == row[col+3]!=0 or \
		 row[col-1] == row[col+1] and row[col+1] == row[col+2] or \
		 row[col-2] == row[col-1] and row[col-1] == row[col+1]!=0 or \
		 row[col-3] == row[col-2] and row[col-2] == row[col-1]!=0: 
			return True
		if i>2 and (dia1con1(i,b,col) or dia2con4(i,b,col)):
			return True
		if i<4 and (dia2con1(i,b,col) or dia1con4(i,b,col)):
			return True
		if i>1 and i<6 and (dia1con2(i,b,col) or dia2con3(i,b,col)):
			return True
		if i>0 and i<5 and (dia2con2(i,b,col) or dia1con3(i,b,col)):
			return True

	if col == 4: 
		# check for four flat in the row. 
		if row[col-1] == row[col-2] and row[col-2] == row[col-3]!=0 or \
		 row[col+1] == row[col-1] and row[col-1] == row[col-2]!=0 or \
		 row[col+2] == row[col+1] and row[col+1] == row[col-1]!=0: 
			return True
		if i>2 and dia2con4(i,b,col):
			return True
		if i<4 and dia1con4(i,b,col):
			return True
		if i>1 and i<6 and (dia1con2(i,b,col) or dia2con3(i,b,col)):
			return True
		if i>0 and i<5 and (dia2con2(i,b,col) or dia1con3(i,b,col)):
			return True

	if col == 5: 
		# check for four flat in the row. 
		if row[col-1] == row[col-2] and row[col-2] == row[col-3]!=0 or \
		 row[col+1] == row[col-1] and row[col-1] == row[col-2]!=0:
			return True
		if i>2 and dia2con4(i,b,col):
			return True
		if i<4 and dia1con4(i,b,col):
			return True
		if i>1 and i<6 and dia2con3(i,b,col):
			return True
		if i>0 and i<5 and dia1con3(i,b,col):
			return True

	if col == 6: 
		# check for four flat in the row. 
		if row[col-1] == row[col-2] and row[col-2] == row[col-3]!=0:
			return True
		if i>2 and dia2con4(i,b,col):
			return True
		if i<4 and dia1con4(i,b,col):
			return True
	
	return False

#diagonal1: /
#0123 i>2, c<4
def dia1con1(i,b,c):
	if b[i-1][c+1] == b[i-2][c+2] and b[i-2][c+2] == b[i-3][c+3]!=0:
		return True
#1012 1<i<6, 0<c<6
def dia1con2(i,b,c):
	if b[i+1][c-1] == b[i-1][c+1] and b[i-1][c+1] == b[i-2][c+2]!=0:
		return True
#2101 0<i<5, 1<c<6
def dia1con3(i,b,c):
	if b[i+2][c-2] == b[i+1][c-1] and b[i-1][c+1] == b[i+1][c-1]!=0:
		return True
#3210 i<4, 2<c
def dia1con4(i,b,c):
	if b[i+3][c-3] == b[i+2][c-2] and b[i+2][c-2] == b[i+1][c-1]!=0:
		return True

#diagonal2: \
#0123 i<2, c<2
def dia2con1(i,b,c):
	if b[i+1][c+1] == b[i+2][c+2] and b[i+2][c+2] == b[i+2][c+3]!=0:
		return True
#1012 0<i<5, 0<c<5
def dia2con2(i,b,c):
	if b[i-1][c-1] == b[i+1][c+1] and b[i+1][c+1] == b[i+2][c+2]!=0:
		return True
#2101 1<i<6, 1<c<6
def dia2con3(i,b,c):
	if b[i-2][c-2] == b[i-1][c-1] and b[i-1][c-1] == b[i+1][c+1]!=0:
		return True
#3210 2<i, 2<c
def dia2con4(i,b,c):
	if b[i-3][c-3] == b[i-2][c-2] and b[i-2][c-2] == b[i-1][c-1]!=0:
		return True


