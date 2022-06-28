# Ali Alkhars
# K20055566
# Lab 23
#
# TrainingSession(0.3, 0.1, 0.4, True, 30000)
# TrainingSession(0.3, 0.1, 0.4, False, 30000)
"""
Author: Jeffery Raphael, Ali Alkhars
Date: Feb. 2020
Version: 2.0

This module is used for labs 23 and 23b.
"""

import random

class TicTacToe :

	"""
	This class represents the TicTacToe board. It draws the board and keeps track
	of the moves that have been made.
	"""

	def __init__(self) :

		"""
		This is the constructor.  It creates a new empty board. Internally,
		the board is a 2D list.  Empty squares are denotes with a single
		asterisk '*'
		"""

		self.board = [['*', '*', '*'], ['*', '*', '*'], ['*', '*', '*']]
		self.moveCount = 0
		self.lastMove = None


	def isGameOver(self) :
		"""
		This method determines if the game is over.

		return: True if someone has won or the came is drawn, otherwise it
				returns false
		"""
		if self.moveCount >= 9:
			return True

		if self.isGameWon('X'):
			return True

		if self.isGameWon('O'):
			return True

		return False


	def isGameDraw(self) :

		"""
		This method determines if the game is a draw

		return: True if game is a draw (no has won), otherwise it returns False
		"""
		if self.moveCount >= 9:
			return True

		return False


	def isGameWon(self, mark):

		"""
		This method checks to see if a player, specified by mark, has won the
		game

		param mark: A letter, e.g., 'X' or 'O'
		return: True if 'mark' has won the game, other false
		"""

		for r in range(3):
			row = self.board[r]
			if self.isSameAs(mark, row[0], row[1], row[2]):
				return True

		for c in range(3):
			if self.isSameAs(mark, self.board[0][c], self.board[1][c], self.board[2][c]):
				return True

		if self.isSameAs(mark, self.board[0][0], self.board[1][1], self.board[2][2]):
			return True

		if self.isSameAs(mark, self.board[0][2], self.board[1][1], self.board[2][0]):
			return True

		return False


	def isSameAs(self, char, a, b, c):

		"""
		This methods checks if all four parameters are equal

		param char:  A character, e.g., 'X' or 'O'
		param a: A character, e.g., 'X' or 'O' or '*'
		param b: A character, e.g., 'X' or 'O' or '*'
		param c: A character, e.g., 'X' or 'O' or '*'
		return: True if all four characters are the same otherwise false
		"""

		if char == a and a == b and b == c:
			return True

		return False


	def drawBoard(self):

		"""
		This method displays the game on the screen.  It can only display the
		letters X and O.
		"""

		letterX = ['  X     X  ', '   X   X   ', '    X X    ', \
					'     X     ', '    X X    ', '   X   X   ', '  X     X  ']
		letterO = ['   OOOOO   ', '  O     O  ', '  O     O  ', \
					'  O     O  ', '  O     O  ', '  O     O  ', '   OOOOO   ']

		tmp = []
		tmp.append((' ' * 11) + '@' + (' ' * 11) + '@' + (' ' * 11))
		for i in range(3):
			row = self.board[i]

			for j in range(7):
				msg = ""
				for k in range(3):
					if row[k] == 'X':
						msg += letterX[j]
					elif row[k] == 'O':
						msg += letterO[j]
					else:
						msg += ' ' * 11

					if k != 2:
						msg += '@'

				tmp.append(msg)

			if i != 2:
				tmp.append((' ' * 11) + '@' + (' ' * 11) + '@' + (' ' * 11))
				tmp.append('@' * 35)
				tmp.append((' ' * 11) + '@' + (' ' * 11) + '@' + (' ' * 11))

		tmp.append((' ' * 11) + '@' + (' ' * 11) + '@' + (' ' * 11))
		print("\n\n")
		for line in tmp:
			print(line)
		print("\n\n")


	def makeMove(self, location, mark):

		"""
		This method puts a letter (mark) on the board, at location, if it's
		legal to do so.

		param location: A list, [x,y] where x and y are coordinates on
				tictactoe board (1 <= x <= 3 and 1 <= y <= 3)
		param mark: The letter, 'X' or 'O'
		return: True if x, y is within bounds and the square has not been
				marked already; false for all other
				conditions
		"""

		if 1 <= location[0] <= 3 and 1 <= location[1] <= 3:

			if self.board[location[1] - 1][location[0] - 1] != '*':
				return False

			self.board[location[1] - 1][location[0] - 1] = mark
			self.moveCount += 1
			self.lastMove = location[:]
			return True

		return False


	def getEmptySpaces(self) :

		"""
		This method returns a list of empty locations on the board.  In other
		words, it searches for '*' and adds that location to the list

		return: A list, e.g., [[x1,y1],...,[xn, yn]] where location x,y is
				empty.
		"""

		moves = []

		for r in range(len(self.board)):
			for c in range(len(self.board[0])):
				if self.board[r][c] == '*':
					moves.append([c+1,r+1])

		return moves


	def copy(self) :

		"""
		This method makes a copy of the tictactoe board.

		return: A new Tictactoe board with all the moves copied to it.
		"""

		newBoard = TicTacToe()
		newBoard.board = []

		for item in self.board:
			newBoard.board.append(item[:])

		newBoard.moveCount = self.moveCount

		return newBoard


	def getAllChildren(self, letter):

		"""
		This method returns a list of tictactoe boards covering all remaining
		legal moves with 'letter'

		param letter:  An 'X' or 'O' which will be used to make moves
		return: List containing TicTacToe objects.  Each board in the list is
				copy of the original board but a move has been made with
				'letter'.  If the board has no children (there's no place to
				make a move on the board) then the method returns an empty list.
		"""

		children = []
		locs = self.getEmptySpaces()

		for loc in locs:
			cp = self.copy()
			cp.makeMove(loc, letter)
			children.append(cp)

		return children


	def getKey(self, letter) :

		"""
		This method transform the 2D list which represents the board into
		a single string to be used as a key. In the key, the Xs and Os are
		replaced with L and T where L represents the letter (X or O) used
		by the learning agent and the T is the opponent. This allows
		the agent to learn by playing as X or O.

		param letter: the letter used by the learning agent.
		return: A string, 9 characters long, of Ls, Ts and *s.
		"""

		r = ""

		for item in self.board:
			tmp = "".join(item)
			r += tmp

		r = r.replace(letter, 'L')
		if letter == 'X' :
			r = r.replace('O', 'T')
		else:
			r = r.replace('X', 'T')

		return r


