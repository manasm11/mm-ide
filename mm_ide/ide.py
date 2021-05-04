from tkinter import *
from threading import Thread
from tkinter.filedialog import asksaveasfilename
import os

print(os.path.split("/home/dir/something"))

editor = None
path = ""
# @property
# def code():


def run():
    global editor, path
    code = editor.get("1.0", END)
    exec(code)


def save():
    global editor, path
    path = asksaveasfilename(filetypes=[("Python Files", "*.py")])
    with open(path, "w") as file_:
        file_.write(path)


def open_():
    global editor, path


def main():
    global editor, path
    ide = Tk()
    ide.title("The Python IDE")
    editor = Text()
    editor.pack()

    menu_bar = Menu(ide)
    menu_bar.add_command(label="Run", command=run)
    menu_bar.add_command(label="Save", command=save)
    menu_bar.add_command(label="Save", command=open_)
    menu_bar.add_command(label="New", command=lambda: Thread(target=main).start())
    ide.config(menu=menu_bar)

    ide.mainloop()


if __name__ == "__main__":
    main()
