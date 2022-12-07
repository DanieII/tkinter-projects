from tkinter import *
from time import strftime
from tkinter.ttk import *

root = Tk()
root.title("Clock")
root.geometry('250x100')
playing = True

style1 = Style()
style1.configure("A.TButton", font="none 8 bold", background="green", foreground="green")

style2 = Style()
style2.configure("B.TButton", font="none 8 bold", background="red", foreground="red")


def time():
    if playing:
        string = strftime('%H:%M:%S %p')
        label.config(text=string)
        label.place(relx=0.5, rely=0.2, anchor=CENTER)
    label.after(1000, time)


def start():
    global playing
    playing = True


def pause():
    global playing
    playing = False


play_button = Button(root, text="PLAY", style="A.TButton", command=start)
play_button.pack()
play_button.place(relx=0.7, rely=0.7, anchor="center")

pause_button = Button(root, text="PAUSE", style="B.TButton", command=pause)
pause_button.pack()
pause_button.place(relx=0.3, rely=0.7, anchor="center")

label = Label(root, font="Times 32", )
label.pack()
time()
root.mainloop()
