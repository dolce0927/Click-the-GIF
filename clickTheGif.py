"""

File: PythonFinal.py
Author: Rosanna

WA170: Programming With Python Final
(Image files will be supplied)
Create a Python app that will allow the user to view 3 unique pictures 
inside the GUI of the application.
Upon load, the module should display a label that says: "Picture Viewer 1.0" and three buttons.

Design the program so that when the user clicks one of the buttons, an image unique to that button appears above the button. 

Clicking the button again should close the image. The user should be able to make images appear, disappear at will by clicking the buttons.

Be sure to comment your code as that will be evaluated as part of the grading process.
"""

from breezypythongui import EasyFrame
from tkinter import PhotoImage
from tkinter.font import Font

class PythonFinal(EasyFrame):
	"""displays and hides images and captions on click"""

	def __init__(self):
		"""sets up the window and widgets."""
		EasyFrame.__init__(self, width = 400, height = 300, title = "Picture Viewer 1.0", background = "cyan")
		self.setResizable(False)

		# sets up the image placement and captions
		self.imageLabel1 = self.addLabel(text = "", row = 0, column = 0, sticky = "NSNEW")
		
		self.imageLabel2 = self.addLabel(text = "", row = 0, column = 1, sticky = "NSNEW")
		
		self.imageLabel3 = self.addLabel(text = "", row = 0, column = 2, sticky = "NSNEW")
		
		#identify the image files
		self.image1 = PhotoImage(file = "")
		self.imageLabel1["image"] = self.image1

		self.image2 = PhotoImage(file = "")
		self.imageLabel2["image"] = self.image2

		self.image3 = PhotoImage(file = "")
		self.imageLabel3["image"] = self.image3

		#add buttons respectively to images
		self.click1 = self.addButton(text = "Click", row = 2, column = 0, command = self.click1)	

		self.click2 = self.addButton(text = "Click", row = 2, column = 1, command = self.click2)	

		self.click3 = self.addButton(text = "Click", row = 2, column = 2, command = self.click3)	

	def click1(self):			
		if self.image1["file"] != "image1.gif":
			self.image1["file"] = "image1.gif"
		else:
			self.image1["file"] = "blank.gif"
			
	def click2(self):				
		if self.image2["file"] != "image2.gif":
			self.image2["file"] = "image2.gif"
		else:
			self.image2["file"] = "blank.gif"

	def click3(self):
		if self.image3["file"] != "image3.gif":
			self.image3["file"] = "image3.gif"
		else:
			self.image3["file"] = "blank.gif"

def main():
	"""Instantiates and pops up the window."""
	PythonFinal().mainloop()

if __name__ == "__main__":
	main()	
