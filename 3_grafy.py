import math
import tkinter as tk
import time as t

c = tk.Canvas(width=600, height=600)
c.pack()
R = 360
def sin(x,y):
    z = 150
    c.create_line(x,y+z/2,x+300,y+z/2)
    c.create_line(x+50,y,x+50,y+z)

    for i in range(R*4):
        c.create_line(x+50+i*0.2,y+z/2-math.sin(math.radians(i))*50,x+50+i*0.2+1,y+z/2-math.sin(math.radians(i))*50)


def cos(x,y):
    z = 150
    c.create_line(x,y+z/2,x+300,y+z/2)
    c.create_line(x+50,y,x+50,y+z)
    
    for i in range(R*4):
        c.create_line(x+50+i*0.2,y+z/2-math.cos(math.radians(i))*50,x+50+i*0.2+1,y+z/2-math.cos(math.radians(i))*50)
    
sin(100,100)
cos(100,400)
c.mainloop()
