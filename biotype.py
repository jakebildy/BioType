import time
from tkinter import *
import random
import glob

root = Tk()

# Colors
darkish = '#%02x%02x%02x' % (29, 30, 38)
whitish = '#%02x%02x%02x' % (214, 216, 218)
code_green = '#%02x%02x%02x' % (80, 230, 70)
greyOut = '#%02x%02x%02x' % (110, 110, 110)
pink = '#%02x%02x%02x' % (254, 102, 238)
cyan = '#%02x%02x%02x' % (50, 250, 250)
whiteblue  = '#%02x%02x%02x' % (173, 250, 220)
orange = '#%02x%02x%02x' % (250, 140, 0)
red = '#%02x%02x%02x' % (239, 30, 0)

root.configure(bg=darkish)


Label(root, text="BioType", font='Futura 25 bold', bg=darkish, fg=whitish).grid(row=0, column=1)
Label(root, text="Construction File Visualizer", font='Futura 15', bg=darkish, fg=whitish).grid(row=1, column=1)

sidebar  = Frame(root, bg=darkish, width=30, height=30)
sidebar.grid(row=2, column=0)
sidebar  = Frame(root, bg=darkish, width=30, height=30)
sidebar.grid(row=2, column=2)

editor  = Text(root, font='Menlo 18', bg=darkish, fg=whitish, width=100, height=30)
editor.grid(row=2, column=1)

editor.tag_config("grey", foreground=greyOut)
editor.tag_config("pink", foreground=pink)
editor.tag_config("green", foreground=code_green)
editor.tag_config("cyan", foreground=cyan)
editor.tag_config("whiteblue", foreground=whiteblue)
editor.tag_config("orange", foreground=orange)
editor.tag_config("red", foreground=red)

editor.tag_config("hRed", background=red)

fileStr = open('KanR_Basic_Part_Construction.txt').read()
editor.insert(INSERT, fileStr)


def running():

    while True:
        time.sleep(0.05)
        root.update_idletasks()
        root.update()



pos = editor.search(r"-|>", '1.0', stopindex=END, regexp=True)

while pos != '':
    editor.tag_add("grey", pos)
    pos = editor.search(r"-|>", pos.__add__("+ 1 chars"), stopindex=END, regexp=True)




pos = editor.search(r"Ligate|Digest|PCR", '1.0', stopindex=END, regexp=True)

while pos != '':

    while (editor.get(pos) != "") & (editor.get(pos) != " ") & (editor.get(pos) != "\n"):
        editor.tag_add("cyan", pos)
        pos = pos.__add__("+ 1 chars")

    while (editor.get(pos) == " "):
        pos = pos.__add__("+ 1 chars")

    while (editor.get(pos) != "") & (editor.get(pos) != " ") & (editor.get(pos) != "\n"):
        if (editor.get(pos) != "/"):
            editor.tag_add("red", pos)
        pos = pos.__add__("+ 1 chars")



    pos = editor.search(r"Ligate|Digest|PCR", pos.__add__("+ 1 chars"), stopindex=END, regexp=True)



pos = editor.search(r"EcoRI|SpeI|BsmI", '1.0', stopindex=END, regexp=True)

while pos != '':

    while (editor.get(pos) != "") & (editor.get(pos) != " ") & (editor.get(pos) != "\n"):
        editor.tag_add("green", pos)
        pos = pos.__add__("+ 1 chars")

    pos = editor.search(r"EcoRI|SpeI|BsmI", pos.__add__("+ 1 chars"), stopindex=END, regexp=True)



pos = editor.search(r"GAATTC|gaattc|ACTAGT|actagt", '1.0', stopindex=END, regexp=True)

while pos != '':

    for x in range(6) :
        editor.tag_add("hRed", pos)
        pos = pos.__add__("+ 1 chars")

    pos = editor.search(r"GAATTC|gaattc|ACTAGT|actagt", pos.__add__("+ 1 chars"), stopindex=END, regexp=True)







pos = editor.search(r"and|on|with", '1.0', stopindex=END, regexp=True)

while pos != '':

    while (editor.get(pos) != "") & (editor.get(pos) != " ") & (editor.get(pos) != "\n"):
        editor.tag_add("whiteblue", pos)
        pos = pos.__add__("+ 1 chars")

    pos = editor.search(r"and|on|with", pos.__add__("+ 1 chars"), stopindex=END, regexp=True)



pos = editor.search("bp", '1.0', stopindex=END)

while pos != '':

    pos2 = pos
    pos = pos.__add__("+ 1 chars")

    while (editor.get(pos) != "") & (editor.get(pos) != " ") & (editor.get(pos) != "("):
        editor.tag_add("orange", pos)
        pos = pos.__add__("- 1 chars")

    pos = editor.search(r"bp", pos2.__add__("+ 1 chars"), stopindex=END, regexp=True)


pos = editor.search(">", '1.0', stopindex=END)

while pos != '':
    while (editor.get(pos) != "") & (editor.get(pos) != " ") & (editor.get(pos) != "\n"):
        pos = pos.__add__("+ 1 chars")
        editor.tag_add("pink", pos)


    pos = editor.search(">", pos.__add__("+ 1 chars"), stopindex=END)


# display everything

root.title("BioType")

top = root.winfo_toplevel()
menuBar = Menu(top)
top['menu'] = menuBar
subMenu = Menu(menuBar)

menuBar.add_cascade(label='Open Construction File', menu=subMenu)

running()



