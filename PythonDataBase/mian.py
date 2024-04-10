from tkinter import *
import sys
import DataBase

class Application:
    def __init__(self, root):
        self.root = root
        self.root.geometry("400x300")
        self.root.title("DataBaseTest")
        
        # テキストボックスの設置
        lbl1 = Label(text = "日付")
        lbl1.place(x = 10, y = 20)  
        txt1 = Entry(width=20)
        txt1.place(x = 70, y = 20)
        
        lbl2 = Label(text = "金額")
        lbl2.place(x = 10, y = 50) 
        txt2 = Entry(width=20)
        txt2.place(x = 70, y = 50)
        
        lbl3 = Label(text = "内容")
        lbl3.place(x = 10, y = 80)  
        txt3 = Entry(width=20)
        txt3.place(x = 70, y = 80)
        
        # ボタン操作
        btn = Button(self.root, text = "データの収納", command = self.button_click)
        btn.place(x = 70, y = 120)
    
    def button_click(self):
        Text.get()

# データベースの構築
class MakeDB(DataBase):
    def __init__ (self, dbname):
        super().__init__(dbname)
        self.dbname = dbname
    
    def executeQuery(self, sql_query):
        super().executeQuery(sql_query)
        
        
def main():
    db = MakeDB("testdb")
    db.execute
    
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