import tkinter as tk
import time
import random as rnd

c = tk.Canvas(width=1000, height=1000)
c.pack()

img = tk.PhotoImage(file='car.png')
img2 = tk.PhotoImage(file='carr.png')
img3 = tk.PhotoImage(file='carrr.png')
img = img.subsample(2)
car3 = c.create_image(-200,700, image=img3)
car1 = c.create_image(-200,200, image=img)
car2 = c.create_image(-200,500, image=img2)

start = True
a = rnd.randrange(12, 20)/10
a2 = rnd.randrange(12, 20)/10
a3 = rnd.randrange(12, 20)/10
first = 1
while start:
    c.move(car1, a, 0)
    c.move(car2, a2, 0)
    c.move(car3, a3, 0)
    if (c.coords(car1)[0] > 1000) and first ==1:
        c.create_text(500,500, text="CAR 1 WOON",font=('Calibri', 150))
        first = 0
    if (c.coords(car2)[0] > 1000) and first==1:
        c.create_text(500,500, text="CAR 2 WOON",font=('Calibri', 150))
        first = 0
    if (c.coords(car3)[0] > 1000) and first ==1:
        c.create_text(500,500, text="CAR 3 WOON",font=('Calibri', 150))
        first = 0
    time.sleep(0.01)
    c.update()

