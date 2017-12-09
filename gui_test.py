'''
des:gui相关操作
author: zhua
'''

from tkinter import *


def test():
    root = Tk()
    word = Label(root, text="hello world!")
    word.pack()
    root.mainloop()

class App:
    def __init__(self, master):
        frame = Frame(master)
        frame.pack()

        self.hellobtn = Button(frame, text="Hello", command=self.hello)
        self.hellobtn.pack(side=LEFT)

        self.quit = Button(frame, text="Quit", fg="red", command=frame.quit())
        self.quit.pack(side=RIGHT)

    def hello(self):
        print("Hello World")

# if __name__ == '__main__':
#     # test()
#     root = Tk()
#     root.wm_title("Hello")
#     root.wm_minsize(200, 200)
#
#     app = App(root)
#
#     root.mainloop()


