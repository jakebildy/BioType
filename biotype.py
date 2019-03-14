import time
from tkinter import *
import tkinter.filedialog
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
blueish = '#%02x%02x%02x' % (143, 220, 210)
whiteblue = '#%02x%02x%02x' % (173, 250, 220)
orangetxt = '#%02x%02x%02x' % (250, 140, 0)
red = '#%02x%02x%02x' % (239, 30, 0)
lightgreen = '#%02x%02x%02x' % (135, 255, 117)
greygreen = '#%02x%02x%02x' % (160, 190, 140)
black = '#%02x%02x%02x' % (20, 20, 20)

red = '#%02x%02x%02x' % (255, 60, 60)
green = '#%02x%02x%02x' % (60, 255, 60)
blue = '#%02x%02x%02x' % (60, 60, 255)
orange = '#%02x%02x%02x' % (250, 140, 0)
yellow = '#%02x%02x%02x' % (200, 240, 70)

colors = ["red", "green", "blue", "orange", "yellow", cyan, pink, lightgreen, blueish]

root.configure(bg=darkish)
root.configure(cursor="arrow")

Label(root, text="BioType", font='Futura 30 bold', bg=darkish, fg=whitish).grid(row=0, column=1)
Label(root, text="Construction File Visualizer", font='Futura 15', bg=darkish, fg=whitish).grid(row=1, column=1)

sidebar = Frame(root, bg=darkish, width=60, height=30)
sidebar.grid(row=3, column=0)
sidebar = Frame(root, bg=darkish, width=60, height=30)
sidebar.grid(row=3, column=2)

editor = Text(root, font='Menlo 18', bg=darkish, fg=whitish, width=100, height=30,
              highlightbackground=greyOut, highlightthickness=2, insertbackground=whitish, insertwidth=4,
              cursor="arrow")
editor.grid(row=5, column=1)
fileStr = open('Basic_Part_Construction.txt').read()
editor.insert(INSERT, fileStr)


tags = ["grey", "pink", "green", "cyan", "whiteblue", "orange",
        "red", "lightgreen", "greygreen", "hRed", "default", "error"]

enzymes = []

class Sequence:
    name = ""
    namePos = ""
    sequence = ""
    endPos = ""
    sequences = []

    def changeName(self, newName):
        print(self.name + " => " + newName)
        editor.delete(self.namePos, self.namePos.__add__("+ " + str(len(self.name)) + " chars"))
        editor.insert(self.namePos, newName)
        self.name = newName

    def updateSeq(self, newSeq):
        editor.delete(self.namePos.__add__(" lineend + 1 chars"),
                      self.namePos.__add__(" lineend + 1 chars + " + str(self.sequence.__len__()) + " chars"))
        editor.insert(self.namePos.__add__(" lineend + 1 chars"), newSeq)
        self.sequence = newSeq

    def get(self, name):
        for s in Sequence.sequences:
            if s.name == name:
                return s
        return "null"

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

    def initSequences(self):
        Sequence.sequences = []

        pos = editor.search(">", '1.0', stopindex=END, regexp=True)

        while pos != '':

            s = Sequence()
            s.namePos = pos.__add__("+ 1 chars")

            if pos != '':
                pos = pos.__add__("+ 1 chars")
                while not util.isCrap(pos, editor):
                    s.name += editor.get(pos)
                    pos = pos.__add__("+ 1 chars")

            Sequence.sequences.append(s)
            pos = editor.search(r">", pos, stopindex=END, regexp=True)
            if pos != '':
                s.endPos = pos
                s.sequence = editor.get(s.namePos.__add__(" lineend + 1 chars"), pos.__add__(" -1 chars"))
            else:
                s.endPos = END
                s.sequence = editor.get(s.namePos.__add__(" lineend + 1 chars"), END)



