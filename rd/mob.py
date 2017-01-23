import random

from rd.commands import COMBAT_COMMANDS, INFO_COMMANDS, ITEM_COMMANDS
from rd.outfit import Outfit


class Mob():
	def __init__(self, config={}, game=None):
		self.buffer = []
		self.combat_buffer = []
		self.name = config['name']
		self.game = game
		self.maxhp = 1500
		self.hp = 1500
		self.maxmana = 200
		self.mana = 100
		self.fighting = None

		self.attacks_per_round = config['attacks_per_round']
		self.damage_noun = config['damage_noun']
		self.damage_dice = (int(config['damage_dice'].split('d')[0]), int(config['damage_dice'].split('d')[1]))

		self.short = config['short'] if 'short' in config else None
		self.keywords = config['keywords'] if 'keywords' in config else None

		self.commands = COMBAT_COMMANDS + INFO_COMMANDS + ITEM_COMMANDS
		print('New Mob: ', self.name, self.maxhp, self.hp, self.maxmana, self.mana)

	def start_combat(self, target):
		if not target.fighting:
			target.fighting = self
		self.fighting = target

	def execute_command(self, command):
		command_key = command.split(' ')[0].lower()
		sorted_commands = sorted(self.commands, key=lambda x: x.keyword)
		for c in sorted_commands:
			if c.keyword.startswith(command_key):
				if c.is_combat_command():
					self.combat_buffer.append(c)
				else:
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
			self.buffer.append(message[:1].upper() + message[1:])

	def update(self):
		if self.is_player() and len(self.buffer) > 0:
			render_buffer = ('\n').join(self.buffer)
			render_buffer += '\n'
			self.game.write_callback(render_buffer)
			self.buffer = []

	def get_short(self):
		if self.is_player():
			return self.get_name()
		else:
			return self.short

	def get_name(self):
		return self.name

	def is_player(self):
		return self == self.game.player

	def get_condition(self):
		percentage = (self.hp / float(self.maxhp)) * 100

		if percentage >= 100:
			return 'is in excellent condition'
		elif percentage >= 80:
			return 'has some small wounds and bruises'
		elif percentage >= 60:
			return 'has a few wounds'
		elif percentage >= 40:
			return 'has some big nasty wounds and scratches'
		elif percentage >= 20:
			return 'looks pretty hurt'
		elif percentage > 0:
			return 'is in awful condition'
		else:
			return 'should be dead (BUG)'


	def do_round_cleanup(self):
		if self.fighting:
			self.output('{} {}.'.format(self.fighting.get_short(), self.fighting.get_condition()))

	def do_round(self):
		for i in range(self.attacks_per_round):
			if not self.fighting:
				break
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
			self.fighting.get_short(),
			damage_string[2]))
		self.fighting.output('{}\'s {} {} {} you{}'.format(
			self.get_short(),
			damage_string[0],
			self.damage_noun,
			damage_string[1],
			damage_string[2]))

		self.fighting.damage(damage)

	def damage(self, amount):
		self.hp -= amount
		if self.hp <= 0:
			self.die()

	def die(self):
		self.output('You have been KILLED!')
		self.fighting.output('You have killed {}!'.format(self.get_short()))
		self.end_combat()
		self.hp = self.maxhp