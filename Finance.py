import sys

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

import Finance_support
from tkinter import END
from backend import DataBase
from tkinter import messagebox
import pandas as pd
from datetime import datetime, datetime
import xlsxwriter   

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    top = Toplevel1 (root)
    Finance_support.init(root, top)
    root.mainloop()

w = None
def create_Toplevel1(rt, *args, **kwargs):
    '''Starting point when module is imported by another module.
       Correct form of call: 'create_Toplevel1(root, *args, **kwargs)' .'''
    global w, w_win, root
    #rt = root
    root = rt
    w = tk.Toplevel (root)
    top = Toplevel1 (w)
    Finance_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Toplevel1():
    global w
    w.destroy()
    w = None

global flag1

class Toplevel1:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'
        font14 = "-family {Segoe UI} -size 14 -weight bold"
        font9 = "-family {Segoe UI} -size 10 -weight bold"
        font8 = "-family {Segoe UI} -size 10 -weight normal"

        top.geometry("1300x760+20+20")
        top.minsize(148, 1)
        top.maxsize(1800, 850)
        top.resizable(1, 1)
        top.title("Finance")
        top.configure(background="#78909C")
        
        self.db = DataBase()

        self.header = tk.Label(top)
        self.header.place(relx=0.446, rely=0.013, height=26, width=192)
        self.header.configure(background="#d9d9d9")
        self.header.configure(disabledforeground="#a3a3a3")
        self.header.configure(font=font14)
        self.header.configure(foreground="#000000")
        self.header.configure(text='''FINANCE''')

        self.Frame1 = tk.Frame(top)
        # self.Frame1.place(relx=0.615, rely=0.079, relheight=0.888, relwidth=0.365)
        self.Frame1.place_forget()
        self.Frame1.configure(relief='groove')
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief="groove")
        self.Frame1.configure(background="#78909C")

        self.Button1 = tk.Button(top, command =lambda: self.showLivestock(1))
        self.Button1.place(relx=0.538, rely=0.053, height=33, width=56)
        self.Button1.configure(activebackground="#ececec")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#d9d9d9")
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''About''')

        self.Frame2 = tk.Frame(top)
        # self.Frame2.place(relx=0.615, rely=0.079, relheight=0.888, relwidth=0.365)
        self.Frame2.place_forget()
        self.Frame2.configure(relief='groove')
        self.Frame2.configure(borderwidth="2")
        self.Frame2.configure(relief="groove")
        self.Frame2.configure(background="#78909C")
        self.Frame2.configure(highlightbackground="#d9d9d9")
        self.Frame2.configure(highlightcolor="black")

        self.Button2 = tk.Button(top, command =lambda: self.showLabour(1))
        self.Button2.place(relx=0.538, rely=0.237, height=33, width=56)
        self.Button2.configure(activebackground="#ececec")
        self.Button2.configure(activeforeground="#000000")
        self.Button2.configure(background="#d9d9d9")
        self.Button2.configure(disabledforeground="#a3a3a3")
        self.Button2.configure(foreground="#000000")
        self.Button2.configure(highlightbackground="#d9d9d9")
        self.Button2.configure(highlightcolor="black")
        self.Button2.configure(pady="0")
        self.Button2.configure(text='''About''')

        self.Frame3 = tk.Frame(top)
        # self.Frame3.place(relx=0.615, rely=0.079, relheight=0.888, relwidth=0.365)
        self.Frame3.place_forget()
        self.Frame3.configure(relief='groove')
        self.Frame3.configure(borderwidth="2")
        self.Frame3.configure(relief="groove")
        self.Frame3.configure(background="#78909C")
        self.Frame3.configure(highlightbackground="#d9d9d9")
        self.Frame3.configure(highlightcolor="black")

        self.Button3 = tk.Button(top, command =lambda: self.showFeed(1))
        self.Button3.place(relx=0.538, rely=0.421, height=33, width=56)
        self.Button3.configure(activebackground="#ececec")
        self.Button3.configure(activeforeground="#000000")
        self.Button3.configure(background="#d9d9d9")
        self.Button3.configure(disabledforeground="#a3a3a3")
        self.Button3.configure(foreground="#000000")
        self.Button3.configure(highlightbackground="#d9d9d9")
        self.Button3.configure(highlightcolor="black")
        self.Button3.configure(pady="0")
        self.Button3.configure(text='''About''')

        self.Frame4 = tk.Frame(top)
        # self.Frame4.place(relx=0.615, rely=0.079, relheight=0.888, relwidth=0.365)
        self.Frame4.place_forget()
        self.Frame4.configure(relief='groove')
        self.Frame4.configure(borderwidth="2")
        self.Frame4.configure(relief="groove")
        self.Frame4.configure(background="#78909C")
        self.Frame4.configure(highlightbackground="#d9d9d9")
        self.Frame4.configure(highlightcolor="black")

        self.Button4 = tk.Button(top, command =lambda: self.showMisc(1))
        self.Button4.place(relx=0.539, rely=0.605, height=32, width=56)
        self.Button4.configure(activebackground="#ececec")
        self.Button4.configure(activeforeground="#000000")
        self.Button4.configure(background="#d9d9d9")
        self.Button4.configure(disabledforeground="#a3a3a3")
        self.Button4.configure(foreground="#000000")
        self.Button4.configure(highlightbackground="#d9d9d9")
        self.Button4.configure(highlightcolor="black")
        self.Button4.configure(pady="0")
        self.Button4.configure(text='''About''')

        self.Frame5 = tk.Frame(top)
        # self.Frame5.place(relx=0.615, rely=0.079, relheight=0.888, relwidth=0.365)
        self.Frame5.place_forget()
        self.Frame5.configure(relief='groove')
        self.Frame5.configure(borderwidth="2")
        self.Frame5.configure(relief="groove")
        self.Frame5.configure(background="#78909C")
        self.Frame5.configure(highlightbackground="#d9d9d9")
        self.Frame5.configure(highlightcolor="black")

        self.Button5 = tk.Button(top, command =lambda: self.showIncome(1))
        self.Button5.place(relx=0.538, rely=0.789, height=32, width=56)
        self.Button5.configure(activebackground="#ececec")
        self.Button5.configure(activeforeground="#000000")
        self.Button5.configure(background="#d9d9d9")
        self.Button5.configure(disabledforeground="#a3a3a3")
        self.Button5.configure(foreground="#000000")
        self.Button5.configure(highlightbackground="#d9d9d9")
        self.Button5.configure(highlightcolor="black")
        self.Button5.configure(pady="0")
        self.Button5.configure(text='''About''')

        self.Frame6 = tk.Frame(top)
        # self.Frame6.place(relx=0.615, rely=0.079, relheight=0.888, relwidth=0.365)
        self.Frame6.place_forget()
        self.Frame6.configure(relief='groove')
        self.Frame6.configure(borderwidth="2")
        self.Frame6.configure(relief="groove")
        self.Frame6.configure(background="#78909C")
        self.Frame6.configure(highlightbackground="#d9d9d9")
        self.Frame6.configure(highlightcolor="black")

        self.button = tk.Button(top, command = self.showTotal)
        self.button.place(relx=0.860, rely=0.01, height=35, width=150)
        self.button.configure(activebackground="#ececec")
        self.button.configure(activeforeground="#000000")
        self.button.configure(background="#d9d9d9")
        self.button.configure(disabledforeground="#a3a3a3")
        self.button.configure(font="-family {Segoe UI} -size 12")
        self.button.configure(foreground="#000000")
        self.button.configure(highlightbackground="#d9d9d9")
        self.button.configure(highlightcolor="black")
        self.button.configure(pady="0")
        self.button.configure(text='''GENERATE TOTAL''')

        self.Label01 = tk.Label(self.Frame6)
        self.Label01.place(relx=0.35, rely=0.001, height=26, width=200)
        self.Label01.configure(background="#d9d9d9")
        self.Label01.configure(disabledforeground="#a3a3a3")
        self.Label01.configure(foreground="#000000")
        self.Label01.configure(font="-family {Segoe UI} -size 12 -weight bold")
        self.Label01.configure(text='''YEARLY EXPENDITURE''')

        self.tree0 = ttk.Treeview(self.Frame6)
        self.tree0["columns"] = ("#0","#1","#2","#3","#4","#5")
        self.tree0.column("#0", width=140,stretch=True,anchor='center')
        self.tree0.column("#1", width=140,stretch=True,anchor='center')
        self.tree0.column("#2", width=140,stretch=True,anchor='center')
        self.tree0.heading("#0", text="S No")
        self.tree0.heading("#1", text="Category")
        self.tree0.heading("#2", text="Cost")
        self.tree0.place(relx=0.05, rely=0.05, height=300, width=420)

        self.Label01 = tk.Label(self.Frame6)
        self.Label01.place(relx=0.15, rely=0.55, height=26, width=133)
        self.Label01.configure(background="#d9d9d9")
        self.Label01.configure(disabledforeground="#a3a3a3")
        self.Label01.configure(foreground="#000000")
        self.Label01.configure(font="-family {Segoe UI} -size 14 -weight bold")
        self.Label01.configure(text='''GRAND TOTAL''')

        self.TEntry02 = ttk.Entry(self.Frame6)
        self.TEntry02.place(relx=0.55,rely=0.54, height=33, width=140)
        self.TEntry02.configure(takefocus="")

        self.GenXcel = tk.Button(self.Frame6, command = self.genExcel)
        self.GenXcel.place(relx=0.35, rely=0.662, height=50, width=140)
        self.GenXcel.configure(activebackground="#ececec")
        self.GenXcel.configure(activeforeground="#000000")
        self.GenXcel.configure(background="#d9d9d9")
        self.GenXcel.configure(disabledforeground="#a3a3a3")
        self.GenXcel.configure(foreground="#000000")
        self.GenXcel.configure(highlightbackground="#d9d9d9")
        self.GenXcel.configure(highlightcolor="black")
        self.GenXcel.configure(pady="0")
        self.GenXcel.configure(font="-family {Segoe UI} -size 11 -weight bold")
        self.GenXcel.configure(text='''Generate Excel''')

        self.Close = tk.Button(self.Frame6, command = lambda: self.cancel(self.Frame6))
        self.Close.place(relx=0.45, rely=0.842, height=30, width=59)
        self.Close.configure(activebackground="#ececec")
        self.Close.configure(activeforeground="#000000")
        self.Close.configure(background="#d9d9d9")
        self.Close.configure(disabledforeground="#a3a3a3")
        self.Close.configure(foreground="#000000")
        self.Close.configure(highlightbackground="#d9d9d9")
        self.Close.configure(highlightcolor="black")
        self.Close.configure(pady="0")
        self.Close.configure(text='''CLOSE''')

        self.treeFrame5 = tk.Frame(top)
        self.treeFrame5.place(relx=0.015, rely=0.105, relheight=0.125, relwidth=0.572)
        self.treeFrame5.configure(relief='groove')
        self.treeFrame5.configure(borderwidth="2")
        self.treeFrame5.configure(relief="groove")
        self.treeFrame5.configure(background="#d9d9d9")

        self.tree1 = ttk.Treeview(self.treeFrame5)
        self.tree1["columns"] = ("#0","#1","#2","#3","#4","#5")
        self.tree1.column("#0", width=125,stretch=True,anchor='center')
        self.tree1.column("#1", width=125,stretch=True,anchor='center')
        self.tree1.column("#2", width=125,stretch=True,anchor='center')
        self.tree1.column("#3", width=125,stretch=True,anchor='center')
        self.tree1.column("#4", width=125,stretch=True,anchor='center')
        self.tree1.column("#5", width=125,stretch=True,anchor='center')
        self.tree1.heading("#0", text="S No")
        self.tree1.heading("#1", text="Category")
        self.tree1.heading("#2", text="Breed")
        self.tree1.heading("#3", text="Cost")
        self.tree1.heading("#4", text="Total Weight")
        self.tree1.heading("#5", text="Total Cost")
        self.tree1.pack(fill='y')
        self.tree1.bind("<<TreeviewSelect>>", self.getLivestockData)

        self.treeFrame6 = tk.Frame(top)
        self.treeFrame6.place(relx=0.015, rely=0.289, relheight=0.125, relwidth=0.572)
        self.treeFrame6.configure(relief='groove')
        self.treeFrame6.configure(borderwidth="2")
        self.treeFrame6.configure(relief="groove")
        self.treeFrame6.configure(background="#d9d9d9")
        self.treeFrame6.configure(highlightbackground="#d9d9d9")
        self.treeFrame6.configure(highlightcolor="black")

        self.tree2 = ttk.Treeview(self.treeFrame6)
        self.tree2["columns"] = ("#0","#1","#2","#3","#4")
        self.tree2.column("#0", width=150, stretch=True, anchor='center')
        self.tree2.column("#1", width=150, stretch=True, anchor='center')
        self.tree2.column("#2", width=150, stretch=True, anchor='center')
        self.tree2.column("#3", width=150, stretch=True, anchor='center')
        self.tree2.column("#4", width=150, stretch=True, anchor='center')
        self.tree2.heading("#0", text="S No")
        self.tree2.heading("#1", text="Category")
        self.tree2.heading("#2", text="Salary")
        self.tree2.heading("#3", text="Count")
        self.tree2.heading("#4", text="Total Salary")
        self.tree2.pack(fill='y')
        self.tree2.bind("<<TreeviewSelect>>", self.getLabourData)

        self.treeFrame7 = tk.Frame(top)
        self.treeFrame7.place(relx=0.015, rely=0.474, relheight=0.125, relwidth=0.572)
        self.treeFrame7.configure(relief='groove')
        self.treeFrame7.configure(borderwidth="2")
        self.treeFrame7.configure(relief="groove")
        self.treeFrame7.configure(background="#d9d9d9")
        self.treeFrame7.configure(highlightbackground="#d9d9d9")
        self.treeFrame7.configure(highlightcolor="black")

        self.tree3 = ttk.Treeview(self.treeFrame7)
        self.tree3["columns"] = ("#0","#1","#2","#3","#4","#5")
        self.tree3.column("#0", width=125,stretch=True,anchor='center')
        self.tree3.column("#1", width=125,stretch=True,anchor='center')
        self.tree3.column("#2", width=125,stretch=True,anchor='center')
        self.tree3.column("#3", width=125,stretch=True,anchor='center')
        self.tree3.column("#4", width=125,stretch=True,anchor='center')
        self.tree3.column("#5", width=125,stretch=True,anchor='center')
        self.tree3.heading("#0", text="S No")
        self.tree3.heading("#1", text="Date")
        self.tree3.heading("#2", text="Item")
        self.tree3.heading("#3", text="Cost")
        self.tree3.heading("#4", text="Weight")
        self.tree3.heading("#5", text="Total Cost")
        self.tree3.pack(fill='y')
        self.tree3.bind("<<TreeviewSelect>>", self.getFeedData)

        self.treeFrame8 = tk.Frame(top)
        self.treeFrame8.place(relx=0.015, rely=0.658, relheight=0.125, relwidth=0.572)
        self.treeFrame8.configure(relief='groove')
        self.treeFrame8.configure(borderwidth="2")
        self.treeFrame8.configure(relief="groove")
        self.treeFrame8.configure(background="#d9d9d9")
        self.treeFrame8.configure(highlightbackground="#d9d9d9")
        self.treeFrame8.configure(highlightcolor="black")

        self.tree4 = ttk.Treeview(self.treeFrame8)
        self.tree4["columns"] = ("#0","#1","#2","#3")
        self.tree4.column("#0", width=185,stretch=True,anchor='center')
        self.tree4.column("#1", width=185,stretch=True,anchor='center')
        self.tree4.column("#2", width=185,stretch=True,anchor='center')
        self.tree4.column("#3", width=185,stretch=True,anchor='center')
        self.tree4.heading("#0", text="S No")
        self.tree4.heading("#1", text="Date")
        self.tree4.heading("#2", text="Category")
        self.tree4.heading("#3", text="Cost")
        self.tree4.pack(fill='y')
        self.tree4.bind("<<TreeviewSelect>>", self.getMiscData)

        self.treeFrame9 = tk.Frame(top)
        self.treeFrame9.place(relx=0.015, rely=0.842, relheight=0.125, relwidth=0.572)
        self.treeFrame9.configure(relief='groove')
        self.treeFrame9.configure(borderwidth="2")
        self.treeFrame9.configure(relief="groove")
        self.treeFrame9.configure(background="#d9d9d9")
        self.treeFrame9.configure(highlightbackground="#d9d9d9")
        self.treeFrame9.configure(highlightcolor="black")

        self.tree5 = ttk.Treeview(self.treeFrame9)
        self.tree5["columns"] = ("#0","#1","#2","#3")
        self.tree5.column("#0", width=185,stretch=True,anchor='center')
        self.tree5.column("#1", width=185,stretch=True,anchor='center')
        self.tree5.column("#2", width=185,stretch=True,anchor='center')
        self.tree5.column("#3", width=185,stretch=True,anchor='center')
        self.tree5.heading("#0", text="S No")
        self.tree5.heading("#1", text="Date")
        self.tree5.heading("#2", text="Details")
        self.tree5.heading("#3", text="Cost")
        self.tree5.pack(fill='y')
        self.tree5.bind("<<TreeviewSelect>>", self.getIncomeData)

        self.Label1 = tk.Label(top)
        self.Label1.place(relx=0.015, rely=0.066, height=26, width=133)
        self.Label1.configure(background="#d9d9d9")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(font=font9)
        self.Label1.configure(text='''LiveStock Networth''')

        self.Label11 = tk.Label(self.Frame1)
        self.Label11.place(relx=0.35, rely=0.001, height=26, width=133)
        self.Label11.configure(background="#d9d9d9")
        self.Label11.configure(disabledforeground="#a3a3a3")
        self.Label11.configure(foreground="#000000")
        self.Label11.configure(font=font9)
        self.Label11.configure(text='''LiveStock Networth''')

        self.Label12 = tk.Label(self.Frame1)
        self.Label12.place(relx=0.1, rely=0.1, height=26, width=133)
        self.Label12.configure(background="#d9d9d9")
        self.Label12.configure(disabledforeground="#a3a3a3")
        self.Label12.configure(foreground="#000000")
        self.Label12.configure(font=font9)
        self.Label12.configure(text='''NETWORTH : ''')

        self.TEntry13 = ttk.Entry(self.Frame1)
        self.TEntry13.place(relx=0.5,rely=0.09, height=35, width=140)
        self.TEntry13.configure(takefocus="")

        self.Label16 = tk.Label(self.Frame1)
        self.Label16.place_forget()
        self.Label16.configure(background="#d9d9d9")
        self.Label16.configure(disabledforeground="#a3a3a3")
        self.Label16.configure(foreground="#000000")
        self.Label16.configure(font=font9)
        self.Label16.configure(text='''Alter Cost''')

        self.Label14 = tk.Label(self.Frame1)
        self.Label14.place_forget()
        self.Label14.configure(background="#d9d9d9")
        self.Label14.configure(disabledforeground="#a3a3a3")
        self.Label14.configure(foreground="#000000")
        self.Label14.configure(font=font8)
        self.Label14.configure(text='''Cost : ''')

        self.TEntry15 = ttk.Entry(self.Frame1)
        self.TEntry15.place_forget()
        self.TEntry15.configure(takefocus="")

        self.Submit1 = tk.Button(self.Frame1, command=self.acceptLivestockNetworth)
        self.Submit1.place(relx=0.580, rely=0.842, height=30, width=59)
        self.Submit1.configure(activebackground="#ececec")
        self.Submit1.configure(activeforeground="#000000")
        self.Submit1.configure(background="#d9d9d9")
        self.Submit1.configure(disabledforeground="#a3a3a3")
        self.Submit1.configure(foreground="#000000")
        self.Submit1.configure(highlightbackground="#d9d9d9")
        self.Submit1.configure(highlightcolor="black")
        self.Submit1.configure(pady="0")
        self.Submit1.configure(text='''SUBMIT''')

        self.Cancel1 = tk.Button(self.Frame1, command = lambda: self.cancel(self.Frame1))
        self.Cancel1.place(relx=0.320, rely=0.842, height=30, width=59)
        self.Cancel1.configure(activebackground="#ececec")
        self.Cancel1.configure(activeforeground="#000000")
        self.Cancel1.configure(background="#d9d9d9")
        self.Cancel1.configure(disabledforeground="#a3a3a3")
        self.Cancel1.configure(foreground="#000000")
        self.Cancel1.configure(highlightbackground="#d9d9d9")
        self.Cancel1.configure(highlightcolor="black")
        self.Cancel1.configure(pady="0")
        self.Cancel1.configure(text='''CANCEL''')

        self.Label2 = tk.Label(top)
        self.Label2.place(relx=0.015, rely=0.25, height=26, width=93)
        self.Label2.configure(activebackground="#f9f9f9")
        self.Label2.configure(activeforeground="black")
        self.Label2.configure(background="#d9d9d9")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(highlightbackground="#d9d9d9")
        self.Label2.configure(highlightcolor="black")
        self.Label2.configure(font=font9)
        self.Label2.configure(text='''Labour Salary''')

        self.Label21 = tk.Label(self.Frame2)
        self.Label21.place(relx=0.35, rely=0.001, height=26, width=133)
        self.Label21.configure(background="#d9d9d9")
        self.Label21.configure(disabledforeground="#a3a3a3")
        self.Label21.configure(foreground="#000000")
        self.Label21.configure(font=font9)
        self.Label21.configure(text='''Labour Salary''')

        self.Label22 = tk.Label(self.Frame2)
        self.Label22.place(relx=0.1, rely=0.1, height=26, width=133)
        self.Label22.configure(background="#d9d9d9")
        self.Label22.configure(disabledforeground="#a3a3a3")
        self.Label22.configure(foreground="#000000")
        self.Label22.configure(font=font8)
        self.Label22.configure(text='''Total Cost : ''')

        self.TEntry23 = ttk.Entry(self.Frame2)
        self.TEntry23.place(relx=0.5,rely=0.09, height=35, width=140)
        self.TEntry23.configure(takefocus="")

        self.Label24 = tk.Label(self.Frame2)
        self.Label24.place(relx=0.35, rely=0.2, height=26, width=133)
        self.Label24.configure(background="#d9d9d9")
        self.Label24.configure(disabledforeground="#a3a3a3")
        self.Label24.configure(foreground="#000000")
        self.Label24.configure(font=font9)
        self.Label24.configure(text='''Add Entry''')

        self.DEntry2 = tk.Label(self.Frame2)
        # self.DEntry2.place(relx=0.35, rely=0.2, height=26, width=133)
        self.DEntry2.place_forget()
        self.DEntry2.configure(background="#d9d9d9")
        self.DEntry2.configure(disabledforeground="#a3a3a3")
        self.DEntry2.configure(foreground="#000000")
        self.DEntry2.configure(font="-family {Segoe UI} -size 10 -weight bold")
        self.DEntry2.configure(text='''Delete Entry''')

        self.Label25 = tk.Label(self.Frame2)
        self.Label25.place(relx=0.1, rely=0.3, height=26, width=133)
        self.Label25.configure(background="#d9d9d9")
        self.Label25.configure(disabledforeground="#a3a3a3")
        self.Label25.configure(foreground="#000000")
        self.Label25.configure(font=font8)
        self.Label25.configure(text='''Category : ''')

        self.TEntry26 = ttk.Entry(self.Frame2)
        self.TEntry26.place(relx=0.5,rely=0.29, height=35, width=140)
        self.TEntry26.configure(takefocus="")

        self.Label27 = tk.Label(self.Frame2)
        self.Label27.place(relx=0.1, rely=0.4, height=26, width=133)
        self.Label27.configure(background="#d9d9d9")
        self.Label27.configure(disabledforeground="#a3a3a3")
        self.Label27.configure(foreground="#000000")
        self.Label27.configure(font=font8)
        self.Label27.configure(text='''Salary(Per Day) : ''')

        self.TEntry28 = ttk.Entry(self.Frame2)
        self.TEntry28.place(relx=0.5,rely=0.39, height=35, width=140)
        self.TEntry28.configure(takefocus="")

        self.Label29 = tk.Label(self.Frame2)
        self.Label29.place(relx=0.1, rely=0.5, height=26, width=133)
        self.Label29.configure(background="#d9d9d9")
        self.Label29.configure(disabledforeground="#a3a3a3")
        self.Label29.configure(foreground="#000000")
        self.Label29.configure(font=font8)
        self.Label29.configure(text='''Count : ''')

        self.TEntry210 = ttk.Entry(self.Frame2)
        self.TEntry210.place(relx=0.5,rely=0.49, height=35, width=140)
        self.TEntry210.configure(takefocus="")

        self.Submit2 = tk.Button(self.Frame2, command=self.acceptLabour)
        self.Submit2.place(relx=0.580, rely=0.842, height=30, width=59)
        self.Submit2.configure(activebackground="#ececec")
        self.Submit2.configure(activeforeground="#000000")
        self.Submit2.configure(background="#d9d9d9")
        self.Submit2.configure(disabledforeground="#a3a3a3")
        self.Submit2.configure(foreground="#000000")
        self.Submit2.configure(highlightbackground="#d9d9d9")
        self.Submit2.configure(highlightcolor="black")
        self.Submit2.configure(pady="0")
        self.Submit2.configure(text='''SUBMIT''')

        self.Delete2 = tk.Button(self.Frame2, command = self.deleteLabour)
        # self.Delete2.place(relx=0.580, rely=0.842, height=30, width=59)
        self.Delete2.place_forget()
        self.Delete2.configure(activebackground="#ececec")
        self.Delete2.configure(activeforeground="#000000")
        self.Delete2.configure(background="#d9d9d9")
        self.Delete2.configure(disabledforeground="#a3a3a3")
        self.Delete2.configure(foreground="#000000")
        self.Delete2.configure(highlightbackground="#d9d9d9")
        self.Delete2.configure(highlightcolor="black")
        self.Delete2.configure(pady="0")
        self.Delete2.configure(text='''DELETE''')

        self.Cancel2 = tk.Button(self.Frame2, command = lambda: self.cancel(self.Frame2))
        self.Cancel2.place(relx=0.320, rely=0.842, height=30, width=59)
        self.Cancel2.configure(activebackground="#ececec")
        self.Cancel2.configure(activeforeground="#000000")
        self.Cancel2.configure(background="#d9d9d9")
        self.Cancel2.configure(disabledforeground="#a3a3a3")
        self.Cancel2.configure(foreground="#000000")
        self.Cancel2.configure(highlightbackground="#d9d9d9")
        self.Cancel2.configure(highlightcolor="black")
        self.Cancel2.configure(pady="0")
        self.Cancel2.configure(text='''CANCEL''')

        self.Label3 = tk.Label(top)
        self.Label3.place(relx=0.015, rely=0.434, height=26, width=71)
        self.Label3.configure(activebackground="#f9f9f9")
        self.Label3.configure(activeforeground="black")
        self.Label3.configure(background="#d9d9d9")
        self.Label3.configure(disabledforeground="#a3a3a3")
        self.Label3.configure(foreground="#000000")
        self.Label3.configure(highlightbackground="#d9d9d9")
        self.Label3.configure(highlightcolor="black")
        self.Label3.configure(font=font9)
        self.Label3.configure(text='''Feed Cost''')

        self.Label31 = tk.Label(self.Frame3)
        self.Label31.place(relx=0.35, rely=0.001, height=26, width=133)
        self.Label31.configure(background="#d9d9d9")
        self.Label31.configure(disabledforeground="#a3a3a3")
        self.Label31.configure(foreground="#000000")
        self.Label31.configure(font=font9)
        self.Label31.configure(text='''Feed Cost''')

        self.Label32 = tk.Label(self.Frame3)
        self.Label32.place(relx=0.1, rely=0.1, height=26, width=133)
        self.Label32.configure(background="#d9d9d9")
        self.Label32.configure(disabledforeground="#a3a3a3")
        self.Label32.configure(foreground="#000000")
        self.Label32.configure(font=font8)
        self.Label32.configure(text='''Total Cost : ''')

        self.TEntry33 = ttk.Entry(self.Frame3)
        self.TEntry33.place(relx=0.5,rely=0.09, height=35, width=140)
        self.TEntry33.configure(takefocus="")

        self.Label34 = tk.Label(self.Frame3)
        self.Label34.place(relx=0.35, rely=0.2, height=26, width=133)
        self.Label34.configure(background="#d9d9d9")
        self.Label34.configure(disabledforeground="#a3a3a3")
        self.Label34.configure(foreground="#000000")
        self.Label34.configure(font=font9)
        self.Label34.configure(text='''Add Entry''')

        self.DEntry3 = tk.Label(self.Frame3)
        # self.DEntry3.place(relx=0.35, rely=0.2, height=26, width=133)
        self.DEntry3.place_forget()
        self.DEntry3.configure(background="#d9d9d9")
        self.DEntry3.configure(disabledforeground="#a3a3a3")
        self.DEntry3.configure(foreground="#000000")
        self.DEntry3.configure(font="-family {Segoe UI} -size 10 -weight bold")
        self.DEntry3.configure(text='''Delete Entry''')

        self.Label35 = tk.Label(self.Frame3)
        self.Label35.place(relx=0.1, rely=0.3, height=26, width=133)
        self.Label35.configure(background="#d9d9d9")
        self.Label35.configure(disabledforeground="#a3a3a3")
        self.Label35.configure(foreground="#000000")
        self.Label35.configure(font=font8)
        self.Label35.configure(text='''Item : ''')

        self.TEntry36 = ttk.Entry(self.Frame3)
        self.TEntry36.place(relx=0.5,rely=0.29, height=35, width=140)
        self.TEntry36.configure(takefocus="")

        self.Label37 = tk.Label(self.Frame3)
        self.Label37.place(relx=0.1, rely=0.4, height=26, width=133)
        self.Label37.configure(background="#d9d9d9")
        self.Label37.configure(disabledforeground="#a3a3a3")
        self.Label37.configure(foreground="#000000")
        self.Label37.configure(font=font8)
        self.Label37.configure(text='''Cost(Rs/kg) : ''')

        self.TEntry38 = ttk.Entry(self.Frame3)
        self.TEntry38.place(relx=0.5,rely=0.39, height=35, width=140)
        self.TEntry38.configure(takefocus="")

        self.Label39 = tk.Label(self.Frame3)
        self.Label39.place(relx=0.1, rely=0.5, height=26, width=133)
        self.Label39.configure(background="#d9d9d9")
        self.Label39.configure(disabledforeground="#a3a3a3")
        self.Label39.configure(foreground="#000000")
        self.Label39.configure(font=font8)
        self.Label39.configure(text='''Weight(Kg) : ''')

        self.TEntry310 = ttk.Entry(self.Frame3)
        self.TEntry310.place(relx=0.5,rely=0.49, height=35, width=140)
        self.TEntry310.configure(takefocus="")

        self.Submit3 = tk.Button(self.Frame3, command = self.acceptFeed)
        self.Submit3.place(relx=0.580, rely=0.842, height=30, width=59)
        self.Submit3.configure(activebackground="#ececec")
        self.Submit3.configure(activeforeground="#000000")
        self.Submit3.configure(background="#d9d9d9")
        self.Submit3.configure(disabledforeground="#a3a3a3")
        self.Submit3.configure(foreground="#000000")
        self.Submit3.configure(highlightbackground="#d9d9d9")
        self.Submit3.configure(highlightcolor="black")
        self.Submit3.configure(pady="0")
        self.Submit3.configure(text='''SUBMIT''')

        self.Delete3 = tk.Button(self.Frame3, command = self.deleteFeed)
        self.Delete3.place(relx=0.580, rely=0.842, height=30, width=59)
        self.Delete3.configure(activebackground="#ececec")
        self.Delete3.configure(activeforeground="#000000")
        self.Delete3.configure(background="#d9d9d9")
        self.Delete3.configure(disabledforeground="#a3a3a3")
        self.Delete3.configure(foreground="#000000")
        self.Delete3.configure(highlightbackground="#d9d9d9")
        self.Delete3.configure(highlightcolor="black")
        self.Delete3.configure(pady="0")
        self.Delete3.configure(text='''DELETE''')

        self.Cancel3 = tk.Button(self.Frame3, command = lambda: self.cancel(self.Frame3))
        self.Cancel3.place(relx=0.320, rely=0.842, height=30, width=59)
        self.Cancel3.configure(activebackground="#ececec")
        self.Cancel3.configure(activeforeground="#000000")
        self.Cancel3.configure(background="#d9d9d9")
        self.Cancel3.configure(disabledforeground="#a3a3a3")
        self.Cancel3.configure(foreground="#000000")
        self.Cancel3.configure(highlightbackground="#d9d9d9")
        self.Cancel3.configure(highlightcolor="black")
        self.Cancel3.configure(pady="0")
        self.Cancel3.configure(text='''CANCEL''')

        self.Label4 = tk.Label(top)
        self.Label4.place(relx=0.015, rely=0.618, height=26, width=143)
        self.Label4.configure(activebackground="#f9f9f9")
        self.Label4.configure(activeforeground="black")
        self.Label4.configure(background="#d9d9d9")
        self.Label4.configure(disabledforeground="#a3a3a3")
        self.Label4.configure(foreground="#000000")
        self.Label4.configure(highlightbackground="#d9d9d9")
        self.Label4.configure(highlightcolor="black")
        self.Label4.configure(font=font9)
        self.Label4.configure(text='''Miscellaneous Expense''')

        self.Label41 = tk.Label(self.Frame4)
        self.Label41.place(relx=0.35, rely=0.001, height=26, width=143)
        self.Label41.configure(background="#d9d9d9")
        self.Label41.configure(disabledforeground="#a3a3a3")
        self.Label41.configure(foreground="#000000")
        self.Label41.configure(font=font9)
        self.Label41.configure(text='''Miscellaneous Expense''')

        self.Label42 = tk.Label(self.Frame4)
        self.Label42.place(relx=0.1, rely=0.1, height=26, width=133)
        self.Label42.configure(background="#d9d9d9")
        self.Label42.configure(disabledforeground="#a3a3a3")
        self.Label42.configure(foreground="#000000")
        self.Label42.configure(font=font8)
        self.Label42.configure(text='''Total Cost : ''')

        self.TEntry43 = ttk.Entry(self.Frame4)
        self.TEntry43.place(relx=0.5,rely=0.09, height=35, width=140)
        self.TEntry43.configure(takefocus="")

        self.Label44 = tk.Label(self.Frame4)
        self.Label44.place(relx=0.35, rely=0.2, height=26, width=133)
        self.Label44.configure(background="#d9d9d9")
        self.Label44.configure(disabledforeground="#a3a3a3")
        self.Label44.configure(foreground="#000000")
        self.Label44.configure(font=font9)
        self.Label44.configure(text='''Add Entry''')

        self.DEntry4 = tk.Label(self.Frame4)
        # self.DEntry4.place(relx=0.35, rely=0.2, height=26, width=133)
        self.DEntry4.place_forget()
        self.DEntry4.configure(background="#d9d9d9")
        self.DEntry4.configure(disabledforeground="#a3a3a3")
        self.DEntry4.configure(foreground="#000000")
        self.DEntry4.configure(font="-family {Segoe UI} -size 10 -weight bold")
        self.DEntry4.configure(text='''Delete Entry''')

        self.Label45 = tk.Label(self.Frame4)
        self.Label45.place(relx=0.1, rely=0.3, height=26, width=133)
        self.Label45.configure(background="#d9d9d9")
        self.Label45.configure(disabledforeground="#a3a3a3")
        self.Label45.configure(foreground="#000000")
        self.Label45.configure(font=font8)
        self.Label45.configure(text='''Category : ''')

        self.TEntry46 = ttk.Entry(self.Frame4)
        self.TEntry46.place(relx=0.5,rely=0.29, height=35, width=140)
        self.TEntry46.configure(takefocus="")

        self.Label47 = tk.Label(self.Frame4)
        self.Label47.place(relx=0.1, rely=0.4, height=26, width=133)
        self.Label47.configure(background="#d9d9d9")
        self.Label47.configure(disabledforeground="#a3a3a3")
        self.Label47.configure(foreground="#000000")
        self.Label47.configure(font=font8)
        self.Label47.configure(text='''Cost : ''')

        self.TEntry48 = ttk.Entry(self.Frame4)
        self.TEntry48.place(relx=0.5,rely=0.39, height=35, width=140)
        self.TEntry48.configure(takefocus="")
        self.TEntry48.configure(cursor="watch")

        self.Submit4 = tk.Button(self.Frame4, command = self.acceptMiscExpense)
        self.Submit4.place(relx=0.580, rely=0.842, height=30, width=59)
        self.Submit4.configure(activebackground="#ececec")
        self.Submit4.configure(activeforeground="#000000")
        self.Submit4.configure(background="#d9d9d9")
        self.Submit4.configure(disabledforeground="#a3a3a3")
        self.Submit4.configure(foreground="#000000")
        self.Submit4.configure(highlightbackground="#d9d9d9")
        self.Submit4.configure(highlightcolor="black")
        self.Submit4.configure(pady="0")
        self.Submit4.configure(text='''SUBMIT''')

        self.Delete4 = tk.Button(self.Frame4, command = self.deleteMisc)
        self.Delete4.place(relx=0.580, rely=0.842, height=30, width=59)
        self.Delete4.configure(activebackground="#ececec")
        self.Delete4.configure(activeforeground="#000000")
        self.Delete4.configure(background="#d9d9d9")
        self.Delete4.configure(disabledforeground="#a3a3a3")
        self.Delete4.configure(foreground="#000000")
        self.Delete4.configure(highlightbackground="#d9d9d9")
        self.Delete4.configure(highlightcolor="black")
        self.Delete4.configure(pady="0")
        self.Delete4.configure(text='''DELETE''')

        self.Cancel4 = tk.Button(self.Frame4, command = lambda: self.cancel(self.Frame4))
        self.Cancel4.place(relx=0.320, rely=0.842, height=30, width=59)
        self.Cancel4.configure(activebackground="#ececec")
        self.Cancel4.configure(activeforeground="#000000")
        self.Cancel4.configure(background="#d9d9d9")
        self.Cancel4.configure(disabledforeground="#a3a3a3")
        self.Cancel4.configure(foreground="#000000")
        self.Cancel4.configure(highlightbackground="#d9d9d9")
        self.Cancel4.configure(highlightcolor="black")
        self.Cancel4.configure(pady="0")
        self.Cancel4.configure(text='''CANCEL''')

        self.Label5 = tk.Label(top)
        self.Label5.place(relx=0.005, rely=0.803, height=26, width=92)
        self.Label5.configure(activebackground="#f9f9f9")
        self.Label5.configure(activeforeground="black")
        self.Label5.configure(background="#d9d9d9")
        self.Label5.configure(disabledforeground="#a3a3a3")
        self.Label5.configure(foreground="#000000")
        self.Label5.configure(highlightbackground="#d9d9d9")
        self.Label5.configure(highlightcolor="black")
        self.Label5.configure(font=font9)
        self.Label5.configure(text='''Income''')

        self.Label51 = tk.Label(self.Frame5)
        self.Label51.place(relx=0.35, rely=0.001, height=26, width=133)
        self.Label51.configure(background="#d9d9d9")
        self.Label51.configure(disabledforeground="#a3a3a3")
        self.Label51.configure(foreground="#000000")
        self.Label51.configure(font=font9)
        self.Label51.configure(text='''Income''')

        self.Label52 = tk.Label(self.Frame5)
        self.Label52.place(relx=0.1, rely=0.1, height=26, width=133)
        self.Label52.configure(background="#d9d9d9")
        self.Label52.configure(disabledforeground="#a3a3a3")
        self.Label52.configure(foreground="#000000")
        self.Label52.configure(font=font8)
        self.Label52.configure(text='''Total Cost : ''')

        self.TEntry53 = ttk.Entry(self.Frame5)
        self.TEntry53.place(relx=0.5,rely=0.09, height=35, width=140)
        self.TEntry53.configure(takefocus="")

        self.Label54 = tk.Label(self.Frame5)
        self.Label54.place(relx=0.35, rely=0.2, height=26, width=133)
        self.Label54.configure(background="#d9d9d9")
        self.Label54.configure(disabledforeground="#a3a3a3")
        self.Label54.configure(foreground="#000000")
        self.Label54.configure(font=font9)
        self.Label54.configure(text='''Add Entry''')

        self.DEntry5 = tk.Label(self.Frame5)
        # self.DEntry5.place(relx=0.35, rely=0.2, height=26, width=133)
        self.DEntry5.place_forget()
        self.DEntry5.configure(background="#d9d9d9")
        self.DEntry5.configure(disabledforeground="#a3a3a3")
        self.DEntry5.configure(foreground="#000000")
        self.DEntry5.configure(font="-family {Segoe UI} -size 10 -weight bold")
        self.DEntry5.configure(text='''Delete Entry''')

        self.Label55 = tk.Label(self.Frame5)
        self.Label55.place(relx=0.1, rely=0.3, height=26, width=133)
        self.Label55.configure(background="#d9d9d9")
        self.Label55.configure(disabledforeground="#a3a3a3")
        self.Label55.configure(foreground="#000000")
        self.Label55.configure(font=font8)
        self.Label55.configure(text='''Details : ''')

        self.TEntry56 = ttk.Entry(self.Frame5)
        self.TEntry56.place(relx=0.5,rely=0.29, height=35, width=140)
        self.TEntry56.configure(takefocus="")

        self.Label57 = tk.Label(self.Frame5)
        self.Label57.place(relx=0.1, rely=0.4, height=26, width=133)
        self.Label57.configure(background="#d9d9d9")
        self.Label57.configure(disabledforeground="#a3a3a3")
        self.Label57.configure(foreground="#000000")
        self.Label57.configure(font=font8)
        self.Label57.configure(text='''Cost : ''')

        self.TEntry58 = ttk.Entry(self.Frame5)
        self.TEntry58.place(relx=0.5,rely=0.39, height=35, width=140)
        self.TEntry58.configure(takefocus="")

        self.Submit5 = tk.Button(self.Frame5, command = self.acceptIncome)
        self.Submit5.place(relx=0.580, rely=0.842, height=30, width=59)
        self.Submit5.configure(activebackground="#ececec")
        self.Submit5.configure(activeforeground="#000000")
        self.Submit5.configure(background="#d9d9d9")
        self.Submit5.configure(disabledforeground="#a3a3a3")
        self.Submit5.configure(foreground="#000000")
        self.Submit5.configure(highlightbackground="#d9d9d9")
        self.Submit5.configure(highlightcolor="black")
        self.Submit5.configure(pady="0")
        self.Submit5.configure(text='''SUBMIT''')

        self.Delete5 = tk.Button(self.Frame5, command = self.deleteIncome)
        self.Delete5.place(relx=0.580, rely=0.842, height=30, width=59)
        self.Delete5.configure(activebackground="#ececec")
        self.Delete5.configure(activeforeground="#000000")
        self.Delete5.configure(background="#d9d9d9")
        self.Delete5.configure(disabledforeground="#a3a3a3")
        self.Delete5.configure(foreground="#000000")
        self.Delete5.configure(highlightbackground="#d9d9d9")
        self.Delete5.configure(highlightcolor="black")
        self.Delete5.configure(pady="0")
        self.Delete5.configure(text='''DELETE''')

        self.Cancel5 = tk.Button(self.Frame5, command = lambda: self.cancel(self.Frame5))
        self.Cancel5.place(relx=0.320, rely=0.842, height=30, width=59)
        self.Cancel5.configure(activebackground="#ececec")
        self.Cancel5.configure(activeforeground="#000000")
        self.Cancel5.configure(background="#d9d9d9")
        self.Cancel5.configure(disabledforeground="#a3a3a3")
        self.Cancel5.configure(foreground="#000000")
        self.Cancel5.configure(highlightbackground="#d9d9d9")
        self.Cancel5.configure(highlightcolor="black")
        self.Cancel5.configure(pady="0")
        self.Cancel5.configure(text='''CANCEL''')

        popData = self.db.getLabourData()
        self.populateTree(self.tree2, popData)
        popData = self.db.getFeedData()
        self.populateTree(self.tree3, popData)
        popData = self.db.getMiscExpenditureData()
        self.populateTree(self.tree4, popData)
        popData = self.db.getIncomeData()
        self.populateTree(self.tree5, popData)
        popData = self.db.getLivestockNetworthData()
        self.populateTree(self.tree1, popData)       

        grand_total = (self.db.getTotalLabourCost() * 12) + (self.db.getTotalFeedCost()) + (self.db.getTotalMiscExpenditure()) 

        self.tree0.insert("", END, text="1", values=("Labour", self.db.getTotalLabourCost() * 12))
        self.tree0.insert("", END, text="2", values=("Feed", self.db.getTotalFeedCost()))
        self.tree0.insert("", END, text="3", values=("Miscellaneous Expense", self.db.getTotalMiscExpenditure()))

        self.TEntry02.delete(0, END)
        self.TEntry02.insert(END, grand_total)

    def showLivestock(self,flag):
        if flag:
            self.refresh()
        self.Label16.place_forget()
        self.Label14.place_forget()
        self.TEntry15.place_forget()
        self.Frame1.place(relx=0.615, rely=0.079, relheight=0.888, relwidth=0.365)
        self.TEntry13.delete(0, END)
        self.TEntry13.insert(END, self.db.getTotalLivestockNetworth())
        self.Frame2.place_forget()
        self.Frame3.place_forget()
        self.Frame4.place_forget()
        self.Frame5.place_forget()
        self.Frame6.place_forget()

    def showLabour(self,flag):
        if flag:
            self.refresh()
        self.tree2.selection_clear()
        self.TEntry23.delete(0,END)
        self.TEntry26.delete(0,END)
        self.TEntry28.delete(0,END)
        self.TEntry210.delete(0,END)
        self.Delete2.place_forget()
        self.DEntry2.place_forget()
        self.Frame2.place(relx=0.615, rely=0.079, relheight=0.888, relwidth=0.365)
        self.Label24.place(relx=0.35, rely=0.2, height=26, width=133)
        self.Submit2.place(relx=0.580, rely=0.842, height=30, width=59)
        self.TEntry23.delete(0, END)
        self.TEntry23.insert(END, self.db.getTotalLabourCost())
        self.Frame1.place_forget()
        self.Frame3.place_forget()
        self.Frame4.place_forget()
        self.Frame5.place_forget()
        self.Frame6.place_forget()

    def showFeed(self,flag):
        if flag:
            self.refresh()
        self.TEntry33.delete(0,END)
        self.TEntry36.delete(0,END)
        self.TEntry38.delete(0,END)
        self.TEntry310.delete(0,END)
        self.Delete3.place_forget()
        self.DEntry3.place_forget()
        self.Frame3.place(relx=0.615, rely=0.079, relheight=0.888, relwidth=0.365)
        self.Label34.place(relx=0.35, rely=0.2, height=26, width=133)
        self.Submit3.place(relx=0.580, rely=0.842, height=30, width=59)
        self.TEntry33.delete(0, END)
        self.TEntry33.insert(END, self.db.getTotalFeedCost())
        self.Frame1.place_forget()
        self.Frame2.place_forget()
        self.Frame4.place_forget()
        self.Frame5.place_forget()
        self.Frame6.place_forget()

    def showMisc(self,flag):
        if flag:
            self.refresh()
        self.TEntry43.delete(0,END)
        self.TEntry46.delete(0,END)
        self.TEntry48.delete(0,END)
        self.Delete4.place_forget()
        self.DEntry4.place_forget()
        self.Frame4.place(relx=0.615, rely=0.079, relheight=0.888, relwidth=0.365)
        self.Label44.place(relx=0.35, rely=0.2, height=26, width=133)
        self.Submit4.place(relx=0.580, rely=0.842, height=30, width=59)
        self.TEntry43.delete(0, END)
        self.TEntry43.insert(END, self.db.getTotalMiscExpenditure())
        self.Frame1.place_forget()
        self.Frame2.place_forget()
        self.Frame3.place_forget()
        self.Frame5.place_forget()
        self.Frame6.place_forget()

    def showIncome(self,flag):
        if flag:
            self.refresh()
        self.TEntry53.delete(0,END)
        self.TEntry56.delete(0,END)
        self.TEntry58.delete(0,END)
        self.Delete5.place_forget()
        self.DEntry5.place_forget()
        self.Frame5.place(relx=0.615, rely=0.079, relheight=0.888, relwidth=0.365)
        self.Label54.place(relx=0.35, rely=0.2, height=26, width=133)
        self.Submit5.place(relx=0.580, rely=0.842, height=30, width=59)
        self.TEntry53.delete(0, END)
        self.TEntry53.insert(END, self.db.getTotalIncome())
        self.Frame1.place_forget()
        self.Frame2.place_forget()
        self.Frame3.place_forget()
        self.Frame4.place_forget()
        self.Frame6.place_forget()

    def showTotal(self):
        self.Frame6.place(relx=0.615, rely=0.079, relheight=0.888, relwidth=0.365)
        self.Frame1.place_forget()
        self.Frame2.place_forget()
        self.Frame3.place_forget()
        self.Frame4.place_forget()
        self.Frame5.place_forget()

    def cancel(self, widget):
        widget.place_forget()
        self.refresh()

    def onselect(self, fwidget1, fwidget2, pwidget1, pwidget2):
        fwidget1.place_forget()
        fwidget2.place_forget()
        pwidget1.place(relx=0.35, rely=0.2, height=26, width=133)
        pwidget2.place(relx=0.580, rely=0.842, height=30, width=59)

    global data1 
    global data2 
    global data3 
    global data4 
    global data5

    def getLivestockData(self, event):
        self.showLivestock(0)
        self.Label16.place(relx=0.35, rely=0.24, height=26, width=133)
        self.Label14.place(relx=0.1, rely=0.33, height=26, width=133)
        self.TEntry15.place(relx=0.5,rely=0.32, height=35, width=140)
        data1 = self.tree1.item(self.tree1.selection())
        self.TEntry15.delete(0,END)
        self.TEntry15.insert(END, data1['values'][2])
        self.selectedLiveStockData = data1['values']
        print(self.selectedLiveStockData)

    def getLabourData(self, event):
        self.showLabour(0)
        self.onselect(self.Label24,self.Submit2,self.DEntry2, self.Delete2)
        data2 = self.tree2.item(self.tree2.selection())
        self.TEntry26.delete(0,END)
        self.TEntry28.delete(0,END)
        self.TEntry210.delete(0,END)
        self.TEntry26.insert(END,data2['values'][0])
        self.TEntry28.insert(END,data2['values'][1])
        self.TEntry210.insert(END,data2['values'][2])
        print(data2)

    def getFeedData(self, event):
        self.showFeed(0)
        self.onselect(self.Label34,self.Submit3,self.DEntry3, self.Delete3)
        data3 = self.tree3.item(self.tree3.selection())
        self.TEntry36.delete(0,END)
        self.TEntry38.delete(0,END)
        self.TEntry310.delete(0,END)
        self.TEntry36.insert(END,data3['values'][1])
        self.TEntry38.insert(END,data3['values'][2])
        self.TEntry310.insert(END,data3['values'][3])
        print(data3)

    def getMiscData(self, event):
        self.showMisc(0)
        self.onselect(self.Label44,self.Submit4,self.DEntry4, self.Delete4)
        data4 = self.tree4.item(self.tree4.selection())
        self.TEntry46.delete(0,END)
        self.TEntry48.delete(0,END)
        self.TEntry46.insert(END,data4['values'][1])
        self.TEntry48.insert(END,data4['values'][2])
        print(data4)

    def getIncomeData(self, event):
        self.showIncome(0)
        self.onselect(self.Label54,self.Submit5,self.DEntry5, self.Delete5)
        data5 = self.tree5.item(self.tree5.selection())
        self.TEntry56.delete(0,END)
        self.TEntry58.delete(0,END)
        self.TEntry56.insert(END,data5['values'][1])
        self.TEntry58.insert(END,data5['values'][2])
        print(data5)
    
    def clearTreeView(self, tree):
        for row in tree.get_children():
            tree.delete(row)

    def populateTree(self, tree, data):
        if data != None:
            for i in range(len(data)):
                tree.insert("", END, text=str(i+1), values=data[i])

    def refresh(self):
        # def refreshLiveStockTree(self):
        livestockNetworthData = self.db.getLivestockNetworthData()
        self.clearTreeView(self.tree1)
        self.populateTree(self.tree1, livestockNetworthData)

        # def refreshLabourTree(self):
        labourData = self.db.getLabourData()
        self.clearTreeView(self.tree2)
        self.populateTree(self.tree2, labourData)

        # def refreshFeedTree(self):
        feedData = self.db.getFeedData()
        self.clearTreeView(self.tree3)
        self.populateTree(self.tree3, feedData)

        # def refreshMiscTree(self):
        miscExpenseData = self.db.getMiscExpenditureData()
        self.clearTreeView(self.tree4)
        self.populateTree(self.tree4, miscExpenseData)

        # def refreshIncomeTree(self):
        incomeData = self.db.getIncomeData()
        self.clearTreeView(self.tree5)
        self.populateTree(self.tree5, incomeData)

        # def grandTotal
        grand_total = (self.db.getTotalLabourCost() * 12) + (self.db.getTotalFeedCost()) + (self.db.getTotalMiscExpenditure()) 

        self.clearTreeView(self.tree0)

        self.tree0.insert("", END, text="1", values=("Labour", self.db.getTotalLabourCost() * 12))
        self.tree0.insert("", END, text="2", values=("Feed", self.db.getTotalFeedCost()))
        self.tree0.insert("", END, text="3", values=("Miscellaneous Expense", self.db.getTotalMiscExpenditure()))

        self.TEntry02.delete(0, END)
        self.TEntry02.insert(END, grand_total)

    def acceptLabour(self):
        count = int(self.TEntry210.get())
        salary = int(self.TEntry28.get())
        category = self.TEntry26.get()

        labourData = {'count': count, 'category': category, 'salary': salary}

        self.db.insertLabour(labourData)

        print(labourData)
        print('Inserted into Labour Successfully')        

        self.refresh()

        self.Frame2.place_forget()

    def acceptFeed(self):
        item = self.TEntry36.get()
        cost = int(self.TEntry38.get())
        weight = int(self.TEntry310.get())

        feedData = {'item': item, 'cost': cost, 'weight': weight}

        self.db.insertFeed(feedData)

        print(feedData)
        print('Inserted into Feed successfully')

        # Update Total cost after submission
        self.TEntry33.delete(0, END)
        self.TEntry33.insert(END, self.db.getTotalFeedCost())

        # Update Treeview
        self.refresh()

        self.Frame3.place_forget()

    def acceptMiscExpense(self):
        category = self.TEntry46.get()
        cost = self.TEntry48.get()

        miscExpenseData = {'category': category, 'cost': cost}

        self.db.insertMiscExpenditure(miscExpenseData)

        print(miscExpenseData)
        print('Inserted into Misc Expense successfully')

        # Update Total cost after submission
        self.TEntry43.delete(0, END)
        self.TEntry43.insert(END, self.db.getTotalMiscExpenditure())

        # Update Treeview
        self.refresh()

        self.Frame4.place_forget()

    def acceptIncome(self):
        details = self.TEntry56.get()
        cost = self.TEntry58.get()

        incomeData = {'details': details, 'cost': cost}

        self.db.insertIncome(incomeData)

        print(incomeData)
        print('Inserted into Income successfully')

        # Update Total cost after submission
        self.TEntry53.delete(0, END)
        self.TEntry53.insert(END, self.db.getTotalIncome())

        # Update Treeview
        self.refresh()

        self.Frame5.place_forget()

    def acceptLivestockNetworth(self):
        cost = int(self.TEntry15.get())

        # print(self.selectedLiveStockData)

        livestockNetworthData = {'cost': cost, 'category': self.selectedLiveStockData[0], 'breed': self.selectedLiveStockData[1], 'total_weight': self.selectedLiveStockData[3]}

        self.db.insertLiveStockNetworth(livestockNetworthData)

        self.refresh()

    def deleteLabour(self):
        answer=messagebox.askokcancel("Delete","Do you want to delete the entry?")
        if(answer==True):
            data2 = self.tree2.item(self.tree2.selection())
            category = data2['values'][0]
            salary = data2['values'][1]
            count = data2['values'][2]
            labourData = {'count': count, 'category': category, 'salary': salary}
            self.db.deleteLabourRecord(labourData)
            self.refresh()
            self.Frame2.place_forget()
            w.deiconify()
        else:
            w.deiconify()

    def deleteFeed(self):
        answer1=messagebox.askokcancel("Delete","Do you want to delete the entry?")
        if(answer1==True):
            data3 = self.tree3.item(self.tree3.selection())
            purchase_date = data3['values'][0]
            item = data3['values'][1]
            weight = data3['values'][2]
            cost = data3['values'][3]
            feedData = {'purchase_date': purchase_date,'item': item, 'cost': cost, 'weight': weight}
            self.db.deleteFeedRecord(feedData)
            self.refresh()
            self.Frame3.place_forget()
            w.deiconify()
        else:
            w.deiconify()

    def deleteMisc(self):
        answer2=messagebox.askokcancel("Delete","Do you want to delete the entry?")
        if(answer2==True):
            data4 = self.tree4.item(self.tree4.selection())
            purchase_date = data4['values'][0]
            category = data4['values'][1]
            cost = data4['values'][2]
            miscExpenseData = {'purchase_date': purchase_date,'category': category, 'cost': cost}
            self.db.deleteMiscExpenditureRecord(miscExpenseData)
            self.refresh()
            self.Frame4.place_forget()
            w.deiconify()
        else:
                w.deiconify()

    def deleteIncome(self):
        answer3=messagebox.askokcancel("Delete","Do you want to delete the entry?")
        if(answer3==True):
            data5 = self.tree5.item(self.tree5.selection())
            purchase_date = data5['values'][0]
            details = data5['values'][1]
            cost = data5['values'][2]
            incomeData = {'purchase_date': purchase_date,'details': details, 'cost': cost}
            self.db.deleteIncomeRecord(incomeData)
            self.refresh()
            self.Frame5.place_forget()
            w.deiconify()
        else:
            w.deiconify()

    def genExcel(self):

        goatdata = self.db.getGoatRecords()
        goatdataColumns = self.db.getColumnNames()
        goatdf = pd.DataFrame(goatdata,columns=goatdataColumns)
        goatdf.name = 'Master Table'

        kiddata = self.db.getKidRecords()
        kiddataColumns = self.db.getKidColumnNames()
        kiddf = pd.DataFrame(kiddata, columns = kiddataColumns)
        kiddf.name = 'Mother-Kid Table'

        livestockdata = self.db.getLivestockRecords()
        livestockdataColumns = self.db.getLivestockColumnNames()
        livestockdf = pd.DataFrame(livestockdata, columns = livestockdataColumns)
        livestockdf.name = 'LiveStock Networth'

        labourdata = self.db.getLabourRecords()
        labourdataColumns = self.db.getLabourColumnNames()
        labourdf = pd.DataFrame(labourdata,columns= labourdataColumns)
        labourdf.name = 'Labour Salary'

        feeddata = self.db.getFeedRecords()
        feeddataColumns = self.db.getFeedColumnNames()
        feeddf = pd.DataFrame(feeddata,columns= feeddataColumns)
        feeddf.name = 'Feed'

        miscdata = self.db.getMiscRecords()
        miscdataColumns = self.db.getMiscColumnNames()
        miscdf = pd.DataFrame(miscdata,columns= miscdataColumns)
        miscdf.name = 'Miscellaneous Expenses'

        incomedata = self.db.getIncomeRecords()
        incomedataColumns = self.db.getIncomeColumnNames()
        incomedf = pd.DataFrame(incomedata,columns= incomedataColumns)
        incomedf.name = 'Income'

        writer = pd.ExcelWriter('./' + str(datetime.date(datetime.now())) + '.xlsx',engine='xlsxwriter')

        goatdf.to_excel(writer, sheet_name=goatdf.name)
        kiddf.to_excel(writer, sheet_name=kiddf.name)
        livestockdf.to_excel(writer, sheet_name=livestockdf.name)
        labourdf.to_excel(writer, sheet_name=labourdf.name)
        feeddf.to_excel(writer, sheet_name=feeddf.name)
        miscdf.to_excel(writer, sheet_name=miscdf.name)
        incomedf.to_excel(writer, sheet_name=incomedf.name)

        writer.save()
        self.showSuccess()

    def showSuccess(self):
        tk.messagebox.showinfo("Success","Successfully Generated")