class Gene:
    genes = []
    name = ""
    color = ""
    pos = ""
    fromPos = 0
    toPos = 0
    sequence = Sequence()
    size = 0

    def initGenes(self):

        pos = editor.search("@", '1.0', END)
        Sequence.initSequences(Sequence)

        while (pos != ''):

            gene = Gene()
            pos = pos.__add__("+ 1 chars")
            gene.pos = pos
            gene.name = util.getVarName(Util, pos)
            pos = pos.__add__("+ " + str(gene.name.__len__()) + " chars")

            while Util.isCrap(pos, editor) &  (pos.__add__("+ 1 chars") != ''):
                pos = pos.__add__("+ 1 chars")

            gene.fromPos = util.getVarName(Util, pos)
            pos = pos.__add__("+ " + str(gene.fromPos.__len__()) + " chars")

            while Util.isCrap(pos, editor) & (pos.__add__("+ 1 chars") != ''):
                pos = pos.__add__("+ 1 chars")

            gene.toPos = util.getVarName(Util, pos)
            gene.size = int(gene.toPos)-int(gene.fromPos)
            pos = pos.__add__("+ " + str(gene.toPos.__len__()) + " chars")

            while Util.isCrap(pos, editor) &  (pos.__add__("+ 1 chars") != ''):
                pos = pos.__add__("+ 1 chars")

            gene.color = util.getVarName(Util, pos)
            pos = pos.__add__("+ " + str(gene.color.__len__()) + " chars")

            while Util.isCrap(pos, editor) & (pos.__add__("+ 1 chars") != ''):
                pos = pos.__add__("+ 1 chars")

            gene.sequence = Sequence.get(Sequence, util.getVarName(Util, pos))

            if (gene.sequence != 'null') :

                Gene.genes.append(gene)

            pos = editor.search("@", pos.__add__(" lineend + 1 chars"), END)




    def greyOut(self):
        editor.insert(self.pos, '#')

    def printToString(self):
        print(str(Gene.genes.__len__())+ " :")
        for g in Gene.genes :
            print(g.name + ", " + g.sequence.name + ", " + g.color + "(" + g.fromPos + "..." + g.toPos + ")")