class Player :

	"""
	This class represents a person or agent playing tictactoe. When it's
	completed it will be able to simulate a random, RL and MiniMax player.  The
	Player class also allows human's to play.
	"""

	def __init__(self, letter, playerType='HUMAN') :

		"""
		This is the constructor.  It creates a new player. When creating
		a Player you have to specify a letter and player type.  The
		letter is either 'X' or 'O' (both capitilised).  The player type
		can be: 'HUMAN', 'MINIMAX', 'RANDOM' or 'RL'. Note, the default
		is 'HUMAN'.

		param letter: The letter the player uses, can only be 'X' or 'O'
		param playerType: The type of player 'HUMAN', 'MINIMAX', 'RL' OR
				'RANDOM'
		"""

		self.letter = letter
		self.opponent = 'O'

		if letter == 'O':
			self.opponent = 'X'

		self.playerType = playerType

		self.name = "Unknown"
		self.rating = 1200
		self.gamesW = 0
		self.gamesD = 0
		self.gamesL = 0
		self.valueFunction = {}
		self.epsilon = 0.02


	def makeMove(self, board) :

		"""
		This method performs a move for the player.  The move is
		determined by the player type. If player type is MINIMAX then the
		MiniMax algorithm is used to find a move. If player type is
		RANDOM then a random move is made.  If the player type is HUMAN
		then the program ask the user to enter a move.  Lastly, if the
		player type is 'RL' then the state value table is used to select
		the move with the highest value.

		param board: A TicTacToe object
		return: True if a legal move was made and False if the user
				wants to quit (only HUMAN players can quit the game)
		"""

		if self.playerType == 'MINIMAX':
			return self.getMiniMaxMove(board)
		elif self.playerType == 'RANDOM':
			return self.getRandomMove(board)
		elif self.playerType == 'RL':
			return self.getRLMove(board)
		else :
			return self.getHumanMove(board)


	def requestMove(self) :

		"""
		This method ask the user to enter a move.  There is little input
		validation; it's best to enter 3 characters: x-coordinate, a comma
		and the y-coordinate.  For example, 2,1.  Valid coordinates are 1, 2
		or 3.

		return: A list with 2 numbers, the first is the x-coordinate and the
				second is the y-coordinate, e.g., [2,1]
		"""

		userInput = input("Player " + self.letter + ", enter a move (e.g. 1,1) : ")
		userInput = userInput.strip()

		if userInput == "quit":
			return None

		return [int(userInput[0]), int(userInput[2])]


	def getHumanMove(self, board) :

		"""
		This method allows a user, HUMAN, to enter his or her move

		param board: A TicTacToe object
		return: True if the move is legal and false if the user entered 'quit'
		"""

		moveLegal = False

		while not moveLegal:
			playerMove = self.requestMove()

			if playerMove is None :
				return False
			else :
				moveLegal = board.makeMove(playerMove, self.letter)

		return True


	def getRandomMove(self, board):

		"""
		This method will be implemented by the student as part of lab 23.

		It will select a random move and then call board.makeMove(...).
		This method should be similar to getHumanMove(...)

		param board: A TicTacToe object
		return: Always returns True
		"""
		isMoveLegal = False

		while not isMoveLegal:
			x = random.randint(1, 3)
			y = random.randint(1, 3)
			isMoveLegal = board.makeMove([x, y], self.letter)

		return True


	def getRLMove(self, board) :

		"""
		This method performs a move based on the learned policy.  It
		first searches the state value table for a move with the
		highest value.  If one isn't found (i.e., it never experienced
		that board or state) a random move is selected.

		param board: A TicTacToe object
		return: It always returns True; either it finds a move in
				it's value table or it performs a random move.

		"""

		boards = board.getAllChildren(self.letter)
		bestBoard = None
		bestValue = -999
		haveBest = False
		playerMove = None

		for tmp in boards:

			if tmp.getKey(self.letter) in self.valueFunction :
				if self.valueFunction[tmp.getKey(self.letter)] > bestValue :
					bestValue = self.valueFunction[tmp.getKey(self.letter)]
					bestBoard = tmp
					haveBest = True

		if haveBest :
			playerMove = bestBoard.lastMove
		else :
			anyone = random.choice(boards)
			playerMove = anyone.lastMove

		moveLegal = board.makeMove(playerMove, self.letter)

		return True


	def getMiniMaxMove(self, board):

		"""
		This method calls the minimax algorithm method to find an optimal moves.

		param board: A TicTacToe object
		return: True if the move is legal and false if the minimax method returns
				None type for the optimal move
		"""

		playerMove = self.minimax(board)

		if playerMove is None :
			return False
		else :
			moveLegal = board.makeMove(playerMove, self.letter)

		return True


	def minimax(self, board):

		"""
		This method will be implemented by the student as part of lab 24.

		It uses a recursive helper method to search the game tree for an
		optimal move.

		param board: A TicTacToe object
		return: The best move, e.g., [x,y], and the score of the move
		"""
		childrenNodes = board.getAllChildren(self.letter)
		bestScore = -999
		bestChild = None

		for child in childrenNodes:
			score = self.minimaxHelper(child, False)

			if score > bestScore:
				bestScore = score
				bestChild = child

		return bestChild.lastMove


	def minimaxHelper(self, board, maximiser):

		"""
		This method will be implemented by the student as part of lab 24.

		It is a recursive method that will search a game tree for an optimal
		move.

		param board: A TicTacToe object
		param maximiser: True if it's the maximiser's turn and false if it's
				the minimiser's turn
		return: The score of the move (board) based on the minimax algorithm
		"""
		if board.isGameOver():
			return self.scoreGame(board)

		score = []
		childrenNodes = None
		bestScore = -999

		if maximiser:
			childrenNodes = board.getAllChildren(self.letter)
		else:
			childrenNodes = board.getAllChildren(self.opponent)

		for child in childrenNodes:
			score.append(self.minimaxHelper(child, not maximiser))

		if maximiser:
			bestScore = max(score)
		else:
			bestScore = min(score)

		return bestScore


	def scoreGame(self, board):

		"""
		This method will be implemented by the student as part of lab 24.

		This method will assign a score to the board.

		param board:  A TicTacToe object
		return: 10 if the player won, -10 if the opponent won, and 0 for all other
				conditions
		"""
		if board.isGameWon(self.letter):
			return 10

		if board.isGameWon(self.opponent):
			return -10

		return 0


	def train(self, opponent, session) :

		"""
		This method executes n (as specified by session.games) tictactoe
		games

		param opponent: The RL agent has to play against another player
					to learn how to play. opponent is another instance
					of Player, however, this should be 'RANDOM' or
					'MINIMAX'
		param session: A TrainingSession object
		"""

		for i in range(session.games) :
			board = TicTacToe()
			self.episode(board, opponent, session)


	def getValueOf(self, board):

		"""
		This method returns the value of the given board from the dictionary valueFunction

		:param board: A TicTacToe object
		:return: the value of the key from valueFunction, if not found returns 0
		"""
		key = board.getKey(self.letter)

		if key in self.valueFunction:
			return self.valueFunction[key]
		else:
			self.valueFunction[key] = 0
			return 0


	def twoLinked(self, board, key, lastMove):

		"""
		This methods checks if the last move made two letters connected

		:param board: A TicTacToe object
		:param key: A string containing the key of the last move
		:param lastMove: A list containing the coordinates of the last move
		:return: True if the lastMove links two letters, otherwise False
		"""
		if (lastMove != [2,2] and key[4] == "L") or (lastMove == [2,2] and board.moveCount > 2):
			return True
		if lastMove == [3,1] and (key[1] == "L" or key[5] == "L"):
			return True
		if lastMove == [2,1] and (key[0] == "L" or key[2] == "L"):
			return True
		if lastMove == [1,1] and (key[1] == "L" or key[3] == "L"):
			return True
		if lastMove == [3,2] and (key[2] == "L" or key[8] == "L"):
			return True
		if lastMove == [1,2] and (key[0] == "L" or key[6] == "L"):
			return True
		if lastMove == [2,3] and (key[6] == "L" or key[8] == "L"):
			return True
		if lastMove == [1,3] and (key[3] == "L" or key[7] == "L"):
			return True
		if lastMove == [3,3] and (key[5] == "L" or key[7] == "L"):
			return True

		return False


	def episode(self, board, opponent, session) :

		"""
		This method will be implemented by the student as part of lab 23

		This method executes a single tictactoe game and updates
		the state value table after every move played by the RL agent.

		param board: A TicTacToe object
		param opponent: The RL agent has to play against another player
					to learn how to play. opponent is another instance
					of Player, however, this should be 'RANDOM' or
					'MINIMAX'
		"""
		result = True
		turn = 0
		previousState = board.copy()

		while not board.isGameOver() and result:
			if turn > 1:
				turn = 0

			agentMoved = False

			if (turn == 0 and session.agentFirst) or (turn == 1 and not session.agentFirst):
				result = self.makeTrainingMove(board, session.epsilon)
				agentMoved = True
			else:
				result = opponent.makeMove(board)

			if agentMoved:
				reward = self.getReward(board)
				v_st1 = self.getValueOf(board)
				v_st0 = self.getValueOf(previousState)
				key = previousState.getKey(self.letter)
				self.valueFunction[key] = v_st0 + session.learningRate * (reward + (session.discountRate * v_st1) - v_st0)
				previousState = board.copy()

			turn += 1

		reward = self.getReward(board)
		v_st1 = self.getValueOf(board)
		key = board.getKey(self.letter)
		self.valueFunction[key] = v_st1 + (session.learningRate * reward)


	def getReward(self, board) :

		"""
		This method will be implemented by the student as part of lab 23

		This method analyses the board and determines a reward.  The
		exact reward scheme will be designed by the student.

		param board: A TicTacToe object
		return: This will be determined by the student.  However, it
				should return an integer value (negative or positive)
		"""

		if board.isGameOver():
			if board.isGameWon(self.letter):
				return 10
			if board.isGameWon(self.opponent):
				return -1
			if board.isGameDraw():
				return 3

		key = board.getKey(self.letter)
		lastMove = board.lastMove

		# RL is first move, goes to a corner
		if board.moveCount == 1 and (lastMove == [1,1] or lastMove == [3,1] or lastMove == [1,3] or lastMove == [3,3]):
			return 5
		# RL is second move and opponent didn't go to a corner, goes to a corner
		if board.moveCount == 2 and (key[0] != "T" and key[2] != "T" and key[6] != "T" and key[8] != "T") and (lastMove == [1,1] or lastMove == [3,1] or lastMove == [1,3] or lastMove == [3,3]):
			return 5

		# RL is second move and opponent goes to a corner, goes to middle
		if board.moveCount == 2 and (key[0] == "T" or key[2] == "T" or key[6] == "T" or key[8] == "T") and lastMove == [2,2]:
			return 5

		# Two letters next to each other
		if self.twoLinked(board, key, lastMove):
			return 2

		return 0

	def makeTrainingMove(self, board, epsilon) :

		"""
		This method will be implemented by the student as part of lab 23

		This method performs moves for the RL agent while it's in
		training. It will either select a move at random (for
		exploration) or select the best move according to the state
		value table (for exploitation).

		param board: A TicTacToe object
		param epsilon: This variable controls how often the RL agent
					exploits it's state value table rather then explore
					new moves
		return: Always returns True
		"""
		n = random.random()

		if n < epsilon:
			return self.getRandomMove(board)
		else:
			boards = board.getAllChildren(self.letter)
			bestBoards = []
			bestValue = -999
			haveBest = False

			for state in boards:
				key = state.getKey(self.letter)

				if key in self.valueFunction:
					if self.valueFunction[key] >= bestValue:
						bestValue = self.valueFunction[key]
						bestBoards.append(state)
						haveBest = True

			if haveBest:
				astate = random.choice(bestBoards)
			else:
				astate = random.choice(boards)

			playerMove = astate.lastMove
			moveLegal = board.makeMove(playerMove, self.letter)

		return True


