import tkinter as tk
from tkinter import *
import time 
import numpy, random, math
import player as pl
from player import *


canvasWidth = 1536
canvasHeight = 864# full width of canvas in pixels
grav=0.5;
floor=800;

win=tk.Tk()
win.geometry("1600x800")

can=Canvas(win, width=1600, height=800, bg="#33FF6E")
can.pack()
can.create_line(800,0,800,800, width=4)

p1=pl.player(can,400,800, "#6431D3")
#p1.draw()
def up(event):
  while (p1.y-p1.dy<=floor):
    p1.y-=p1.dy
    can.move(p1.body,0,-p1.dy)
    time.sleep(0.02)
    p1.dy-=grav 
    can.update() 
    if(p1.y==floor):
      break
  p1.dy=15
  #print(p1.y) 
def right(event):
  p1.x+=p1.dx
  can.move(p1.body,p1.dx,0)
  
def left(event):
  p1.x-=p1.dx
  can.move(p1.body,-p1.dx,0)
  
win.bind("<w>" , up)  
win.bind("<a>" , left)  
win.bind("<d>" , right)  

p2=pl.player(can,1200,800, "#6431D3")
#p1.draw()
def up(event):
  while (p2.y-p2.dy<=floor):
    p2.y-=p2.dy
    can.move(p2.body,0,-p2.dy)
    time.sleep(0.02)
    p2.dy-=grav 
    can.update() 
    if(p2.y==floor):
      break
  p2.dy=15
  #print(p1.y) 
def right(event):
  if p2.x<1580:
    p2.x+=p2.dx
    can.move(p2.body,p2.dx,0)
  
def left(event):
  if p2.x>820:
    p2.x-=p2.dx
    can.move(p2.body,-p2.dx,0)
  
win.bind("<Up>" , up)  
win.bind("<Left>" , left)  
win.bind("<Right>" , right)  

can.pack()

win.mainloop()
