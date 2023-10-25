from tkinter import *
from backend import Database

class Window(object):

    def __init__(self, window, db, tablename, columns):

        #SETTING UP WINDOW

        self.window = window
        self.window.wm_title(tablename)

        searchLbl = Label(window, text="Search by...")
        searchLbl.grid(row=0, column=0, sticky="W")

        recipeLbl = Label(window, text="Data:")
        recipeLbl.grid(row=0, column=2)

        textSearchLbl = Label(window, text="Text contains:")
        textSearchLbl.grid(row=1, column=0)

        self.textSearchVar = StringVar()
        self.textSearchEntry = Entry(window, textvariable=self.textSearchVar)
        self.textSearchEntry.grid(row=1, column=1)

        colSearchLbl = Label(window, text="Column:")
        colSearchLbl.grid(row=2, column=0)

        self.tagSearchVar = StringVar()
        self.tagSearchVar.set("Select Option:")
        options = ['opt1', 'opt2']
        tagMenu = OptionMenu(window, self.tagSearchVar, *options)
        tagMenu.config(width=18)
        tagMenu.grid(row=2, column=1, padx=10)

        searchBtn = Button(window, text="Search", command=self.search_command)
        searchBtn.config(width=13)
        searchBtn.grid(row=3, column=0, pady=5, ipady=5, padx=5)

        viewBtn = Button(window, text="View All Rows", command=self.view_command)
        viewBtn.config(width=13)
        viewBtn.grid(row=3, column=1, pady=5, ipady=5, padx=5)

        self.list = Listbox(window, width=25, height=14)
        self.list.grid(row=1, column=2, rowspan=8)

        scrollbar = Scrollbar(window)
        scrollbar.config(width=13)
        scrollbar.grid(row=1, column=3, rowspan=8, sticky='ns')

        self.list.configure(yscrollcommand=scrollbar.set)
        scrollbar.configure(command=self.list.yview)

        self.list.bind('<<ListboxSelect>>', self.getSelection)

        selectLbl = Label(window, text="Add/Update:")
        selectLbl.grid(row=4, column=0, columnspan=2, pady=5, sticky="W")

        rownum = 5
        self.col_values = list(range(len(columns)))
        self.col_entries = list(range(len(columns)))
        colnum = 0

        for col in columns:

            nameLbl = Label(window, text=str(col))
            nameLbl.grid(row=rownum, column=0)

            self.col_values[colnum] = StringVar()
            self.col_entries[colnum] = Entry(window, textvariable=self.col_values[colnum])
            self.col_entries[colnum].grid(row=rownum, column=1)
            rownum += 1
            colnum += 1

        addBtn = Button(window, text="Add New Row", command=self.add_command)
        addBtn.config(width=13)
        addBtn.grid(row=rownum, column=0, pady=5, ipady=5, padx=5)

        clearBtn = Button(window, text="Clear All", command=self.clear_command)
        clearBtn.config(width=13)
        clearBtn.grid(row=rownum, column=1, pady=5, ipady=5)

        updateBtn = Button(window, text="Update Selected", command=self.update_command)
        updateBtn.config(width=13)
        updateBtn.grid(row=rownum+1, column=0, ipady=5, padx=5)

        deleteBtn = Button(window, text="Delete Selected", command=self.delete_command)
        deleteBtn.config(width=13)
        deleteBtn.grid(row=rownum+1, column=1, ipady=5)

        self.msgTextVar = StringVar()
        msgLbl = Label(window, textvariable=self.msgTextVar)
        msgLbl.grid(row=rownum+2, column=0)

    # BACKEND FUNCTIONS

    def getSelection(self, event):
        if self.list.curselection() != ():
            index = self.list.curselection()[0]
            self.selection = self.list.get(index)
            self.clear_command()
            entry = db.getEntry(self.selection)
            n = 1
            for c in self.col_entries:
                c.insert(END,entry[n])
                n+=1

    def search_command(self):
        print("Search")

    def view_command(self):
        self.list.delete(0,END)
        for row in db.view():
            print(row)
            self.list.insert(END,row[1])

    def add_command(self):
        values = []
        for c in self.col_values:
            values.append(c.get())
        res = db.insert(values)
        if (res):
            self.message("New row added")
            self.clear_command()
        else:
            self.message("Error adding new row")

    def clear_command(self):
        for c in self.col_entries:
            c.delete(0,END)
        self.message("")

    def update_command(self):
        values = []
        for c in self.col_values:
            values.append(c.get())
        res = db.update(values)
        self.view_command()
        self.clear_command()

    def delete_command(self):
        if self.list.curselection() != ():
            id = db.getEntry(self.selection)[0]
            db.delete(id)
            self.view_command()
            self.clear_command()
        else:
            self.message("Select an entry to delete")

    def message(self, msg):
        self.msgTextVar.set(msg)


if __name__ == "__main__":
    dbname = input("Enter a name for the database: ")
    dbname = dbname + ".db"

    tablename = input("Enter a name for your table: ")

    columns = {}
    while (True):
        i = input("Enter a column name or 0 to exit: ")
        if (i == "0"):
            break;
        datatype = input("Enter T for TEXT value or I for INTEGER value: ")
        if (datatype == "T") or (datatype == "I"):
            columns[i] = "TEXT" if datatype == "T" else "INTEGER"
        else:
            print("Error, please retry")

    db = Database(dbname, tablename, columns)

    # load window
    window = Tk()
    Window(window, db, tablename, columns)
    window.mainloop()
