
class Simulation:
	def __init__(self):
		pass

	def turn(self, angle):
		pass

	def set_speed(self, speed):
		assert speed >= 0 and speed <= 100

	def update(self):
		pass
from tkinter import *
from d import D
root = Tk()
t = 3
g0 = 0
v = 10
c = Canvas(root, width=1600, height=900, bg='white')
c.pack() 

for i in range(len(D)-1):

    x0, y0, x1, y1 = D[i] + D[i+1]
    g = ((x1 - x0) ** 2 + (y1 - y0) ** 2) ** 0.5
    print(g)
    c.create_line(x0, y0, x1, y1, fill='green',
                width=5, arrow=LAST, dash=(10,2),
                activefill='lightgreen',
                arrowshape="10 20 10")
    while g0 < g:
        g0 += v * t
        print(g, g0)

root.mainloop()
