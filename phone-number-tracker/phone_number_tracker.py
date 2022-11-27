from tkinter import *
import phonenumbers
from colorama import Fore
from phonenumbers import geocoder
from phonenumbers import carrier
from colorama import Fore

root = Tk()
root.geometry('260x270')
root.title("Phone Number Locator")
root['bg'] = '#D0CBEC'

Label(root, text='Phone Number:', font="none 15 bold", bg='#D0CBEC').pack()
textbox = Entry(root)
textbox.pack()


def locating_the_number():
    # Getting the information about the given number
    number = phonenumbers.parse(textbox.get())
    location = geocoder.description_for_number(number, 'en')
    Label(root, text=f"The device's location is {location}", bg='#D0CBEC', font="none 10 bold").pack()
    service_provider = phonenumbers.parse(textbox.get())
    provider = carrier.name_for_number(service_provider, 'en')
    Label(root, text=f"The current provider is {provider}", bg='#D0CBEC', font="none 10 bold").pack()


button1 = Button(root, text='OK', command=locating_the_number)
button1.pack(pady=5)
informative_label = Label(root, text="The given number must start with the country's prefix\nExample: +359 886548596",
                          font="none 7 bold", bg='#D0CBEC')
informative_label.pack()
informative_label.place(relx=0.5, rely=0.9, anchor="center")
root.mainloop()
