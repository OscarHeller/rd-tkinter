class KillCommand():
	def __init__(self):
		self.keyword = 'kill'

	def execute(self, game=None):
		if game.player.fighting:
			game.player.output('You are already fighting!')
		else:
			game.player.start_combat(game.enemy)


class FleeCommand():
	def __init__(self):
		self.keyword = 'flee'

	def execute(self, game=None):
		if not game.player.fighting:
			game.player.output('You aren\'t fighting anyone.')
		else:
			game.enemy.output('{} has fled!'.format(game.player.get_name()))
			game.player.output('You flee from combat!')
			game.player.end_combat()