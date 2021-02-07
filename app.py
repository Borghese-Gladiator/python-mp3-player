
import os  # it permits to interact with the operating system
from tkinter.filedialog import askdirectory  # it permit to select dir
from tkinter import Tk, Label, Button, Listbox, ACTIVE, SINGLE, StringVar # used to develop GUI
import pygame  # used to create video games

class MusicPlayer:
    def __init__(self, master):
        self.master = master
        master.title("Life In Music")
        master.geometry("350x700")

        self.var = StringVar() 
        self.song_title = Label(master, font="Helvetica 12 bold", textvariable=self.var)
        self.song_title.pack()

        self.Button1 = Button(master, width=17, height=3, font="Helvetica 12 bold", text="PLAY", command=self.play, bg="blue", fg="white")
        self.Button1.pack(fill="x")

        self.Button2 = Button(master, width=17, height=3, font="Helvetica 12 bold", text="STOP", command=self.stop, bg="red", fg="white")
        self.Button2.pack(fill="x")

        self.Button3 = Button(master, width=17, height=3, font="Helvetica 12 bold", text="PAUSE", command=self.pause, bg="purple", fg="white")
        self.Button3.pack(fill="x")

        self.Button4 = Button(master, width=17, height=3, font="Helvetica 12 bold", text="UNPAUSE", command=self.unpause, bg="orange", fg="white")
        self.Button4.pack(fill="x")

        directory = askdirectory()
        os.chdir(directory)  # it permits to chenge the current dir
        song_list = os.listdir()  # it returns the list of files song

        self.play_list = Listbox(
            master, font="Helvetica 12 bold", bg="yellow", selectmode=SINGLE)
        for item in song_list:
            self.play_list.insert('end', item)
        self.play_list.pack(fill="both", expand="yes")

        self.close_button = Button(master, text="Close", command=master.quit)
        self.close_button.pack()

        pygame.init()
        pygame.mixer.init()

    def play(self):
        pygame.mixer.music.load(self.play_list.get(ACTIVE))
        self.var.set(self.play_list.get(ACTIVE))
        pygame.mixer.music.play()

    def stop(self):
        pygame.mixer.music.stop()

    def pause(self):
        pygame.mixer.music.pause()


    def unpause(self):
        pygame.mixer.music.unpause()

    def greet(self):
        print("Greetings!")


root = Tk()
my_gui = MusicPlayer(root)
root.mainloop()
