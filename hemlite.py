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

root.geometry("300x300")
root.title("Melody")
root.iconbitmap(r"icon.ico")

text = Label(root, text="Lets! Make some noise.")
text.pack()


def play_music():
    try:
        mixer.music.load(filename)
        mixer.music.play()
    except:
        tkinter.messagebox.showerror(
            "File not Found", "Could not find a file ! Please cheack again.")


def stop_music():
    mixer.music.stop()


def set_vol(val):
    volume = int(val) / 100
    mixer.music.set_volume(volume)


playPhoto = PhotoImage(file="play.png")
playBtn = Button(root, image=playPhoto, command=play_music)
playBtn.pack()

stopPhoto = PhotoImage(file="stop.png")
stopBtn = Button(root, image=stopPhoto, command=stop_music)
stopBtn.pack()

scale = Scale(root, from_=0, to=100, orient=HORIZONTAL, command=set_vol)
scale.set(75)  # set default volume
mixer.music.set_volume(0.7)
scale.pack()

root.mainloop()
