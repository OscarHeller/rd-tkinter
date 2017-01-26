import random


class Command():
	def __init__(self, config):
		self.keyword = config['keyword'] if 'keyword' in config else None
		self.mana = config['mana'] if 'mana' in config else 0

	def init_user(self, user):
		self.user = user
		self.game = user.game

	def is_combat_command(self):
		return self.combat_command if hasattr(self, 'combat_command') else False

	def get_lag(self):
		return self.lag

	def execute(self):
		if self.mana > 0 and self.mana > self.user.mana:
			self.user.output('You don\'t have enough mana.')
			return


class KillCommand(Command):
	def __init__(self):
		config = {
			'keyword' : 'kill'
		}
		super().__init__(config)

	def execute(self):
		super().execute()

		user = self.user
		game = self.game

		if user.fighting:
			user.output('You are already fighting!')
		else:
			candidates = [mob for mob in game.mobs if mob != user]

			victim = random.choice(candidates)
			user.start_combat(victim)

			user.output('You attack {}!'.format(victim.get_short()))
			victim.output('{} attacks you!'.format(user.get_short()))


# class FleeCommand(Command):
# 	def __init__(self):
# 		super().__init__(keyword='flee')

# 	def execute(self, user=None, game=None):
# 		if not user.fighting:
# 			user.output('You aren\'t fighting anyone.')
# 		else:
# 			user.fighting.output('{} has fled!'.format(user.get_short()))
# 			user.output('You flee from combat!')
# 			user.end_combat()


# class LookCommand(Command):
# 	def __init__(self):
# 		super().__init__(keyword='look')

# 	def execute(self, user=None, game=None):
# 		user.output('Limbo')
# 		user.output('You stand in a formless void. White mist swirls around you. You cannot move.\n')
# 		user.output('[Exits: none]\n')

# 		for mob in [mob for mob in game.mobs if mob != user]:
# 			user.output(mob.get_short() + ' is here.')


# class ClearCommand(Command):
# 	def __init__(self):
# 		super().__init__(keyword='clear')

# 	def execute(self, user=None, game=None):
# 		user.output('You clear your combat buffer.')
# 		user.clear_combat_buffer()


# class PhantomForceCommand(Command):
# 	def __init__(self):
# 		super().__init__(keyword='phantom', combat_command=True, mana=75)

# 	def execute(self, user=None, game=None):
# 		user.do_damage(damage=150, noun='phantom force', target=user.fighting)

COMMANDS = [KillCommand]
COMBAT_COMMANDS = []