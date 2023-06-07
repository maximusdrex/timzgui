from tkinter import *
from tkinter import ttk
from interface.db_manager import DBManager

class SelBox():
    def __init__(self, main, frame, db):
        self.program_str = StringVar()
        self.main = main
        self.db = db
        self.container = ttk.Frame(frame)
        program_sel = ttk.Combobox(self.container, textvariable=self.program_str)
        program_sel['values'] = [x[0] for x in db.getPrograms()]
        program_sel.state(["readonly"])
        program_sel.bind('<<ComboboxSelected>>', self.onChange)
        program_sel.grid(column=0, row=0, sticky=(N,S,E,W))
        self.container.columnconfigure(0, weight=1)
        self.container.rowconfigure(0, minsize=40)
        self.sel_box = program_sel

    def refreshVals(self):
        programs = [x[0] for x in self.db.getPrograms()]
        self.sel_box['values'] = programs
        if self.program_str.get() not in programs:
            if(len(programs) > 0):
                self.program_str.set(programs[0])
            else:
                self.setVal(None)
            self.onChange(None)

    def setVal(self, name):
        if(not name):
            self.program_str.set("")
        else:
            self.program_str.set(name)
        self.onChange(None)

    def onChange(self, arg):
        self.main.refreshAll()

