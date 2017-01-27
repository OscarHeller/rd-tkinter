import random


class Command():
	def __init__(self, config={}, keyword=None):
		self.keyword = config['keyword'] if 'keyword' in config else keyword

		self.mana_cost = config['mana_cost'] if 'mana_cost' in config else 0
		self.mana_gain = config['mana_gain'] if 'mana_gain' in config else 0
		self.combat_command = config['combat_command'] if 'combat_command' in config else False
		self.lag = config['lag'] if 'lag' in config else 0
		self.speed = config['speed'] if 'speed' in config else 10
		self.base_damage = config['base_damage'] if 'base_damage' in config else 0

		self.stale = False

	def init_user(self, user):
		self.user = user
		self.game = user.game

	def is_combat_command(self):
		return self.combat_command if hasattr(self, 'combat_command') else False

	def get_lag(self):
		return self.lag

	def prepare(self):
		self.user.spend_mana(self.mana_cost)

	def super_execute(self):
		self.user.gain_mana(self.mana_gain)

		self.execute([])

	def get_damage(self):
		base_damage = self.base_damage
		if self in self.user.stale:
			base_damage *= 0.9
		return base_damage


class KillCommand(Command):
	def __init__(self):
		super().__init__(keyword='kill')

	def execute(self, args):
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


class PhantomForceCommand(Command):
	def __init__(self):
		config = {
			'keyword' : 'phantom',
			'combat_command' : True,
			'mana_cost' : 50,
			'speed' : 9,
			'base_damage'  : 150
		}
		super().__init__(config=config)

	def execute(self, args):
		self.user.do_damage(self.get_damage(), noun='phantom force', target=self.user.fighting)


class EnergyDrainCommand(Command):
	def __init__(self):
		config = {
			'keyword' : 'energydrain',
			'combat_command' : True,
			'mana_gain' : 25,
			'speed' : 11,
			'base_damage'  : 25
		}
		super().__init__(config=config)

	def execute(self, args):
		self.user.do_damage(self.get_damage(), noun='energy drain', target=self.user.fighting)


class DunkCommand(Command):
	def __init__(self):
		config = {
			'keyword' : 'dunk',
			'combat_command' : True,
			'base_damage'  : 50
		}
		super().__init__(config=config)

	def execute(self, args):
		self.user.do_damage(self.get_damage(), noun='dunk', target=self.user.fighting)


class FleeCommand(Command):
	def __init__(self):
		super().__init__(keyword='flee')

	def execute(self, args):
		user = self.user
		game = self.game

		if not user.fighting:
			user.output('You aren\'t fighting anyone.')
		else:
			user.fighting.output('{} has fled!'.format(user.get_short()))
			user.output('You flee from combat!')
			user.end_combat()


class LookCommand(Command):
	def __init__(self):
		super().__init__(keyword='look')

	def execute(self, args):
		user = self.user
		game = self.game

		user.output('Limbo')
		user.output('You stand in a formless void. White mist swirls around you. You cannot move.\n')
		user.output('[Exits: none]\n')

		for mob in [mob for mob in game.mobs if mob != user]:
			user.output(mob.get_short() + ' is here.')


class ClearCommand(Command):
	def __init__(self):
		super().__init__(keyword='clear')

	def execute(self, args):
		user = self.user

		user.output('You clear your combat buffer.')
		user.clear_combat_buffer()


class RestoreCommand(Command):
	def __init__(self):
		super().__init__(keyword='restore')

	def execute(self, args):
		user = self.user
		game = self.game

		user.output('You restore the game.')
		for mob in game.mobs:
			mob.restore()


class SayCommand(Command):
	def __init__(self):
		super().__init__(keyword='say')

	def execute(self, args):
		user = self.user
		game = self.game
		message = ' '.join(args)

		user.output('You say \'{}\''.format(message))
		for mob in [mob for mob in game.mobs if mob is not user]:
			mob.output('{} says \'{}\''.format(user.get_short(), message))

COMMANDS = [KillCommand, LookCommand, FleeCommand, ClearCommand, RestoreCommand, SayCommand]
COMBAT_COMMANDS = [PhantomForceCommand, EnergyDrainCommand, DunkCommand]