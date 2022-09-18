
from asyncore import read
from curses.textpad import Textbox
import tkinter as tk
from turtle import width
from typing import Text

class todo:
    def __init__(self, root):
        self.root = root
        self.root.title('To-do-app')
        self.root.geometry('650x410+300+150')

        self.label = tk.Label(self.root, text='To-Do-List-App',
         font='ariel, 25 bold', width=10,bd=5, bg='red', fg='black')
        self.label.pack(side='top', fill=tk.BOTH)

        self.label2 = tk.Label(self.root, text='Add Task',
         font='ariel, 18 bold', width=10,bd=5, bg='red', fg='black')
        self.label2.place(x=40, y=54)

        self.label3 = tk.Label(self.root, text='Tasks',
         font='ariel, 18 bold', width=10,bd=5, bg='red', fg='black')
        self.label3.place(x=320, y=54)

        self.main_text = tk.Listbox(self.root, height=9, bd=5, width=23, font="ariel, 20 italic bold")
        self.main_text.place(x=200, y=100)

        self.text = tk.Text(self.root, bd=5, height=2, width=24, font='ariel, 10 bold')
        self.text.place(x=15, y=100)

        #============add task========#

        def add():
            content = self.text.get(1.0, tk.END)
            self.main_text.insert(tk.END, content)
            with open('data.txt', 'a') as file:
                file.write(content)
                file.seek(0)
                file.close()
            self.text.delete(1.0, tk.END)

        def delete():
            delete_ = self.main_text.curselection()
            look = self.main_text.get(delete_)
            with open('data.txt', 'r+') as f:
                new_f = f.readlines()
                f.seek(0)
                for line in new_f:
                    item = str(look)
                    if item not in line:
                        f.write(line)
                f.truncate()
            self.main_text.delete(delete_)

        with open('data.txt', 'r') as file:
            read = file.readline()
            for i in read:
                ready = i.split()
                self.main_text.insert(tk.END, ready)
            file.close()

        self.button = tk.Button(self.root, text="Add", font='sarif, 20 bold italic', 
                      width=9,bd=5, bg='red', fg='black', command=add)
        self.button.place(x=20, y=180)

        self.button2 = tk.Button(self.root, text="Delete", font='sarif, 20 bold italic', 
                      width=10,bd=5, bg='red', fg='black', command=delete)
        self.button2.place(x=10, y=150)


def main():
    root = tk.Tk()
    ui = todo(root)
    root.mainloop()

if __name__ == "__main__":
    main()