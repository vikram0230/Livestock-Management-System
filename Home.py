import sys
import os.path
import numpy as np
from matplotlib.figure import Figure
import matplotlib.animation as ani
from pandas import DataFrame
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from PIL import ImageTk, Image
import graph_backend as graph
import pandas as pd
import numpy as np
from datetime import datetime, date
from tkinter import *
from tkinter import PhotoImage, Label

from MasterChart import displayMasterChart
import addGoat
import alerts
import Finance

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

import Home_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    global prog_location
    prog_call = sys.argv[0]
    prog_location = os.path.split(prog_call)[0]
    top = Toplevel1 (root)
    Home_support.init(root, top)
    root.mainloop()

w = None
def create_Toplevel1(rt, *args, **kwargs):
    '''Starting point when module is imported by another module.
       Correct form of call: 'create_Toplevel1(root, *args, **kwargs)' .'''
    global w, w_win, root
    #rt = root
    root = rt
    global prog_location
    prog_call = sys.argv[0]
    prog_location = os.path.split(prog_call)[0]
    w = tk.Toplevel (root)
    top = Toplevel1 (w)
    Home_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Toplevel1():
    global w
    w.destroy()
    w = None

class Toplevel1:
    def __init__(self, top=None):

        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'

        top.geometry("1300x760+20+20")
        top.minsize(800, 500)
        top.maxsize(1800, 850)
        top.resizable(1, 1)
        top.title("Home")
        top.configure(background="#f3f3f3")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="#090000")

        self.Label1 = tk.Label(top)
        self.Label1.place(relx=0.1, rely=0.005, height=400, width=644)
        self.Label1.configure(background="#d9d9d9")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(foreground="#000000")
        photo_location = os.path.join(prog_location,"boer.jpg")
        global _img0
        _img0 = ImageTk.PhotoImage(file=photo_location)
        self.Label1.configure(image=_img0)
        self.Label1.configure(text='''Label''')

        self.frame1 = tk.Frame(top)
        self.frame1.place(relx=0.01, rely=0.01, relheight=0.095, relwidth=0.075)
        self.frame1.configure(relief='groove')
        self.frame1.configure(borderwidth="2")
        self.frame1.configure(relief="groove")
        self.frame1.configure(background="#d9d9d9")

        self.Label1_5 = tk.Label(self.frame1)

        self.Label1_6 = tk.Label(self.frame1)

        self.Button2_2 = tk.Button(top, command=self.openMasterChart)
        self.Button2_2.place(relx=0.792, rely=0.021, height=54, width=215)
        self.Button2_2.configure(activebackground="#ececec")
        self.Button2_2.configure(activeforeground="#000000")
        self.Button2_2.configure(background="#d9d9d9")
        self.Button2_2.configure(disabledforeground="#a3a3a3")
        self.Button2_2.configure(font="-family {Segoe UI} -size 14")
        self.Button2_2.configure(foreground="#000000")
        self.Button2_2.configure(highlightbackground="#d9d9d9")
        self.Button2_2.configure(highlightcolor="black")
        self.Button2_2.configure(pady="0")
        self.Button2_2.configure(text='''Master Database''')

        self.Button2 = tk.Button(top,command = lambda: Finance.create_Toplevel1(root))
        self.Button2.place(relx=0.792, rely=0.131, height=53, width=215)
        self.Button2.configure(activebackground="#ececec")
        self.Button2.configure(activeforeground="#000000")
        self.Button2.configure(background="#d9d9d9")
        self.Button2.configure(disabledforeground="#a3a3a3")
        self.Button2.configure(font="-family {Segoe UI} -size 14")
        self.Button2.configure(foreground="#000000")
        self.Button2.configure(highlightbackground="#d9d9d9")
        self.Button2.configure(highlightcolor="black")
        self.Button2.configure(pady="0")
        self.Button2.configure(text='''Finance''')

        self.Button3 = tk.Button(top, command= lambda: addGoat.create_Toplevel1(root))
        self.Button3.place(relx=0.792, rely=0.241, height=53, width=215)
        self.Button3.configure(activebackground="#ececec")
        self.Button3.configure(activeforeground="#000000")
        self.Button3.configure(background="#d9d9d9")
        self.Button3.configure(disabledforeground="#a3a3a3")
        self.Button3.configure(font="-family {Segoe UI} -size 14")
        self.Button3.configure(foreground="#000000")
        self.Button3.configure(highlightbackground="#d9d9d9")
        self.Button3.configure(highlightcolor="black")
        self.Button3.configure(pady="0")
        self.Button3.configure(text='''Add Goat''')

        self.Button2_3 = tk.Button(top,command=lambda: alerts.create_Toplevel1(root))
        self.Button2_3.place(relx=0.792, rely=0.351, height=70, width=215)
        self.Button2_3.configure(activebackground="#ececec")
        self.Button2_3.configure(activeforeground="#000000")
        self.Button2_3.configure(background="#d9d9d9")
        self.Button2_3.configure(disabledforeground="#a3a3a3")
        self.Button2_3.configure(font="-family {Segoe UI} -size 14")
        self.Button2_3.configure(foreground="#000000")
        self.Button2_3.configure(highlightbackground="#d9d9d9")
        self.Button2_3.configure(highlightcolor="black")
        self.Button2_3.configure(pady="0")
        self.Button2_3.configure(text='''Alerts''')

        self.Button4 = tk.Button(top,command= self.refresh)
        self.Button4.place(relx=0.842, rely=0.471, height=50, width=150)
        self.Button4.configure(activebackground="#ececec")
        self.Button4.configure(activeforeground="#000000")
        self.Button4.configure(background="#d9d9d9")
        self.Button4.configure(disabledforeground="#a3a3a3")
        self.Button4.configure(font="-family {Segoe UI} -size 14")
        self.Button4.configure(foreground="#000000")
        self.Button4.configure(highlightbackground="#d9d9d9")
        self.Button4.configure(highlightcolor="black")
        self.Button4.configure(pady="0")
        self.Button4.configure(text='''Refresh Graph''')        

        self.figure1 = plt.Figure(figsize=(5,5), dpi=60)
        self.figure2 = plt.Figure(figsize=(5,5), dpi=60)
        self.figure3 = plt.Figure(figsize=(5, 5), dpi=60)
        self.figure4 = plt.Figure(figsize=(6,6), dpi=50)

        self.plot()

    global prof_loss
        
    def plot(self):
        self.figure1.clear() 
        self.figure2.clear()
        self.figure3.clear()
        self.figure4.clear()
        self.Label1_5['text']=""
        self.Label1_6['text']=""


        breed, gender, maleKidCount, femaleKidCount, maleDeadCount, femaleDeadCount, income, expense= graph.getData()

        prof_loss = income-expense

        # Current Holding
        data1 = {'breed':breed,'gender':gender}
        cur_holding = DataFrame(data1,columns=['breed','gender'])

        ax1 = self.figure1.add_subplot(111)
        bar1 = FigureCanvasTkAgg(self.figure1, root)
        bar1.get_tk_widget().place(x=20,y=430)
        df1 = cur_holding[['breed','gender']]
        pd.crosstab(cur_holding.breed,cur_holding.gender).plot(kind='bar', ax=ax1, fontsize=12)
        ax1.set_title('Current Holding')
        ax1.set_xlabel('Breed')
        ax1.set_ylabel('Count')
        ax1.tick_params(axis ='x', rotation = 0)

        # Birth Rate
        values2 = [maleKidCount, femaleKidCount]
        label2 = 'Male:' + str(maleKidCount),'Female:' + str(femaleKidCount)
        colors = ['lightcoral', 'lightskyblue']

        ax2 = self.figure2.add_subplot(111)
        ax2.pie(values2, labels=label2, colors=colors)
        pie2 =  FigureCanvasTkAgg(self.figure2, root) 
        pie2.get_tk_widget().place(x=340,y=430)
        ax2.legend()
        ax2.set_title('Birth Rate')

        # Death Rate        
        values3 = [maleDeadCount, femaleDeadCount]
        labels3 = 'Male:' + str(maleDeadCount),'Female:' + str(femaleDeadCount)

        ax3 = self.figure3.add_subplot(111)
        ax3.pie(values3, labels=labels3, colors=colors)
        pie3 =  FigureCanvasTkAgg(self.figure3, root)
        pie3.get_tk_widget().place(x=660,y=430)
        ax3.legend()
        ax3.set_title('Death Rate')

        # Income Vs Expense
        data4 = {'Finance':['Income','Expense'],
              'Amount':[income,expense]}
        df4 = DataFrame(data4,columns=['Finance','Amount'])

        ax4 = self.figure4.add_subplot(111)
        bar4 = FigureCanvasTkAgg(self.figure4, root)
        bar4.get_tk_widget().place(x=980,y=430)
        df4 = df4[['Finance','Amount']]
        df4.plot(kind='bar', legend=True, ax=ax4, color='lightskyblue', fontsize=12)
        ax4.set_title('Income Vs Expense') 
        ax4.set_xlabel('Income                      Expense',fontsize = 14)

        self.Label1_5.configure(background="#d9d9d9")
        self.Label1_5.configure(foreground="#13C41F")
        self.Label1_5.configure(disabledforeground="#a3a3a3")
        self.Label1_5.configure(font="-family {Segoe UI} -size 15 -weight bold")
        # self.Label1_5.configure(text='''Profit''')
        self.Label1_5.grid(row=0, column=0, padx=10)
        self.Label1_5['text']=prof_loss

        self.Label1_6.configure(background="#d9d9d9")
        self.Label1_6.configure(font="-family {Segoe UI} -size 12 ")
        self.Label1_6.configure(foreground="#F80000")
        # self.Label1_6.configure(text='''PROFIT''')
        self.Label1_6.grid(row=1, column=0, padx=10, sticky='s')

        if prof_loss>0:
            self.Label1_6['text']='    PROFIT'
            self.Label1_5.configure(foreground="#13C41F")
            self.Label1_6.configure(foreground="#13C41F")

        else: 
            self.Label1_6['text']='     LOSS'
            self.Label1_5.configure(foreground="#F80000")
            self.Label1_6.configure(foreground="#F80000")

    def refresh(self):
        self.plot()
                     
    def openMasterChart(self):
        displayMasterChart()

    
        
if __name__ == '__main__':
    vp_start_gui()