class Util:
    contents = ""

    def updateColorToSelection(self, label, l2):

        tag = editor.tag_names(INSERT)

        if tag.__len__() > 0 :
            if "pink" in tag :
                label.config(text="• Sequence", fg=pink)
                l2.config(text="    Sequence can be a/c/t/g")
            if "_" in tag[0] :
                name = "• " + tag[0][1:]
                c = editor.tag_cget(tag[0], "background")
                label.config(text=name, fg=c)
                if (Enzyme.get(Enzyme, tag[0][1:]) != "null") :
                    l2.config(text="    "+Enzyme.get(Enzyme, tag[0][1:]).type+", site : "+Enzyme.get(Enzyme, tag[0][1:]).siteCut)
            if "lightgreen" in tag :
                label.config(text="• Plasmid", fg=lightgreen)
                l2.config(text="    Call something 'pName' to make it a plasmid")
            if "orangetxt" in tag :
                label.config(text="• Click anything for more info", fg=whitish)
                l2.config(text="")
            if "cyan" in tag:
                label.config(text="• Instruction", fg=whiteblue)
                l2.config(text="    Supports PCR/Ligate/Digest")
            if "blueish" in tag:
                label.config(text="• Feature", fg=whiteblue)
                l2.config(text="    Declare a feature with '@[name] [fromBP] [toBP] [color] [sequence]'")
            else:
                for g in Gene.genes:
                    if g.name in tag:
                        name = "• Feature: " + g.name
                        c = editor.tag_cget(tag[0], "foreground")
                        label.config(text=name, fg=c)
                        l2.config(text="    size: " + str(int(g.fromPos) - int(g.toPos)) + "bp")
                for e in enzymes:
                    if e.name in tag:
                        name = "• " + e.name
                        c = e.color
                        label.config(text=name, fg=c)
                        l2.config(text="    " + e.type + ", site : " + e.siteCut)

        else :
            label.config(text="• Click anything for more info", fg=whitish)
            l2.config(text="")

    def revCompliment(self, str):
        revStr = ""

        for i in str :
            if (i=='a') :
                revStr += 't'
            if (i=='t') :
                revStr += 'a'
            if (i=='c') :
                revStr += 'g'
            if (i=='g') :
                revStr += 'c'

        return revStr

    # superscript for reference ᵃ ᶜ ᵗ ᵍ
    def superscript(self, str):
        newStr = ""

        for i in str :
            if (i=='a') :
                newStr += 'ᵃ'
            if (i=='c') :
                newStr += 'ᶜ'
            if (i=='t') :
                newStr += 'ᵗ'
            if (i=='g') :
                newStr += 'ᵍ'

        return newStr

    def getVarName(self, pos):

        var = ""

        while not Util.isCrap(pos, editor):
            var += editor.get(pos)
            pos = pos.__add__("+ 1 chars")

        return var


    def getVarNameStr(self, pos, str, WITHSPACE):

        var = ""

        if WITHSPACE :
            if str.__len__() > pos :
                while (not Util.isCrapStr(self, pos, str) )| (str[pos] == " "):

                    if str[pos] == " " :
                        var += "-"
                    else :
                        var += str[pos]
                    pos += 1
        else :
            while (not Util.isCrapStr(self, pos, str)):
                var += str[pos]
                pos += 1
        return var

    def isPlasmid(pos, txt):
        if (txt.get(pos) == "p") & (txt.get(pos.__add__("+ 1 chars")).isupper()):
            return True

    def seqColor(pos, txt):
        if util.isPlasmid(pos, txt):
            return "lightgreen"
        else:
            return "pink"

    def isCrap(pos, txt):
        if (txt.get(pos) == " ") | (txt.get(pos) == "(") | (txt.get(pos) == ")") \
                | (txt.get(pos) == ",") | (txt.get(pos) == "/") | (txt.get(pos) == ",") | (txt.get(pos) == "+") | (
                txt.get(pos) == "\n"):
            return True

        else:
            return False
        
    def isCrapStr (self, pos, str):

        if (pos >= str.__len__()) :
            return True

        if (str[pos] == " ") | (str[pos] == "(") | (str[pos] == ")") \
                | (str[pos] == ",") | (str[pos] == "/") | (str[pos] == ",") | (str[pos] == "+")| (str[pos] == ".") | (
                str[pos] == "\n"):
            return True

        else:
            return False

    def geneStyle(self):

        for gene in Gene.genes:

            editor.tag_config(gene.name, foreground=gene.color)

            pos = editor.search(gene.sequence.sequence[int(gene.fromPos):int(gene.toPos)], '1.0', stopindex=END,
                             regexp=True)


            while (pos != ''):

                for g in Gene.genes :
                    if gene.size < g.size:
                        editor.tag_remove(g.name, pos,  pos.__add__("+ " + str(int(gene.toPos)-int(gene.fromPos)) +  " chars"))

                editor.tag_add(gene.name, pos,  pos.__add__("+ " + str(int(gene.toPos)-int(gene.fromPos)) +  " chars"))
                pos = pos.__add__("+ 1 chars")


                seq = gene.sequence.sequence[int(gene.fromPos):]
                seq = seq[:int(gene.toPos)]

                pos = editor.search(seq, pos.__add__("+ 1 chars"),
                                 stopindex=END, regexp=True)





    def textStyle(self, txt):

        txt.tag_config("grey", foreground=greyOut)
        txt.tag_config("pink", foreground=pink)
        txt.tag_config("green", foreground=code_green, underline=True)
        txt.tag_config("cyan", foreground=cyan)
        txt.tag_config("whiteblue", foreground=whiteblue)
        txt.tag_config("orangetxt", foreground=orangetxt)
        txt.tag_config("red", foreground=red)
        txt.tag_config("lightgreen", foreground=lightgreen)
        txt.tag_config("greygreen", foreground=greygreen)
        txt.tag_config("blueish", foreground=blueish)
        txt.tag_config("hRed", background=red)
        txt.tag_config("default", foreground=whitish, background=darkish)
        txt.tag_config("error", foreground=red, underline=True)
        txt.tag_config("sticky", font="Futura 12")
        txt.tag_config("stickyOnCompliment", font="Futura 12", underline=True)
        txt.tag_configure("sel", background=greyOut)

        for t in tags:
            txt.tag_remove(t, '1.0', END)

        for e in enzymes:
            txt.tag_remove(e.name, '1.0', END)
            txt.tag_remove("_" + e.name, '1.0', END)

        pos = txt.search(r"-|>|{|}|@", '1.0', stopindex=END, regexp=True)
        while pos != '':
            txt.tag_add("grey", pos)
            pos = txt.search(r"-|>|{|}|@", pos.__add__("+ 1 chars"), stopindex=END, regexp=True)

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

            if not util.isCrap(pos, txt):
                txt.tag_add(color, pos)

            pos = txt.search(r"Ligate|Digest|PCR", pos.__add__("+ 1 chars"), stopindex=END, regexp=True)



        pos = txt.search(r"and|on|with", '1.0', stopindex=END, regexp=True)
        while pos != '':

            while (txt.get(pos) != "") & (txt.get(pos) != " ") & (txt.get(pos) != "\n"):
                txt.tag_add("whiteblue", pos)
                pos = pos.__add__("+ 1 chars")

            pos = txt.search(r"and|on|with|product|is", pos.__add__("+ 1 chars"), stopindex=END, regexp=True)


        # Highlight specific genes
        pos = txt.search("@", '1.0', stopindex=END)

        while pos != '':
            pos2 = pos.__add__("lineend")

            if pos2 == '':
                pos2 = END

            color = "blueish"
            txt.tag_add(color, pos.__add__("+ 1 chars"), pos2)

            pos = txt.search("@", pos2, stopindex=END)

        # Numbers, bp, etc (orange)

        pos = txt.search(" L,", '1.0', stopindex=END)
        while pos != '':
            txt.tag_add("orangetxt", pos.__add__("+ 1 chars"))
            pos = txt.search(" L,", pos.__add__("+ 1 chars"), stopindex=END)

        pos = txt.search(r"\d", '1.0', stopindex=END, regexp=True)
        while (pos != ''):
            while (txt.get(pos.__add__("- 1 chars")) == "+") | (txt.get(pos.__add__("- 1 chars")) == " ") | (
                    ("orangetxt" in txt.tag_names(pos.__add__(" - 1 chars"))) & (txt.get(pos) in "1234567890")):
                txt.tag_add("orangetxt", pos)
                txt.tag_remove("blueish", pos)
                pos = pos.__add__("+ 1 chars")

            pos = txt.search(r"\d", pos.__add__("+ 1 chars"), stopindex=END, regexp=True)

        pos = txt.search("bp", '1.0', stopindex=END)
        while pos != '':

            pos2 = pos
            pos = pos.__add__("+ 1 chars")

            txt.tag_add("orangetxt", pos)
            pos = pos.__add__("- 1 chars")
            txt.tag_add("orangetxt", pos)
            pos = pos.__add__("- 1 chars")

            while not (util.isCrap(pos, txt)):
                if txt.get(pos) in "1234567890":
                    txt.tag_add("orangetxt", pos)
                    pos = pos.__add__("- 1 chars")
                else:
                    break

            pos = txt.search(r"bp", pos2.__add__("+ 1 chars"), stopindex=END, regexp=True)

        pos = txt.search(">", '1.0', stopindex=END)
        while pos != '':

            pos = pos.__add__("+ 1 chars")

            color = util.seqColor(pos, txt)

            while (txt.get(pos.__add__("+ 1 chars")) != txt.get(pos.__add__(" lineend"))):

                if txt.get(pos) == " ":
                    color = "greygreen"
                    if not (txt.get(pos.__add__("+ 1 chars")) != txt.get(pos.__add__(" lineend"))):
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

            if not util.isCrap(pos, txt):
                txt.tag_add(color, pos)

            pos = txt.search(">", pos.__add__("+ 1 chars"), stopindex=END)

        for enzyme in enzymes:

            txt.tag_config(enzyme.name, foreground=enzyme.color, underline=True)
            txt.tag_config("_" + enzyme.name, foreground="black", background=enzyme.color)

            pos = txt.search(enzyme.name, '1.0', stopindex=END, regexp=True)

            while pos != '':
                while not (util.isCrap(pos, txt)):
                    txt.tag_add(enzyme.name, pos)
                    pos = pos.__add__("+ 1 chars")

                pos = txt.search(enzyme.name, pos.__add__("+ 1 chars"), stopindex=END, regexp=True)

            regex = r"(?i)(" + enzyme.site + "|" + enzyme.siteRC + ").*"

            pos = txt.search(regex, '1.0', stopindex=END, regexp=True)
            while pos != '':

                for x in range(6):
                    txt.tag_add("_"+ enzyme.name, pos)
                    pos = pos.__add__("+ 1 chars")

                pos = txt.search(regex, pos.__add__("+ 1 chars"), stopindex=END, regexp=True)


        for color in colors:

            txt.tag_config(color, foreground=color, underline=True)
            #txt.tag_config("_" + enzyme.name, foreground="black", background=enzyme.color)

            pos = txt.search(color, '1.0', stopindex=END, regexp=True)

            while pos != '':
                while not (util.isCrap(pos, txt)):
                    txt.tag_add(color, pos)
                    txt.tag_remove("blueish", pos)
                    pos = pos.__add__("+ 1 chars")

                pos = txt.search(color, pos.__add__("+ 1 chars"), stopindex=END, regexp=True)


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


