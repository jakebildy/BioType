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
root.configure(cursor="arrow")

Label(root, text="BioType", font='Futura 30 bold', bg=darkish, fg=whitish).grid(row=0, column=1)
Label(root, text="Construction File Visualizer", font='Futura 15', bg=darkish, fg=whitish).grid(row=1, column=1)

sidebar  = Frame(root, bg=darkish, width=60, height=30)
sidebar.grid(row=3, column=0)
sidebar  = Frame(root, bg=darkish, width=60, height=30)
sidebar.grid(row=3, column=2)

editor  = Text(root, font='Menlo 18', bg=darkish, fg=whitish, width=100, height=30,
               highlightbackground=greyOut, highlightthickness=2, insertbackground=whitish,insertwidth=4,cursor="arrow")
editor.grid(row=4, column=1)
fileStr = open('KanR_Basic_Part_Construction.txt').read()
editor.insert(INSERT, fileStr)


tags = ["grey", "pink", "green", "cyan", "whiteblue", "orange",
        "red", "lightgreen", "greygreen", "hRed", "default", "error"]

enzymes =[]


class Enzyme :

    name = ""
    site = "" #5'-3'
    siteRC = "" #3'-5'
    color = ""
    cutBefore = 0

    def addNew(self, n, s, src, c, before):
        e  = Enzyme()
        e.site = s
        e.name = n
        e.siteRC = src
        e.color = c
        e.cutBefore = before
        enzymes.append(e)
    def toHex(self, r,g,b):
        return '#%02x%02x%02x' % (r, g, b)

Enzyme.addNew(Enzyme, "EcoRI", "GAATTC", "GAATTC", Enzyme.toHex(Enzyme, 200, 240, 69),1)
Enzyme.addNew(Enzyme, "SpeI", "ACTAGT", "TGATCA", Enzyme.toHex(Enzyme, 120, 120, 244), 1)


class Sequence :

    name = ""

    def changeName (self, newName):
        print()

    def cutBefore(self, seq):
        print()

    def cutAfter(self, seq):
        print()

    def addPrimerF(self, primer):
        print()

    def addPrimerR(self, primer):
        print()



