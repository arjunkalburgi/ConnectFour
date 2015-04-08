from flask import flash, redirect, render_template, request
from app import app

from flask import jsonify 
import copy
from game.Board import board as b
from game.connectfour import SBM as comp
g = b()

@app.route("/")
@app.route("/startup/", methods=['GET', 'POST'])
def start(): 
	return render_template('start.html', 
							title='Connect4')


@app.route("/more/")
def credits(): 
	return render_template('credits.html', 
							title='Connect4')




@app.route('/game/', methods=["GET", "POST"])
def game(): 
	return render_template('game.html', 
							title='Connect4')

@app.route('/user_play/', methods=['POST'])
def user_play(): 
	user_col = request.form['col']
	g.add_piece(2, int(user_col))
	return jsonify(board=g.board)

@app.route('/check_win/', methods=['POST']) 
def check_win(): 
	return jsonify(player=g.check_win())

@app.route('/comp_play/', methods=['POST'])
def comp_play(): 
	# get the parameters 
	difficulty = int(request.form['val'])
	# memo = eval(request.form['memo'])

	# save the board 
	p = copy.deepcopy(g)

	# find the computers best way
	# q, memo = comp(p, difficulty,1,memo)
	q = comp(p, difficulty)

	# add it to the board
	g.add_piece(1,q)

	return jsonify(board=g.board)
	# return jsonify({'board':g.board,'m':str(memo)})

@app.route('/restart/', methods=['POST'])
def restart():
	g.clear_board()
	# g.print_board()
	return jsonify(board=g.board)
