import pyautogui
from PIL import Image
from PIL import ImageOps
from PIL import ImageDraw
from PIL import ImageGrab
from tkinter import *
from tkinter import filedialog
from time import sleep
import os


root = Tk()
root.title("Screenshot")
root.geometry("250x200")
root.resizable(width=False, height=False)
default = os.getcwd()
location = default


def get_save_location():
    global location
    path = filedialog.asksaveasfilename()
    location = path + ".png"


def screenshot_func():
    sleep(int(entry.get()))
    ss = pyautogui.screenshot()
    ss.save(location)


label = Label(root, text="Enter in how many seconds you\nwant to take the screenshot:")
label.pack()

entry = Entry(root)
entry.pack()

screenshot_button = Button(root, text="Take screenshot", command=screenshot_func)
screenshot_button.pack(anchor=CENTER, pady=20)

directory_button = Button(root, text="Choose directory", command=get_save_location)
directory_button.pack()

root.mainloop()
