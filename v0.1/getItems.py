from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from os import system
from pyautogui import alert

tasks_list = []
counter = 1


def inputError():
    if enterTaskField.get() == "":
        messagebox.showerror("Input Error")
        return 0
    return 1


def clear_taskNumberField():
    taskNumberField.delete(0.0, END)


def clear_taskField():
    enterTaskField.delete(0, END)


def insertTask():
    global counter

    value = inputError()

    if value == 0:
        return

    content = enterTaskField.get() + "\n"
    tasks_list.append(content)
    TextArea.insert('end -1 chars', str(counter) + ". " + content)
    counter += 1
    clear_taskField()


def delete():

    global counter

    if len(tasks_list) == 0:
        messagebox.showerror("No task")
        return

    number = taskNumberField.get(1.0, END)

    if number == "\n":
        messagebox.showerror("input error")
        return
    else:
        task_no = int(number)
    clear_taskNumberField()
    tasks_list.pop(task_no - 1)
    counter -= 1
    TextArea.delete(1.0, END)
    for i in range(len(tasks_list)):
        TextArea.insert('end -1 chars', str(i + 1) + ". " + tasks_list[i])

def upload():
    if tasks_list!=[]:
        with open('temp.py','a') as f:
            f.write(f"""\nitems = {[items[:-1] for items in tasks_list]}""")
        alert('Uploaded')
    else:
        alert('Upload Not Possible: All Values Not Provided')

if __name__ == "__main__":

    gui = Tk()
    gui.configure(background="white")
    gui.title("Invoice Generator")
    #gui.geometry("300x300")

    #enterTask = Label(gui, text="Enter Your Task", bg="white", font=('Helvetica', 8, 'bold'))
    enterTaskField = Entry(gui,bg="#EFEFEF")
    enterTaskField.insert(0,'Item <SPACE> Qty <SPACE> Unit_Price')
    Submit = Button(gui, text="ADD", font=('Helvetica', 8, 'bold'), fg="#444444", bg="#CFCFCF", command=insertTask, width=3)

    TextArea = Text(gui, height=5, width=32, font="lucida 10", bg="#EFEFEF")
    taskNumberField = Text(gui, height=1, width=2, font="lucida 10", bg="#EFEFEF")

    delete = Button(gui, text="DEL", font=('Helvetica', 8, 'bold'), fg="#444444", bg="#CFCFCF", command=delete, width=3)

    #Exit = Button(gui, text="Exit", font=('Helvetica', 8, 'bold'), fg="#444444", bg="#CFCFCF", command=exit)
    Upload = Button(gui, text='Upload', 
                        command=upload).grid(row=8,
                                            column=1,
                                            sticky=W,
                                            pady=4)
    #enterTask.grid(row=0, column=1)
    enterTaskField.grid(row=1, column=1, ipadx=51, sticky=W)
    Submit.grid(row=1, column=2)
    TextArea.grid(row=3, columnspan=2, sticky=W)
    taskNumberField.grid(row=5, column=1, ipadx=103, sticky=W)
    delete.grid(row=5, column=2)
    #Exit.grid(row=7, column=1)

    gui.mainloop()
