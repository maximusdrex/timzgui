from tkinter import *
from tkinter import ttk
from tkinter import font
from interface.db_manager import DBManager

HEADER_ROW = 0
ROW_SIZE=0

class TableHeader():
    def __init__(self, parent):
        parent.rowconfigure(HEADER_ROW, minsize=ROW_SIZE)
        headerFont = font.Font(family=font.nametofont('TkHeadingFont').actual()['family'], name='appHeaderFont', size=18, weight='bold')
        self.transText = ttk.Label(parent, text="Trans (in)", font=headerFont, background='white')
        self.transText.grid(column=1, row=HEADER_ROW, ipadx=5, ipady=10)
        self.lengthText = ttk.Label(parent, text="Length (in)", font=headerFont, background='white')
        self.lengthText.grid(column=2, row=HEADER_ROW, padx=5, ipady=10)
        self.PPIText = ttk.Label(parent, text="PPI", font=headerFont, background='white')
        self.PPIText.grid(column=3, row=HEADER_ROW, ipadx=5, ipady=10)
        self.PauseText = ttk.Label(parent, text="Pause", font=headerFont, background='white')
        self.PauseText.grid(column=4, row=HEADER_ROW, ipadx=5, ipady=10)
        self.EditText = ttk.Label(parent, text="Edit", font=headerFont, background='white')
        self.EditText.grid(column=5, row=HEADER_ROW, ipadx=5, ipady=10)

