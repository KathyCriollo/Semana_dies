#Juego

from tkinter import *
import random
import time

class Pelota:
    def __init__(self, canvas, color):
        self.canvas= canvas
        self.id= canvas.create_oval(10, 10, 25, 25, fill=color)
        self.canvas.move(self.id, 245, 100)

        self.x= 0;
        self.y= -1;
        self.canvas_height= self.canvas.winfo_height()
 
    def draw(self):
        self.canvas.move(self.id, self.x, self.y)
        pos= self.canvas.coords(self.id)
        print (self.canvas.coords(self.id)) #imprime las coordenadas pero consecutivamente

tk= Tk()
tk.title("Mi primer juego en Python")
tk.resizable(0, 0)
tk.wm_attributes("-topmost", 1)
canvas= Canvas(tk, width=500, height=400, bd=0, highlightthickness=0)
canvas.pack()
tk.update()

pelota= Pelota(canvas, 'red')
while 1:
    pelota.draw()
    tk.update_idletasks()
    tk.update()
    time.sleep(0.01)

tk.mainloop()