def insertFASTA(name):
    fileStr = open(name).read()
    namePos = fileStr.find("LOCUS") + 6

    while Util.isCrapStr(Util, namePos, fileStr):
        namePos += 1

    seqName = Util.getVarNameStr(Util, namePos, fileStr, False)


    sequence = ""
    for l in fileStr[fileStr.find("ORIGIN")+7:] :

        if l in "atcgATCG":
            sequence += l


    namePos = fileStr.find("FEATURES")
    spot = 0
    spotLabel = 0
    i=0
    while namePos < fileStr.__len__() :


        while Util.isCrapStr(Util, namePos, fileStr) & (namePos < fileStr.__len__()):
            namePos += 1

        gene =  Util.getVarNameStr(Util, namePos, fileStr, False)


        print(fileStr[namePos-6])

        if (fileStr[namePos-6] == '\n') :
            if (fileStr[namePos] not in '1234567890'):


                color = ""
                if fileStr[spot:].find("fwdcolor=") > 0 :
                    color = Util.getVarNameStr(Util, fileStr[spot:].find("fwdcolor=")+9, fileStr[spot:], False)
                    spot += fileStr[spot:].find("fwdcolor=") + 9
                    colors.append(color)
                else :
                    color = colors[i]

                label = ""
                if fileStr[spotLabel:].find("label=") > 0:
                    label = Util.getVarNameStr(Util, fileStr[spotLabel:].find("label=") + 6, fileStr[spotLabel:], True)
                    spotLabel+= fileStr[spotLabel:].find("label=") + 6
                else:
                    label = gene

                namePos += gene.__len__()

                while Util.isCrapStr(Util, namePos, fileStr) & (namePos < fileStr.__len__()):
                    namePos += 1

                fromPos = Util.getVarNameStr(Util, namePos, fileStr, False)
                namePos += fromPos.__len__()
                while Util.isCrapStr(Util, namePos, fileStr) & (namePos < fileStr.__len__()):
                    namePos += 1

                toPos = Util.getVarNameStr(Util, namePos, fileStr, False)

                space1 = ""
                for l in range(26-label.__len__()) :
                    space1 += " "

                space2 = ""
                for l in range(10-fromPos.__len__()) :
                    space1 += " "

                space3 = ""
                for l in range(6-toPos.__len__()) :
                    space1 += " "

                editor.insert(END, "\n@" + label + space1  +  fromPos  + space3 + space2  +"    " + toPos + space3 + "    " + color  +"    " + seqName + "         #"+gene)
        namePos += gene.__len__()
        i = (i + 1) % colors.__len__()



    editor.insert(END, "\n>" + seqName + "\n")
    editor.insert(END, sequence)



