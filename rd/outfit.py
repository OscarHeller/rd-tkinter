class Outfit():
	def __init__(self):
		self.inventory = []
		self.equipped = {
			'wield': None
		}

	def has_item(self, item):
		if item in self.inventory or item in self.equipped.values():
			return True
		return False

	def add_to_inventory(self, item):
		self.inventory.append(item)

	def remove_from_inventory(self, item):
		self.inventory.remove(item)