class Game():
	def __init__(self,write):
		self.queue = []
		self.write = write

	def enqueue_command(self, command):
		self.queue.append(command)

	def update(self):
		if len(self.queue) > 0:
			command = self.queue.pop(0)
			self.execute_command(command)

	def execute_command(self, command):
		print('Executing [{}].'.format(command))
		self.write(command)