from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askopenfilename, asksaveasfilename
import os

win= Tk()
win.title("Untitled Notepad")
win.geometry("526x354")
# win.iconbitmap("C:\\Users\\Aditya Barai\\OneDrive\\Desktop\\project\\calculate_image.PNG ")
win.iconbitmap("C:\\Users\\Aditya Barai\\OneDrive\\Desktop\\project\\python project\\man-icon.PNG ")
def newfile():
    global file
    win.title("New Untitled")
    file=None
    text.delete(1.0,END)
    pass
def openfile():
    global file
    file=askopenfilename(defaultextension=".txt",filetypes=[("All Files","*.*"),("Text Documents","*.txt")])
    if file == " ":
        file = None
    else :
        win.title(os.path.basename(file)+" - Notepad")
        text.delete(1.0,END)
        f=open(file,'r')
        text.insert(1.0,f.read())
        f.close
def savefile():
    global file
    if file == None:
        file=asksaveasfilename(initialfile=".txt",defaultextension=".txt",filetypes=[("All Files","*.*"),("Text Documents","*.txt")])
        if file == " ":
            file = None
        else:
            f = open(file,"w")
            f.write(text.get(1.0,END))
            f.close
    else:
        f = open(file,"w")
        f.write(text.get(1.0,END))
        f.close
def saveasfile():
    pass
def exitfile():
    win.destroy()
def cut():
    text.event_generate(("<<Cut>>"))
def copy():
    text.event_generate(("<<Copy>>"))
def paste():
    text.event_generate(("<<Paste>>"))
def undo():
    text.event_generate(("<<Undo>>"))
def select():
    text.event_generate(("<<Select all>>"))
def Help():
    pass
def about():
    messagebox.showinfo("Notepad",  "Notepad © 2023 Aditya Barai. All Rights Reserved.")
text=Text(win)
file=None
mainmenu=Menu(win)
File=Menu(mainmenu,tearoff=0)     
File.add_command(label="New",command=newfile)
File.add_command(label="Open",command=openfile)
File.add_command(label="Save",command=savefile)
File.add_command(label="Save as",command=saveasfile)
File.add_separator()
File.add_command(label="Exit",command=exitfile)
mainmenu.add_cascade(label="File", menu=File)

Edit=Menu(mainmenu,tearoff=0)
Edit.add_command(label="Cut",command=cut)
Edit.add_command(label="Copy",command=copy)
Edit.add_command(label="Paste",command=paste)
Edit.add_command(label="Undo",command=undo)
Edit.add_separator()
Edit.add_command(label="Select all",command=select)
mainmenu.add_cascade(label="Edit",menu=Edit)

View=Menu(mainmenu,tearoff=0)
View.add_command(label="Help",command=Help)
View.add_separator()
View.add_command(label="About",command=about)
mainmenu.add_cascade(label="View",menu=View)

scroll=Scrollbar(text)
scroll.pack(side=RIGHT,fill=Y)
scroll.config(command=text.yview)
text.configure(yscrollcommand=scroll.set)
win.config(menu=mainmenu)
text.pack(expand=True,fill=BOTH)
win.mainloop()
