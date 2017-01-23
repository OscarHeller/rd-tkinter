class Item():
	def __init__(self, config, game=None):
		self.short = config['short']
		self.wear_location = config['wear_location']
		self.damage_noun = config['damage_noun']
		self.damage_dice = (int(config['damage_dice'].split('d')[0]), int(config['damage_dice'].split('d')[1]))

		print('New Item: ', self.short, self.wear_location, self.damage_dice, self.damage_noun)

	def get_short(self):
		return self.short