class Tournament :

	"""
	This class performs a tournament between two tictactoe players.
	Four games are played where each player gets to go first twice.
	By default the board is not drawn.  If a human is playing in the
	tournament, call enableHumanPlayer() to show the board.
	"""

	def __init__(self):

		"""
		This is the constructor.  It creates a new tournament.
		By default the board is not drawn.
		"""

		self.humanPlaying = False

	def enableHumanPlayer(self) :
		"""
		This method enables the board drawing, i.e., if called
		the board is drawn during the tournament.  This should only
		be used if one of the players is human.
		"""

		self.humanPlaying = True


	def start(self, player1, player2) :
		"""
		This method performs the tournament.  Four games are played.
		Each player gets to go first in 2 of the four games.

		param player1: A Player object
		param player2: A Player object
		"""

		winner = self.game(player1, player2)
		self.elo(player1, player2, winner)

		winner = self.game(player1, player2)
		self.elo(player1, player2, winner)

		winner = self.game(player2, player1)
		self.elo(player2, player1, winner)

		winner = self.game(player2, player1)
		self.elo(player2, player1, winner)


	def game(self, p1, p2) :

		"""
		This method executes a single game of tictactoe between
		player1 and player2

		param player1: A Player object
		param player2: A Player object
		return: 1 if player1 won, 2 if player2 won, otherwise -1
		"""

		board = TicTacToe()

		if self.humanPlaying :
			board.drawBoard()

		players = [p1, p2]
		turn = 0
		result = True
		winner = -1

		while not board.isGameOver() and result:

			if turn > 1:
				turn = 0

			result = players[turn].makeMove(board)

			if self.humanPlaying :
				board.drawBoard()

			if result :
				if board.isGameWon(players[turn].letter) :
					winner = turn + 1

			turn += 1

		return winner


	def elo(self, player1, player2, winner) :

		"""
		This method updates each players rating according to the ELO rating
		system

		param player1: A Player object
		param player2: A Player object
		param winner: integer identifying the winner, 1 or 2
		"""

		K = 30
		qa = 10**(player1.rating/400)
		qb = 10**(player2.rating/400)

		e1 = qa / (qa + qb)
		e2 = qb / (qa + qb)

		if winner == 1 :
			r1 = player1.rating + K * (1 - e1)
			r2 = player2.rating + K * (0 - e2)
			player1.gamesW += 1
			player2.gamesL += 1
		elif winner == 2 :
			r1 = player1.rating + K * (0 - e1)
			r2 = player2.rating + K * (1 - e2)
			player2.gamesW += 1
			player1.gamesL += 1
		else :
			r1 = player1.rating + K * (0.5 - e1)
			r2 = player2.rating + K * (0.5 - e2)
			player1.gamesD += 1
			player2.gamesD += 1

		player1.rating = r1
		player2.rating = r2

	def printStats(self, player1, player2) :

		"""
		This method prints the stats (number of games won, lost, drawn
		and rating) for player1 and player2

		param player1: A Player object
		param player2: A Player object
		"""

		players = [player1, player2]

		for player in players :
			print(player.name  + " " + str(player.gamesW) +  "W " +
			str(player.gamesL) + "L " + str(player.gamesD) + "D " +
			str(round(player.rating,2)))


class TrainingSession :

	"""
	This is a wrapper class for Reinforcement Learning parameters.
	"""

	def __init__(self, epsilon, discountRate, learningRate, agentFirst, games) :

		"""
		This constructor initialises RL parameters

		param epsilon: This variable controls how often the RL
				agent exploits it's state value table rather then
				explore new moves
		param learningRate: This variable affects the learning
				rate.  It determines how much the old state value
				will change.
		param discountRate: This variable expresses the value of
				future rewards.  If it's set to zero then the RL
				agent is most concerned about the immediate reward
				than future rewards.
		param agentFirst: This variable is True or False, it
				determines the turn of the RL agent. If True then
				the RL agent moves first, otherwise the RL agent
				moves second
		param games: The number of games/episodes the agent will
				perform
		"""

		self.games = games
		self.learningRate = learningRate
		self.discountRate = discountRate
		self.epsilon = epsilon
		self.agentFirst = agentFirst
