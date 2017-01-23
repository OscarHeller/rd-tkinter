import random


class KillCommand():
	def __init__(self):
		self.keyword = 'kill'

	def execute(self, user=None, game=None):
		if user.fighting:
			user.output('You are already fighting!')
		else:
			candidates = [mob for mob in game.mobs if mob != user]

			victim = random.choice(candidates)
			user.start_combat(victim)

			user.output('You attack {}!'.format(victim.get_name()))
			victim.output('{} attacks you!'.format(user.get_name()))
			user.do_round()

			if user.fighting == victim:
				user.output('{} {}.'.format(victim.get_name(), victim.get_condition()))



class FleeCommand():
	def __init__(self):
		self.keyword = 'flee'

	def execute(self, user=None, game=None):
		if not user.fighting:
			user.output('You aren\'t fighting anyone.')
		else:
			user.fighting.output('{} has fled!'.format(user.get_name()))
			user.output('You flee from combat!')
			user.end_combat()


class LookCommand():
	def __init__(self):
		self.keyword = 'look'

	def execute(self, user=None, game=None):
		user.output('Limbo')
		user.output('You stand in a formless void. White mist swirls around you. You cannot move.\n')
		user.output('[Exits: none]\n')

		for mob in [mob for mob in game.mobs if mob != user]:
			user.output(mob.get_short() + ' is here.')