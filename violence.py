import tkinter, numpy, random, math
                  # width of one site in pixels (change if desired)
canvasWidth = 1536
canvasHeight = 864# full width of canvas in pixels

running = False                     # will be true when simulation is running
theWindow = tkinter.Tk()            # create the GUI window
theWindow.title("player screen")

theCanvas = tkinter.Canvas(theWindow, width=canvasWidth, height=canvasHeight)