class Enzyme:
    name = ""
    site = ""  # 5'-3'
    siteRC = ""  # 3'-5'
    color = ""
    cutBefore = 0
    cutOnCompl = 0
    stickyEnd = ""
    reverseSticky = ""
    type = ""
    siteCut = ""

    def get(self, str):
        for e in enzymes :
            if str.__eq__(e.name) :
                return e
        return "null"

    def digest(self, seq):

        sequence = seq.sequence

        newSeq = sequence


        spot = newSeq.find(self.site)

        while spot != -1:
            newSeq = newSeq[
                     :spot + self.cutBefore] + self.reverseSticky + "\n>" + seq.name + "\n" + self.stickyEnd + newSeq[
                                                                                                               spot + self.cutOnCompl:]
            spot = newSeq.find(self.site)


        #RC Site

        spot = newSeq.find(self.siteRC)

        while spot != -1:
            newSeq = newSeq[
                     :spot + self.site.__len__() - self.cutOnCompl] + self.stickyEnd + "\n>" + seq.name + "\n" + self.reverseSticky + newSeq[
                                                                                                               spot + self.site.__len__() - self.cutBefore:]
            spot = newSeq.find(self.siteRC)
        return newSeq

    def addNew(self, n, s, c, before, compl, t):
        e = Enzyme()
        e.site = s
        e.name = n
        e.siteRC = Util.revCompliment(Util, s)
        e.color = c
        e.cutBefore = before
        e.cutOnCompl = compl
        e.stickyEnd = Util.superscript(Util, s[before:compl])
        e.reverseSticky = "{" + Util.superscript(Util, e.siteRC[e.site.__len__()-compl:e.site.__len__()-before]) + "}"
        e.type = t
        enzymes.append(e)
        e.siteCut = e.site[:before]+"/"+e.site[before:]

    def toHex(self, r, g, b):
        return '#%02x%02x%02x' % (r, g, b)

    def __str__(self):
        return self.name

    def arrayStr(self, list):
        str = ""
        for e in list:
            str += e.__str__() + ", "
        return str

