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


def rewind_music():
    try:
        mixer.music.load(filename)
        mixer.music.play()
        statusbar["text"] = "Restarted Music"+" | "+os.path.basename(filename)
    except:
        tkinter.messagebox.showerror(
            "File not Found", "Could not find a file ! Please cheack again.")


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

muted=FALSE

def mute_music():
    global muted
    if muted:
        mixer.music.set_volume(0.75)
        volumeBtn.configure(image=volumePhoto)
        scale.set(75)
        muted=FALSE
    else:
        mixer.music.set_volume(0)
        volumeBtn.configure(image=mutePhoto)
        scale.set(0)
        muted=TRUE

midframe=Frame(root)
midframe.pack(pady=30,padx=30)

playPhoto = PhotoImage(file="play.png")
playBtn = Button(midframe, image=playPhoto, command=play_music)
playBtn.grid(row=0,column=0, padx=10)

pausePhoto = PhotoImage(file="paused.png")
pauseBtn = Button(midframe, image=pausePhoto, command=pause_music)
pauseBtn.grid(row=0,column=1, padx=10)

stopPhoto = PhotoImage(file="stop.png")
stopBtn = Button(midframe, image=stopPhoto, command=stop_music)
stopBtn.grid(row=0,column=2, padx=10)

#bottom frame for rewind, mute and scale

bottomframe=Frame(root)
bottomframe.pack(pady=10)

rewindPhoto = PhotoImage(file="rewind.png")
rewindBtn = Button(bottomframe, image=rewindPhoto, command=rewind_music)
rewindBtn.grid(row=0,column=0)

mutePhoto = PhotoImage(file="mute.png")
volumePhoto = PhotoImage(file="volume.png")
volumeBtn = Button(bottomframe, image=volumePhoto, command=mute_music)
volumeBtn.grid(row=0,column=1,padx=10)

scale = Scale(bottomframe, from_=0, to=100, orient=HORIZONTAL, command=set_vol)
scale.set(75)  # set default volume
mixer.music.set_volume(0.7)
scale.grid(row=0,column=2,padx=30,pady=10)

statusbar = Label(root,text="Welcome! to hemlite music Player",relief=SUNKEN, anchor=W)
statusbar.pack(side=BOTTOM,fill=X)

root.mainloop()
