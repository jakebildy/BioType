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
sequences = []

class Enzyme :

    name = ""
    site = "" #5'-3'
    siteRC = "" #3'-5'
    color = ""
    cutBefore = 0

    def digest(self, sequence):

        spot = sequence.find(self.site)
        sequence[spot+ self.cutBefore].insert("\n \n \n \n")



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
    namePos = ""
    sequence = ""
    endPos = ""

    def changeName (self, newName) :
        editor.delete(self.namePos, self.namePos.__add__("+ "+str(len(self.name))+" chars"))
        editor.insert(self.namePos, newName)
        self.name = newName

    def get(self, name):
        for s in sequences:
            if s.name == name :
                return s

    def cutBefore(self, seq):
        print()

    def cutAfter(self, seq):
        print()

    def addPrimerF(self, primer):
        print()

    def addPrimerR(self, primer):
        print()

    def greyOut(self):
        editor.delete(self.namePos.__add__("- 1 chars"))
        editor.insert(self.namePos.__add__("- 1 chars"), "#")
        editor.insert(self.namePos.__add__("- 1 chars + 1 lines"), "#")
        editor.tag_add("grey", self.namePos.__add__("- 1 chars"), self.endPos)

    def showReverseCompliment(self):
        print()

    def initSequences(self) :

        pos = editor.search(">", '1.0', stopindex=END, regexp=True)

        while pos != '':

            s = Sequence()
            s.namePos = pos.__add__("+ 1 chars")

            if pos != '':
                pos = pos.__add__("+ 1 chars")
                while not util.isCrap(pos, editor) :

                    s.name += editor.get(pos)
                    pos = pos.__add__("+ 1 chars")

            sequences.append(s)
            pos = editor.search(r">", pos, stopindex=END, regexp=True)
            if pos != '' :
                s.endPos = pos
                s.sequence = editor.get(s.namePos.__add__(" lineend + 1 chars"), pos.__add__(" -1 chars"))
            else :
                s.endPos = END
                s.sequence = editor.get(s.namePos.__add__(" lineend + 1 chars"), END)



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
        | (txt.get(pos) == ",") | (txt.get(pos) == "/")| (txt.get(pos) == ",")| (txt.get(pos) == "+")| (txt.get(pos) == "\n"):
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
        txt.tag_config("sticky", font="Futura 12")
        txt.tag_config("stickyOnCompliment", font="Futura 12", underline=True)
        
        for t in tags:
            txt.tag_remove(t, '1.0', END)

        for e in enzymes:
            txt.tag_remove(e.name, '1.0', END)
            txt.tag_remove(e.name+"_site", '1.0', END)

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

            pos = txt.search(r"and|on|with|product|is", pos.__add__("+ 1 chars"), stopindex=END, regexp=True)


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


        pos = txt.search("#", '1.0', stopindex=END)
        while pos != '':

            pos2 = pos.__add__("lineend")

            if pos2 == '':
                pos2 = END

            for t in tags:
                txt.tag_remove(t, pos, pos2)

            color = "grey"
            txt.tag_add(color, pos, pos2)

            pos = txt.search("#", pos2, stopindex=END)



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

instructions = []

class Instruction :
    type = ""
    inputs = []
    inputOn = Sequence()
    enzymes = []
    output = Sequence()
    pos =  ""
    bp = 0

    def initInstructions(self):
        print()

    def greyOut(self):
        editor.insert(self.pos, '#')



def PCR():
    Sequence.initSequences(Sequence)
    Sequence.changeName(sequences[2], "pcrpdt")

    for i in instructions[0].inputs :
        Sequence.greyOut(Sequence.get(i.name))

    Sequence.greyOut(sequences[0])
    editor.insert(instructions[0].pos, '#')

def Ligate():
    Sequence.initSequences(Sequence)
    Sequence.changeName(sequences[2], "pcrpdt")

    for i in instructions[0].inputs :
        Sequence.greyOut(Sequence.get(i.name))

    Sequence.greyOut(sequences[0])
    editor.insert(instructions[0].pos, '#')

def Digest():
    instruct = instructions[0]
    Instruction.greyOut(instruct)

    Sequence.initSequences(Sequence)
    Sequence.changeName(instruct.inputs[0].name, instruct.output.name)

    for enz in instructions[0].enzymes :
        Enzyme.digest(enz, instruct.inputs[0].sequence)

    Sequence.selectSeqFromBp(instruct.bp)


# display everything

root.title("BioType")

top = root.winfo_toplevel()
menuBar = Menu(top)
top['menu'] = menuBar
subMenu = Menu(menuBar)
enzymeMenu = Menu(menuBar)
runMenu = Menu(menuBar)

menuBar.add_cascade(label='Run', menu=runMenu)
runMenu.add_command(label='Run PCR', command=PCR)
runMenu.add_command(label='Run Digest', command=Digest)

menuBar.add_cascade(label='Open Construction File', menu=subMenu)
menuBar.add_cascade(label='Enzymes', menu=enzymeMenu)

label = Label(root, text='▶ Run PCR', bg=darkish,fg=whitish, font="Futura 20")

label.grid(row=3,column=1, sticky='e')



running()



