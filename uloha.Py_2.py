import tkinter, random, math,time
Height = 500
Width = 500

c = tkinter.Canvas(width = Width, height = Height, background = "white")

c.pack()

def create_circle(x, y, r, canvas, color):

    x0 = x - r

    y0 = y - r

    x1 =x + r

    y1 = y + r

    return canvas.create_oval(x0, y0, x1,y1,fill = color, outline = color)

def create_animated_circle(x, y, r, color):

    while r <=x:

        colour=color[random.randint(0,2)]

        create_circle(x,y,r,c,colour)

        time.sleep(0.001)

        c.update()

        r+=1

    create_circle(x,y,r,c,"white")

    time.sleep(0.001)

    c.update()


color =["pink","Cyan","blue"]

x=Height/2

y=Width/2

r=0

while True: 
    create_animated_circle(x,y,r,color)

c.mainloop()