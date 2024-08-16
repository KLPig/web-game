import pymysql
from database import config
from tkinter import messagebox as msgbox

db: pymysql.Connection | None = None
connected = False

def connect():
    global db, connected

    db = None
    db = pymysql.connect(
        host=config.DB_HOST,
        user='kl',
        password='kl',
        database='game',
        port=3306
    )

    conn = db.cursor()
    result = conn.execute("SELECT VERSION()")
    conn.close()

    if result:
        data = conn.fetchone()
        if not connected:
            print(f"Database version: {data[0]}")
            connected = True
    else:
        msgbox.showerror("Database Error", "Failed to connect to database")
        raise Expection("Failed to connect to database")

def update(cmd: str):
    global db
    conn = db.cursor()
    result = conn.execute(cmd)
    db.commit()
    conn.close()
    return result

def select(cmd: str):
    global db
    db.ping(reconnect=True)
    conn = db.cursor()
    result = conn.execute(cmd)
    conn.close()
    return result, conn.fetchall()

def select_one(cmd: str):
    global db
    db.ping(reconnect=True)
    conn = db.cursor()
    result = conn.execute(cmd)
    conn.close()
    return result, conn.fetchone()

def end():
    global db
    db.close()
