from Tkinter import *
from time import sleep
from random import randint
from Tkinter import *
#from ctypes import windll


WIDTH = 640
HEIGHT = 640
CELLCOLOR = "PaleGreen2"

def init_cells(window,numCells):
	global WIDTH
	global HEIGHT
	global CELLCOLOR
	cells = []
	for cell in range(numCells):
		x_val = randint(0, WIDTH-1)
		y_val = randint(0, HEIGHT-1)
		window.create_rectangle(x_val, y_val, x_val, y_val, outline = CELLCOLOR)
		cells.append((x_val, y_val))
		#readCanvas(window, cells, x_val, y_val)
	return cells

def getRandomHex():
	hexcolor = "#"	
	hexNumbers = "1234567890abcdef"
	hexlen = 6
	i = 0
	while(i < 6):
		rando = randint(0,15)
		hexcolor+= hexNumbers[rando]
		i+= 1
	#print hexcolor
	return hexcolor

def update_step(window, cells):
	#Need a 2D array that is a mimic of the canvas
	bookbook = []

def readCanvas(window, cells, x_val, y_val):
	rgb = getPixel(x_val, y_val)
	r = rgb & 0xff
	g = (rgb >> 8) & 0xff
	b = (rgb >> 16) & 0xff
	'#%02x%02x%02x' % (r, g, b)
	print r,g,b
		

def move_cells(window, cells):
	for cell in cells:
		window.create_rectangle(cell[0], cell[1], cell[0], cell[1], fill = "white", outline = "white")		
		ncell = (cell[0]+randint(-50,50), cell[1]+randint(-50,50))
		window.create_rectangle(ncell[0], ncell[1], ncell[0], ncell[1], outline = getRandomHex())
		cells[cells.index(cell)] = ncell
	return cells

def main():
	global WIDTH
	global HEIGHT
	master = Tk()
	window = Canvas(master, width = WIDTH, height = HEIGHT, background = "white")
	window.pack()
	initial_cells = 500
	cells = init_cells(window, initial_cells)
	#readCanvas(window, cells)
	while True:	
		#Do
		cells = move_cells(window, cells)
		#Update
		window.update()
		sleep(1)


if __name__ == '__main__':
	main()
