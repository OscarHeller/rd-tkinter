import datetime

from rd.object import Object
from rd.mob import Mob


class Game():
	def __init__(self,write_callback):
		self.queue = []
		self.write_callback = write_callback

		self.combat_counter = 0
		self.previous_combat_round = datetime.datetime.now()

		playerConfig = Object()
		playerConfig.name = 'Player'
		playerConfig.player = True
		playerConfig.game = self

		enemyConfig = Object()
		enemyConfig.name = 'Fungusaur'
		enemyConfig.player = False
		enemyConfig.game = self

		self.player = Mob(playerConfig)
		self.enemy = Mob(enemyConfig)

	def enqueue_command(self, command):
		self.queue.append(command)

	def update(self):
		self.combat_counter += 1
		if self.combat_counter > 200:
			self.combat_counter = 0
			self.do_combat_round()

		if len(self.queue) > 0:
			command = self.queue.pop(0)
			self.execute_command(command)

	def execute_command(self, command):
		self.player.execute_command(command)
		# print('Executing [{}].'.format(command))
		# self.write_callback(command)

	def do_combat_round(self):
		current_time = datetime.datetime.now()
		elapsed_time = (current_time - self.previous_combat_round).total_seconds()

		print('Combat round. {:.2f} sec elapsed.'.format(elapsed_time))

		self.previous_combat_round = current_time