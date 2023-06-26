from tkinter import *
from tkinter import ttk
from tkinter import font
from interface.db_manager import DBManager
from interface.help_button import HelpButton
from interface.sel_box import SelBox
from interface.new_program import CreateProgramButton
from interface.delete_button import DeleteProgramButton
from interface.seg_window import SegmentWindow
import configparser

HelpString = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
HEADER_ROW = 0
ROW_SIZE=0
SCROLLBAR_SIZE=40

class DataEntryGUI:
    def __init__(self, root, db):
        self.root = root
        self.db = db
        self.root.title("Main Control")

        appFont = font.Font(family=font.nametofont('TkDefaultFont').actual()['family'], name='appFont', size=16)

        self.mainframe = self.createMainFrame()

        self.help_button = HelpButton(root, self.mainframe, HelpString)
        self.program_sel = SelBox(self, self.mainframe, self.db)
        self.new_button = CreateProgramButton(root, self.mainframe, self.db, self.program_sel)
        self.deleteButton = DeleteProgramButton(root, self.mainframe, self.program_sel, self.db)
        self.tableFrame = ttk.Frame(self.mainframe)
        self.tableFrame['borderwidth'] = 2
        self.tableFrame['relief'] = 'sunken'

        self.createElements()

        self.segWindow = SegmentWindow(self.tableFrame, self.db, self.program_sel, self.mainframe, self.root)
        

        for child in self.mainframe.winfo_children(): 
            child.grid_configure(padx=5, pady=5)

        self.segWindow.canvas.wait_visibility()
        self.refreshAll()
        self.program_sel.refreshVals()

    def createMainFrame(self):
        mainframe = ttk.Frame(self.root, padding="3 3 12 12")
        mainframe.grid(column=0, row=0, sticky=(N,W,E,S))
        mainframe.configure(width=1280, height=800)
        mainframe.columnconfigure(0, weight=0, minsize=200)
        mainframe.columnconfigure(1, minsize=200)
        mainframe.columnconfigure(2, minsize=100, weight=4)
        mainframe.columnconfigure(3, minsize=200)
        mainframe.columnconfigure(4, minsize=100, weight=1)
        mainframe.rowconfigure(0, weight=1, minsize=80)
        mainframe.rowconfigure(1, weight=3, minsize=200)
        mainframe.rowconfigure(2, weight=1, minsize=80)

        return mainframe

    def createElements(self):
        mf = self.mainframe
        programFont = font.Font(family=font.nametofont('TkHeadingFont').actual()['family'], name='appProgramFont', size=20)
        ttk.Label(mf, text="PROGRAM:", font=programFont).grid(column=0, row=0, sticky=(E))

        # Place program selection box
        self.program_sel.container.grid(column=1, row=0, sticky=(W,E), columnspan=3)
        # Place program creation button
        self.new_button.btn.grid(column=4, row=0, sticky=(N,S,E,W))

        self.tableFrame.grid(column=0, columnspan=4, row=1, sticky=(N,S,E,W))

       
        self.deleteButton.btn.grid(column=3, row=2, sticky=(N,W,E,S))
        ttk.Button(mf, text="START", command=self.runStart).grid(column=4, row=1, sticky=(N,S,E,W))

        # Place Help button
        self.help_button.button.grid(column=4, row=2, sticky=(N,S,W,E))


    def runStart(self):
        pass

    def refreshAll(self):
        self.deleteButton.refreshVals()
        self.segWindow.refreshVals()
        self.segWindow.FrameHeight()


def run():
    parser=configparser.ConfigParser()
    parser.read("gui.cfg")
    HelpString = parser.get('GUI', 'Help')
    user = parser.get('Database', 'User')
    passw = parser.get('Database', 'Pass')
    host = parser.get('Database', 'Host')
    # Create the main window
    root = Tk()
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)

    s = ttk.Style()
    buttonFont = font.Font(family=font.nametofont('TkDefaultFont').actual()['family'], name='appButtonFont', size=18)
    s.configure('TButton', font=buttonFont)
    s.configure('Table.TButton', font=buttonFont, background='white')
    s.configure('Table.TFrame', background='white')
    s.configure('TCombobox', font=buttonFont, arrowsize=20)
    s.configure('Table.TCheckbutton', background='white')
    s.configure('Table.TLabel', background='white')
    s.element_create("My.Vertical.TScrollbar.trough", "from", "clam")
    s.element_create("My.Vertical.TScrollbar.thumb", "from", "clam")
    s.element_create("My.Vertical.TScrollbar.grip", "from", "clam")

    s.layout("My.Vertical.TScrollbar",
    [('My.Vertical.TScrollbar.trough',
        {'children': [('My.Vertical.TScrollbar.thumb',
                        {'unit': '1',
                        'children':
                            [('My.Vertical.TScrollbar.grip', {'sticky': ''})],
                        'sticky': 'nswe'})
                    ],
        'sticky': 'ns'})])

    s.configure("My.Vertical.TScrollbar", gripcount=0, borderwidth=2, arrowsize=SCROLLBAR_SIZE) #bordercolor='#252526', troughcolor='#252526', relief='sunken', gripinset=0, padding=0, background='#b0b0b0')


    root.option_add("*TCombobox*Listbox*Font", buttonFont)

    # Create an instance of the database manager

    dbm = DBManager(user, passw, host)
    # Create an instance of the DataEntryGUI class
    app = DataEntryGUI(root, dbm)
    
    # Run the GUI application
    root.mainloop()
    
if __name__ == '__main__': 
    run()