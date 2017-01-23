import random


class Command():
	def __init__(self):
		self.keyword = None

	def is_combat_command(self):
		return self.is_combat_command if hasattr(self, 'is_combat_command') else False


class KillCommand(Command):
	def __init__(self):
		self.keyword = 'kill'

	def execute(self, user=None, game=None):
		if user.fighting:
			user.output('You are already fighting!')
		else:
			candidates = [mob for mob in game.mobs if mob != user]

			victim = random.choice(candidates)
			user.start_combat(victim)

			user.output('You attack {}!'.format(victim.get_short()))
			victim.output('{} attacks you!'.format(user.get_short()))
			# user.do_round()

			# if user.fighting == victim:
			# 	user.output('{} {}.'.format(victim.get_short(), victim.get_condition()))



class FleeCommand(Command):
	def __init__(self):
		self.keyword = 'flee'

	def execute(self, user=None, game=None):
		if not user.fighting:
			user.output('You aren\'t fighting anyone.')
		else:
			user.fighting.output('{} has fled!'.format(user.get_short()))
			user.output('You flee from combat!')
			user.end_combat()


class LookCommand(Command):
	def __init__(self):
		self.keyword = 'look'

	def execute(self, user=None, game=None):
		user.output('Limbo')
		user.output('You stand in a formless void. White mist swirls around you. You cannot move.\n')
		user.output('[Exits: none]\n')

		for mob in [mob for mob in game.mobs if mob != user]:
			user.output(mob.get_short() + ' is here.')

COMBAT_COMMANDS = [KillCommand(), FleeCommand()]
INFO_COMMANDS = [LookCommand()]