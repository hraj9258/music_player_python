from tkinter import *

root = Tk()
root.geometry("300x300")
root.title("Melody")
root.iconbitmap(r"icon.ico")

text=Label(root,text="Lets! Make some noise.")
text.pack()

def play_btn():
    print("Play button works very well!")

photo=PhotoImage(file="play_2.png")
btn=Button(root, image=photo, command=play_btn)
btn.pack()

root.mainloop()
