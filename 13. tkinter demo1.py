try:
    import tkinter
except ImportError: #For python2
    import Tkinter as tinter

import os    

mainWindow = tkinter.Tk()
mainWindow.title("Demo design")
mainWindow.geometry("640x480+8+8")

mainWindow.columnconfigure(0,weight=1)
mainWindow.columnconfigure(1,weight=1)
mainWindow.columnconfigure(2,weight=1)
mainWindow.columnconfigure(3,weight=3)
mainWindow.columnconfigure(4,weight=3)

mainWindow.rowconfigure(0,weight=1)
mainWindow.rowconfigure(2,weight=10)
mainWindow.rowconfigure(3,weight=1)
mainWindow.rowconfigure(4,weight=3)
mainWindow.rowconfigure(5,weight=3)

# Label
label = tkinter.Label(mainWindow, text="Demo Application Design")
label.grid(row=0, column=0, columnspan=3)


# List box
fileList = tkinter.Listbox(mainWindow)
fileList.grid(row=1, column=0, sticky='nsew', rowspan=2)
fileList.config(border=2, relief='sunken')

for item in os.listdir('C:\\Users\\757966\\Documents\\Personal\\Need Backup\\Python Workspace'):
    fileList.insert(tkinter.END, item)

# Scrollbar to list box
listScroll = tkinter.Scrollbar(mainWindow, orient=tkinter.VERTICAL, command=fileList.yview)
listScroll.grid(row=1, column=1, sticky="nsw", rowspan=2)
fileList['yscrollcommand'] = listScroll.set


# Frame for Radio Buttons
optionFrame = tkinter.LabelFrame(mainWindow, text="Details")
optionFrame.grid(row=1, column=2, sticky="ne")

mainWindow.mainloop()

