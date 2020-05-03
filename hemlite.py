import os
from tkinter import *
import tkinter.messagebox
from tkinter import filedialog
from pygame import mixer


root = Tk()

# menubar
menubar = Menu(root)
root.config(menu=menubar)

# submenu

def browse_file():
    global filename
    filename = filedialog.askopenfilename()
    print(filename)


submenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="File", menu=submenu)
submenu.add_command(label="Open", command=browse_file)
submenu.add_command(label="Exit", command=root.destroy)


def about_us():
    tkinter.messagebox.showinfo(
        "Hemlite Music Player", "This is a Music Player(WIP) written in python, based on tkinter and pygame librari \nBy:hraj9258")


submenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Help", menu=submenu)
submenu.add_command(label="About us", command=about_us)

mixer.init()  # initializing the mixer

root.title("Melody")
root.iconbitmap(r"icon.ico")

text = Label(root, text="Lets! Make some noise.")
text.pack()


def play_music():
    try:
        paused #check if "paused" is initlised pr not
    except NameError: #if not initlised then run the following code
        try:
            mixer.music.load(filename)
            mixer.music.play()
            statusbar["text"] = "Playing Music"+" | "+os.path.basename(filename)
        except:
            tkinter.messagebox.showerror(
                "File not Found", "Could not find a file ! Please cheack again.")
    else: #if initilised then continue
        mixer.music.unpause()
        statusbar["text"] = "Resumed Music"+" | "+os.path.basename(filename)



def pause_music():
    global paused
    paused = TRUE
    mixer.music.pause()
    statusbar["text"] = "Paused Music"+" | "+os.path.basename(filename)

def stop_music():
    mixer.music.stop()
    statusbar["text"] = "Stoped Music"


def set_vol(val):
    volume = int(val) / 100
    mixer.music.set_volume(volume)


midframe=Frame(root)
midframe.pack(padx=10,pady=10)

playPhoto = PhotoImage(file="play.png")
playBtn = Button(midframe, image=playPhoto, command=play_music)
playBtn.pack(side=LEFT, padx=10)

pausePhoto = PhotoImage(file="paused.png")
pauseBtn = Button(midframe, image=pausePhoto, command=pause_music)
pauseBtn.pack(side=LEFT, padx=10)

stopPhoto = PhotoImage(file="stop.png")
stopBtn = Button(midframe, image=stopPhoto, command=stop_music)
stopBtn.pack(side=LEFT, padx=10)

scale = Scale(root, from_=0, to=100, orient=HORIZONTAL, command=set_vol)
scale.set(75)  # set default volume
mixer.music.set_volume(0.7)
scale.pack()

statusbar = Label(root,text="Welcome! to hemlite music Player",relief=SUNKEN, anchor=W)
statusbar.pack(side=BOTTOM,fill=X)

root.mainloop()
