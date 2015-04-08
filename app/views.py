from flask import flash, redirect, render_template, request, session
from app import app

from flask import jsonify 
import copy
from game.Board import board as b
from game.connectfour import SBM as comp
g = b()


# routes for startup, need to render start.html
@app.route("/")
@app.route("/startup/", methods=['GET', 'POST'])
def start(): 
	return render_template('start.html', 
							title='Connect4')


# route for the back page, need to render credits.html 
@app.route("/more/")
def credits(): 
	return render_template('credits.html', 
							title='Connect4')


# route and ajax functions for game page
# takes care of rendering the template, 
@app.route('/game/', methods=["GET", "POST"])
def game(): 
	return render_template('game.html', 
							title='Connect4')

# what to do when the user must play, 
@app.route('/user_play/', methods=['POST'])
def user_play(): 
	# receive the input parameters 
	g.board = eval(request.form['b'])
	user_col = request.form['col']

	# adds a user piece to that column
	g.add_piece(2, int(user_col))

	# returns a json string of the new board
	return jsonify(board=g.board)

# what to do to check if there is a winner, 
@app.route('/check_win/', methods=['POST']) 
def check_win(): 
	# receive the input parameters 
	g.board = eval(request.form['b'])
	# returns a json of the result of check_win()
	return jsonify(player=g.check_win())

# what to do when the computer must play, 
@app.route('/comp_play/', methods=['POST'])
def comp_play(): 
	# receive the input parameters 
	g.board = eval(request.form['b'])
	difficulty = int(request.form['val'])

	# save the board 
	p = copy.deepcopy(g)

	# find the computers best way
	q = comp(p, difficulty)

	# add it to the board
	g.add_piece(1,q)

	# returns a json string of the new board
	return jsonify(board=g.board)

# and what to do when the game is restarted
@app.route('/restart/', methods=['POST'])
def restart():
	# receive the input parameters 
	g.board = eval(request.form['b'])
	
	# clears the board
	g.clear_board()

	# returns a json string of the new board
	return jsonify(board=g.board)