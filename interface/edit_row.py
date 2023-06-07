from tkinter import *
from tkinter import ttk
from tkinter import font
from interface.db_manager import DBManager

HEADER_ROW = 0
ROW_SIZE=0

class EditRow():
    def __init__(self, segwin, parent, row, db, pid,segment=None):
        self.window = segwin
        self.window.AddButton.state(['disabled'])
        self.edit = False
        self.db = db
        self.pid = pid
        self.trans = StringVar()
        self.length = StringVar()
        self.PPI = StringVar()
        self.Pause = StringVar(value="No")
        if(segment):
            self.segment=segment
            self.edit = True
            self.trans.set(segment[0])
            self.length.set(segment[1])
            self.PPI.set(segment[2])
            
        self.transEntry = ttk.Entry(parent, textvariable=self.trans)
        if(not db.segmentTrans0(pid)):
            self.trans.set("0")
            self.transEntry.state(["readonly", "disabled"])
        self.lengthEntry = ttk.Entry(parent, textvariable=self.length)
        self.PPIEntry = ttk.Entry(parent, textvariable=self.PPI)
        self.PauseEntry = ttk.Combobox(parent, textvariable=self.Pause)
        self.PauseEntry['values'] = ["Yes", "No"]
        self.PauseEntry.state(["readonly"])
        self.EditBtn = ttk.Button(parent, text="\u2713", command=self.confirm, style='Table.TButton')
        self.window.root.bind('<Return>', lambda e: self.EditBtn.invoke())

        self.items = [self.transEntry, self.lengthEntry, self.PPIEntry, self.PauseEntry, self.EditBtn]
        x = 1
        for i in self.items:
            i.grid(column=x, row=row+1, ipadx=5, ipady=10)
            parent.rowconfigure(x, minsize=ROW_SIZE)
            x += 1

    def validateEntries(self):
        return True
    
    def confirm(self):
        if(self.validateEntries()):
            if(self.edit):
                pause = 0
                if(self.Pause.get() == "Yes"):
                    pause = 1
                try:
                    self.db.updateSegment((float(self.trans.get()), 
                                        float(self.length.get()), 
                                        int(self.PPI.get()), 
                                        pause,
                                        self.segment[4]))
                except ValueError:
                    print("Error, segment values incorrect")
            else:
                pause = 0
                if(self.Pause.get() == "Yes"):
                    pause = 1
                try:
                    self.db.addSegment((self.pid, 
                                        float(self.trans.get()), 
                                        float(self.length.get()), 
                                        int(self.PPI.get()), 
                                        pause))
                except ValueError:
                    print("Error, segment values incorrect")
            self.destroy()
            self.window.refreshVals()
    
    def destroy(self):
        self.window.root.unbind_all('<Return>')
        for x in self.items:
            x.destroy()
        self.window.AddButton.state(['!disabled'])

