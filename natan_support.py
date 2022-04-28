#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# Support module generated by PAGE version 6.2
#  in conjunction with Tcl version 8.6
#    Apr 28, 2022 02:41:44 PM +0300  platform: Windows NT

import sys
import main
import re

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

def limitSizeDay(*args):
    hour_regex = r'\d'
    hour_regex1 = r'\d\d'

    start_hour_value = start_hour.get()
    if not re.match(hour_regex, start_hour_value):
        start_hour.set('')
    elif len(start_hour_value) >= 1 and not re.match(hour_regex1, start_hour_value):
        start_hour.set(start_hour_value[:1])
    if len(start_hour_value) > 2:
        start_hour.set(start_hour_value[:2])

    start_minute_value = start_minute.get()
    if not re.match(hour_regex, start_minute_value):
        start_minute.set('')
    elif len(start_minute_value) >= 1 and not re.match(hour_regex1, start_minute_value):
        start_minute.set(start_minute_value[:1])
    if len(start_minute_value) > 2:
        start_minute.set(start_minute_value[:2])

    end_hour_value = end_hour.get()
    if not re.match(hour_regex, end_hour_value):
        end_hour.set('')
    elif len(end_hour_value) >= 1 and not re.match(hour_regex1, end_hour_value):
        end_hour.set(end_hour_value[:1])
    if len(end_hour_value) > 2:
        end_hour.set(end_hour_value[:2])

    end_minute_value = end_minute.get()
    if not re.match(hour_regex, end_minute_value):
        end_minute.set('')
    elif len(end_minute_value) >= 1 and not re.match(hour_regex1, end_minute_value):
        end_minute.set(end_minute_value[:1])
    if len(end_minute_value) > 2:
        end_minute.set(end_minute_value[:2])

def set_Tk_var():
    global start_hour,start_minute,end_hour,end_minute,selected_date
    start_hour = tk.StringVar()
    start_minute = tk.StringVar()
    end_hour = tk.StringVar()
    end_minute = tk.StringVar()
    selected_date = tk.StringVar()
    start_hour.trace('w', limitSizeDay)
    start_minute.trace('w', limitSizeDay)
    end_hour.trace('w', limitSizeDay)
    end_minute.trace('w', limitSizeDay)
    
    #start_hour.set("Hour")
    #start_minute.set("Minutes")
    #end_hour.set("Hour")
    #end_minute.set("Minutes")

def init(top, gui, *args, **kwargs):
    global w, top_level, root
    w = gui
    top_level = top
    root = top

def submit():
    global selected_date
    hour_regex = r'\d\d'
    #selected_date = selected_date.selection_get()
    
    start_hour_value = start_hour.get()
    start_minute_value = start_minute.get()
    end_hour_value = end_hour.get()
    end_minute_value = end_minute.get()
    sel_date = selected_date.get().split('/')
    sel_date[2] = "20"+sel_date[2]
    if int(sel_date[0]) < 10:
        sel_date[0] = '0'+sel_date[0]
    windows_date = sel_date[2]+'-'+sel_date[0]+'-'+sel_date[1]
    if  int(start_hour_value) in range(0,24) and int(start_minute_value) in range(0,60) and int(end_hour_value) in range(0,24) and int(end_minute_value) in range(0,60):
        logs_time = []
        logs_time.append(start_hour_value+":"+start_minute_value)
        logs_time.append(end_hour_value+":"+end_minute_value)
        main.search_logs(windows_date,logs_time)
    else:
        print('invalid input')
    sys.stdout.flush()

def destroy_window():
    # Function which closes the window.
    global top_level
    top_level.destroy()
    top_level = None

Custom = tk.Frame  # To be updated by user with name of custom widget.

if __name__ == '__main__':
    import natan
    natan.vp_start_gui()




