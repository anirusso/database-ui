import sqlite3 as sq

class Database:

    def __init__(self, db, tablename, columns):
        self.con = sq.connect(db)
        self.cur = self.con.cursor()
        cr_str = "CREATE TABLE IF NOT EXISTS " + tablename + "(Id INTEGER PRIMARY KEY)"
        print(cr_str)
        self.cur.execute(cr_str)
        for col in columns.keys():
            al_str = "ALTER TABLE " + tablename + " ADD COLUMN " + col + " " + columns[col]
            self.cur.execute(al_str)
            
    def insert(self, tablename, columns, values):
        col_str = ""
        for i in columns.keys():
            col_str = i + ","
        col_str += col_str[:-1]
        
        num_values = len(values)
        q_str = "?," * num_values
        q_str = q_str[:-1]    
        in_str = "INSERT INTO " + tablename + "(" + col_str + ") VALUES(" + q_str + ")"
        print(in_str)
        self.cur.execute(in_str, values)
