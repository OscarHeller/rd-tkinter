import datetime

from rd.mob import Mob
from rd.constants import HALF_ROUND
from rd.ai import FungusaurAI


class Game():
	def __init__(self, write_callback):
		self.mobs = []

		self.queue = []
		self.write_callback = write_callback
		self.combat_counter = 0
		self.previous_combat_round = datetime.datetime.now()

		self.init_demo()

		self.enqueue_command('look')

	def enqueue_command(self, command):
		self.queue.append(command)

	def update(self):
		self.combat_counter += 1
		if self.combat_counter == HALF_ROUND:
			self.do_mid_combat_round()
		elif self.combat_counter >= (2 * HALF_ROUND):
			self.combat_counter = 0
			self.do_combat_round()

		if len(self.queue) > 0:
			command = self.queue.pop(0)
			self.player.execute_command(command)

		for mob in self.mobs:
			mob.update()

	def broadcast(self, message, blacklist=[]):
		for mob in [mob for mob in self.mobs if mob not in blacklist]:
			mob.output(message)

	def do_mid_combat_round(self):
		command_mobs = []

		for mob in (mob for mob in self.mobs if mob.fighting):
			m = mob.start_mid_round()
			if m is not None:
				command_mobs.append([m, not mob.is_player(), mob])

		sorted_command_mobs = sorted(command_mobs)

		for mob in sorted_command_mobs:
			mob[2].do_mid_round()

		for mob in (mob for mob in self.mobs if mob.fighting):
			mob.end_mid_round()

	def do_combat_round(self):
		current_time = datetime.datetime.now()
		elapsed_time = (current_time - self.previous_combat_round).total_seconds()
		# print('Combat round. {:.2f} sec elapsed.'.format(elapsed_time))

		for mob in (mob for mob in self.mobs if mob.fighting):
			mob.do_round()

		self.previous_combat_round = current_time

	def init_demo(self):
		playerConfig = {
			'name': 'Player',
			'attacks_per_round': 3,
			'damage_noun': 'punch',
			'damage_dice': '4d6'
		}

		enemyConfig = {
			'name': 'Fungusaur',
			'short': 'a fungusaur',
			'attacks_per_round': 3,
			'damage_noun': 'slice',
			'damage_dice': '4d6',
			'keywords': ['fungusaur', 'dinosaur'],
			# 'AI': FungusaurAI
		}

		self.player = Mob(config=playerConfig, game=self)
		self.player.write_stats()

		self.mobs.append(self.player)
		self.mobs.append(Mob(config=enemyConfig, game=self))