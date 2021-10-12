import pyttsx3
from tkinter import *
import datetime
import time
from playsound import playsound

parent = Tk()

# function to speak your name
def speak():
    speak = "Hello " + e1.get() + " it's time to wake up"
    engine = pyttsx3.init()
    volume = engine.getProperty('volume')
    engine.setProperty('volume', 1.0)
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.say(speak)
    engine.runAndWait()

#funtion to play alarm sound
def play():
    while True:
        time.sleep(1)
        current_time = datetime.datetime.now()
        now = current_time.strftime("%H:%M:%S")
        print(now)
        set_hour = e2.get()
        set_min = e3.get()
        # when set hour and set minutes equals to current time below code executes
        if set_hour == now[:2] and set_min == now[3:5]:
            print('time to wake up')
            speak()
            playsound("C:/Users/narendra/Desktop/alarm_sound.wav")
            break


name = Label(parent, text="name").grid(row=0, column=0) #label of name
e1 = Entry(parent)  # entry box to enter name of the person
e1.grid(row=0, column=1)
hour = Label(parent, text="SET HOUR").grid(row=1, column=0)  #label of set hour
e2 = Entry(parent)   #entry box to enter hour
e2.grid(row=1, column=1)
min = Label(parent, text="SET MIN").grid(row=2, column=0)  #label of set hour
e3 = Entry(parent)   #entry box to enter hour
e3.grid(row=2, column=1)
submit = Button(parent, text="SET ALARM", command=play).grid(row=4, column=1) #button to set alarm
parent.mainloop()
