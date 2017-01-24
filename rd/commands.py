import random


class Command():
	def __init__(self, keyword=None, combat_command=False, lag=0):
		self.keyword = keyword
		self.combat_command = combat_command
		self.lag = lag

	def is_combat_command(self):
		return self.combat_command if hasattr(self, 'combat_command') else False

	def get_lag(self):
		return self.lag


class KillCommand(Command):
	def __init__(self):
		super().__init__(keyword='kill')

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
		super().__init__(keyword='flee')

	def execute(self, user=None, game=None):
		if not user.fighting:
			user.output('You aren\'t fighting anyone.')
		else:
			user.fighting.output('{} has fled!'.format(user.get_short()))
			user.output('You flee from combat!')
			user.end_combat()


class LookCommand(Command):
	def __init__(self):
		super().__init__(keyword='look')

	def execute(self, user=None, game=None):
		user.output('Limbo')
		user.output('You stand in a formless void. White mist swirls around you. You cannot move.\n')
		user.output('[Exits: none]\n')

		for mob in [mob for mob in game.mobs if mob != user]:
			user.output(mob.get_short() + ' is here.')


class ClearCommand(Command):
	def __init__(self):
		super().__init__(keyword='clear')

	def execute(self, user=None, game=None):
		user.output('You clear your combat buffer.')
		user.clear_combat_buffer()


class TestCombatCommand(Command):
	def __init__(self):
		super().__init__(keyword='test', combat_command=True)

	def execute(self, user=None, game=None):
		user.output('You use the test command on {}.'.format(user.fighting.get_short()))
		user.fighting.output('{} uses the test command on you.'.format(user.get_short()))

COMMANDS = [KillCommand(), FleeCommand(), LookCommand(), ClearCommand()]
TEST_COMMANDS = [TestCombatCommand()]