# Type II Restriction Endonucleases

#5' 4bp Overhang
Enzyme.addNew(Enzyme, "EcoRI", "gaattc", Enzyme.toHex(Enzyme, 200, 240, 69), 1, 5, "5' 4bp overhang")
Enzyme.addNew(Enzyme, "SpeI", "actagt", Enzyme.toHex(Enzyme, 120, 120, 244), 1, 5, "5' 4bp overhang")
Enzyme.addNew(Enzyme, "BamHI", "ggatcc", Enzyme.toHex(Enzyme, 220, 120, 244), 1, 5, "5' 4bp overhang")
Enzyme.addNew(Enzyme, "XbaI", "tctaga", Enzyme.toHex(Enzyme, 100, 240, 69), 1, 5, "5' 4bp overhang")

#3' 4bp Overhang
Enzyme.addNew(Enzyme, "PstI", "ctgcag", Enzyme.toHex(Enzyme, 244, 89, 66), 5, 1, "3' 4bp overhang")

#5' 2bp Overhang
Enzyme.addNew(Enzyme, "NdeI", "catatg", Enzyme.toHex(Enzyme, 244, 89, 126), 2, 4, "5' 2bp overhang")

#3' 2bp Overhang
Enzyme.addNew(Enzyme,  "PacI", "ttaattaa", Enzyme.toHex(Enzyme, 244, 189, 66), 5, 3, "3' 2bp overhang")

