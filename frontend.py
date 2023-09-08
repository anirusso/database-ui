from tkinter import *

class Window(object):

    def __init__(self, window, tablename, columns):
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

        for col in columns:
            nameLbl = Label(window, text=str(col))
            nameLbl.grid(row=rownum, column=0)

            self.nameVar = StringVar()
            self.nameEntry = Entry(window, textvariable=self.nameVar)
            self.nameEntry.grid(row=rownum, column=1)
            rownum += 1

        addBtn = Button(window, text="Add New Recipe", command=self.add_command)
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

        self.errorTextVar = StringVar()
        errorLbl = Label(window, textvariable=self.errorTextVar)
        errorLbl.grid(row=rownum+2, column=0)

    def getSelection(self, event):
        print(event)

    def search_command(self):
        print("Search")

    def view_command(self):
        print("View")

    def add_command(self):
        print("Add")

    def clear_command(self):
        print("clear")

    def update_command(self):
        print("update")

    def delete_command(self):
        print("Delete")


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

    print(columns)

    # load window
    window = Tk()
    Window(window, tablename, columns)
    window.mainloop()

