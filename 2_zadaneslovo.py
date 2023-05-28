import tkinter as tk
import time

word = input('Zadaj slovo:')

c = tk.Canvas(width=1000, height=1000)
c.pack()

pismenka = []
y = 450
for x in word:
    pismenka.append(x)
    letter = c.create_text(1000,500, text=x, font=('Calibri', '24'))
    
    while c.coords(letter)[0] > y:
        c.move(letter, -10,0)
        print(c.coords(letter)[0])

        time.sleep(0.02)
        c.update()
    y += 20
c.mainloop()