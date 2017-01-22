import tkinter
from tkinter import font


class App():
	def __init__(self):
		self.root = tkinter.Tk()
		courier = font.Font(family='Courier New',size=13)

		self.entry = tkinter.Entry(self.root,width=100,font=courier)
		self.entry.grid(row=9)
		self.text = tkinter.Text(self.root,width=100,font=courier)
		self.text.grid(row=0,rowspan=9)

		self.root.bind('<Return>', self.press_enter)
		self.root.bind('<KP_Enter>', self.press_enter)

	def run(self):
		self.root.mainloop()

	def press_enter(self, event):
		print(event)
		print('You pressed enter: [{}]'.format(self.entry.get()))
		self.entry.delete(0,len(self.entry.get()))


if __name__ == '__main__':
	app = App()
	app.run()