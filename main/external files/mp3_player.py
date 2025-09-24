import os
import tkinter as tk
from tkinter import filedialog
import pygame

pygame.mixer.init()

# functions
def choose_folder():
    global music_files, current_index
    folder = filedialog.askdirectory()
    if folder:
        music_files = [os.path.join(folder, f) for f in os.listdir(folder) if f.endswith(".mp3")]
        current_index = 0
        if music_files:
            current_song.set(os.path.basename(music_files[current_index]))

def play():
    if music_files:
        pygame.mixer.music.load(music_files[current_index])
        pygame.mixer.music.play()
        current_song.set(os.path.basename(music_files[current_index]))

def stop():
    pygame.mixer.music.stop()

def next_song():
    global current_index
    if music_files:
        current_index = (current_index + 1) % len(music_files)
        play()

def prev_song():
    global current_index
    if music_files:
        current_index = (current_index - 1) % len(music_files)
        play()

# gui
root = tk.Tk()
root.title("https://github.com/nucax/chasze")
root.geometry("300x200")

current_song = tk.StringVar()
tk.Label(root, textvariable=current_song, wraplength=280, justify="center").pack(pady=10)

tk.Button(root, text="Folder", command=choose_folder).pack(pady=5)
tk.Button(root, text="Play", command=play).pack(pady=5)
tk.Button(root, text="Stop", command=stop).pack(pady=5)
tk.Button(root, text="Prev", command=prev_song).pack(pady=5)
tk.Button(root, text="Next", command=next_song).pack(pady=5)

root.mainloop()
