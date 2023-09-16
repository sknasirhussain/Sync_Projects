from datetime import datetime
from time import *

from tkinter.ttk import *
from tkinter import *

from PIL import ImageTk, Image
from pygame import mixer

from threading import *

#Parent window
clock = Tk()
clock.title("Alarm Clock")
clock.geometry("450x200")
clock.configure(bg = '#f7f0f9')

#frames
frameLine = Frame(clock, width=500, 
                  height = 5, 
                  bg = '#9908ef')
frameLine.grid(row=0, column=0)

frameBody= Frame(clock, 
                 width=500, 
                 height = 400, 
                 bg = '#f7f0f9')
frameBody.grid(row=1, column=0)


# Load and resize the image
img = Image.open('Alarm_clock/Clock.png')
img = img.resize((110, 110))

img = ImageTk.PhotoImage(img)

# Setting up the body
Icon_image = Label(frameBody, 
                   height=155, 
                   image=img, 
                   bg ='#f7f0f9')
Icon_image.place(x=20, y=15)

name = Label(frameBody, 
             text = "Alarm Clock", 
             height= 1, 
             font=('helvetica','20','bold'), 
             bg = '#f7f0f9')
name.place(x=180, y=17)

#For the hour settings
hour = Label(frameBody, 
             text = "Hour", 
             height= 1, 
             font=('helvetica','12','bold'), 
             bg = '#f7f0f9')
hour.place(x=140, y=55)
hourBox = Combobox(frameBody, 
                   width=2, 
                   font='arial 15')
hourBox['values'] = ("00", "01", "02", 
                     "03", "04", "05", 
                     "06", "07", "08", 
                     "09", "10", "11", "12")
hourBox.current(0)
hourBox.place(x=143, y=80)

#for the minutes settings
min = Label(frameBody, 
            text = "Minutes", 
            height= 1, 
            font=('helvetica','12','bold'), 
            bg = '#f7f0f9')
min.place(x=200, y=55)
minBox = Combobox(frameBody, 
                  width=2, 
                  font='arial 15')
minBox['values'] = ("00", "01", "02", "03", "04", 
                    "05", "06", "07", "08", "09", 
                    "10", "11", "12", "13", "14", 
                    "15", "16", "17", "18", "19",
                    "20", "21", "22", "23", "24", 
                    "25", "26", "27", "28", "29", 
                    "30", "31", "32", "33", "34", 
                    "35", "36", "37", "38", "39", 
                    "40", "41", "42", "43", "44", 
                    "45", "46", "47", "48", "49", 
                    "50", "51", "52", "53", "54", 
                    "55", "56", "57", "58", "59", "60")
minBox.current(0)
minBox.place(x=203, y=80)

#for the seconds settings
sec = Label(frameBody, 
            text = "Seconds", 
            height= 1, 
            font=('helvetica','12','bold'), 
            bg = '#f7f0f9')
sec.place(x=275, y=55)
secBox = Combobox(frameBody, 
                  width=2, 
                  font='arial 15')
secBox['values'] = ("00", "01", "02", "03", "04", 
                    "05", "06", "07", "08", "09", 
                    "10", "11", "12", "13", "14", 
                    "15", "16", "17", "18", "19",
                    "20", "21", "22", "23", "24", 
                    "25", "26", "27", "28", "29", 
                    "30", "31", "32", "33", "34", 
                    "35", "36", "37", "38", "39", 
                    "40", "41", "42", "43", "44", 
                    "45", "46", "47", "48", "49", 
                    "50", "51", "52", "53", "54", 
                    "55", "56", "57", "58", "59", "60")
secBox.current(0)
secBox.place(x=279, y=80)

#For the hour settings
per = Label(frameBody, 
            text = "Period", 
            height= 1, 
            font=('helvetica','12','bold'), 
            bg = '#f7f0f9')
per.place(x=360, y=55)
perBox = Combobox(frameBody, 
                  width=3, 
                  font='arial 15')
perBox['values'] = ("AM", "PM")
perBox.current(0)
perBox.place(x=363, y=80)



def activate_alarm():
    print("Alarm has been activated!")
    trigger = Thread(target=alarm)
    trigger.start() 

def deactivate_alarm():
    print("Alarm has been deactivated!")
    mixer.music.stop()

selected = IntVar()

#activate and deactivate buttons
activate = Radiobutton(frameBody, 
                       font=('arial 14 bold'), 
                       value=1, 
                       text="Activate", 
                       bg= '#f7f0f9', 
                       command=activate_alarm, 
                       variable=selected)
activate.place(x=140, y=135)


def soundAlarm():
    mixer.music.load('Alarm_clock/Alarm_sound.mp3')
    mixer.music.play()
    selected.set(0)

    deactivate = Radiobutton(frameBody, 
                             font=('arial 14 bold'), 
                             value=2, 
                             text="Deactivate", 
                             bg= '#f7f0f9', 
                             command=deactivate_alarm, 
                             variable=selected)
    deactivate.place(x=250, y=135)

def alarm():
    while True:
        control = 1
        print(control)
        #user time settings
        alarmHour = hourBox.get()
        alarmMin = minBox.get()
        alarmSec = secBox.get()
        alarmPeriod = perBox.get()

        #current time
        now = datetime.now()
        c_hour = now.strftime("%I")
        c_minute = now.strftime("%M")
        c_second = now.strftime("%S")
        c_period = now.strftime("%p")
        print(c_hour,c_minute,c_second,c_period)

        if control == 1:
            if alarmPeriod == c_period:
                if alarmHour == c_hour:
                    if alarmMin == c_minute:
                        if alarmSec == c_second:
                            print("Please deativate the alarm")
                            soundAlarm()

        sleep(1)



mixer.init() 

clock.mainloop()