import datetime

from rd.object import Object
from rd.mob import Mob


class Game():
	def __init__(self,write_callback):
		self.queue = []
		self.mobs = []
		self.write_callback = write_callback

		self.combat_counter = 0
		self.previous_combat_round = datetime.datetime.now()

		playerConfig = Object()
		playerConfig.name = 'Player'

		enemyConfig = Object()
		enemyConfig.name = 'Fungusaur'

		self.player = Mob(playerConfig, game=self)

		self.mobs.append(self.player)
		self.mobs.append(Mob(enemyConfig, game=self))

	def enqueue_command(self, command):
		self.queue.append(command)

	def update(self):
		self.combat_counter += 1
		if self.combat_counter > 300:
			self.combat_counter = 0
			self.do_combat_round()

		if len(self.queue) > 0:
			command = self.queue.pop(0)
			self.player.execute_command(command)

		for mob in self.mobs:
			mob.update()

	def do_combat_round(self):
		current_time = datetime.datetime.now()
		elapsed_time = (current_time - self.previous_combat_round).total_seconds()
		print('Combat round. {:.2f} sec elapsed.'.format(elapsed_time))

		for mob in self.mobs:
			if mob.fighting:
				mob.do_round()

		self.previous_combat_round = current_time