#Blunt cutters
Enzyme.addNew(Enzyme,  "EcoRV", "gatatc", Enzyme.toHex(Enzyme, 244, 89, 0), 3, 3, "Blunt cutter")
Enzyme.addNew(Enzyme,  "PvuII", "cagctg", Enzyme.toHex(Enzyme, 44, 209, 66), 3, 3, "Blunt cutter")

#Degenerate cutters
#Enzyme.addNew(Enzyme,  "XcmI", "ccaNNNNN/NNNNtgg", Enzyme.toHex(Enzyme, 44, 89, 166), 5, 3, "Degenerate cutter")
#Enzyme.addNew(Enzyme,  "AlwNI", "CAGNNN/CTG", Enzyme.toHex(Enzyme, 24, 209, 66), 5, 3)
#Enzyme.addNew(Enzyme,  "SfiI", "GGCCNNNN/NGGCC", Enzyme.toHex(Enzyme, 214, 89, 66), 5, 3)
#Enzyme.addNew(Enzyme,  "FalI", "AAGNNNNNCTT", Enzyme.toHex(Enzyme, 66, 89, 244), 5, 3)


def running():
    i = 0

    while True:
        time.sleep(0.01)
        i += 1

        if (i % 100 == 0):
            util.textStyle(util, editor)


        util.updateColorToSelection(util, whatIs, whatIs2)
        root.update_idletasks()
        root.update()


def show_genes() :
    Gene.initGenes(Gene)
    for j in Gene.genes:
        j.printToString()
    Util.geneStyle(Util)
    editor.tag_remove('', '1.0', END)

instructions = []


class Instruction:
    type = ""
    inputs = []
    inputOn = Sequence()
    enzymes = []
    output = Sequence()
    pos = ""
    bp = 0

    def initInstructions(self):
        pos = '1.0'

        while (editor.get(pos) != '-'):

            if editor.get(pos) == 'L':
                instruct = Instruction()
                instruct.type = "ligation"
                instructions.append(instruct)
            if editor.get(pos) == 'P':
                instruct = Instruction()
                instruct.type = "PCR"
                instructions.append(instruct)
            if editor.get(pos) == 'D':
                instruct = Instruction()
                instruct.pos = pos
                instruct.type = "digestion"
                instruct.inputOn = util.getVarName(Util, pos.__add__(" + 7 chars"))

                for e in enzymes:
                    ePos = editor.search(e.name, pos, stopindex=pos.__add__(" lineend"))
                    if ePos != '':
                        instruct.enzymes.append(e)

                prodPos = pos
                for i in range(3):
                    if (prodPos != ''):
                        prodPos = editor.search(',', prodPos.__add__("+ 1 chars"), stopindex=pos.__add__(" lineend"))

                if (prodPos != ''):
                    instruct.output = util.getVarName(Util, prodPos.__add__(" + 2 chars"))
                    instructions.append(instruct)

            pos = pos.__add__(" lineend + 1 chars")

    def greyOut(self):
        editor.insert(self.pos, '#')

    def printToString(self):
        if (self.type == "digestion"):
            print(self.type + ": " + self.inputOn + " using " + Enzyme.arrayStr(Enzyme,
                                                                                enzymes) + "to produce " + self.output)
        else:
            print(self.type + ": " + str(self.inputs.__sizeof__()) + " inputs, ", str(self.inputs))


def PCR():
    if Util.contents == "" :
        Util.contents = editor.get('1.0', END)
    Sequence.initSequences(Sequence)
    Sequence.changeName(Sequence.sequences[2], "pcrpdt")

    for i in instructions[0].inputs:
        Sequence.greyOut(Sequence.get(i.name))

    Sequence.greyOut(Sequence.sequences[0])
    editor.insert(instructions[0].pos, '#')


