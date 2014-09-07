from os import walk
import sqlite3
import threading
class db:

    def __init__(self):
        self.conn = sqlite3.connect(r'/tmp/store.db')
        self.conn.text_factory = str
    def generate(self):
        print "Generating database....Please Wait"
        ob=db()
        for root,dirs,files in walk('/home'):
            for filename in files:
                filetype=filename.split('.')
                filetype=filetype[-1]
                ob.conn.execute("insert into logs values (?,?,?)",(root,filename,filetype))
        ob.conn.close()
        print "Database successfully generated"
        
    def setup(self):
        cur=self.conn.cursor()
        cur.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='logs'")
        if cur.fetchone()[0]!="logs":
           cur.execute("create table logs if not exists (root_dir,filename,type)")
        t=threading.Thread(name="generate",target=self.generate)
        t.start()

    
    def cleanall(self):
        cur=self.conn.cursor()
        cur.execute("delete from logs")

