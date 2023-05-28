import tkinter as tk

f = open('oznam.txt', 'r')

sentence = f.read()
transformed = ''
for x in sentence:
    transformed = transformed + str(ord(x))

c = tk.Canvas(width=500, height=500)
c.pack()

c.create_text(250,100, text=sentence, fill='blue', activefill='orange' )
c.create_text(250,200, text=transformed, fill='red')


c.mainloop()
''' premena spat na str
hah = transformed.split(' ')
new = ''
for x in hah[:-1]:
    new += chr(int(x))
print(new)
'''