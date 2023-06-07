from tkinter import *
from tkinter import ttk
from tkinter import font
from interface.db_manager import DBManager

class SegDeletion():
    def __init__(self, root, window, db):
        self.seg_list = []
        self.root = root
        self.db = db
        self.window = window

    def deleteSegment(self, seg_list):
        self.seg_list = seg_list
        appFont = font.Font(family=font.nametofont('TkDefaultFont').actual()['family'], name='appFont', size=16)
        segn = len(seg_list)
        if(segn == 0):
            print("Error, no segments selected")
            return
        else:
            del_dlg = Toplevel(self.root)
            self.del_dlg = del_dlg
            del_dlg.title("Delete Program")
            ttk.Label(del_dlg, 
                    text="Are you sure you would like to delete {} segment(s)?".format(segn), 
                    wraplength=400, 
                    justify=LEFT, font=appFont).grid(column=0, row=0, columnspan=2)
            ttk.Button(del_dlg, text="Cancel", command=self.closeDialog).grid(column=0, row=1, sticky=(N,S))
            ttk.Button(del_dlg, text="Yes", command=self.delete).grid(column=1, row=1, sticky=(N,S))
            del_dlg.rowconfigure(1, minsize=50)
            del_dlg.protocol("WM_DELETE_WINDOW", self.closeDialog)
            del_dlg.transient(self.root)
            self.root.eval(f'tk::PlaceWindow {str(del_dlg)} center')
            del_dlg.wait_visibility()
            del_dlg.grab_set()
            del_dlg.wait_window()

    def delete(self):
        self.db.deleteSegments([x.idn for x in self.seg_list])
        self.closeDialog()
        self.window.refreshVals()

    def closeDialog(self):
        if(self.del_dlg):
            self.del_dlg.destroy()
        else:
            print("Error: Delete dialog already destroyed")

