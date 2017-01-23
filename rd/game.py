import datetime

from rd.mob import Mob


class Game():
	def __init__(self,write_callback):
		self.queue = []
		self.mobs = []
		self.write_callback = write_callback

		self.combat_counter = 0
		self.previous_combat_round = datetime.datetime.now()

		playerConfig = {
			'name': 'Player',
			'attacks_per_round': 3,
			'damage_noun': 'punch',
			'damage_dice': '10d4'
		}

		enemyConfig = {
			'name': 'Fungusaur',
			'attacks_per_round': 3,
			'damage_noun': 'slice',
			'damage_dice': '4d6'
		}

		self.player = Mob(config=playerConfig, game=self)

		self.mobs.append(self.player)
		self.mobs.append(Mob(config=enemyConfig, game=self))

		self.enqueue_command('look')

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

		for mob in self.mobs:
			if mob.fighting:
				mob.do_round_cleanup()

		self.previous_combat_round = current_time