import tkinter as tk

def input_window(title, message):
    root = tk.Tk()
    root.title(title)
    root.geometry("300x150")
    tk.Label(root, text=message).pack()
    e = tk.Entry(root)
    e.pack()
    r = ''

    def on_ok_button_click():
        nonlocal r
        r = e.get()
        root.destroy()

    tk.Button(root, text="OK", command=on_ok_button_click).pack()
    root.mainloop()
    return r
