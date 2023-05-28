import random
import tkinter as tk

cislo = random.randint(1, 9) * 10**7

for i in range(7):
    cislo += random.randint(1, 9) * 10**i
    
print(cislo)

c = tk.Canvas(width=500, height=500)
c.pack()

x = 250
y = 200
BOLDNESS = 15

numbers = c.create_text(x, y, text=cislo, font=('Arial', BOLDNESS))

for i in range(len(str(cislo))):
    line_x = x - 8*BOLDNESS/2 +10
    c.create_line(line_x+i*15, 100, line_x+i*15, 175, width=str(cislo)[i])


c.mainloop()

