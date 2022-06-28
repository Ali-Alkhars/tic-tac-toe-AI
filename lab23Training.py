import aalkharslab23 as lab


def main():

	rlAgent = lab.Player('X', 'RL')
	rlAgent.name = "AI"

	partner = lab.Player('O', 'RANDOM')
	partner.name = "Random"

	# mm = ttt.Player('X', 'MINIMAX')
	# mm.name = "MiniMax"

	session = lab.TrainingSession(0.3, 0.1, 0.4, True, 30000)
	rlAgent.train(partner, session)

	session2 = lab.TrainingSession(0.3, 0.1, 0.4, False, 30000)
	rlAgent.train(partner, session2)

	tournament = lab.Tournament()

	# print(tournament.game(mm, partner))

	for i in range(10):
		tournament.start(rlAgent, partner)

	tournament.printStats(rlAgent, partner)

main()
