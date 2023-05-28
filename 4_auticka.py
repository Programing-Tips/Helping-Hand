import tkinter as tk
import time

c = tk.Canvas(width=700, height=800)
c.pack()
c.update()
#car1 = tk.PhotoImage(file='Adresa suboru')
auto_1 = c.create_image(c.winfo_width() + 100,100, image=car1)

#car2 = tk.PhotoImage(file='adresa suboru')
auto_2 = c.create_image(-100,100, image=car2)

while True:
    c.move(auto_1, -3,0)
    c.move(auto_2, 3,0)
    time.sleep(0.01)
    c.update()
    if c.coords(auto_1)[0] < -50:
        exit()

