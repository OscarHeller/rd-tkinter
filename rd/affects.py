class Affect():
	def __init__(self, config={}):
		self.name = config['name']
		self.duration = config['duration'] if 'duration' in config else 1
		self.refreshable = config['refreshable'] if 'refreshable' in config else False

	def initialize(self, target=None, caster=None):
		self.target = target
		self.caster = caster
		self.game = target.game

		self.apply()

	def update(self):
		self.duration -= 1
		if self.duration <= 0:
			self.wear()

	def get_short(self):
		return self.name[:1].lower() + self.name[1:]

	def apply(self):
		current_matches = [affect for affect in self.target.affects if affect == self]
		found = False
		for affect in self.target.affects:
			if type(affect) == type(self):
				found = True
				if self.refreshable:
					self.target.output('{} refreshes your {}.'.format(self.caster.get_short(), \
						self.get_short()))
					self.game.broadcast('{}\'s {} is refreshed.'.format(self.target.get_short(), \
						self.get_short()),	blacklist=[self.target])
					affect.duration = self.duration
				else:
					self.game.broadcast('{} is already affected by {}.'.format(self.target.get_short(), \
						self.get_short()),	blacklist=[self.target])
					return

		if not found:
			self.target.affects.append(self)

			self.target.output('{} affects you with {}.'.format(self.caster.get_short(), self.get_short()))
			self.game.broadcast('{} is affected by {}.'.format(self.target.get_short(), self.get_short()), \
				blacklist=[self.target])
	
	def wear(self):
		self.target.output('You are no longer affected by {}.'.format(self.get_short()))
		self.game.broadcast('{} is no longer affected by {}.'.format(self.target.get_short(), self.get_short()), \
			blacklist=[self.target])
		self.target.affects.remove(self)


class DunkedAffect(Affect):
	def __init__(self):
		config = {
			'name' : 'Dunked',
			'duration' : 2,
			'refreshable' : True
		}
		super().__init__(config=config)