#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 5.0.2
#  in conjunction with Tcl version 8.6
#    Mar 06, 2020 10:26:54 AM IST  platform: Windows NT

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

import alerts_support
from backend import DataBase
from tkinter import END
import vaccination

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    top = Toplevel1 (root)
    alerts_support.init(root, top)
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
    alerts_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Toplevel1():
    global w
    w.destroy()
    w = None

class Toplevel1:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#78909C'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'
        font11 = "-family {Segoe UI} -size 20 -weight bold"
        font9 = "-family {Segoe UI} -size 11"
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.',background=_bgcolor)
        self.style.configure('.',foreground=_fgcolor)
        self.style.configure('.',font="TkDefaultFont")
        self.style.map('.',background=
            [('selected', _compcolor), ('active',_ana2color)])

        top.geometry("1300x760+20+20")
        top.minsize(800, 500)
        top.maxsize(1500, 750)
        top.resizable(0, 0)
        top.title("Alerts")
        top.configure(background="#78909C")

        self.Frame1 = tk.Frame(top)
        self.Frame1.place(relx=0.0, rely=-0.017, relheight=1.028, relwidth=1.008)
        self.Frame1.configure(relief='groove')
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief="groove")
        self.Frame1.configure(background="#78909C")

        self.Label1_5 = tk.Label(self.Frame1)
        self.Label1_5.place(relx=0.41, rely=0.014, height=51, width=193)
        self.Label1_5.configure(activebackground="#f9f9f9")
        self.Label1_5.configure(activeforeground="black")
        self.Label1_5.configure(background="#78909C")
        self.Label1_5.configure(disabledforeground="#a3a3a3")
        self.Label1_5.configure(font=font11)
        self.Label1_5.configure(foreground="#000000")
        self.Label1_5.configure(highlightbackground="#d9d9d9")
        self.Label1_5.configure(highlightcolor="black")
        self.Label1_5.configure(text='''ALERTS''')

        self.TSeparator1 = ttk.Separator(self.Frame1)
        self.TSeparator1.place(relx=0.788, rely=0.145, relheight=0.804)
        self.TSeparator1.configure(orient="vertical")

        self.Label2 = tk.Label(self.Frame1)
        self.Label2.place(relx=0.054, rely=0.09, height=41, width=136)
        self.Label2.configure(background="#78909C")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(font=font9)
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(text='''Anthrax''')

        self.Label1 = tk.Label(self.Frame1)
        self.Label1.place(relx=0.203, rely=0.09, height=53, width=234)
        self.Label1.configure(background="#78909C")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font="-family {Segoe UI} -size 10")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(text='''Haemorrhagic Septicemia''')

        self.Label1_5 = tk.Label(self.Frame1)
        self.Label1_5.place(relx=0.406, rely=0.09, height=50, width=234)
        self.Label1_5.configure(background="#78909C")
        self.Label1_5.configure(disabledforeground="#a3a3a3")
        self.Label1_5.configure(font=font9)
        self.Label1_5.configure(foreground="#000000")
        self.Label1_5.configure(text='''Enterotoxaemia''')

        self.Label1_5 = tk.Label(self.Frame1)
        self.Label1_5.place(relx=0.596, rely=0.09, height=50, width=234)
        self.Label1_5.configure(background="#78909C")
        self.Label1_5.configure(disabledforeground="#a3a3a3")
        self.Label1_5.configure(font=font9)
        self.Label1_5.configure(foreground="#000000")
        self.Label1_5.configure(text='''Black Quarter''')

        self.Label1_5 = tk.Label(self.Frame1)
        self.Label1_5.place(relx=0.02, rely=0.519, height=51, width=234)
        self.Label1_5.configure(activebackground="#f9f9f9")
        self.Label1_5.configure(activeforeground="black")
        self.Label1_5.configure(background="#78909C")
        self.Label1_5.configure(disabledforeground="#a3a3a3")
        self.Label1_5.configure(font=font9)
        self.Label1_5.configure(foreground="#000000")
        self.Label1_5.configure(highlightbackground="#d9d9d9")
        self.Label1_5.configure(highlightcolor="black")
        self.Label1_5.configure(text='''P.P.R''')

        self.Label1_5 = tk.Label(self.Frame1)
        self.Label1_5.place(relx=0.203, rely=0.519, height=51, width=234)
        self.Label1_5.configure(activebackground="#f9f9f9")
        self.Label1_5.configure(activeforeground="black")
        self.Label1_5.configure(background="#78909C")
        self.Label1_5.configure(disabledforeground="#a3a3a3")
        self.Label1_5.configure(font=font9)
        self.Label1_5.configure(foreground="#000000")
        self.Label1_5.configure(highlightbackground="#d9d9d9")
        self.Label1_5.configure(highlightcolor="black")
        self.Label1_5.configure(text='''Foot & mouth disease''')

        self.Label1_5 = tk.Label(self.Frame1)
        self.Label1_5.place(relx=0.406, rely=0.519, height=51, width=234)
        self.Label1_5.configure(activebackground="#f9f9f9")
        self.Label1_5.configure(activeforeground="black")
        self.Label1_5.configure(background="#78909C")
        self.Label1_5.configure(disabledforeground="#a3a3a3")
        self.Label1_5.configure(font=font9)
        self.Label1_5.configure(foreground="#000000")
        self.Label1_5.configure(highlightbackground="#d9d9d9")
        self.Label1_5.configure(highlightcolor="black")
        self.Label1_5.configure(text='''Goat Pox''')

        self.Label1_5 = tk.Label(self.Frame1)
        self.Label1_5.place(relx=0.596, rely=0.519, height=51, width=234)
        self.Label1_5.configure(activebackground="#f9f9f9")
        self.Label1_5.configure(activeforeground="black")
        self.Label1_5.configure(background="#78909C")
        self.Label1_5.configure(disabledforeground="#a3a3a3")
        self.Label1_5.configure(font=font9)
        self.Label1_5.configure(foreground="#000000")
        self.Label1_5.configure(highlightbackground="#d9d9d9")
        self.Label1_5.configure(highlightcolor="black")
        self.Label1_5.configure(text='''C.C.P.P''')

        self.Label1_5 = tk.Label(self.Frame1)
        self.Label1_5.place(relx=0.808, rely=0.09, height=51, width=234)
        self.Label1_5.configure(activebackground="#f9f9f9")
        self.Label1_5.configure(activeforeground="black")
        self.Label1_5.configure(background="#78909C")
        self.Label1_5.configure(disabledforeground="#a3a3a3")
        self.Label1_5.configure(font=font9)
        self.Label1_5.configure(foreground="#000000")
        self.Label1_5.configure(highlightbackground="#d9d9d9")
        self.Label1_5.configure(highlightcolor="black")
        self.Label1_5.configure(text='''DATE OF DELIVERY''')

        self.Label1_5 = tk.Label(self.Frame1)
        self.Label1_5.place(relx=0.808, rely=0.519, height=51, width=234)
        self.Label1_5.configure(activebackground="#f9f9f9")
        self.Label1_5.configure(activeforeground="black")
        self.Label1_5.configure(background="#78909C")
        self.Label1_5.configure(disabledforeground="#a3a3a3")
        self.Label1_5.configure(font=font9)
        self.Label1_5.configure(foreground="#000000")
        self.Label1_5.configure(highlightbackground="#d9d9d9")
        self.Label1_5.configure(highlightcolor="black")
        self.Label1_5.configure(text='''BREED READY''')

        #vacc 1
        self.tree1 = ttk.Treeview(self.Frame1)
        self.tree1["columns"] = ("#0", "#1", "#2")
        self.tree1.column("#0", width=0)
        self.tree1.column("#1", width=60, anchor='center')
        self.tree1.column("#2", width=120, anchor='center')
        self.tree1.heading("#1", text="GOAT ID")
        self.tree1.heading("#2", text="NEXT VACCINATION")
        self.tree1.place(relx=0.035, rely=0.15, relheight=0.376, relwidth=0.157)

        #vacc 2
        self.tree2 = ttk.Treeview(top)
        self.tree2["columns"] = ("#0", "#1", "#2")
        self.tree2.column("#0", width=0)
        self.tree2.column("#1", width=60, anchor='center')
        self.tree2.column("#2", width=120, anchor='center')
        self.tree2.heading("#1", text="GOAT ID")
        self.tree2.heading("#2", text="NEXT VACCINATION")
        self.tree2.place(relx=0.23, rely=0.14, relheight=0.383, relwidth=0.157)

        #vacc 3
        self.tree3 = ttk.Treeview(top)
        self.tree3["columns"] = ("#0", "#1", "#2")
        self.tree3.column("#0", width=0)
        self.tree3.column("#1", width=60, anchor='center')
        self.tree3.column("#2", width=120, anchor='center')
        self.tree3.heading("#1", text="GOAT ID")
        self.tree3.heading("#2", text="NEXT VACCINATION")
        self.tree3.place(relx=0.42, rely=0.14, relheight=0.383, relwidth=0.157)

        #vacc 4
        self.tree31 = ttk.Treeview(top)
        self.tree31["columns"] = ("#0", "#1", "#2")
        self.tree31.column("#0", width=0)
        self.tree31.column("#1", width=60, anchor='center')
        self.tree31.column("#2", width=120, anchor='center')
        self.tree31.heading("#1", text="GOAT ID")
        self.tree31.heading("#2", text="NEXT VACCINATION")
        self.tree31.place(relx=0.61, rely=0.14, relheight=0.384, relwidth=0.157)

        #vacc 5
        self.tree4 = ttk.Treeview(top)
        self.tree4["columns"] = ("#0", "#1", "#2")
        self.tree4.column("#0", width=0)
        self.tree4.column("#1", width=60, anchor='center')
        self.tree4.column("#2", width=120, anchor='center')
        self.tree4.heading("#1", text="GOAT ID")
        self.tree4.heading("#2", text="NEXT VACCINATION")
        self.tree4.place(relx=0.035, rely=0.573, relheight=0.384, relwidth=0.158)

        #vacc 6
        self.tree5 = ttk.Treeview(top)
        self.tree5["columns"] = ("#0", "#1", "#2")
        self.tree5.column("#0", width=0)
        self.tree5.column("#1", width=60, anchor='center')
        self.tree5.column("#2", width=120, anchor='center')
        self.tree5.heading("#1", text="GOAT ID")
        self.tree5.heading("#2", text="NEXT VACCINATION")
        self.tree5.place(relx=0.23, rely=0.573, relheight=0.384, relwidth=0.157)

        #vacc 7
        self.tree6 = ttk.Treeview(top)
        self.tree6["columns"] = ("#0", "#1", "#2")
        self.tree6.column("#0", width=0)
        self.tree6.column("#1", width=60, anchor='center')
        self.tree6.column("#2", width=120, anchor='center')
        self.tree6.heading("#1", text="GOAT ID")
        self.tree6.heading("#2", text="NEXT VACCINATION")
        self.tree6.place(relx=0.42, rely=0.573, relheight=0.384, relwidth=0.157)

        #vacc 8
        self.tree61 = ttk.Treeview(top)
        self.tree61["columns"] = ("#0", "#1", "#2")
        self.tree61.column("#0", width=0)
        self.tree61.column("#1", width=60, anchor='center')
        self.tree61.column("#2", width=120, anchor='center')
        self.tree61.heading("#1", text="GOAT ID")
        self.tree61.heading("#2", text="NEXT VACCINATION")
        self.tree61.place(relx=0.61, rely=0.573, relheight=0.384, relwidth=0.157)

        self.tree7 = ttk.Treeview(top)
        self.tree7["columns"] = ("#0", "#1", "#2")
        self.tree7.column("#0", width=0)
        self.tree7.column("#1", width=80, anchor='center')
        self.tree7.column("#2", width=100, anchor='center')
        self.tree7.heading("#1", text="MOTHER  ID")
        self.tree7.heading("#2", text="EXPECTED DATE")
        self.tree7.place(relx=0.820, rely=0.14, relheight=0.383, relwidth=0.157)

        self.tree8 = ttk.Treeview(top)
        self.tree8["columns"] = ("#0", "#1", "#2")
        self.tree8.column("#0", width=0)
        self.tree8.column("#1", width=90, anchor='center')
        self.tree8.column("#2", width=90, anchor='center')
        self.tree8.heading("#1", text="MOTHER  ID")
        self.tree8.heading("#2", text="BREED")
        self.tree8.place(relx=0.820, rely=0.573, relheight=0.384, relwidth=0.157)

        self.Button1 = tk.Button(top)
        self.Button1.place(relx=0.16, rely=0.09, height=30, width=40)
        self.Button1.configure(activebackground="#ececec")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#d9d9d9")
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(font=font9)
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''Done''')
        self.Button1.configure(command=lambda: self.setVaccinated(1))

        self.Button2 = tk.Button(top)
        self.Button2.place(relx=0.355, rely=0.09, height=30, width=40)
        self.Button2.configure(activebackground="#ececec")
        self.Button2.configure(activeforeground="#000000")
        self.Button2.configure(background="#d9d9d9")
        self.Button2.configure(disabledforeground="#a3a3a3")
        self.Button2.configure(font=font9)
        self.Button2.configure(foreground="#000000")
        self.Button2.configure(highlightbackground="#d9d9d9")
        self.Button2.configure(highlightcolor="black")
        self.Button2.configure(pady="0")
        self.Button2.configure(text='''Done''')
        self.Button2.configure(command=lambda: self.setVaccinated(2))

        self.Button3 = tk.Button(top)
        self.Button3.place(relx=0.545, rely=0.09, height=30, width=40)
        self.Button3.configure(activebackground="#ececec")
        self.Button3.configure(activeforeground="#000000")
        self.Button3.configure(background="#d9d9d9")
        self.Button3.configure(disabledforeground="#a3a3a3")
        self.Button3.configure(font=font9)
        self.Button3.configure(foreground="#000000")
        self.Button3.configure(highlightbackground="#d9d9d9")
        self.Button3.configure(highlightcolor="black")
        self.Button3.configure(pady="0")
        self.Button3.configure(text='''Done''')
        self.Button3.configure(command=lambda: self.setVaccinated(3))

        self.Button4 = tk.Button(top)
        self.Button4.place(relx=0.737, rely=0.09, height=30, width=40)
        self.Button4.configure(activebackground="#ececec")
        self.Button4.configure(activeforeground="#000000")
        self.Button4.configure(background="#d9d9d9")
        self.Button4.configure(disabledforeground="#a3a3a3")
        self.Button4.configure(font=font9)
        self.Button4.configure(foreground="#000000")
        self.Button4.configure(highlightbackground="#d9d9d9")
        self.Button4.configure(highlightcolor="black")
        self.Button4.configure(pady="0")
        self.Button4.configure(text='''Done''')
        self.Button4.configure(command=lambda: self.setVaccinated(4))

        self.Button5 = tk.Button(top)
        self.Button5.place(relx=0.16, rely=0.53, height=30, width=40)
        self.Button5.configure(activebackground="#ececec")
        self.Button5.configure(activeforeground="#000000")
        self.Button5.configure(background="#d9d9d9")
        self.Button5.configure(disabledforeground="#a3a3a3")
        self.Button5.configure(font=font9)
        self.Button5.configure(foreground="#000000")
        self.Button5.configure(highlightbackground="#d9d9d9")
        self.Button5.configure(highlightcolor="black")
        self.Button5.configure(pady="0")
        self.Button5.configure(text='''Done''')
        self.Button5.configure(command=lambda: self.setVaccinated(5))

        self.Button6 = tk.Button(top)
        self.Button6.place(relx=0.355, rely=0.53, height=30, width=40)
        self.Button6.configure(activebackground="#ececec")
        self.Button6.configure(activeforeground="#000000")
        self.Button6.configure(background="#d9d9d9")
        self.Button6.configure(disabledforeground="#a3a3a3")
        self.Button6.configure(font=font9)
        self.Button6.configure(foreground="#000000")
        self.Button6.configure(highlightbackground="#d9d9d9")
        self.Button6.configure(highlightcolor="black")
        self.Button6.configure(pady="0")
        self.Button6.configure(text='''Done''')
        self.Button6.configure(command=lambda: self.setVaccinated(6))

        self.Button7 = tk.Button(top)
        self.Button7.place(relx=0.545, rely=0.53, height=30, width=40)
        self.Button7.configure(activebackground="#ececec")
        self.Button7.configure(activeforeground="#000000")
        self.Button7.configure(background="#d9d9d9")
        self.Button7.configure(disabledforeground="#a3a3a3")
        self.Button7.configure(font=font9)
        self.Button7.configure(foreground="#000000")
        self.Button7.configure(highlightbackground="#d9d9d9")
        self.Button7.configure(highlightcolor="black")
        self.Button7.configure(pady="0")
        self.Button7.configure(text='''Done''')
        self.Button7.configure(command=lambda: self.setVaccinated(7))

        self.Button8 = tk.Button(top)
        self.Button8.place(relx=0.737, rely=0.53, height=30, width=40)
        self.Button8.configure(activebackground="#ececec")
        self.Button8.configure(activeforeground="#000000")
        self.Button8.configure(background="#d9d9d9")
        self.Button8.configure(disabledforeground="#a3a3a3")
        self.Button8.configure(font=font9)
        self.Button8.configure(foreground="#000000")
        self.Button8.configure(highlightbackground="#d9d9d9")
        self.Button8.configure(highlightcolor="black")
        self.Button8.configure(pady="0")
        self.Button8.configure(text='''Done''')
        self.Button8.configure(command=lambda: self.setVaccinated(8))

        self.vButton = tk.Button(top)
        self.vButton.place(relx=0.837, rely=0.001, height=50, width=170)
        self.vButton.configure(activebackground="#ececec")
        self.vButton.configure(activeforeground="#000000")
        self.vButton.configure(background="#d9d9d9")
        self.vButton.configure(disabledforeground="#a3a3a3")
        self.vButton.configure(font=font9)
        self.vButton.configure(foreground="#000000")
        self.vButton.configure(highlightbackground="#d9d9d9")
        self.vButton.configure(highlightcolor="black")
        self.vButton.configure(pady="0")
        self.vButton.configure(text='''Vaccination Reference''')
        self.vButton.configure(command = lambda: vaccination.create_Toplevel1(root))

        self.db = DataBase()

        self.v1data = self.db.getGoatsToBeVaccinated(1)
        self.v2data = self.db.getGoatsToBeVaccinated(2)
        self.v3data = self.db.getGoatsToBeVaccinated(3)
        self.v4data = self.db.getGoatsToBeVaccinated(4)
        self.v5data = self.db.getGoatsToBeVaccinated(5)
        self.v6data = self.db.getGoatsToBeVaccinated(6)
        self.v7data = self.db.getGoatsToBeVaccinated(7)
        self.v8data = self.db.getGoatsToBeVaccinated(8)

        self.deliveryDates = self.db.getDeliveryDates()

        self.breedReadyGoats = self.db.getBreedReadyGoats()

        if self.v1data != None:
            for i in range(len(self.v1data)):
                self.tree1.insert("", END, text="", values=self.v1data[i])
        if self.v2data != None:
            for i in range(len(self.v2data)):
                self.tree2.insert("", END, text="", values=self.v2data[i])
        if self.v3data != None:
            for i in range(len(self.v3data)):
                self.tree3.insert("", END, text="", values=self.v3data[i])
        if self.v4data != None:
            for i in range(len(self.v4data)):
                self.tree31.insert("", END, text="", values=self.v4data[i])
        if self.v5data != None:
            for i in range(len(self.v5data)):
                self.tree4.insert("", END, text="", values=self.v5data[i])
        if self.v6data != None:
            for i in range(len(self.v6data)):
                self.tree5.insert("", END, text="", values=self.v6data[i])
        if self.v7data != None:
            for i in range(len(self.v7data)):
                self.tree6.insert("", END, text="", values=self.v7data[i])
        if self.v8data != None:
            for i in range(len(self.v8data)):
                self.tree61.insert("", END, text="", values=self.v8data[i])
        if self.deliveryDates != None:
            for i in range(len(self.deliveryDates)):
                self.tree7.insert("", END, text="", values=self.deliveryDates[i])
        if self.breedReadyGoats != None:
            for i in range(len(self.breedReadyGoats)):
                self.tree8.insert("", END, text="", values=self.breedReadyGoats[i])

    def setVaccinated(self, vacc_no):
        self.db.vaccinateGoats(vacc_no)

# The following code is added to facilitate the Scrolled widgets you specified.
class AutoScroll(object):
    '''Configure the scrollbars for a widget.'''
    def __init__(self, master):
        #  Rozen. Added the try-except clauses so that this class
        #  could be used for scrolled entry widget for which vertical
        #  scrolling is not supported. 5/7/14.
        try:
            vsb = ttk.Scrollbar(master, orient='vertical', command=self.yview)
        except:
            pass
        hsb = ttk.Scrollbar(master, orient='horizontal', command=self.xview)
        try:
            self.configure(yscrollcommand=self._autoscroll(vsb))
        except:
            pass
        self.configure(xscrollcommand=self._autoscroll(hsb))
        self.grid(column=0, row=0, sticky='nsew')
        try:
            vsb.grid(column=1, row=0, sticky='ns')
        except:
            pass
        hsb.grid(column=0, row=1, sticky='ew')
        master.grid_columnconfigure(0, weight=1)
        master.grid_rowconfigure(0, weight=1)
        # Copy geometry methods of master  (taken from ScrolledText.py)
        if py3:
            methods = tk.Pack.__dict__.keys() | tk.Grid.__dict__.keys() \
                  | tk.Place.__dict__.keys()
        else:
            methods = tk.Pack.__dict__.keys() + tk.Grid.__dict__.keys() \
                  + tk.Place.__dict__.keys()
        for meth in methods:
            if meth[0] != '_' and meth not in ('config', 'configure'):
                setattr(self, meth, getattr(master, meth))

    @staticmethod
    def _autoscroll(sbar):
        '''Hide and show scrollbar as needed.'''
        def wrapped(first, last):
            first, last = float(first), float(last)
            if first <= 0 and last >= 1:
                sbar.grid_remove()
            else:
                sbar.grid()
            sbar.set(first, last)
        return wrapped

    def __str__(self):
        return str(self.master)

def _create_container(func):
    '''Creates a ttk Frame with a given master, and use this new frame to
    place the scrollbars and the widget.'''
    def wrapped(cls, master, **kw):
        container = ttk.Frame(master)
        container.bind('<Enter>', lambda e: _bound_to_mousewheel(e, container))
        container.bind('<Leave>', lambda e: _unbound_to_mousewheel(e, container))
        return func(cls, container, **kw)
    return wrapped

class ScrolledListBox(AutoScroll, tk.Listbox):
    '''A standard Tkinter Listbox widget with scrollbars that will
    automatically show/hide as needed.'''
    @_create_container
    def __init__(self, master, **kw):
        tk.Listbox.__init__(self, master, **kw)
        AutoScroll.__init__(self, master)
    def size_(self):
        sz = tk.Listbox.size(self)
        return sz

import platform
def _bound_to_mousewheel(event, widget):
    child = widget.winfo_children()[0]
    if platform.system() == 'Windows' or platform.system() == 'Darwin':
        child.bind_all('<MouseWheel>', lambda e: _on_mousewheel(e, child))
        child.bind_all('<Shift-MouseWheel>', lambda e: _on_shiftmouse(e, child))
    else:
        child.bind_all('<Button-4>', lambda e: _on_mousewheel(e, child))
        child.bind_all('<Button-5>', lambda e: _on_mousewheel(e, child))
        child.bind_all('<Shift-Button-4>', lambda e: _on_shiftmouse(e, child))
        child.bind_all('<Shift-Button-5>', lambda e: _on_shiftmouse(e, child))

def _unbound_to_mousewheel(event, widget):
    if platform.system() == 'Windows' or platform.system() == 'Darwin':
        widget.unbind_all('<MouseWheel>')
        widget.unbind_all('<Shift-MouseWheel>')
    else:
        widget.unbind_all('<Button-4>')
        widget.unbind_all('<Button-5>')
        widget.unbind_all('<Shift-Button-4>')
        widget.unbind_all('<Shift-Button-5>')

def _on_mousewheel(event, widget):
    if platform.system() == 'Windows':
        widget.yview_scroll(-1*int(event.delta/120),'units')
    elif platform.system() == 'Darwin':
        widget.yview_scroll(-1*int(event.delta),'units')
    else:
        if event.num == 4:
            widget.yview_scroll(-1, 'units')
        elif event.num == 5:
            widget.yview_scroll(1, 'units')

def _on_shiftmouse(event, widget):
    if platform.system() == 'Windows':
        widget.xview_scroll(-1*int(event.delta/120), 'units')
    elif platform.system() == 'Darwin':
        widget.xview_scroll(-1*int(event.delta), 'units')
    else:
        if event.num == 4:
            widget.xview_scroll(-1, 'units')
        elif event.num == 5:
            widget.xview_scroll(1, 'units')

if __name__ == '__main__':
    vp_start_gui()





