import tkinter as tk
from tkinter import *
import numpy, random, math
                  # width of one site in pixels (change if desired)
canvasWidth = 1536
canvasHeight = 864# full width of canvas in pixels

win=tk.Tk()
win.geometry("1600x800")
p1=Canvas(win, width=800, height=800, bg="#FF5733")
p1.pack(side="left")
#p2=Canvas(win, width=800, height=500)
win.mainloop()