def Ligate():
    if Util.contents == "" :
        Util.contents = editor.get('1.0', END)
    Sequence.initSequences(Sequence)
    Sequence.changeName(Sequence.sequences[2], "pcrpdt")

    for i in instructions[0].inputs:
        Sequence.greyOut(Sequence.get(i.name))

    Sequence.greyOut(Sequence.sequences[0])
    editor.insert(instructions[0].pos, '#')


def Digest():
    if Util.contents == "" :
        Util.contents = editor.get('1.0', END)
    Instruction.initInstructions(Instruction)
    instruct = instructions[1]
    Instruction.greyOut(instruct)

    Sequence.initSequences(Sequence)

    seq = Sequence.get(Sequence, instruct.inputOn)
    name = seq.name

    for enz in instruct.enzymes:
        seq.updateSeq(enz.digest(seq))
        print("digesting " + seq.name + " with " + enz.name + ", site: " + enz.site + "/" + enz.siteRC)

    Sequence.initSequences(Sequence)

    for s in Sequence.sequences:
        if (s.name == name):
            s.changeName("dig-" + name + "-" + str(s.sequence.__len__()))
    time.sleep(0.2)
    Util.geneStyle(Util)
    # seq.changeName(instruct.output)

    # Sequence.selectSeqFromBp(instruct.bp)


def save_file():

    filename = tkinter.filedialog.asksaveasfilename(initialfile='construction.txt', defaultextension='.txt')

    if filename :
        f = open(filename, 'w')
        f.write(editor.get('1.0', 'end'))
        f.close()


def import_fasta():
    filename = tkinter.filedialog.askopenfilename(defaultextension='.seq')
    insertFASTA(filename)

def open_file():
    filename = tkinter.filedialog.askopenfilename(defaultextension='.txt')
    fileStr = open(filename).read()
    editor.delete('1.0', END)
    editor.insert(INSERT, fileStr)


def new_file():
    fileStr = open('Basic_Part_Construction.txt').read()
    editor.delete('1.0', END)
    editor.insert(INSERT, fileStr)

def stop_running():
    editor.delete('1.0', END)
    editor.insert('1.0', Util.contents)
    Util.contents = ""

# display everything

root.title("BioType")

top = root.winfo_toplevel()
menuBar = Menu(top)
top['menu'] = menuBar
subMenu = Menu(menuBar)
enzymeMenu = Menu(menuBar)
runMenu = Menu(menuBar)
fileMenu = Menu(menuBar)
editMenu = Menu(menuBar)

menuBar.add_cascade(label='File', menu=fileMenu)
fileMenu.add_command(label='New', command=new_file)
fileMenu.add_command(label='Open', command=open_file)
fileMenu.add_command(label='Save As', command=save_file)
fileMenu.add_command(label='Render Genes', command=show_genes)
fileMenu.add_command(label='Import FASTA file', command=import_fasta)

menuBar.add_cascade(label='Edit', menu=editMenu)
editMenu.add_command(label='Undo', command=Digest)

menuBar.add_cascade(label='Run', menu=runMenu)
runMenu.add_command(label='Run PCR', command=PCR)
runMenu.add_command(label='Run Digest', command=Digest)
runMenu.add_command(label='Stop', command=stop_running)

menuBar.add_cascade(label='Enzymes', menu=enzymeMenu)
enzymeMenu.add_command(label='Add')
enzymeMenu.add_command(label='List')

label = Label(root, text='▶ Run PCR', bg=darkish, fg=whitish, font="Futura 20")

label.grid(row=3, column=1, sticky='e')

whatIs= Label(root, text='• Click on any restriction site', bg=darkish, fg=whitish, font="Futura 20")
whatIs.grid(row=3, column=1, sticky='w')
whatIs2= Label(root, text='', bg=darkish, fg=whitish, font="Futura 16")
whatIs2.grid(row=4, column=1, sticky='w')

for i in instructions:
    print(i.printToString())


running()