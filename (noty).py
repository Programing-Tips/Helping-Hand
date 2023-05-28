import tkinter as tk


c = tk.Canvas(width=600, height=600)
c.pack()

x = 100
y = 250

for i in range (1, 6):
    c.create_line(x, y+i*10, x+400, y+i*10, widt=3, fill='black')

c.create_line(130, 310, 160, 310, width=3)

x = 135
y = 315

for i in range (0, 8):
    c.create_oval(x+i*25, y-i*5, x+20+i*25, y-10-i*5, width=2)

c.mainloop()
