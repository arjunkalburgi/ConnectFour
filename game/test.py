from Board import board as b
from connectfour import SBM as comp # get_best_move 
import copy

def playgame():
	g = b()

	g.print_board()

	for i in range(0, 10): 
		print("")
		user_col = int(input("Hey bro, where do you want to put the value? ")) - 1
		g.add_piece(2, user_col)

		# check for a connect four.
		g.print_board()
		if g.check_win(): 
			print("Congratulations!!")
			break

		print("")
		print("Alright, my turn")
		# save the board 
		p = copy.deepcopy(g)
		# find the computers best way
		q = comp(p, 5)

		# add it to the board
		g.add_piece(1,q)

		# check for a connect four.
		g.print_board()
		if g.check_win(): 
			print("Congratulations!!")
			break

playgame()

if input("Play again? (y/n) ") == "y": 
	print(" ")
	print("ALRIGHT")
	playgame()
else: 
	pass
