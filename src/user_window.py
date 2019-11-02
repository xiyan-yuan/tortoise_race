# -*- coding: UTF-8 -*-
import tkinter as tk

class Player:

    def __init__(self, num):
        # Initialize player window
        self.window = tk.Tk()
        self.window.wm_attributes('-topmost',1)
        self.window.title('Player Info')
        self.window_width = 330
        self.window_height = 180
        alignstr = '%dx%d+%d+%d' % (self.window_width, self.window_height, 200, 200)
        self.window.geometry(alignstr) 
        
        self.num = num      
        self.entry_list = []   
        self.number_user = {}          
        for i in range(self.num):
            self.number_user["number %s: " % (i+1)] = ""
        
    def save_player_info(self):
        ii = 1
        for e in self.entry_list:
            self.number_user["number %s: " % ii] = e.get()
            ii += 1
        self.window.destroy()
        
    def start(self):
        i = 0
        for i in range(self.num):
            tk.Label(self.window, width=12, text = "number %s: " % (i+1)).grid(row = i)
            e = tk.Entry(self.window, width=30)
            e.grid(row = i, column = 1)
            self.entry_list.append(e)
            i += 1
        tk.Button(self.window, width=12, text='保存', command=self.save_player_info).grid(row=self.num + 1, 
                      column=1, sticky=tk.E, pady=4)
        self.window.mainloop()
