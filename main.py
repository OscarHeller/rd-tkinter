import tkinter
from tkinter import font
from rd.game import Game


class App():
	def __init__(self):
		self.root = tkinter.Tk()
		courier = font.Font(family='Courier New',size=13)

		self.text = tkinter.Text(self.root, width=70, font=courier, state='disabled')
		self.text.grid(row=0,column=0)
		self.commands = tkinter.Text(self.root, width=30, font=courier, state='disabled')
		self.commands.grid(row=0,column=1)
		self.entry = tkinter.Entry(self.root, width=100, font=courier)
		self.entry.grid(row=1,column=0, columnspan=2)

		self.entry.focus_force()

		self.root.bind('<Return>', self.press_enter)
		self.root.bind('<KP_Enter>', self.press_enter)

		self.game = Game(self.write, self.write_to_commands)
		self.root.after(10, self.game_update)

	def write_to_commands(self, commands):
		self.commands.configure(state='normal')
		self.commands.delete(1.0, tkinter.END)
		for command in commands:
			self.commands.insert(tkinter.END, '\n' + command)
		self.commands.configure(state='disabled')

	def write(self,output):
		self.text.configure(state='normal')
		self.text.insert(tkinter.END, '\n' + output)
		self.text.see(tkinter.END)
		self.text.configure(state='disabled')

	def game_update(self):
		self.game.update()
		self.root.after(10, self.game_update)

	def run(self):
		self.root.mainloop()

	def press_enter(self, event):
		command = self.entry.get()
		self.entry.delete(0, tkinter.END)
		self.game.enqueue_command(command)


if __name__ == '__main__':
	app = App()
	app.run()