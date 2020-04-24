import tkinter as tk
from PIL import Image,ImageTk
class Snake(tk.Canvas):
	"""docstring for snake"""
	def __init__(self):
		super().__init__(width=600,height=600,background="black",highlightthickness=0)
		
		self.snake_positions=[(100,100),(80,100),(60,100)]
		self.load_assets()

		self.create_objects()
	def load_assets(self):
			try:
				self.snake_body_image=Image.open("C:/Users/sanket/Documents/New folder (3)")
				self.snake_body=ImageTk.PhotoImage(self.snake_body_image)

				self.food_image=Image.open("./New folder(3)/food.png")	
				self.food=ImageTk.PhotoImage(self.food_image)
			except IOError as error:
				print(error)
				root.destroy()
	def create_objects(self):
		for x_position,y_position in self.snake_positions:
			self.create_image(x_position,y_position,image=self.snake_body ,tag="snake")

root=tk.Tk()
root.title("Snake")
root.resizable(False,False)

board= Snake()
board.pack()
root.mainloop()