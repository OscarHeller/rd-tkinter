import random

class FungusaurAI():
	def __init__(self, user):
		self.user = user

	def decide(self):
		user = self.user

		if random.randint(0, 99) < 50:
			user.execute_command('say I\'m so confused! I don\'t know what to do!')
		else:
			user.execute_command('dunk')