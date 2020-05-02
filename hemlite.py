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
    print("Play button works very well!")

playPhoto = PhotoImage(file = "play_2.png")
playBtn = Button(root, image = playPhoto, command = play_music)
playBtn.pack()

root.mainloop()
