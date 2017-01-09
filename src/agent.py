import numpy as np

def RandomAgent(gameState):
	legalActions = gameState.getLegalActions()
	actionIndex = np.random.choice(range(len(legalActions)))
	action = legalActions[actionIndex]
	return action

def HumanAgent(gameState):
	legalActions = gameState.getLegalActions()
	while True:
		yourMoveStr = input('Your move: ')
		tokens = yourMoveStr.split(',')
		if len(tokens) != 2:
			print('Illegal input!')
			continue
		action = tuple([int(i) for i in tokens])
		if action not in legalActions:
			print('Illegal action!')
			continue
		break
	return action

def NoDeadCellRandomAgent(gameState):
	legalActions = gameState.getLegalActions()
	goodActions = [a for a in legalActions if not gameState.isDeadCell(a)]
	actionIndex = np.random.choice(range(len(goodActions)))
	action = goodActions[actionIndex]
	return action

def BetterRandomAgent(gameState):
	legalActions = gameState.getLegalActions()
	for a in legalActions:
		print(gameState.getSuccessorState(a, 1).board)
	return a

def OnlyAttackAgent(gameState):
	action = 0


	return action

def evaluationFunction(gameState):
	reward = HexEnv.game_finished(gameState)
	return reward

def ExpectimaxAgent(gameState, max_depth=1):

	legal_actions = HexEnv.get_possible_actions(gameState)	
	if len(legal_actions) == 0:
		return 'resign'
	
	INT_MAX = 999999
	PLAYER = 0
	
	def getExpectimaxScoreAction(gameState, agentIndex, depth):
		legal_actions = HexEnv.get_possible_actions(gameState)	
		reward = HexEnv.game_finished(gameState)
		if depth == 0 or reward != 0:
			return reward, 0

		bestActions = []
		if agentIndex == PLAYER:
			bestScore = -INT_MAX
			for act in legal_actions:
				sucState = gameState.copy()
				HexEnv.make_move(sucState, act, agentIndex)
				score, a = getExpectimaxScoreAction(sucState, 1-PLAYER, depth)
				if score > bestScore:
					bestScore = score
					bestActions = []
				if score == bestScore:
					bestActions.append(act)
		
		elif agentIndex == 1-PLAYER:
			bestScore = 0.0
			for act in legal_actions:
				sucState = gameState.copy()
				HexEnv.make_move(sucState, act, agentIndex)
				score, a = getExpectimaxScoreAction(sucState, PLAYER, depth-1)
				bestScore += float(score)
			bestScore /= float(len(legal_actions))
		
		return bestScore, bestActions

	bestScore, bestActions = getExpectimaxScoreAction(gameState, PLAYER, max_depth)
		
	bestAction = np.random.choice(bestActions)
	#bestAction = bestActions[0]
	#print bestScore, bestAction
	return bestAction


