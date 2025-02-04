#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import print_function
##############################################
#
# Name: U11.3_GUI_Farben.py
#
# Author: Peter Christen
#
# Version: 1.0
#
# Date: 05.11.2015
#
# Purpose: Zeigt ein GUI mit verschiedenen Farben an
#
##############################################

import Tkinter
import random
import time

# Funktion zu Button Ende


def ende():
    # Beenden
    main.destroy()


def rechne1():
    # Grösser als
    r = vergleiche(1)


def rechne2():
    # Gleich
    r = vergleiche(2)


def rechne3():
    # Kleiner als
    r = vergleiche(3)


def vorgaben():
    # Zufallszahlen setzen
    random.seed()
    fl1["text"] = random.randint(1, 1000)
    fl3["text"] = random.randint(1, 1000)


def vergleiche(v):
    # Vergleiche auswerten
    if fl1["text"] > fl3["text"]:
        r = 1
    elif fl1["text"] == fl3["text"]:
        r = 2
    else:
        r = 3
    if r == v:
        t["text"] = "Richtig"
        t["bg"] = "green"
        vorgaben()
    else:
        t["text"] = "Falsch"
        t["bg"] = "red"


random.seed()
za = random.randint(1, 1000)
zb = random.randint(1, 1000)
if za > zb:
    r = 1
elif za == zb:
    r = 2
else:
    r = 3

# Hauptfenster
main = Tkinter.Tk()
main.wm_title("Vergleichen")

# 0 Frame
fr0 = Tkinter.Frame(main)
fr0.pack(expand=1)
b = Tkinter.Button(fr0, text="Ende", command=ende)
b["width"] = 25
t = Tkinter.Label(fr0, text="?", relief="raised")
t["width"] = 27
b.pack()
t.pack()

# Frame 1
fr1 = Tkinter.Frame(main)
fr1.pack(side="left")
#
fl1 = Tkinter.Label(fr1, text=za, relief="ridge")
fl1["borderwidth"] = 5
fl1["width"] = 11
fl1["height"] = 4
fl1.pack()

# Frame2
fr2 = Tkinter.Frame(main)
fr2.pack(side="left")
#
b21 = Tkinter.Button(fr2, text=">", command=rechne1)
b22 = Tkinter.Button(fr2, text="=", command=rechne2)
b23 = Tkinter.Button(fr2, text="<", command=rechne3)
b21.pack()
b22.pack()
b23.pack()

# Frame3
fr3 = Tkinter.Frame(main)
fr3.pack(side="right")
#
fl3 = Tkinter.Label(fr3, text=zb, relief="ridge")
fl3["borderwidth"] = 5
fl3["width"] = 11
fl3["height"] = 4
fl3.pack()

main.mainloop()
