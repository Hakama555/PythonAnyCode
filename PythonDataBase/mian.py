from tkinter import *
from tkinter import messagebox
import sys
import os
import DataBase
import sqlite3

class Application:
    def __init__(self, root):
        self.root = root
        self.root.geometry("400x300")
        self.root.title("DataBaseTest")
        
        # テキストボックスの設置
        self.lbl1 = Label(text = "日付")
        self.lbl1.place(x = 10, y = 20)  
        self.txt1 = Entry(width=20)
        self.txt1.place(x = 70, y = 20)
        
        self.lbl2 = Label(text = "金額")
        self.lbl2.place(x = 10, y = 50) 
        self.txt2 = Entry(width=20)
        self.txt2.place(x = 70, y = 50)
        
        self.lbl3 = Label(text = "内容")
        self.lbl3.place(x = 10, y = 80)  
        self.txt3 = Entry(width=20)
        self.txt3.place(x = 70, y = 80)
        
        # ボタン操作
        btn = Button(self.root, text = "データの収納", command = self.button_click)
        btn.place(x = 70, y = 120)
    
    def button_click(self):
        #　挿入するクエリを書く
        sql_query = ""
        
        db = MakeDB("testdb")
        db.executeQuery(sql_query)
        if self.txt1 and self.txt2 and self.txt1 != None:
            Text.get()
            
        else:
            messagebox.showerror("注意", "")  

# データベースの構築
class MakeDB(DataBase):
    def __init__ (self, dbname):
        super().__init__(dbname)
        self.dbname = dbname
        
        if os.path(self.dbname):
            conn = sqlite3.connect(self.dbname)
            cur = conn.cursor()
            cur.execute(
                "CREATE TABLE kakeibo(id INTEGER )"
            )
    
    def executeQuery(self, sql_query):
        super().executeQuery(sql_query)
        
        
def main():
    root = Tk()
    app = Application(root)
    app.root.mainloop()

if __name__ == "__main__":
    try:
        main()
        sys.exit(0)
        
    except Exception as ex:
        print(ex, file = sys.stderr)
        sys.exit(1)