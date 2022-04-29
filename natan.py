#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 6.2
#  in conjunction with Tcl version 8.6
#    Apr 28, 2022 02:42:13 PM +0300  platform: Windows NT
# maxdate ------------ CALENDAR MAX DATE
from datetime import datetime
from faulthandler import disable
import sys
from tkinter import HORIZONTAL
from click import progressbar
from tkcalendar import Calendar,DateEntry
import re
import log_scan

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

import natan_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    natan_support.set_Tk_var()
    log_scan.init_progress()
    top = Toplevel1 (root)
    natan_support.init(root, top)
    log_scan.init(root,top)
    
    root.mainloop()

w = None
def create_Toplevel1(rt, *args, **kwargs):
    '''Starting point when module is imported by another module.
       Correct form of call: 'create_Toplevel1(root, *args, **kwargs)' .'''
    global w, w_win, root
    #rt = root
    root = rt
    w = tk.Toplevel (root)
    natan_support.set_Tk_var()
    top = Toplevel1 (w)
    natan_support.init(w, top, *args, **kwargs)
    log_scan.init(w,top,*args,**kwargs)
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
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.',background=_bgcolor)
        self.style.configure('.',foreground=_fgcolor)
        self.style.configure('.',font="TkDefaultFont")
        self.style.map('.',background=
            [('selected', _compcolor), ('active',_ana2color)])

        top.geometry("275x364")
        #top.minsize(120, 1)
        #top.maxsize(5764, 1061)
        top.resizable(0,  0)
        top.title("Log-Scanner")
        top.configure(background="#d9d9d9")

        today = str(datetime.today())
        today_date = re.findall(r'\d\d\d\d-\d\d-\d\d',today).pop().split('-')
        print(f"today: {today_date}")
        cal = DateEntry(top,selectmode = 'day',year = int(today_date[0]), month = int(today_date[1]), day = int(today_date[2]), textvariable = natan_support.selected_date)
        cal.place(relx=0.320, rely=0.121)

        self.Label1 = tk.Label(top)
        self.Label1.place(relx=0.100, rely=0.270, height=13, width=61)
        self.Label1.configure(background="#d9d9d9")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(text='''Start Time''')

        self.Entry1 = tk.Entry(top)
        self.Entry1.place(relx=0.35, rely=0.265, height=20, width=32)
        self.Entry1.configure(background="white")
        self.Entry1.configure(disabledforeground="#a3a3a3")
        self.Entry1.configure(font="TkFixedFont")
        self.Entry1.configure(foreground="#000000")
        self.Entry1.configure(insertbackground="black")
        self.Entry1.configure(textvariable=natan_support.start_hour)


        self.Label2 = tk.Label(top)
        self.Label2.place(relx=0.48, rely=0.265, height=13, width=10)
        self.Label2.configure(background="#d9d9d9")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(text=''':''')

        self.Entry2 = tk.Entry(top)
        self.Entry2.place(relx=0.52, rely=0.265, height=20, width=32)
        self.Entry2.configure(background="white")
        self.Entry2.configure(disabledforeground="#a3a3a3")
        self.Entry2.configure(font="TkFixedFont")
        self.Entry2.configure(foreground="#000000")
        self.Entry2.configure(insertbackground="black")
        self.Entry2.configure(textvariable=natan_support.start_minute)

        self.Label1_1 = tk.Label(top)
        self.Label1_1.place(relx=0.100, rely=0.380, height=13, width=61)
        self.Label1_1.configure(activebackground="#f9f9f9")
        self.Label1_1.configure(activeforeground="black")
        self.Label1_1.configure(background="#d9d9d9")
        self.Label1_1.configure(disabledforeground="#a3a3a3")
        self.Label1_1.configure(foreground="#000000")
        self.Label1_1.configure(highlightbackground="#d9d9d9")
        self.Label1_1.configure(highlightcolor="black")
        self.Label1_1.configure(text='''End Time''')

        self.Entry1_1 = tk.Entry(top)
        self.Entry1_1.place(relx=0.35, rely=0.375, height=20, width=32)
        self.Entry1_1.configure(background="white")
        self.Entry1_1.configure(disabledforeground="#a3a3a3")
        self.Entry1_1.configure(font="TkFixedFont")
        self.Entry1_1.configure(foreground="#000000")
        self.Entry1_1.configure(highlightbackground="#d9d9d9")
        self.Entry1_1.configure(highlightcolor="black")
        self.Entry1_1.configure(insertbackground="black")
        self.Entry1_1.configure(selectbackground="blue")
        self.Entry1_1.configure(selectforeground="white")
        self.Entry1_1.configure(textvariable=natan_support.end_hour)

        self.Label2_1 = tk.Label(top)
        self.Label2_1.place(relx=0.48, rely=0.375, height=13, width=10)
        self.Label2_1.configure(activebackground="#f9f9f9")
        self.Label2_1.configure(activeforeground="black")
        self.Label2_1.configure(background="#d9d9d9")
        self.Label2_1.configure(disabledforeground="#a3a3a3")
        self.Label2_1.configure(foreground="#000000")
        self.Label2_1.configure(highlightbackground="#d9d9d9")
        self.Label2_1.configure(highlightcolor="black")
        self.Label2_1.configure(text=''':''')

        self.Entry2_1 = tk.Entry(top)
        self.Entry2_1.place(relx=0.52, rely=0.375, height=20, width=32)
        self.Entry2_1.configure(background="white")
        self.Entry2_1.configure(disabledforeground="#a3a3a3")
        self.Entry2_1.configure(font="TkFixedFont")
        self.Entry2_1.configure(foreground="#000000")
        self.Entry2_1.configure(highlightbackground="#d9d9d9")
        self.Entry2_1.configure(highlightcolor="black")
        self.Entry2_1.configure(insertbackground="black")
        self.Entry2_1.configure(selectbackground="blue")
        self.Entry2_1.configure(selectforeground="white")
        self.Entry2_1.configure(textvariable=natan_support.end_minute)

        self.TButton1 = ttk.Button(top)
        self.TButton1.place(relx=0.35, rely=0.50, height=25, width=76)
        self.TButton1.configure(command=natan_support.submit)
        self.TButton1.configure(takefocus="")
        self.TButton1.configure(text='''Submit''')

        something = 0
        progress = ttk.Progressbar(root, orient = HORIZONTAL ,length = 100, mode = 'determinate',maximum=100)
        progress.place(relx=0.310, rely=0.65)
        progress.configure(variable=log_scan.progress_var)

        self.Label3 = tk.Label(top)
        self.Label3.place(relx=0.0008, rely=0.75, height=50, width=280)
        self.Label3.configure(activebackground="#f9f9f9")
        self.Label3.configure(activeforeground="black")
        self.Label3.configure(background="#d9d9d9")
        self.Label3.configure(font="Helvetica 9 bold")
        self.Label3.configure(disabledforeground="#a3a3a3")
        self.Label3.configure(foreground="#000000")
        self.Label3.configure(highlightbackground="#d9d9d9")
        self.Label3.configure(highlightcolor="black")
        self.Label3.configure(textvariable=log_scan.progress_status)

        #something = progress.configure)

if __name__ == '__main__':
    vp_start_gui()





