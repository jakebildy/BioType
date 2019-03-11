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

fileStr = open('KanR_Basic_Part_Construction.txt').read()
editor.insert(INSERT, fileStr)

tags = ["grey", "pink", "green", "cyan", "whiteblue", "orange",
        "red", "lightgreen", "greygreen", "hRed", "default"]

class Util :
    def isPlasmid(pos):
        if (editor.get(pos) == "p") &  (editor.get(pos.__add__("+ 1 chars")).isupper()):
            return True

    def seqColor(pos):
        if util.isPlasmid(pos):
            return "lightgreen"
        else:
            return "pink"

    def textStyle(self, txt):

        txt.tag_config("grey", foreground=greyOut)
        txt.tag_config("pink", foreground=pink)
        txt.tag_config("green", foreground=code_green, underline=True)
        txt.tag_config("cyan", foreground=cyan)
        txt.tag_config("whiteblue", foreground=whiteblue)
        txt.tag_config("orange", foreground=orange)
        txt.tag_config("red", foreground=red)
        txt.tag_config("lightgreen", foreground=lightgreen)
        txt.tag_config("greygreen", foreground=greygreen)
        txt.tag_config("hRed", background=red)
        txt.tag_config("default", foreground=whitish, background=darkish)
        
        for t in tags:
            txt.tag_remove(t, '1.0', END)

        pos = txt.search(r"-|>", '1.0', stopindex=END, regexp=True)

        while pos != '':
            txt.tag_add("grey", pos)
            pos = txt.search(r"-|>", pos.__add__("+ 1 chars"), stopindex=END, regexp=True)

        pos = txt.search(r"Ligate|Digest|PCR", '1.0', stopindex=END, regexp=True)

        while pos != '':

            while (txt.get(pos) != "") & (txt.get(pos) != " ") & (txt.get(pos) != "\n"):
                txt.tag_add("cyan", pos)
                pos = pos.__add__("+ 1 chars")

            color = util.seqColor(pos)

            while (txt.get(pos) != "") & (txt.get(pos) != "\n"):

                while (txt.get(pos) == " ") | (txt.get(pos) == "(") | (txt.get(pos) == ")") \
                        | (txt.get(pos) == ",") | (txt.get(pos) == "/"):
                    pos = pos.__add__("+ 1 chars")
                    color = util.seqColor(pos)

                if txt.get(pos) == "\n":
                    break

                if (txt.get(pos) == "a") & (txt.get(pos.__add__("+ 1 chars")) == "n") & \
                        (txt.get(pos.__add__("+ 2 chars")) == "d") & (txt.get(pos.__add__("+ 3 chars")) == " "):
                    pos = pos.__add__("+ 4 chars")
                    color = util.seqColor(pos)
                if (txt.get(pos) == "o") & (txt.get(pos.__add__("+ 1 chars")) == "n") & \
                        (txt.get(pos.__add__("+ 3 chars")) == " "):

                    pos = pos.__add__("+ 3 chars")
                    color = util.seqColor(pos)

                else:
                    txt.tag_add(color, pos)
                    pos = pos.__add__("+ 1 chars")

            pos = txt.search(r"Ligate|Digest|PCR", pos.__add__("+ 1 chars"), stopindex=END, regexp=True)

        pos = txt.search(r"EcoRI|SpeI|BsmI", '1.0', stopindex=END, regexp=True)

        while pos != '':

            while (txt.get(pos) != "") & (txt.get(pos) != " ") & (txt.get(pos) != "\n") \
                    & (txt.get(pos) != "/") & (txt.get(pos) != ","):
                txt.tag_add("green", pos)
                pos = pos.__add__("+ 1 chars")

            pos = txt.search(r"EcoRI|SpeI|BsmI", pos.__add__("+ 1 chars"), stopindex=END, regexp=True)

        pos = txt.search(r"GAATTC|gaattc|ACTAGT|actagt", '1.0', stopindex=END, regexp=True)

        while pos != '':

            for x in range(6):
                txt.tag_add("hRed", pos)
                pos = pos.__add__("+ 1 chars")

            pos = txt.search(r"GAATTC|gaattc|ACTAGT|actagt", pos.__add__("+ 1 chars"), stopindex=END, regexp=True)

        pos = txt.search(r"and|on|with", '1.0', stopindex=END, regexp=True)

        while pos != '':

            while (txt.get(pos) != "") & (txt.get(pos) != " ") & (txt.get(pos) != "\n"):
                txt.tag_add("whiteblue", pos)
                pos = pos.__add__("+ 1 chars")

            pos = txt.search(r"and|on|with", pos.__add__("+ 1 chars"), stopindex=END, regexp=True)

        pos = txt.search("bp", '1.0', stopindex=END)

        while pos != '':

            pos2 = pos
            pos = pos.__add__("+ 1 chars")

            while (txt.get(pos) != "") & (txt.get(pos) != " ") & (txt.get(pos) != "("):
                txt.tag_add("orange", pos)
                pos = pos.__add__("- 1 chars")

            pos = txt.search(r"bp", pos2.__add__("+ 1 chars"), stopindex=END, regexp=True)

        pos = txt.search(">", '1.0', stopindex=END)

        while pos != '':

            pos = pos.__add__("+ 1 chars")

            color = util.seqColor(pos)

            while (txt.get(pos.__add__("+ 1 chars")) != txt.get(pos.__add__(" lineend"))):

                if txt.get(pos) == " ":
                    color = "greygreen"
                    if not (txt.get(pos.__add__("+ 1 chars")) != txt.get(pos.__add__(" lineend"))) :
                        pos = pos.__add__("+ 1 chars")

                if (txt.get(pos) == "a") & (txt.get(pos.__add__("+ 1 chars")) == "n") & \
                        (txt.get(pos.__add__("+ 2 chars")) == "d") & (txt.get(pos.__add__("+ 3 chars")) == " "):
                    pos = pos.__add__("+ 4 chars")
                    # color = util.seqColor(pos)
                if (txt.get(pos) == "o") & (txt.get(pos.__add__("+ 1 chars")) == "n") & \
                        (txt.get(pos.__add__("+ 3 chars")) == " "):

                    pos = pos.__add__("+ 3 chars")
                    # color = util.seqColor(pos)

                else:
                    txt.tag_add(color, pos)
                    pos = pos.__add__("+ 1 chars")

            pos = txt.search(">", pos.__add__("+ 1 chars"), stopindex=END)


util = Util

util.textStyle(util, editor)
util.textStyle(util, instructions)

def running():

    i = 0

    while True:
        time.sleep(0.05)
        i += 1

        if (i % 20 == 0) :
            util.textStyle(util,  editor)
            util.textStyle(util, instructions)

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



