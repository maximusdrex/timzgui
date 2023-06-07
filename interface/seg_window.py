from tkinter import *
from tkinter import ttk
from tkinter import font
from interface.db_manager import DBManager
from interface.edit_row import EditRow
from interface.seg_delete import SegDeletion
from interface.table_row import TableRow
from interface.table_header import TableHeader

class SegmentWindow():
    def __init__(self, parent, db, sel, mainframe, root):
        self.root = root
        self.AddButton = ttk.Button(mainframe, 
                   text="ADD SEGMENT", 
                   command=self.addSegment)
        self.AddButton.grid(column=0, row=2, sticky=(N,W,E,S)) 
        self.delmanager = SegDeletion(root, self, db)
        self.DelButton = ttk.Button(mainframe, 
                   text="DELETE SEGMENT", 
                   command=self.deleteSegment)
        self.DelButton.grid(column=1, row=2, sticky=(N,W,E,S))
        self.DelButton.state(['disabled'])

        self.db = db
        self.sel = sel
        v = ttk.Scrollbar(parent, orient=VERTICAL)
        self.canvas = Canvas(parent, yscrollcommand=v.set, background='white')
        self.canvas.grid(column=0, row=0, sticky=(N,S,E,W))
        parent.columnconfigure(0, weight=1)
        parent.rowconfigure(0, weight=1)
        v.grid(column=1, row=0, sticky=(N,S,E,W))
        v['command'] = self.canvas.yview
        self.segFrame = ttk.Frame(self.canvas, style='Table.TFrame')
        self.canvasFrame = self.canvas.create_window(0,0, anchor='nw', window=self.segFrame)
        self.canvas.bind('<Configure>', self.FrameWidth)

        # Configure table columns
        self.segFrame.columnconfigure(0, weight=0, minsize=50)
        self.segFrame.columnconfigure(1, weight=1, minsize=50)
        self.segFrame.columnconfigure(2, weight=1, minsize=50)
        self.segFrame.columnconfigure(3, weight=1, minsize=50)
        self.segFrame.columnconfigure(4, weight=1, minsize=50)
        self.segFrame.columnconfigure(5, weight=1, minsize=50)
        self.header = TableHeader(self.segFrame)
        self.segments = []
        
        programName = self.sel.program_str.get()
        self.pid = self.db.getProgramFromName(programName)
    
    def FrameHeight(self):
        if(len(self.segments) > 0):
            self.canvas.configure(scrollregion=(0,0,self.segFrame.winfo_width(), ((self.lastRow - 1) * (self.segments[0].EditBtn.winfo_height() + 10)) + self.header.transText.winfo_height() + 10))
            #self.canvas.configure(scrollregion=(0,0,self.segFrame.winfo_width(), (self.lastRow) * (self.segments[0].transText.winfo_height() + 10)))
            

    def FrameWidth(self, event):
        canvas_width = event.width
        self.canvas.itemconfig(self.canvasFrame, width = canvas_width)
        self.FrameHeight()
        
    
    def refreshVals(self):
        for x in self.segments:
            x.destroy()
        self.segments = []
        programName = self.sel.program_str.get()
        self.pid = self.db.getProgramFromName(programName)
        if(self.db.programValid(programName)):
            x = 0
            for segment in self.db.getSegFromName(programName):
                self.segments.append(TableRow(self.segFrame, x, segment, self))
                x += 1
            self.lastRow=x
            if(x>0):
                self.segments[0].EditBtn.wait_visibility()
        self.FrameHeight()

    def refreshSelection(self):
        selected = False
        for seg in self.segments:
            if(seg.checkvar):
                if(seg.checkvar.get() == "1"):
                    selected = True
        if(selected):
            self.DelButton.state(['!disabled'])
        else:
            self.DelButton.state(['disabled'])
        self.FrameHeight()

    def addSegment(self):
        self.segments.append(EditRow(self, self.segFrame, 
                                     self.lastRow, 
                                     self.db, 
                                     self.db.getProgramFromName(self.sel.program_str.get())))
        self.lastRow += 1
        self.FrameHeight()

    def deleteSegment(self):
        seg_list = []
        for seg in self.segments:
            if(seg.checkvar):
                if(seg.checkvar.get() == "1"):
                    seg_list.append(seg)
        if(len(seg_list) > 0):
            self.delmanager.deleteSegment(seg_list)