class Util :
    def isPlasmid(pos, txt):
        if (txt.get(pos) == "p") &  (txt.get(pos.__add__("+ 1 chars")).isupper()):
            return True

    def seqColor(pos, txt):
        if util.isPlasmid(pos, txt):
            return "lightgreen"
        else:
            return "pink"

    def isCrap(pos, txt):
        if (txt.get(pos) == " ") | (txt.get(pos) == "(") | (txt.get(pos) == ")") \
        | (txt.get(pos) == ",") | (txt.get(pos) == "/")| (txt.get(pos) == ",")| (txt.get(pos) == "+"):
            return True

        else :
            return False

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
        txt.tag_config("error", foreground=red, underline=True)
        
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

            color = util.seqColor(pos, txt)

            while (txt.get(pos.__add__("+ 1 chars")) != txt.get(pos.__add__(" lineend"))):

                while (util.isCrap(pos, txt)):
                    pos = pos.__add__("+ 1 chars")
                    color = util.seqColor(pos, txt)

                if (txt.get(pos) == "a") & (txt.get(pos.__add__("+ 1 chars")) == "n") & \
                        (txt.get(pos.__add__("+ 2 chars")) == "d") & (txt.get(pos.__add__("+ 3 chars")) == " "):
                    pos = pos.__add__("+ 4 chars")
                    color = util.seqColor(pos, txt)
                if (txt.get(pos) == "o") & (txt.get(pos.__add__("+ 1 chars")) == "n") & \
                        (txt.get(pos.__add__("+ 3 chars")) == " "):

                    pos = pos.__add__("+ 3 chars")
                    color = util.seqColor(pos, txt)

                else:
                    txt.tag_add(color, pos)
                    pos = pos.__add__("+ 1 chars")


            if not util.isCrap(pos, txt) :
                txt.tag_add(color, pos)

            pos = txt.search(r"Ligate|Digest|PCR", pos.__add__("+ 1 chars"), stopindex=END, regexp=True)


        pos = txt.search(r"and|on|with", '1.0', stopindex=END, regexp=True)
        while pos != '':

            while (txt.get(pos) != "") & (txt.get(pos) != " ") & (txt.get(pos) != "\n"):
                txt.tag_add("whiteblue", pos)
                pos = pos.__add__("+ 1 chars")

            pos = txt.search(r"and|on|with", pos.__add__("+ 1 chars"), stopindex=END, regexp=True)


    # Numbers, bp, etc (orange)

        pos = txt.search(" L,", '1.0', stopindex=END)
        while pos != '':
            txt.tag_add("orange", pos.__add__("+ 1 chars"))
            pos = txt.search(" L,", pos.__add__("+ 1 chars"), stopindex=END)

        pos = txt.search(r"\d", '1.0', stopindex=END, regexp=True)
        while (pos != ''):
            while (txt.get(pos.__add__("- 1 chars")) == "+") | (txt.get(pos.__add__("- 1 chars")) == " ") | (("orange" in txt.tag_names(pos.__add__(" - 1 chars"))) & (txt.get(pos) in "1234567890")) :
                txt.tag_add("orange", pos)
                pos = pos.__add__("+ 1 chars")

            pos = txt.search(r"\d", pos.__add__("+ 1 chars"), stopindex=END, regexp=True)

        pos = txt.search("bp", '1.0', stopindex=END)
        while pos != '':

            pos2 = pos
            pos = pos.__add__("+ 1 chars")

            txt.tag_add("orange", pos)
            pos = pos.__add__("- 1 chars")
            txt.tag_add("orange", pos)
            pos = pos.__add__("- 1 chars")

            while not (util.isCrap(pos, txt)):
                if txt.get(pos) in "1234567890" :
                    txt.tag_add("orange", pos)
                    pos = pos.__add__("- 1 chars")
                else :
                    break

            pos = txt.search(r"bp", pos2.__add__("+ 1 chars"), stopindex=END, regexp=True)

        pos = txt.search(">", '1.0', stopindex=END)
        while pos != '':

            pos = pos.__add__("+ 1 chars")

            color = util.seqColor(pos, txt)

            while (txt.get(pos.__add__("+ 1 chars")) != txt.get(pos.__add__(" lineend"))):

                if txt.get(pos) == " ":
                    color = "greygreen"
                    if not (txt.get(pos.__add__("+ 1 chars")) != txt.get(pos.__add__(" lineend"))) :
                        pos = pos.__add__("+ 1 chars")

                if (txt.get(pos) == "a") & (txt.get(pos.__add__("+ 1 chars")) == "n") & \
                        (txt.get(pos.__add__("+ 2 chars")) == "d") & (txt.get(pos.__add__("+ 3 chars")) == " "):
                    pos = pos.__add__("+ 4 chars")
                    # color = util.seqColor(pos, txt)
                if (txt.get(pos) == "o") & (txt.get(pos.__add__("+ 1 chars")) == "n") & \
                        (txt.get(pos.__add__("+ 3 chars")) == " "):

                    pos = pos.__add__("+ 3 chars")
                    # color = util.seqColor(pos, txt)

                else:
                    txt.tag_add(color, pos)
                    pos = pos.__add__("+ 1 chars")

            if not util.isCrap(pos, txt) :
                txt.tag_add(color, pos)

            pos = txt.search(">", pos.__add__("+ 1 chars"), stopindex=END)

        for enzyme in enzymes :

            txt.tag_config(enzyme.name, foreground=enzyme.color, underline=True)
            txt.tag_config(enzyme.name+"_site", foreground="black", background=enzyme.color)

            pos = txt.search(enzyme.name, '1.0', stopindex=END, regexp=True)

            while pos != '':
                while not (util.isCrap(pos, txt)):
                    txt.tag_add(enzyme.name, pos)
                    pos = pos.__add__("+ 1 chars")

                pos = txt.search(enzyme.name, pos.__add__("+ 1 chars"), stopindex=END, regexp=True)

            regex = r"(?i)("+enzyme.site +"|"+enzyme.siteRC+").*"

            pos = txt.search(regex, '1.0', stopindex=END, regexp=True)
            while pos != '':

                for x in range(6):
                    txt.tag_add(enzyme.name+"_site", pos)
                    pos = pos.__add__("+ 1 chars")

                pos = txt.search(regex, pos.__add__("+ 1 chars"), stopindex=END, regexp=True)


util = Util

util.textStyle(util, editor)

def running():

    i = 0

    while True:
        time.sleep(0.01)
        i += 1

        if (i % 100 == 0) :
            util.textStyle(util,  editor)

        root.update_idletasks()
        root.update()






# display everything

root.title("BioType")

top = root.winfo_toplevel()
menuBar = Menu(top)
top['menu'] = menuBar
subMenu = Menu(menuBar)
enzymeMenu = Menu(menuBar)

menuBar.add_cascade(label='Open Construction File', menu=subMenu)
menuBar.add_cascade(label='Enzymes', menu=enzymeMenu)

label = Label(root, text='▶ Run PCR', bg=darkish,fg=whitish, font="Futura 20")

label.grid(row=3,column=1, sticky='e')


running()



