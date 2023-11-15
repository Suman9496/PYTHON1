import tkinter as tk
from time import strftime

def update_time():
    string = strftime('%H:%M:%S %p')
    label.config(text=string)
    label.after(1000, update_time)

root = tk.Tk()
root.title("Digital Clock")

label = tk.Label(root, font=('calibri', 40, 'bold'), background='black', foreground='white')
label.pack(anchor='center')

update_time()
root.mainloop()
