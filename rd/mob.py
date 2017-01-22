from rd.commands import KillCommand, FleeCommand


class Mob():
	def __init__(self, config):
		self.name = config.name
		self.player = config.player
		self.game = config.game
		self.maxhp = 1500
		self.hp = 1500
		self.maxmana = 100
		self.mana = 100
		self.fighting = None
		self.commands = [KillCommand(), FleeCommand()]
		print('New Mob: ', self.name, self.maxhp, self.hp, self.maxmana, self.mana)

	def start_combat(self, target):
		if not target.fighting:
			target.fighting = self
		self.fighting = target
		self.output('You attack {}!'.format(target.get_name()))

	def execute_command(self, command):
		sorted_commands = sorted(self.commands, key=lambda x: x.keyword)
		for c in sorted_commands:
			if c.keyword.startswith(command):
				c.execute(game=self.game)
				break
		else:
			self.output('Huh?')

	def end_combat(self):
		self.fighting = None
		self.game.enemy.fighting = None

	def output(self, message):
		if self.player:
			self.game.write_callback(message)

	def get_name(self):
		return self.name