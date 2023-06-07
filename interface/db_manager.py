import mysql.connector

DB_NAME = "tzgui"

class DBManager:
    def __init__(self, user, password, host):
        mydb = mysql.connector.connect(
        host=host,
        database="tzgui",
        user=user,
        password=password
        )
        if(not mydb):
            raise ConnectionError()
        mycursor = mydb.cursor()

        mycursor.execute("CREATE TABLE IF NOT EXISTS tblProgram (ProgramID INT AUTO_INCREMENT, strProgramName VARCHAR(255), PRIMARY KEY(ProgramID), UNIQUE(strProgramName))")
        mycursor.execute("CREATE TABLE IF NOT EXISTS tblSegment (SegmentID INT AUTO_INCREMENT, ProgramID INT, dblTransition DOUBLE, dblLength DOUBLE, intPPI INT, Pause BOOL, PRIMARY KEY(SegmentID), FOREIGN KEY (ProgramID) REFERENCES tblProgram(ProgramID))")
        self.db = mydb
        self.cur = mycursor

    def getPrograms(self):
        self.cur.execute("SELECT strProgramName,ProgramID FROM tblProgram")
        return [x for x in self.cur]
    
    def getProgramFromName(self, name):
        self.cur.execute("SELECT ProgramID FROM tblProgram WHERE strProgramName=%s",(name,))
        out = self.cur.fetchone()
        if(out):
            return int(out[0])
        return None
    
    def getProgramFromSegment(self, sid):
        self.cur.execute("SELECT ProgramID FROM tblSegment WHERE SegmentID=%s",(sid,))
        out = self.cur.fetchall()
        if(out):
            return out[0][0]
        return None
    
    def addProgram(self, name):
        # TODO: Handle non-unique names
        print("Adding: {}".format(name))
        self.cur.execute("INSERT INTO tblProgram (strProgramName) VALUES (%s)", (name,))
        self.db.commit()

    def deleteProgram(self, name):
        self.cur.execute("SELECT ProgramID FROM tblProgram WHERE strProgramName=%s",(name,))
        out = self.cur.fetchone()
        if(out):
            self.cur.execute("DELETE FROM tblSegment WHERE ProgramID=%s", (int(out[0]),))
            self.cur.execute("DELETE FROM tblProgram WHERE ProgramID=%s", (int(out[0]),))
        self.db.commit()

    def getSegments(self, pid):
        self.cur.execute("SELECT dblTransition, dblLength, intPPI, Pause, SegmentID FROM tblSegment WHERE ProgramID=%s", (pid,))
        return self.cur.fetchall()

    def getSegFromName(self, name):
        self.cur.execute("SELECT ProgramID FROM tblProgram WHERE strProgramName=%s",(name,))
        out = self.cur.fetchone()
        if(out):
            return self.getSegments(int(out[0]))
        else:
            return None
        
    def addSegment(self, seg):
        self.cur.execute("INSERT INTO tblSegment (ProgramID, dblTransition, dblLength, intPPI, Pause) VALUES (%s,%s,%s,%s,%s)", seg)
        self.db.commit()

    def deleteSegment(self, sid):
        pid = self.getProgramFromSegment(sid)
        self.cur.execute("DELETE FROM tblSegment WHERE SegmentID=%s", (sid,))
        if(not self.checkTableFor0(pid)):
            self.cur.execute("SELECT SegmentID FROM tblSegment WHERE ProgramID=%s", (pid,))
            first = self.cur.fetchall()
            if(first):
                self.cur.execute("UPDATE tblSegment SET dblTransition=0 WHERE SegmentId=%s", (first[0][0],))
        self.db.commit()

    def checkTableFor0(self, pid):
        self.cur.execute("SELECT SegmentID FROM tblSegment WHERE dblTransition=0 and ProgramID=%s", (pid,))
        return len(self.cur.fetchall()) > 0

    def updateSegment(self, seg):
        self.cur.execute("UPDATE tblSegment SET dblTransition=%s, dblLength=%s, intPPI=%s, Pause=%s WHERE SegmentId=%s", (seg))
        self.db.commit()

    def segmentTrans0(self, pid, sid=None):
        if(sid):
            self.cur.execute("SELECT * FROM tblSegment WHERE ProgramID=%s AND dblTransition=0 AND SegmentID!=%s", (pid, sid))
        else:
            self.cur.execute("SELECT * FROM tblSegment WHERE ProgramID=%s AND dblTransition=0", (pid, ))
        if(len(self.cur.fetchall()) > 0):
            return True
        return False

    def deleteSegments(self, seg_list):
        for x in seg_list:
            self.deleteSegment(x)
        
    def programValid(self, name):
        programs = [x[0] for x in self.getPrograms()]
        
        if(name in programs):
            return True
        return False