import sqlite3 
from config import *
con = sqlite3.connect(database) 
cur = con.cursor()
cur.execute("CREATE TABLE answersquestions(answer, question, id)")
con.close()
