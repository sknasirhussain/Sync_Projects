import pyshorteners
from tkinter import *

def short():
    url = newentry.get()
    shortened = pyshorteners.Shortener().tinyurl.short(url)
    shortTExt.insert(END,shortened)
    pass

window = Tk()
window.title("URL Shortener")
window.geometry("400x200")
window.configure(bg='#f7f0f9')

Label(window,text='Enter the URL to be shortened', font='helvetica 17 bold', bg='#f7f0f9', fg='black').pack(fill='x')

newentry = Entry(window, font='10', bd=1, width=40)
newentry.pack(pady=5)
newentry.place(x=20, y=45)

newbutton = Button(window, text='Submit', font='impack 12 bold', bg = 'blue', fg = 'white', command=short)
newbutton.pack()
newbutton.place(x = 160,y=80)

shortTExt= Entry(window, font="impack 12 bold", bg='#f7f0f9', width=40, bd = 0)

shortTExt.place(x=20, y=125)
mainloop()
