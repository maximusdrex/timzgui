from tkinter import *
from tkinter import ttk
from tkinter import font
from interface.db_manager import DBManager

class CreateProgramButton():
    def __init__(self, root, frame, db, sel):
        self.root = root
        self.btn = ttk.Button(frame, text="CREATE NEW", command=self.addDialog)
        self.db = db
        self.sel = sel
        self.entry = None
    
    def addDialog(self):
        appFont = font.Font(family=font.nametofont('TkDefaultFont').actual()['family'], name='appFont', size=16)
        create_dlg = Toplevel(self.root)
        self.create_dlg = create_dlg
        create_dlg.title("CREATE PROGRAM")
        self.entry = StringVar()
        ttk.Label(create_dlg, 
                  text="PROGRAM NAME:", 
                  wraplength=400, 
                  justify=LEFT, font=appFont).grid(column=0, row=0)
        ttk.Entry(create_dlg, textvariable=self.entry).grid(column=1, row=0, columnspan=3)
        ttk.Button(create_dlg, text="Cancel", command=self.closeDialog).grid(column=2, row=1, sticky=(N,S))
        ttk.Button(create_dlg, text="Enter", command=self.addProgram).grid(column=3, row=1, sticky=(N,S))
        create_dlg.rowconfigure(1, minsize=50)
        create_dlg.protocol("WM_DELETE_WINDOW", self.closeDialog)
        create_dlg.transient(self.root)
        self.root.eval(f'tk::PlaceWindow {str(create_dlg)} center')
        create_dlg.wait_visibility()
        create_dlg.grab_set()
        create_dlg.wait_window()

    def addProgram(self):
        name = self.entry.get()
        if(name):
            self.db.addProgram(name)
            self.sel.refreshVals()
            self.sel.setVal(name)
        else:
            print("Error: Name invalid or null")
        self.closeDialog()

    def closeDialog(self):
        if(self.create_dlg):
            self.create_dlg.destroy()
        else:
            print("Error: Creation dialog already destroyed")

