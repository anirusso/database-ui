import sqlite3 as sq

class Database:

    def __init__(self, db, tablename, columns):
        self.con = sq.connect(db)
        self.cur = self.con.cursor()
        self.table = tablename
        self.columns = columns
        cr_str = "CREATE TABLE IF NOT EXISTS " + self.table + "(Id INTEGER PRIMARY KEY)"
        self.cur.execute(cr_str)
        for col in self.columns.keys():
            al_str = "ALTER TABLE " + self.table + " ADD COLUMN " + col + " " + self.columns[col]
            self.cur.execute(al_str)

    def view(self):
        self.cur.execute("SELECT * FROM " + self.table)
        rows = self.cur.fetchall()
        return rows

    def insert(self, values):
        col_str = ""
        for i in self.columns.keys():
            col_str += i + ","
        col_str = col_str[:-1]
        num_values = len(values)
        q_str = "?," * num_values
        q_str = q_str[:-1]
        in_str = "INSERT INTO " + self.table + "(" + col_str + ") VALUES(" + q_str + ")"
        res = self.cur.execute(in_str, values)
        return res

    def getEntry(self, value):
        self.cur.execute("SELECT * FROM " + self.table + " WHERE " + list(self.columns.keys())[0] + "=?", (value,))
        row = self.cur.fetchone()
        return row

    def delete(self, id):
        self.cur.execute("DELETE FROM " + self.table + " WHERE Id=?",(id,))

    def update(self, values):
        cur_str = "UPDATE " + self.table + " SET "
        for i in self.columns.keys():
            cur_str += i
            cur_str += "=?, "
        cur_str = cur_str[:-2]
        cur_str += " WHERE " + list(self.columns.keys())[0] + "=?"
        values.append(values[0])
        self.cur.execute(cur_str, values)
