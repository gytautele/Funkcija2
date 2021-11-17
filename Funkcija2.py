import thkinter
import time
import sqlite3
import random
import tempfile
import win32api
import win32print

global c, cur, flag, rev
login = sqlite3.connect("admin.db")
l = login.cursor()
c = sqlite3.connect("medicine.db")
cur = c.cursor()

columns = ('Sl No', 'Name', 'Type', 'Quantity Left', 'Cost', 'Purpose', 'Expiry Date', 'Rack location', 'Manufacture')

def show_rev():
    apt.destroy()
    flag = 'rev'
    rev = Tk()
    total = 0.0
    today = str(time.localtime()[2]) + '/' + str(time.localtime()[1]) + '/' + str(time.localtime()[0])
    Label(rev, text='Today: ' + today).grid(row=0, column=0)
    cur.execute('select * from bills')
    for i in cur:
        if i[4] == today:
            total += float(i[3])
    print(total)
    Label(rev, width=22, text='Total revenue: PHP ' + str(total), bg='blue', fg='white').grid(row=1, column=0)
    cx = 0
    vsb = Scrollbar(orient='vertical')
    lb1 = Listbox(rev, width=25, yscrollcommand=vsb.set)
    vsb.grid(row=2, column=1, sticky=N + S)
    lb1.grid(row=2, column=0)
    vsb.config(command=lb1.yview)
    cur.execute("select * from bills")
    for i in cur:
        if i[4] == today:
            cx += 1
            lb1.insert(cx, 'Bill No.: ' + str(i[5]) + '    : PHP ' + str(i[3]))
    c.commit()
    Button(rev, text='Main Menu', bg='green', fg='white', command=main_menu).grid(row=15, column=0)
    rev.mainloop()
