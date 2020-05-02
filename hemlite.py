from tkinter import *
from pygame import mixer


root = Tk()

mixer.init()#initializing the mixer

root.geometry("300x300")
root.title("Melody")
root.iconbitmap(r"icon.ico")

text=Label(root,text="Lets! Make some noise.")
text.pack()


def play_music():
    mixer.music.load("tiger.mp3")
    mixer.music.play()


def stop_music():
    mixer.music.stop()

def set_vol(val):
    volume = int(val) / 100
    mixer.music.set_volume(volume)


playPhoto = PhotoImage(file = "play.png")
playBtn = Button(root, image = playPhoto, command = play_music)
playBtn.pack()

stopPhoto = PhotoImage(file = "stop.png")
stopBtn = Button(root, image = stopPhoto, command = stop_music)
stopBtn.pack()

scale = Scale(root, from_=0, to=100, orient = HORIZONTAL, command = set_vol)
scale.set(75) #set default volume
mixer.music.set_volume(75)
scale.pack()

root.mainloop()
