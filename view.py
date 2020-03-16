#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 5.0.2
#  in conjunction with Tcl version 8.6
#    Mar 07, 2020 09:09:08 AM IST  platform: Windows NT

import sys
from tkinter import ttk

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

import view_support
from tkinter import END
from backend import DataBase
import graph_backend as graph
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import pandas as pd


def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    top = Toplevel1 (root)
    view_support.init(root, top)
    root.mainloop()

w = None
def create_Toplevel1(rt, *args, **kwargs):
    '''Starting point when module is imported by another module.
       Correct form of call: 'create_Toplevel1(root, *args, **kwargs)' .'''
    global w, w_win, root
    #rt = root
    root = rt
    w = tk.Toplevel (root)

    goatData = args[0]

    top = Toplevel1 (w, goatData)
    view_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Toplevel1():
    global w
    w.destroy()
    w = None

class Toplevel1:
    def __init__(self, top=None, goatData=[]):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'
        font10 = "-family {Segoe UI} -size 13"
        font12 = "-family {Segoe UI} -size 16 -weight bold"
        font13 = "-family {Segoe UI Semibold} -size 13 -weight bold"
        font9 = "-family {Segoe UI} -size 20 -weight bold"

        top.geometry("1300x760+20+20")
        top.minsize(800, 500)
        top.maxsize(1500, 750)
        top.resizable(0, 0)
        top.title("New Toplevel")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")
        
        self.goatData = goatData
        self.db = DataBase()

        self.Label1 = tk.Label(top)
        self.Label1.place(relx=0.416, rely=0.0, height=52, width=173)
        self.Label1.configure(activebackground="#f9f9f9")
        self.Label1.configure(activeforeground="black")
        self.Label1.configure(background="#d9d9d9")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font=font9)
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(highlightbackground="#d9d9d9")
        self.Label1.configure(highlightcolor="black")
        self.Label1.configure(text='''About Goat''')

        self.Label2 = tk.Label(top)
        self.Label2.place(relx=0.051, rely=0.017, height=52, width=112)
        self.Label2.configure(activebackground="#f9f9f9")
        self.Label2.configure(activeforeground="black")
        self.Label2.configure(background="#d9d9d9")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(font=("font10",10))
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(highlightbackground="#d9d9d9")
        self.Label2.configure(highlightcolor="black")
        self.Label2.configure(text='''Goat ID''')

        self.Label2_1 = tk.Label(top)
        self.Label2_1.place(relx=0.051, rely=0.072, height=52, width=112)
        self.Label2_1.configure(activebackground="#f9f9f9")
        self.Label2_1.configure(activeforeground="black")
        self.Label2_1.configure(background="#d9d9d9")
        self.Label2_1.configure(disabledforeground="#a3a3a3")
        self.Label2_1.configure(font=("font10",10))
        self.Label2_1.configure(foreground="#000000")
        self.Label2_1.configure(highlightbackground="#d9d9d9")
        self.Label2_1.configure(highlightcolor="black")
        self.Label2_1.configure(text='''Breed''')

        self.Label2_2 = tk.Label(top)
        self.Label2_2.place(relx=0.051, rely=0.134, height=40, width=112)
        self.Label2_2.configure(activebackground="#f9f9f9")
        self.Label2_2.configure(activeforeground="black")
        self.Label2_2.configure(background="#d9d9d9")
        self.Label2_2.configure(disabledforeground="#a3a3a3")
        self.Label2_2.configure(font=("font10",10))
        self.Label2_2.configure(foreground="#000000")
        self.Label2_2.configure(highlightbackground="#d9d9d9")
        self.Label2_2.configure(highlightcolor="black")
        self.Label2_2.configure(text='''DOB''')

        self.Label2_3 = tk.Label(top)
        self.Label2_3.place(relx=0.051, rely=0.177, height=53, width=112)
        self.Label2_3.configure(activebackground="#f9f9f9")
        self.Label2_3.configure(activeforeground="black")
        self.Label2_3.configure(background="#d9d9d9")
        self.Label2_3.configure(disabledforeground="#a3a3a3")
        self.Label2_3.configure(font=("font10",10))
        self.Label2_3.configure(foreground="#000000")
        self.Label2_3.configure(highlightbackground="#d9d9d9")
        self.Label2_3.configure(highlightcolor="black")
        self.Label2_3.configure(text='''Gender''')

        self.Label2_4 = tk.Label(top)
        self.Label2_4.place(relx=0.071, rely=0.300, height=52, width=266)
        self.Label2_4.configure(activebackground="#f9f9f9")
        self.Label2_4.configure(activeforeground="black")
        self.Label2_4.configure(background="#d9d9d9")
        self.Label2_4.configure(disabledforeground="#a3a3a3")
        self.Label2_4.configure(font=font12)
        self.Label2_4.configure(foreground="#000000")
        self.Label2_4.configure(highlightbackground="#d9d9d9")
        self.Label2_4.configure(highlightcolor="black")
        self.Label2_4.configure(text='''Last Vaccinated Date''')

        self.Text1 = tk.Text(top)
        self.Text1.place(relx=0.152, rely=0.025, relheight=0.036, relwidth=0.139)
        self.Text1.configure(background="white")
        self.Text1.configure(font="TkTextFont")
        self.Text1.configure(foreground="black")
        self.Text1.configure(highlightbackground="#d9d9d9")
        self.Text1.configure(highlightcolor="black")
        self.Text1.configure(insertbackground="black")
        self.Text1.configure(selectbackground="#c4c4c4")
        self.Text1.configure(selectforeground="black")
        self.Text1.configure(wrap="word")

        self.Text1_12 = tk.Text(top)
        self.Text1_12.place(relx=0.152, rely=0.080, relheight=0.036
                , relwidth=0.139)
        self.Text1_12.configure(background="white")
        self.Text1_12.configure(font="TkTextFont")
        self.Text1_12.configure(foreground="black")
        self.Text1_12.configure(highlightbackground="#d9d9d9")
        self.Text1_12.configure(highlightcolor="black")
        self.Text1_12.configure(insertbackground="black")
        self.Text1_12.configure(selectbackground="#c4c4c4")
        self.Text1_12.configure(selectforeground="black")
        self.Text1_12.configure(wrap="word")

        self.Text1_12.insert(END, self.goatData[4])

        self.Text1_13 = tk.Text(top)
        self.Text1_13.place(relx=0.152, rely=0.137, relheight=0.035
                , relwidth=0.139)
        self.Text1_13.configure(background="white")
        self.Text1_13.configure(font="TkTextFont")
        self.Text1_13.configure(foreground="black")
        self.Text1_13.configure(highlightbackground="#d9d9d9")
        self.Text1_13.configure(highlightcolor="black")
        self.Text1_13.configure(insertbackground="black")
        self.Text1_13.configure(selectbackground="#c4c4c4")
        self.Text1_13.configure(selectforeground="black")
        self.Text1_13.configure(wrap="word")

        self.Text1_13.insert(END, self.goatData[2])

        self.Text1_14 = tk.Text(top)
        self.Text1_14.place(relx=0.152, rely=0.190, relheight=0.035
                , relwidth=0.139)
        self.Text1_14.configure(background="white")
        self.Text1_14.configure(font="TkTextFont")
        self.Text1_14.configure(foreground="black")
        self.Text1_14.configure(highlightbackground="#d9d9d9")
        self.Text1_14.configure(highlightcolor="black")
        self.Text1_14.configure(insertbackground="black")
        self.Text1_14.configure(selectbackground="#c4c4c4")
        self.Text1_14.configure(selectforeground="black")
        self.Text1_14.configure(wrap="word")

        self.Text1_14.insert(END, self.goatData[3])

        self.Text1_15 = tk.Text(top)
        self.Text1_15.place(relx=0.159, rely=0.405, relheight=0.036
                , relwidth=0.139)
        self.Text1_15.configure(background="white")
        self.Text1_15.configure(font="TkTextFont")
        self.Text1_15.configure(foreground="black")
        self.Text1_15.configure(highlightbackground="#d9d9d9")
        self.Text1_15.configure(highlightcolor="black")
        self.Text1_15.configure(insertbackground="black")
        self.Text1_15.configure(selectbackground="#c4c4c4")
        self.Text1_15.configure(selectforeground="black")
        self.Text1_15.configure(wrap="word")

        self.Text1_15.insert(END, self.goatData[11])

        self.Text1_16 = tk.Text(top)
        self.Text1_16.place(relx=0.159, rely=0.475, relheight=0.036
                , relwidth=0.139)
        self.Text1_16.configure(background="white")
        self.Text1_16.configure(font="TkTextFont")
        self.Text1_16.configure(foreground="black")
        self.Text1_16.configure(highlightbackground="#d9d9d9")
        self.Text1_16.configure(highlightcolor="black")
        self.Text1_16.configure(insertbackground="black")
        self.Text1_16.configure(selectbackground="#c4c4c4")
        self.Text1_16.configure(selectforeground="black")
        self.Text1_16.configure(wrap="word")

        self.Text1_16.insert(END, self.goatData[12])

        self.Text1_17 = tk.Text(top)
        self.Text1_17.place(relx=0.159, rely=0.540, relheight=0.036
                , relwidth=0.139)
        self.Text1_17.configure(background="white")
        self.Text1_17.configure(font="TkTextFont")
        self.Text1_17.configure(foreground="black")
        self.Text1_17.configure(highlightbackground="#d9d9d9")
        self.Text1_17.configure(highlightcolor="black")
        self.Text1_17.configure(insertbackground="black")
        self.Text1_17.configure(selectbackground="#c4c4c4")
        self.Text1_17.configure(selectforeground="black")
        self.Text1_17.configure(wrap="word")

        self.Text1_17.insert(END, self.goatData[13])

        self.Text1_18 = tk.Text(top)
        self.Text1_18.place(relx=0.159, rely=0.600, relheight=0.036
                , relwidth=0.139)
        self.Text1_18.configure(background="white")
        self.Text1_18.configure(font="TkTextFont")
        self.Text1_18.configure(foreground="black")
        self.Text1_18.configure(highlightbackground="#d9d9d9")
        self.Text1_18.configure(highlightcolor="black")
        self.Text1_18.configure(insertbackground="black")
        self.Text1_18.configure(selectbackground="#c4c4c4")
        self.Text1_18.configure(selectforeground="black")
        self.Text1_18.configure(wrap="word")

        self.Text1_18.insert(END, self.goatData[14])

        self.Text1_19 = tk.Text(top)
        self.Text1_19.place(relx=0.159, rely=0.665, relheight=0.036
                , relwidth=0.139)
        self.Text1_19.configure(background="white")
        self.Text1_19.configure(font="TkTextFont")
        self.Text1_19.configure(foreground="black")
        self.Text1_19.configure(highlightbackground="#d9d9d9")
        self.Text1_19.configure(highlightcolor="black")
        self.Text1_19.configure(insertbackground="black")
        self.Text1_19.configure(selectbackground="#c4c4c4")
        self.Text1_19.configure(selectforeground="black")
        self.Text1_19.configure(wrap="word")

        self.Text1_19.insert(END, self.goatData[15])

        self.Text1_20 = tk.Text(top)
        self.Text1_20.place(relx=0.159, rely=0.730, relheight=0.036
                , relwidth=0.139)
        self.Text1_20.configure(background="white")
        self.Text1_20.configure(font="TkTextFont")
        self.Text1_20.configure(foreground="black")
        self.Text1_20.configure(highlightbackground="#d9d9d9")
        self.Text1_20.configure(highlightcolor="black")
        self.Text1_20.configure(insertbackground="black")
        self.Text1_20.configure(selectbackground="#c4c4c4")
        self.Text1_20.configure(selectforeground="black")
        self.Text1_20.configure(wrap="word")
        self.Text1_20.insert(END, self.goatData[16])

        self.Text205 = tk.Text(top)
        self.Text205.place(relx=0.159, rely=0.800, relheight=0.036
                , relwidth=0.139)
        self.Text205.configure(background="white")
        self.Text205.configure(font="TkTextFont")
        self.Text205.configure(foreground="black")
        self.Text205.configure(highlightbackground="#d9d9d9")
        self.Text205.configure(highlightcolor="black")
        self.Text205.configure(insertbackground="black")
        self.Text205.configure(selectbackground="#c4c4c4")
        self.Text205.configure(selectforeground="black")
        self.Text205.configure(wrap="word")
        self.Text205.insert(END, self.goatData[17])

        self.Text305 = tk.Text(top)
        self.Text305.place(relx=0.159, rely=0.865, relheight=0.036
                , relwidth=0.139)
        self.Text305.configure(background="white")
        self.Text305.configure(font="TkTextFont")
        self.Text305.configure(foreground="black")
        self.Text305.configure(highlightbackground="#d9d9d9")
        self.Text305.configure(highlightcolor="black")
        self.Text305.configure(insertbackground="black")
        self.Text305.configure(selectbackground="#c4c4c4")
        self.Text305.configure(selectforeground="black")
        self.Text305.configure(wrap="word")
        self.Text305.insert(END, self.goatData[18])

        self.Canvas1 = tk.Text(top)
        self.Canvas1.place(relx=0.159, rely=0.927, relheight=0.049
                , relwidth=0.138)
        self.Canvas1.configure(background="white")
        self.Canvas1.configure(font="TkTextFont")
        self.Canvas1.configure(foreground="black")
        self.Canvas1.configure(highlightbackground="#d9d9d9")
        self.Canvas1.configure(highlightcolor="black")
        self.Canvas1.configure(insertbackground="black")
        self.Canvas1.configure(selectbackground="#c4c4c4")
        self.Canvas1.configure(selectforeground="black")
        self.Canvas1.configure(wrap="word")

        self.Frame1 = tk.Frame(top)
        self.Frame1.place(relx=0.325, rely=0.512, relheight=0.454, relwidth=0.248)
        self.Frame1.configure(relief='groove')
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief="groove")
        self.Frame1.configure(background="#d9d9d9")
        self.Frame1.configure(highlightbackground="#d9d9d9")
        self.Frame1.configure(highlightcolor="black")

        self.Frame2 = tk.Frame(top)
        self.Frame2.place(relx=0.599, rely=0.075, relheight=0.92, relwidth=0.39)
        self.Frame2.configure(relief='groove')
        self.Frame2.configure(borderwidth="2")
        self.Frame2.configure(relief="groove")
        self.Frame2.configure(background="#d9d9d9")
        self.Frame2.configure(highlightbackground="#d9d9d9")
        self.Frame2.configure(highlightcolor="black")

        self.Label2_00 = tk.Label(self.Frame2)
        self.Label2_00.place(relx=0.1, rely=0.066, height=52, width=141)
        self.Label2_00.configure(activebackground="#f9f9f9")
        self.Label2_00.configure(activeforeground="black")
        self.Label2_00.configure(background="#d9d9d9")
        self.Label2_00.configure(disabledforeground="#a3a3a3")
        self.Label2_00.configure(font=font10)
        self.Label2_00.configure(foreground="#000000")
        self.Label2_00.configure(highlightbackground="#d9d9d9")
        self.Label2_00.configure(highlightcolor="black")
        self.Label2_00.configure(text='''Pregnant''')

        self.Canvas2 = tk.Text(self.Frame2)
        self.Canvas2.place(relx=0.469, rely=0.066, relheight=0.055, relwidth=0.346)
        self.Canvas2.configure(background="white")
        self.Canvas2.configure(font="TkTextFont")
        self.Canvas2.configure(foreground="black")
        self.Canvas2.configure(highlightbackground="#d9d9d9")
        self.Canvas2.configure(highlightcolor="black")
        self.Canvas2.configure(insertbackground="black")
        self.Canvas2.configure(selectbackground="#c4c4c4")
        self.Canvas2.configure(selectforeground="black")
        self.Canvas2.configure(wrap="word")

        self.Label2_7 = tk.Label(self.Frame2)
        self.Label2_7.place(relx=0.25, rely=0.15, height=51, width=174)
        self.Label2_7.configure(activebackground="#f9f9f9")
        self.Label2_7.configure(activeforeground="black")
        self.Label2_7.configure(background="#d9d9d9")
        self.Label2_7.configure(disabledforeground="#a3a3a3")
        self.Label2_7.configure(font=font13)
        self.Label2_7.configure(foreground="#000000")
        self.Label2_7.configure(highlightbackground="#d9d9d9")
        self.Label2_7.configure(highlightcolor="black")
        self.Label2_7.configure(text='''Kid Details''')

        self.Label2_8 = tk.Label(self.Frame2)
        self.Label2_8.place(relx=0.1, rely=0.24, height=50, width=140)
        self.Label2_8.configure(activebackground="#f9f9f9")
        self.Label2_8.configure(activeforeground="black")
        self.Label2_8.configure(background="#d9d9d9")
        self.Label2_8.configure(disabledforeground="#a3a3a3")
        self.Label2_8.configure(font=font10)
        self.Label2_8.configure(foreground="#000000")
        self.Label2_8.configure(highlightbackground="#d9d9d9")
        self.Label2_8.configure(highlightcolor="black")
        self.Label2_8.configure(text='''No of Male Kids''')

        self.Text2_9 = tk.Text(self.Frame2)
        self.Text2_9.place(relx=0.469, rely=0.25, relheight=0.055, relwidth=0.346)
        self.Text2_9.configure(background="white")
        self.Text2_9.configure(font="TkTextFont")
        self.Text2_9.configure(foreground="black")
        self.Text2_9.configure(highlightbackground="#d9d9d9")
        self.Text2_9.configure(highlightcolor="black")
        self.Text2_9.configure(insertbackground="black")
        self.Text2_9.configure(selectbackground="#c4c4c4")
        self.Text2_9.configure(selectforeground="black")
        self.Text2_9.configure(wrap="word")
        self.Text2_9.insert(END, self.goatData[8])

        self.Label2_6 = tk.Label(self.Frame2)
        self.Label2_6.place(relx=0.1, rely=0.34, height=50, width=141)
        self.Label2_6.configure(activebackground="#f9f9f9")
        self.Label2_6.configure(activeforeground="black")
        self.Label2_6.configure(background="#d9d9d9")
        self.Label2_6.configure(disabledforeground="#a3a3a3")
        self.Label2_6.configure(font=font10)
        self.Label2_6.configure(foreground="#000000")
        self.Label2_6.configure(highlightbackground="#d9d9d9")
        self.Label2_6.configure(highlightcolor="black")
        self.Label2_6.configure(text='''No of Female Kids''')

        self.Text2 = tk.Text(self.Frame2)
        self.Text2.place(relx=0.469, rely=0.35, relheight=0.055, relwidth=0.346)
        self.Text2.configure(background="white")
        self.Text2.configure(font="TkTextFont")
        self.Text2.configure(foreground="black")
        self.Text2.configure(highlightbackground="#d9d9d9")
        self.Text2.configure(highlightcolor="black")
        self.Text2.configure(insertbackground="black")
        self.Text2.configure(selectbackground="#c4c4c4")
        self.Text2.configure(selectforeground="black")
        self.Text2.configure(wrap="word")
        self.Text2.insert(END, self.goatData[9])

        self.Frame3 = tk.Frame(self.Frame2)
        self.Frame3.place(relx=0.234, rely=0.525, relheight=0.442, relwidth=0.612)
        self.Frame3.configure(relief='groove')
        self.Frame3.configure(borderwidth="2")
        self.Frame3.configure(relief="groove")
        self.Frame3.configure(background="#d9d9d9")
        
        self.tree3 = ttk.Treeview(self.Frame3)
        self.tree3.place(relx=0.00,rely=0.00,height=300,width=310)
        self.tree3["columns"] = ("#0", "#1", "#2", "#3")
        self.tree3.column("#0", width=50,stretch=True,anchor='center')
        self.tree3.column("#1", width=80,stretch=True,anchor='center')
        self.tree3.column("#2", width=80,stretch=True,anchor='center')
        self.tree3.column("#3", width=80,stretch=True,anchor='center')
        self.tree3.heading("#0", text="S.NO")
        self.tree3.heading("#1", text="MOTHER ID")
        self.tree3.heading("#2", text="KID ID")
        self.tree3.heading("#3", text="GENDER")

        self.Label2_1 = tk.Label(top)
        self.Label2_1.place(relx=0.041, rely=0.390, height=53, width=113)
        self.Label2_1.configure(activebackground="#f9f9f9")
        self.Label2_1.configure(activeforeground="black")
        self.Label2_1.configure(background="#d9d9d9")
        self.Label2_1.configure(disabledforeground="#a3a3a3")
        self.Label2_1.configure(font=("font10",10))
        self.Label2_1.configure(foreground="#000000")
        self.Label2_1.configure(highlightbackground="#d9d9d9")
        self.Label2_1.configure(highlightcolor="black")
        self.Label2_1.configure(text='''Anthrax''')

        self.Label2_2 = tk.Label(top)
        self.Label2_2.place(relx=0.011, rely=0.460, height=52, width=195)
        self.Label2_2.configure(activebackground="#f9f9f9")
        self.Label2_2.configure(activeforeground="black")
        self.Label2_2.configure(background="#d9d9d9")
        self.Label2_2.configure(disabledforeground="#a3a3a3")
        self.Label2_2.configure(font=("font10",10))
        self.Label2_2.configure(foreground="#000000")
        self.Label2_2.configure(highlightbackground="#d9d9d9")
        self.Label2_2.configure(highlightcolor="black")
        self.Label2_2.configure(text='''Haemorrhagic Septicemia(H.S)''')

        self.Label2_3 = tk.Label(top)
        self.Label2_3.place(relx=0.041, rely=0.530, height=53, width=113)
        self.Label2_3.configure(activebackground="#f9f9f9")
        self.Label2_3.configure(activeforeground="black")
        self.Label2_3.configure(background="#d9d9d9")
        self.Label2_3.configure(disabledforeground="#a3a3a3")
        self.Label2_3.configure(font=("font10",10))
        self.Label2_3.configure(foreground="#000000")
        self.Label2_3.configure(highlightbackground="#d9d9d9")
        self.Label2_3.configure(highlightcolor="black")
        self.Label2_3.configure(text='''Enterotoxaemia''')

        self.Label2_5 = tk.Label(top)
        self.Label2_5.place(relx=0.041, rely=0.590, height=52, width=114)
        self.Label2_5.configure(activebackground="#f9f9f9")
        self.Label2_5.configure(activeforeground="black")
        self.Label2_5.configure(background="#d9d9d9")
        self.Label2_5.configure(disabledforeground="#a3a3a3")
        self.Label2_5.configure(font=("font10",10))
        self.Label2_5.configure(foreground="#000000")
        self.Label2_5.configure(highlightbackground="#d9d9d9")
        self.Label2_5.configure(highlightcolor="black")
        self.Label2_5.configure(text='''Black Quarter''')

        self.Label2_5 = tk.Label(top)
        self.Label2_5.place(relx=0.011, rely=0.655, height=52, width=195)
        self.Label2_5.configure(activebackground="#f9f9f9")
        self.Label2_5.configure(activeforeground="black")
        self.Label2_5.configure(background="#d9d9d9")
        self.Label2_5.configure(disabledforeground="#a3a3a3")
        self.Label2_5.configure(font=("font10",10))
        self.Label2_5.configure(foreground="#000000")
        self.Label2_5.configure(highlightbackground="#d9d9d9")
        self.Label2_5.configure(highlightcolor="black")
        self.Label2_5.configure(text='''P.P.R.''')

        self.Label2_5 = tk.Label(top)
        self.Label2_5.place(relx=0.011, rely=0.720, height=52, width=180)
        self.Label2_5.configure(activebackground="#f9f9f9")
        self.Label2_5.configure(activeforeground="black")
        self.Label2_5.configure(background="#d9d9d9")
        self.Label2_5.configure(disabledforeground="#a3a3a3")
        self.Label2_5.configure(font=("font10",10))
        self.Label2_5.configure(foreground="#000000")
        self.Label2_5.configure(highlightbackground="#d9d9d9")
        self.Label2_5.configure(highlightcolor="black")
        self.Label2_5.configure(text='''Foot and Mouth Disease''')

        self.label205 = tk.Label(top)
        self.label205.place(relx=0.041, rely=0.790, height=52, width=113)
        self.label205.configure(activebackground="#f9f9f9")
        self.label205.configure(activeforeground="black")
        self.label205.configure(background="#d9d9d9")
        self.label205.configure(disabledforeground="#a3a3a3")
        self.label205.configure(font=("font10",10))
        self.label205.configure(foreground="#000000")
        self.label205.configure(highlightbackground="#d9d9d9")
        self.label205.configure(highlightcolor="black")
        self.label205.configure(text='''Goat Pox''')

        self.label305 = tk.Label(top)
        self.label305.place(relx=0.041, rely=0.860, height=52, width=113)
        self.label305.configure(activebackground="#f9f9f9")
        self.label305.configure(activeforeground="black")
        self.label305.configure(background="#d9d9d9")
        self.label305.configure(disabledforeground="#a3a3a3")
        self.label305.configure(font=("font10",10))
        self.label305.configure(foreground="#000000")
        self.label305.configure(highlightbackground="#d9d9d9")
        self.label305.configure(highlightcolor="black")
        self.label305.configure(text='''C.C.P.P''')

        self.Label2_5 = tk.Label(top)
        self.Label2_5.place(relx=0.051, rely=0.923, height=52, width=93)
        self.Label2_5.configure(activebackground="#f9f9f9")
        self.Label2_5.configure(activeforeground="black")
        self.Label2_5.configure(background="#d9d9d9")
        self.Label2_5.configure(disabledforeground="#a3a3a3")
        self.Label2_5.configure(font=font13)
        self.Label2_5.configure(foreground="#000000")
        self.Label2_5.configure(highlightbackground="#d9d9d9")
        self.Label2_5.configure(highlightcolor="black")
        self.Label2_5.configure(text='''Mortality''')

        self.Label2_5 = tk.Label(top)
        self.Label2_5.place(relx=0.051, rely=0.238, height=52, width=113)
        self.Label2_5.configure(activebackground="#f9f9f9")
        self.Label2_5.configure(activeforeground="black")
        self.Label2_5.configure(background="#d9d9d9")
        self.Label2_5.configure(disabledforeground="#a3a3a3")
        self.Label2_5.configure(font=("font10",10))
        self.Label2_5.configure(foreground="#000000")
        self.Label2_5.configure(highlightbackground="#d9d9d9")
        self.Label2_5.configure(highlightcolor="black")
        self.Label2_5.configure(text='''Value''')

        self.Text1_5 = tk.Text(top)
        self.Text1_5.place(relx=0.152, rely=0.250, relheight=0.036
                , relwidth=0.139)
        self.Text1_5.configure(background="white")
        self.Text1_5.configure(font="TkTextFont")
        self.Text1_5.configure(foreground="black")
        self.Text1_5.configure(highlightbackground="#d9d9d9")
        self.Text1_5.configure(highlightcolor="black")
        self.Text1_5.configure(insertbackground="black")
        self.Text1_5.configure(selectbackground="#c4c4c4")
        self.Text1_5.configure(selectforeground="black")
        self.Text1_5.configure(wrap="word")

        self.Text1_5.insert(END, self.goatData[5])

        self.Text1.insert(END, self.goatData[0])

        self.isAlive = self.goatData[10]
        self.Canvas1.insert(END, self.isAlive)

        self.isPregnant = self.goatData[4]
        self.Canvas2.insert(END, self.isPregnant)

        if goatData[3] == 'm':
            self.Frame2.place_forget()

        self.populateTree()

        counter = 0

        # Weight graph
        data1 = self.db.getWeightRecords(goatData[0])
        dataColumns1 = self.db.getWeightColumnNames(goatData[0])
        df = pd.DataFrame(data1,columns=dataColumns1)
        # print(type(df1.date_checked[0]))

        figure = plt.Figure(figsize=(6,6), dpi=60)
        ax1 = figure.add_subplot(111)
        line2 = FigureCanvasTkAgg(figure, self.Frame1)
        line2.get_tk_widget().pack(side=tk.LEFT, fill=tk.NONE,padx=2)
        df.plot(kind='line',legend= True, ax=ax1, color='r',marker='o', fontsize=15)
        ax1.set_title('Chart of Growth') 
        ax1.set_xlabel('Date_checked')
        # plt.xticks(df.index,df['Date_checked'])

    def populateTree(self):
        self.rowData = self.db.getKidsTableData(self.goatData[0])       
        for i in range(0, len(self.rowData)):
            self.tree3.insert("", END, text=i+1, values=list(self.rowData[i]))
        
    def forget(self, widget1, widget2, widget3, widget4, widget5, widget6, widget7):
        widget1.place_forget()
        widget2.place_forget()
        widget3.place_forget()
        widget4.place_forget()
        widget5.place_forget()
        widget6.place_forget()
        widget7.place_forget()
     



