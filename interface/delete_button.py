from tkinter import *
from tkinter import ttk
from tkinter import font
from interface.db_manager import DBManager

class DeleteProgramButton():
    def __init__(self, root, frame, sel, db):
        self.btn = ttk.Button(frame, text="DELETE PROGRAM", command=self.showDialog)
        self.root = root
        self.sel = sel
        self.db = db

    def refreshVals(self):
        programs = [x[0] for x in self.db.getPrograms()]
        if self.sel.program_str.get() not in programs:
            self.btn.state(["disabled"])
        else:
            self.btn.state(["!disabled"])

    def showDialog(self):
        appFont = font.Font(family=font.nametofont('TkDefaultFont').actual()['family'], name='appFont', size=16)
        del_dlg = Toplevel(self.root)
        self.del_dlg = del_dlg
        del_dlg.title("Delete Program")
        ttk.Label(del_dlg, 
                  text="Are you sure you would like to delete \"{}\"".format(self.sel.program_str.get()), 
                  wraplength=400, 
                  justify=LEFT, font=appFont).grid(column=0, row=0, columnspan=2)
        ttk.Button(del_dlg, text="Cancel", command=self.closeDialog).grid(column=0, row=1, sticky=(N,S))
        ttk.Button(del_dlg, text="Enter", command=self.deleteProgram).grid(column=1, row=1, sticky=(N,S))
        del_dlg.rowconfigure(1, minsize=50)
        del_dlg.protocol("WM_DELETE_WINDOW", self.closeDialog)
        del_dlg.transient(self.root)
        self.root.eval(f'tk::PlaceWindow {str(del_dlg)} center')
        del_dlg.wait_visibility()
        del_dlg.grab_set()
        del_dlg.wait_window()

    def deleteProgram(self):
        programs = [x[0] for x in self.db.getPrograms()]
        if self.sel.program_str.get() not in programs:
            print("Error: the selected program does not exist")
        else:
            self.db.deleteProgram(self.sel.program_str.get())
        self.sel.refreshVals()
        self.closeDialog()

    def closeDialog(self):
        if(self.del_dlg):
            self.del_dlg.destroy()
        else:
            print("Error: Delete dialog already destroyed")

