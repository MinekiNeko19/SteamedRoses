import tkinter as tk
from tkinter import *
import numpy, random, math
                  # width of one site in pixels (change if desired)
canvasWidth = 1536
canvasHeight = 864# full width of canvas in pixels

win=tk.Tk()
win.geometry("1600x800")

cut=Canvas(win, width=1600, height=800, bg="#33FF6E")
cut.pack()

cut.create_line(800,0,800,800, width=4)

win.mainloop()