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

			user.output('You attack {}!'.format(victim.get_short()))
			victim.output('{} attacks you!'.format(user.get_short()))
			user.do_round()

			if user.fighting == victim:
				user.output('{} {}.'.format(victim.get_short(), victim.get_condition()))



class FleeCommand():
	def __init__(self):
		self.keyword = 'flee'

	def execute(self, user=None, game=None):
		if not user.fighting:
			user.output('You aren\'t fighting anyone.')
		else:
			user.fighting.output('{} has fled!'.format(user.get_short()))
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


class GetCommand():
	def __init__(self):
		self.keyword = 'get'

	def execute(self, user=None, game=None):
		candidates = [item for item in game.items if not user.has_item(item)]

		try:
			target = random.choice(candidates)
			user.outfit.add_to_inventory(target)
			user.output('You get {}.'.format(target.get_short()))
		except IndexError:
			user.output('There\'s nothing here.')


class DropCommand():
	def __init__(self):
		self.keyword = 'drop'

	def execute(self, user=None, game=None):
		candidates = [item for item in user.outfit.inventory]

		try:
			target = random.choice(candidates)
			user.outfit.remove_from_inventory(target)
			user.output('You drop {}.'.format(target.get_short()))
		except IndexError:
			user.output('You aren\'t carrying anything.')


class InventoryCommand():
	def __init__(self):
		self.keyword = 'inventory'

	def execute(self, user=None, game=None):
		user.output('You are carrying:')
		if len(user.outfit.inventory) > 0:
			for item in user.outfit.inventory:
				user.output('  {}'.format(item.get_short()))
		else:
			user.output('  Nothing.')

COMBAT_COMMANDS = [KillCommand(), FleeCommand()]
INFO_COMMANDS = [LookCommand()]
ITEM_COMMANDS = [GetCommand(), InventoryCommand(), DropCommand()]