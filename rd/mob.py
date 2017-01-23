import random

from rd.commands import KillCommand, FleeCommand


class Mob():
	def __init__(self, config={}, game=None):
		self.buffer = []
		self.name = config['name']
		self.game = game
		self.maxhp = 1500
		self.hp = 1500
		self.maxmana = 100
		self.mana = 100
		self.fighting = None

		self.attacks_per_round = config['attacks_per_round']
		self.damage_noun = config['damage_noun']
		self.damage_dice = (int(config['damage_dice'].split('d')[0]), int(config['damage_dice'].split('d')[1]))

		self.commands = [KillCommand(), FleeCommand()]
		print('New Mob: ', self.name, self.maxhp, self.hp, self.maxmana, self.mana)

	def start_combat(self, target):
		if not target.fighting:
			target.fighting = self
		self.fighting = target
		self.output('You attack {}!'.format(target.get_name()))
		target.output('{} attacks you!'.format(self.get_name()))

	def execute_command(self, command):
		command_key = command.split(' ')[0].lower()
		sorted_commands = sorted(self.commands, key=lambda x: x.keyword)
		for c in sorted_commands:
			if c.keyword.startswith(command_key):
				c.execute(game=self.game,user=self)
				break
		else:
			self.output('Huh?')

	def end_combat(self):
		old_target = self.fighting
		self.fighting = None

		if old_target.fighting == self:
			candidates = [mob for mob in self.game.mobs if mob.fighting == old_target]
			if len(candidates) > 0:
				old_target.fighting = random.choice(candidates)
			else:
				old_target.fighting = None

	def output(self, message):
		if self.is_player():
			self.buffer.append(message)

	def update(self):
		if self.is_player() and len(self.buffer) > 0:
			render_buffer = ('\n').join(self.buffer)
			render_buffer += '\n'
			self.game.write_callback(render_buffer)
			self.buffer = []

	def get_name(self):
		return self.name

	def is_player(self):
		return self == self.game.player

	def do_round(self):
		for i in range(self.attacks_per_round):
			self.do_hit()

	def do_hit(self):
		hit = random.randint(0,99) < 75
		damage = 0
		if hit:
			for i in range(self.damage_dice[0]):
				damage += random.randint(1, self.damage_dice[1])
		if damage > 0:
			damage_string = ('competent', 'does {} damage to'.format(damage), ', leaving marks!')
		else:
			damage_string = ('clumsy', 'misses', '.')

		self.output('Your {} {} {} {}{}'.format(
			damage_string[0],
			self.damage_noun,
			damage_string[1],
			self.fighting.get_name(),
			damage_string[2]))
		self.fighting.output('{}\'s {} {} {} you{}'.format(
			self.get_name(),
			damage_string[0],
			self.damage_noun,
			damage_string[1],
			damage_string[2]))