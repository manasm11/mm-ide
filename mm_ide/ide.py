from tkinter import *
from threading import Thread
from tkinter.filedialog import asksaveasfilename, askopenfilename
import os
import subprocess

START = "1.0"
editor = None
display = None
path = ""
# @property
# def code():


def run():
    global editor, path, display
    if path == "":
        save_prompt = Toplevel()
        message = Label(save_prompt, text="SAVE BEFORE YOU EXECUTE")
        message.pack()
        return
    code = editor.get("1.0", END)
    # exec(code)
    command = f"python3 {path}"
    process = subprocess.Popen(
        command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True
    )
    output, error = process.communicate()
    display.insert(START, output.decode())
    display.insert(START, error.decode())
    display.insert(START, "\n")


def save():
    global editor, path
    path = asksaveasfilename(filetypes=[("Python Files", "*.py")])
    with open(path, "w") as file_:
        file_.write(editor.get(START, END))


def open_():
    global editor, path
    path = askopenfilename(initialdir=os.path.split(path)[0], title="Open File")
    with open(path) as file_:
        editor.delete(START, END)
        editor.insert(START, file_.read())


def main():
    global editor, path, display
    ide = Tk()
    ide.title("The Python IDE")
    editor = Text()
    editor.pack()

    menu_bar = Menu(ide)
    menu_bar.add_command(label="Run", command=run)
    menu_bar.add_command(label="Save", command=save)
    menu_bar.add_command(label="Open", command=open_)
    menu_bar.add_command(label="New", command=lambda: Thread(target=main).start())
    ide.config(menu=menu_bar)

    display = Text(height=7)
    display.pack()

    ide.mainloop()


if __name__ == "__main__":
    main()
