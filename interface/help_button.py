from tkinter import *
from tkinter import ttk
from tkinter import font

class HelpButton:
    def __init__(self, root, frame, help):
        self.root = root
        self.button = ttk.Button(frame, text="Help", command=self.showHelp)
        self.help_str = StringVar()
        self.help_str.set(help)

    def showHelp(self):
        appFont = font.Font(family=font.nametofont('TkDefaultFont').actual()['family'], name='appFont', size=16)
        help_dlg = Toplevel(self.root)
        help_dlg.title("Help")
        self.help_dlg = help_dlg
        ttk.Label(help_dlg, 
                  textvariable=self.help_str, 
                  wraplength=400, 
                  justify=LEFT, font=appFont).grid(column=0, columnspan=2, row=0)
        ttk.Button(help_dlg, text="Exit", command=self.closeHelp).grid(column=1, row=1, sticky=(N,S,E,W))
        help_dlg.rowconfigure(1,minsize=50)
        help_dlg.protocol("WM_DELETE_WINDOW", self.closeHelp)
        help_dlg.transient(self.root)
        self.root.eval(f'tk::PlaceWindow {str(help_dlg)} center')
        help_dlg.wait_visibility()
        help_dlg.grab_set()
        help_dlg.wait_window()

    def closeHelp(self):
        if(self.help_dlg):
            self.help_dlg.destroy()
        else:
            print("Error: Help dialog already destroyed")

