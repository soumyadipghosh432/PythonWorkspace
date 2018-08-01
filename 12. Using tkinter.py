try:
    import tkinter
except ImportError: #For python2
    import Tkinter as tinter

print(tkinter.TkVersion)
print(tkinter.TclVersion)

# test if tkinter is working
tkinter._test()

mainWindow = tkinter.Tk() # Initialize
mainWindow.title("My Application") # Setting the window title
# set initial size of application window : (width x height + offset from left + offset from top) or (width x height - offset from right - offset from bottom)
mainWindow.geometry("640x480+15+20")

label = tkinter.Label(mainWindow, text="This is some text in label")
label.pack(side="top")

canvas = tkinter.Canvas(mainWindow, relief="raised", borderwidth=1)

#### CANVAS with left alignment
#canvas.pack(side="left", fill=tkinter.BOTH, expand=True) # make the canvas occupy full space as of the window
#canvas.pack(side="left", fill=tkinter.X) # will not make canvas full
#canvas.pack(side="left", fill=tkinter.X, expand=True) # will make canvas full
#canvas.pack(side="left", fill=tkinter.Y, expand=True) # will make canvas full, but align to centre not left
#canvas.pack(side="left", fill=tkinter.Y) # will make canvas full from left

#### CANVAS with top alignment
#canvas.pack(side="top", fill=tkinter.BOTH, expand=True) # make the canvas occupy full space as of the window
#canvas.pack(side="top", fill=tkinter.X) # will make canvas full
#canvas.pack(side="top", fill=tkinter.X, expand=True) # will make canvas full, but from middle alignment
#canvas.pack(side="top", fill=tkinter.Y, expand=True) # will make canvas full
#canvas.pack(side="top", fill=tkinter.Y) # will not make canvas full

canvas.pack(side="left")


button1 = tkinter.Button(mainWindow, text = "Button 1")
button2 = tkinter.Button(mainWindow, text = "Button 2")
button3 = tkinter.Button(mainWindow, text = "Button 3")
# this will add these buttons left relative to parent canvas i.e. right to the canvas of element last added but aligned to left
button1.pack(side="left", anchor='n') # north direction to main window, since main,canvas and buttons are aligned left, this will be affected
button2.pack(side="left", anchor='s') # south direction to main window, since main,canvas and buttons are aligned left, this will NOT be affected
button3.pack(side="left", anchor='e') # east direction to main window, since main,canvas and buttons are aligned left, this will be affected

mainWindow.mainloop() # This will start the application in GUI


########################### Using Frames ###############################

try:
    import tkinter
except ImportError: #For python2
    import Tkinter as tinter

mainWindow = tkinter.Tk()
mainWindow.title("My Application")
mainWindow.geometry("640x480+15+20")

label = tkinter.Label(mainWindow, text="This is some text in label")
label.pack(side="top")

leftFrame = tkinter.Frame(mainWindow)
leftFrame.pack(side="left", anchor ="n", fill=tkinter.Y, expand=False)

rightFrame = tkinter.Frame(mainWindow)
rightFrame.pack(side="right", anchor ="n", expand=True)

canvas = tkinter.Canvas(leftFrame, relief="raised", borderwidth=1)
canvas.pack(side="left", anchor="n")

button1 = tkinter.Button(rightFrame, text = "Button 1")
button2 = tkinter.Button(rightFrame, text = "Button 2")
button3 = tkinter.Button(rightFrame, text = "Button 3")

button1.pack(side="top") 
button2.pack(side="top")
button3.pack(side="top")

mainWindow.mainloop()

########################### Using Tkinter GRID Geometry ###############################

try:
    import tkinter
except ImportError: #For python2
    import Tkinter as tinter

mainWindow = tkinter.Tk()
mainWindow.title("My Application")
mainWindow.geometry("640x480")

label = tkinter.Label(mainWindow, text="This is some text in label")
label.grid(row=0, column=0)

leftFrame = tkinter.Frame(mainWindow)
leftFrame.grid(row=1, column=1, sticky="ns") # anchoring the element to north and expand to south relative to parent

rightFrame = tkinter.Frame(mainWindow)
rightFrame.grid(row=1, column=2, sticky="new") # anchoring the element to north and expand in east-west relative to parent


canvas = tkinter.Canvas(leftFrame, relief="raised", borderwidth=1)
canvas.grid(row=1, column=0)


button1 = tkinter.Button(rightFrame, text = "Button 1")
button2 = tkinter.Button(rightFrame, text = "Button 2")
button3 = tkinter.Button(rightFrame, text = "Button 3")

button1.grid(row=0, column=0, sticky="ew") 
button2.grid(row=1, column=0, sticky="ew")
button3.grid(row=2, column=0, sticky="ew")

# Configure the columns to add space to the elements. STICKY will work only if the weight is assigned to parent
mainWindow.columnconfigure(0, weight=1)
mainWindow.columnconfigure(1, weight=1)
mainWindow.columnconfigure(2, weight=1)
rightFrame.columnconfigure(0, weight=1) # If this weight is not assigned, the sticky for child buttons will not work

leftFrame.config(relief='sunken', borderwidth=1)
rightFrame.config(relief='sunken', borderwidth=1)


mainWindow.mainloop()

