import tkinter
from tkinter import font
from rd.game import Game


class App():
	def __init__(self):
		self.root = tkinter.Tk()
		courier = font.Font(family='Courier New',size=13)

		self.entry = tkinter.Entry(self.root,width=100,font=courier)
		self.entry.grid(row=9)
		self.text = tkinter.Text(self.root,width=100,font=courier)
		self.text.grid(row=0,rowspan=9)

		self.entry.focus_force()

		self.root.bind('<Return>', self.press_enter)
		self.root.bind('<KP_Enter>', self.press_enter)

		self.game = Game(self.write)
		self.root.after(10, self.game_update)

	def write(self,output):
		self.text.insert(tkinter.END,'\n' + output)

	def game_update(self):
		self.game.update()
		self.root.after(10, self.game_update)

	def run(self):
		self.root.mainloop()

	def press_enter(self, event):
		command = self.entry.get()
		print('You pressed enter: [{}]'.format(command))
		self.entry.delete(0, tkinter.END)
		self.game.enqueue_command(command)


if __name__ == '__main__':
	app = App()
	app.run()