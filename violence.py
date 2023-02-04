import tkinter as tk
from tkinter import *
import time 
import numpy, random, math
import player as pl
from player import *
import keyboard


canvasWidth = 1536
canvasHeight = 864# full width of canvas in pixels
grav=9

win=tk.Tk()
win.geometry("1600x800")

can=Canvas(win, width=1600, height=800, bg="#33FF6E")
can.pack()
can.create_line(800,0,800,800, width=4)

p1=pl.player(can,400,800, "#6431D3")
#p1.draw()
def up(event):
  p1.jump()
win.bind("<w>" , up) 
while True:
  
  time.sleep(0.01)
  win.update()
  


win.mainloop()