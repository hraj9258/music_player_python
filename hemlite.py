import os
from tkinter import *
import tkinter.messagebox
from tkinter import filedialog
from tkinter import ttk
from pygame import mixer
import threading
import time
from mutagen.mp3 import MP3


root = Tk()

# menubar
menubar = Menu(root)
root.config(menu=menubar)

 # it contain the filename + full_path
 # it contain only just filename
 #full_path +file name is required to play the music inside "play_music" load function
playlist=[]

def browse_file():
    global filename_path
    filename_path = filedialog.askopenfilename()
    #print(filename_path)
    #filelabel["text"]="Opened : "+os.path.basename(filename_path)
    add_to_playlist(filename_path)

def add_to_playlist(filename):
    filename = os.path.basename(filename)
    index = 0
    playlistbox.insert(index, filename)
    playlist.insert(index, filename_path)
    index +=1


# submenu

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

#statusbar

statusbar = Label(root,text="Welcome! to hemlite music Player | By:hraj9258",relief=SUNKEN, anchor=W)
statusbar.pack(side=BOTTOM,fill=X)

#left frame start from hear

leftframe =  Frame(root)
leftframe.pack(side=LEFT,padx=30)

playlistbox = Listbox(leftframe)# it just contain filename
playlistbox.pack()

btn1=ttk.Button(leftframe,text="+ ADD", command=browse_file)
btn1.pack(side = LEFT)

def del_song():
    selected_song = playlistbox.curselection()
    selected_song = int(selected_song[0])
    playlistbox.delete(selected_song)
    playlist.pop(selected_song)

btn2=ttk.Button(leftframe,text="- DEL", command=del_song)
btn2.pack(side = LEFT)
#rightframe starts from hear

rightframe=Frame(root)
rightframe.pack()

topframe= Frame(rightframe)
topframe.pack()

filelabel = ttk.Label(topframe, text="Lets! Make some noise.")
filelabel.pack()

lengthlabel = ttk.Label(topframe, text="Total Length : --:--")
lengthlabel.pack(pady=5)

currenttimelabel = ttk.Label(topframe, text="Current Time : --:--", relief = GROOVE)
currenttimelabel.pack()

def show_details(play_song):
    filelabel["text"]="Playing : "+os.path.basename(play_song)

    file_data = os.path.splitext(play_song)
    
    if file_data[1] == ".mp3":
        audio = MP3(play_song)
        total_length = audio.info.length
    else:
        a=mixer.Sound(play_song)
        total_length=a.get_length()

    mins, secs = divmod(total_length,60)
    mins = round(mins)
    secs = round(secs)
    timeformat = "{:02d}:{:02d}".format(mins,secs)
    lengthlabel["text"] = "Total Length : "+timeformat

    t1 = threading.Thread(target=start_count, args = (total_length,))
    t1.start()

def start_count(t):
    global paused
    current_time = 0
    while current_time <= t and mixer.music.get_busy():
        if paused:
            continue
        else:
            mins, secs = divmod(current_time,60)
            mins = round(mins)
            secs = round(secs)
            timeformat = "{:02d}:{:02d}".format(mins,secs)
            currenttimelabel["text"] = "Current Time : "+timeformat
            time.sleep(1)
            current_time += 1

def play_music():
    global paused

    if paused:
        mixer.music.unpause()
        statusbar["text"] = "Resumed Music"+" | "+os.path.basename(filename_path)
        paused = FALSE
    else:
        try:
            stop_music()
            time.sleep(1)
            selected_song = playlistbox.curselection()
            selected_song = int(selected_song[0])
            play_it = playlist[selected_song]
            mixer.music.load(play_it)
            mixer.music.play()
            statusbar["text"] = "Playing Music"+" | "+os.path.basename(play_it)
            show_details(play_it)
        except:
            tkinter.messagebox.showerror(
                "File not Found", "Could not find a file ! Please cheack again.")


def rewind_music():
    try:
        mixer.music.load(filename_path)
        mixer.music.play()
        statusbar["text"] = "Restarted Music"+" | "+os.path.basename(filename_path)
        filelabel["text"]="Restarted : "+os.path.basename(filename_path)
    except:
        tkinter.messagebox.showerror(
            "File not Found", "Could not find a file ! Please cheack again.")

paused=FALSE

def pause_music():
    global paused
    paused = TRUE
    mixer.music.pause()
    statusbar["text"] = "Paused Music"+" | "+os.path.basename(filename_path)
    filelabel["text"] = "Paused : "+os.path.basename(filename_path)

def stop_music():
    mixer.music.stop()
    statusbar["text"] = "Stoped Music"
    filelabel["text"] = "Lets! Make some noise."
    lengthlabel["text"] = "Total Length : --:--"
    currenttimelabel["text"] = "Current Time : --:--"

def set_vol(val):
    volume = float(val) / 100
    mixer.music.set_volume(volume)

muted=FALSE

def mute_music():
    global muted
    if muted:
        mixer.music.set_volume(0.75)
        volumeBtn.configure(image=volumePhoto)
        scale.set(75)
        muted=FALSE
        statusbar["text"]="Unmuted : "+os.path.basename(filename_path)
    else:
        mixer.music.set_volume(0)
        volumeBtn.configure(image=mutePhoto)
        scale.set(0)
        muted=TRUE
        statusbar["text"]="Muted : "+os.path.basename(filename_path)

midframe=Frame(rightframe)
midframe.pack(pady=30,padx=30)

playPhoto = PhotoImage(file="asset/play.png")
playBtn = ttk.Button(midframe, image=playPhoto, command=play_music)
playBtn.grid(row=0,column=0, padx=10)

pausePhoto = PhotoImage(file="asset/paused.png")
pauseBtn = ttk.Button(midframe, image=pausePhoto, command=pause_music)
pauseBtn.grid(row=0,column=1, padx=10)

stopPhoto = PhotoImage(file="asset/stop.png")
stopBtn = ttk.Button(midframe, image=stopPhoto, command=stop_music)
stopBtn.grid(row=0,column=2, padx=10)

#bottom frame for rewind, mute and scale

bottomframe=Frame(rightframe)
bottomframe.pack(pady=10)

rewindPhoto = PhotoImage(file="asset/rewind.png")
rewindBtn = ttk.Button(bottomframe, image=rewindPhoto, command=rewind_music)
rewindBtn.grid(row=0,column=0)

mutePhoto = PhotoImage(file="asset/mute.png")
volumePhoto = PhotoImage(file="asset/volume.png")
volumeBtn = ttk.Button(bottomframe, image=volumePhoto, command=mute_music)
volumeBtn.grid(row=0,column=1,padx=10)

scale = ttk.Scale(bottomframe, from_=0, to=100, orient=HORIZONTAL, command=set_vol)
scale.set(75)  # set default volume
mixer.music.set_volume(0.7)
scale.grid(row=0,column=2,padx=30,pady=10)


def root_exit():
    stop_music()
    root.destroy()

root.protocol("WM_DELETE_WINDOW",root_exit)
root.mainloop()
