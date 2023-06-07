from tkinter import *
from tkinter import ttk
from tkinter import font
from interface.db_manager import DBManager
from interface.edit_row import EditRow

class TableRow():
    def __init__(self, parent, row, seg, window):
        rowFont = font.Font(family=font.nametofont('TkDefaultFont').actual()['family'], name='appRowFont', size=16)
        self.window = window
        self.parent = parent
        self.row = row
        self.seg = seg
        self.checkvar = StringVar(value="0")
        self.check = ttk.Checkbutton(parent, variable=self.checkvar, onvalue="1", offvalue="0", command=window.refreshSelection, style='Table.TCheckbutton')
        self.transText = ttk.Label(parent, text=str(seg[0]), font=rowFont, background='white')
        self.lengthText = ttk.Label(parent, text=str(seg[1]), font=rowFont, background='white')
        self.PPIText = ttk.Label(parent, text=str(seg[2]), font=rowFont, background='white')
        self.EditBtn = ttk.Button(parent, text="\u270D", command=self.edit, style='Table.TButton')
        txt = ""
        if(seg[3] == 0):
            txt = "No"
        else:
            txt = "Yes"
        self.PauseText = ttk.Label(parent, text=txt, font=rowFont, background='white')
        self.items = [self.check, self.transText, self.lengthText, self.PPIText, self.PauseText, self.EditBtn]
        self.idn = int(seg[4])
        x = 0
        for i in self.items:
            i.grid(column=x, row=row+1, ipadx=5, ipady=10)
            x += 1
    
    def edit(self):
        self.window.segments.remove(self)
        self.destroy()
        self.window.segments.append(EditRow(self.window, 
                                            self.parent, 
                                            self.row, 
                                            self.window.db, 
                                            self.window.pid, 
                                            segment=self.seg))

    def destroy(self):
        for x in self.items:
            x.destroy()

