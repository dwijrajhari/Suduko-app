from tkinter import *
import turtle as tl
from time import sleep
from random import shuffle
import keyboard as k
import threading as th
import numpy as np
import suduko_lev

class Suduko(Canvas):

	def __init__(self, master):
		Canvas.__init__(self, master, width = 360, height = 360)     
		self.t_obj = tl.TurtleScreen(self)							 
		self.t_obj.bgcolor('wheat')
		self.active_cell = None
		self.array = suduko_lev.lev_2          # lev_0 = np.array([[None for i in range(9)] for i in range(9)])
		self.barred_cells = []
		for i in range(81):
			if self.array.take(i) != None:
				self.barred_cells.append((i//9, i%9))
		self.red_flagged = set()
		self.listener = th.Thread(target = self.eventListener)
		self.daemon = True 
		self.primary_pen = tl.RawPen(self.t_obj)
		self.primary_pen.ht()
		self.focus_set()
		self.pack()
		self.beginScreen()

	def beginScreen(self):
		self.t_obj.reset()
		self.primary_pen.ht()
		sleep(1)
		letters = ['S           ', '  U         ', '    D       ', '      U     ', '        K   ', '          O ']
		cols = ['green', 'blue', 'red', 'brown', 'purple', 'violet']
		shuffle(letters)
		for i in range(6):
			self.primary_pen.pd()
			self.primary_pen.color(cols[i])
			self.primary_pen.write(letters[i], align ='center', font = ('Papyrus', 50, 'bold'))
			self.primary_pen.pu()
			self.primary_pen.home()
			sleep(0.1)
		self.primary_pen.goto(-100, 20)
		self.primary_pen.pd()
		self.primary_pen.width(3)
		self.primary_pen.color('skyblue')
		self.t_obj.tracer(2, 1)
		for i in range(200):
			self.primary_pen.fd(1)
		sleep(1)
		self.primary_pen.pu()
		self.primary_pen.goto(0, -5)
		self.primary_pen.color('black')
		self.primary_pen.write('Press any key to enter...', align = 'center', font = ('Times', 15))
		self.bind('<KeyPress>', self.animateGridDraw)
		
	def animateGridDraw(self, dummy):
		self.unbind('<KeyPress>')
		self.t_obj.reset()
		self.primary_pen.ht()
		self.primary_pen.pu()
		self.primary_pen.color('skyblue')
		self.primary_pen.width(3)
		self.t_obj.tracer(5, 1)
		pen_list = [tl.RawPen(self.t_obj) for i in range(8)]
		pen_list2 = [tl.RawPen(self.t_obj) for i in range(8)]
		for i in range(1, 9):
			alias = pen_list[i-1]; alias2 = pen_list2[i-1]
			alias.ht(); alias2.ht()
			alias.pu(); alias2.pu()
			alias.setx(40*i-180); alias2.setx(-(40*i+180))
			alias.sety(40*i+180); alias2.sety(40*i-180)
			alias.speed(0); alias2.speed(0)
			alias.pd(); alias2.pd()
			alias.rt(90)
		for i in [2, 5]:
			pen_list[i].width(3)
			pen_list2[i].width(3)
		for i in range(400):
			for i in range(8):
				pen_list[i].fd(2)
				pen_list2[i].fd(2)
		alias = pen_list[0]
		alias.goto(-180, -180)
		alias.rt(180)
		self.t_obj.tracer(1, 0.1)
		alias.width(5)
		alias.speed(3)
		alias.color('green')
		for i in range(5):
			alias.fd(360)
			alias.rt(90)
		self.num_writer = tl.RawPen(self.t_obj)
		self.num_writer.ht()
		self.num_writer.pu()
		self.num_writer.fillcolor('wheat')
		self.num_writer.color('blue', 'wheat')
		for i in self.barred_cells:
			num = self.array[i[0]][i[1]] 
			posx = i[1]*40 - 180
			posy = 180 - i[0]*40
			self.num_writer.goto(posx+17, posy-35)
			self.num_writer.write(str(num), font = ('Times', 18))
		self.bind('<Button-1>', self.grabCell)
		self.listener.start()

	def grabCell(self, dummy):
		self.unbind('<Button-1>')
		rootx, rooty = self.winfo_pointerxy()
		posx = rootx - self.winfo_rootx()
		posy = rooty - self.winfo_rooty()
		posx -= (posx%40)
		posy -= (posy%40)
		posx = posx- 180
		posy = 180 - posy
		if ((180-posy)/40, (posx+180)/40) not in self.barred_cells:
			if self.active_cell != None:
				for i in range(9):
					self.primary_pen.undo()
			self.active_cell = (posx, posy)
			self.primary_pen.pu()
			self.primary_pen.goto(self.active_cell)
			self.primary_pen.pd()
			for i in range(4):
				self.primary_pen.fd(40)
				self.primary_pen.rt(90)
			self.primary_pen.pu()
		self.bind('<Button-1>', self.grabCell)

	def eventListener(self):
		char = k.read_key()
		if self.active_cell and char.isdigit() and char != '0':
			try:
				self.unbind('<Button-1>')
				self.flagCheck(int(char))
				self.flagUpdate()
				self.flagCheck(int(char))
				self.bind('<Button-1>', self.grabCell)
				self.eventListener()
			except:
				pass
		else:
			self.eventListener()

	def enterNum(self, char, cell = None, numCol = 'black'):
		posx, posy = cell
		self.num_writer.goto(posx+3, posy-3)
		self.num_writer.begin_fill()
		for i in range(4):
			self.num_writer.fd(36)
			self.num_writer.rt(90)
		self.num_writer.end_fill()
		self.num_writer.goto(posx+22, posy-35)
		self.num_writer.color(numCol, 'wheat')
		self.num_writer.write(char, align = 'center', font = ('Times', 18))		
		arr_x = (posx + 180)//40
		arr_y = (180 - posy)//40
		self.array[arr_y][arr_x] = int(char)

	def flagCheck(self, char, cell = None):
		if cell == None:
			posx, posy = self.active_cell
		else:
			posx, posy = cell
		arr_x = (posx + 180)//40
		arr_y = (180 - posy)//40
		x = arr_y-arr_y%3
		y = arr_x-arr_x%3
		sub_array = self.array[x:x+3].T[y:y+3]
		if self.array[arr_y].tolist().count(char) > 1 or self.array.T[arr_x].tolist().count(char) > 1 \
		or sub_array.flatten().tolist().count(char) > 1:
			self.red_flagged.add((char, (posx, posy)))	
			self.enterNum(char, (posx, posy), 'red')
		else:
			self.enterNum(char, (posx, posy), 'black')
	
	def flagUpdate(self):
		changed_ones = []
		for i in self.red_flagged:
			char = i[0]
			posx, posy = i[1]
			arr_x = (posx + 180)//40
			arr_y = (180 - posy)//40
			x = arr_y-arr_y%3
			y = arr_x-arr_x%3
			sub_array = self.array[x:x+3].T[y:y+3]
			if self.array[arr_y].tolist().count(char) > 1 or self.array.T[arr_x].tolist().count(char) > 1 \
			or sub_array.flatten().tolist().count(char) > 1:
				pass
			else:
				self.enterNum(char, (posx, posy), 'black')
				changed_ones.append(i)
		for i in changed_ones:
			self.red_flagged.remove(i)

# Driver Code...			
if __name__ == '__main__':
	mainTk = Tk()
	mainTk.title('Suduko!')
	mainTk.wm_resizable(width = False, height = False)
	s = Suduko(mainTk)
	mainTk.mainloop()
