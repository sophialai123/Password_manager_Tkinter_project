from tkinter import *

#create window
window = Tk()

#create labels
r = Label(bg="red", width=20, height=5)
r.grid(row=0, column=0)

g = Label(bg="green", width=20, height=5)
g.grid(row=1, column=1)

# to doubled the width
b = Label(bg="blue", width=40, height=5)

# grid columnspan to expand two columns
b.grid(row=2, column=0, columnspan=2)

window.mainloop()