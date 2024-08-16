from tkinter import *
from database import config, connect


def next_page():
    root = Tk()
    root.title("Database Connection Guide")
    Label(root, text='Make sure you have connected the wifi \'fms_student\'').pack()
    Label(root, text='Enter the IP address of the host:').pack()
    ip_input = Entry(root, width=50)
    ip_input.insert(0, config.DB_HOST)
    ip_input.pack()
    Button(root, text="Connect", command=connect_db).pack()

    root.mainloop()

def connect_db():
    config.DB_HOST = ip_input.get()
    connect.connect()

def start_guide():
    root = Tk()
    root.title("Database Connection Guide")

    Label(root, text="Welcome to the Database Connection Guide!").pack()
    Label(root, text="Please follow the steps connect to the database").pack()


    Button(root, text="Next", command=next_page).pack()

    root.mainloop()
