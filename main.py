import database
import socket
from tkinter import messagebox as msgbox
from tkinter import *

ip = socket.gethostbyname(socket.gethostname())
print(ip)

database.start_guide()
cur_user: str | None = None
result, array = database.select(f'SELECT * FROM users WHERE ip=\'{ip}\';')
if result > 0:
    cur_user = array[0][0]
else:
    root = Tk()
    root.title("Register")
    Label(root, text='Enter your name: ').pack()
    name_input = Entry(root, width=30)
    name_input.pack()

    def add_user():
        global cur_user
        cur_user = name_input.get()
        root.destroy()
        cmd = f"INSERT INTO users (ip, username) VALUES ('{ip}', '{cur_user}');"
        database.update(cmd)

    Button(root, text='Register', command=add_user).pack()

    root.mainloop()

if cur_user is None:
    msgbox.showerror("Error", "Unable to register!")
    raise Exception("Unable to register")
msgbox.showinfo("Welcome", f"Welcome {cur_user}")


database.end()
