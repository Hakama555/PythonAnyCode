import sqlite3

class DataBase:
    def __init__(self, dbname):
        self.dbname = dbname
        
           
    def executeQuery(self, sql_query):
        conn = sqlite3.connect(self.dbname)
        cur = conn.cursor()
        # クエリー文の実行
        cur.execute(sql_query)
        conn.commit()
        conn.close()
        cur.close()
        
        
           
           
        