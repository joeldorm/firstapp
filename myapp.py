import tkinter as tk
import tkinter.messagebox as msgbox


class Window(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title = ("Hello world")

    def say_hello(self):
        msgbox.showinfo('Hello there', "Are you there!")


if __name__ == '___main__':
    win = Window()
    win.mainloop()
