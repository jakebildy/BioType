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
lightgreen = '#%02x%02x%02x' % (135, 255, 117)
greygreen = '#%02x%02x%02x' % (160, 190, 140)

root.configure(bg=darkish)


Label(root, text="BioType", font='Futura 30 bold', bg=darkish, fg=whitish).grid(row=0, column=1)
Label(root, text="Construction File Visualizer", font='Futura 15', bg=darkish, fg=whitish).grid(row=1, column=1)

sidebar  = Frame(root, bg=darkish, width=30, height=30)
sidebar.grid(row=3, column=0)
sidebar  = Frame(root, bg=darkish, width=30, height=30)
sidebar.grid(row=3, column=2)

instructions  = Text(root, font='Menlo 18', bg=darkish, fg=whitish, width=100, height=6)
instructions.grid(row=3, column=1)

editor  = Text(root, font='Menlo 18', bg=darkish, fg=whitish, width=100, height=30)
editor.grid(row=4, column=1)

tags = ["grey", "pink", "green", "cyan", "whiteblue", "orange",
        "red", "lightgreen", "greygreen", "hRed", "default"]

editor.tag_config("grey", foreground=greyOut)
editor.tag_config("pink", foreground=pink)
editor.tag_config("green", foreground=code_green)
editor.tag_config("cyan", foreground=cyan)
editor.tag_config("whiteblue", foreground=whiteblue)
editor.tag_config("orange", foreground=orange)
editor.tag_config("red", foreground=red)
editor.tag_config("lightgreen", foreground=lightgreen)
editor.tag_config("greygreen", foreground=greygreen)
editor.tag_config("hRed", background=red)
editor.tag_config("default", foreground=whitish, background=darkish)

fileStr = open('KanR_Basic_Part_Construction.txt').read()
editor.insert(INSERT, fileStr)

class Util :
    def isPlasmid(pos):
        if (editor.get(pos) == "p") &  (editor.get(pos.__add__("+ 1 chars")).isupper()):
            return True

    def seqColor(pos):
        if util.isPlasmid(pos):
            return "lightgreen"
        else:
            return "pink"

    def textStyle(self):

        for t in tags:
            editor.tag_remove(t, '1.0', END)

        pos = editor.search(r"-|>", '1.0', stopindex=END, regexp=True)

        while pos != '':
            editor.tag_add("grey", pos)
            pos = editor.search(r"-|>", pos.__add__("+ 1 chars"), stopindex=END, regexp=True)

        pos = editor.search(r"Ligate|Digest|PCR", '1.0', stopindex=END, regexp=True)

        while pos != '':

            while (editor.get(pos) != "") & (editor.get(pos) != " ") & (editor.get(pos) != "\n"):
                editor.tag_add("cyan", pos)
                pos = pos.__add__("+ 1 chars")

            color = util.seqColor(pos)

            while (editor.get(pos) != "") & (editor.get(pos) != "\n"):

                while (editor.get(pos) == " ") | (editor.get(pos) == "(") | (editor.get(pos) == ")") \
                        | (editor.get(pos) == ",") | (editor.get(pos) == "/"):
                    pos = pos.__add__("+ 1 chars")
                    color = util.seqColor(pos)

                if editor.get(pos) == "\n":
                    break

                if (editor.get(pos) == "a") & (editor.get(pos.__add__("+ 1 chars")) == "n") & \
                        (editor.get(pos.__add__("+ 2 chars")) == "d") & (editor.get(pos.__add__("+ 3 chars")) == " "):
                    pos = pos.__add__("+ 4 chars")
                    color = util.seqColor(pos)
                if (editor.get(pos) == "o") & (editor.get(pos.__add__("+ 1 chars")) == "n") & \
                        (editor.get(pos.__add__("+ 3 chars")) == " "):

                    pos = pos.__add__("+ 3 chars")
                    color = util.seqColor(pos)

                else:
                    editor.tag_add(color, pos)
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

            for x in range(6):
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

            pos = pos.__add__("+ 1 chars")

            color = util.seqColor(pos)

            while (editor.get(pos) != "") & (editor.get(pos) != "\n"):

                if editor.get(pos) == " ":
                    pos = pos.__add__("+ 1 chars")
                    color = "greygreen"
                if (editor.get(pos) == "a") & (editor.get(pos.__add__("+ 1 chars")) == "n") & \
                        (editor.get(pos.__add__("+ 2 chars")) == "d") & (editor.get(pos.__add__("+ 3 chars")) == " "):
                    pos = pos.__add__("+ 4 chars")
                    # color = util.seqColor(pos)
                if (editor.get(pos) == "o") & (editor.get(pos.__add__("+ 1 chars")) == "n") & \
                        (editor.get(pos.__add__("+ 3 chars")) == " "):

                    pos = pos.__add__("+ 3 chars")
                    # color = util.seqColor(pos)

                else:
                    editor.tag_add(color, pos)
                    pos = pos.__add__("+ 1 chars")

            pos = editor.search(">", pos.__add__("+ 1 chars"), stopindex=END)


util = Util

util.textStyle(util)

def running():

    i = 0

    while True:
        time.sleep(0.05)
        i += 1

        if (i % 20 == 0) :
            util.textStyle(util)

        root.update_idletasks()
        root.update()






# display everything

root.title("BioType")

top = root.winfo_toplevel()
menuBar = Menu(top)
top['menu'] = menuBar
subMenu = Menu(menuBar)

menuBar.add_cascade(label='Open Construction File', menu=subMenu)

button = Button(root, text='▶', font='Futura 35', borderwidth=0, highlightbackground="black", bg=darkish, fg=code_green).grid(row=2,column=0)
label = Label(root, text=' Run PCR', bg=darkish,fg=whitish, font="Futura 20").grid(row=2,column=1, sticky='w')

running()



