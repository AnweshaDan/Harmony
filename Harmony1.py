# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 19:13:00 2020

@author: Prasun
"""

import os
from tkinter import filedialog
from tkinter import *
from pygame import mixer
import tkinter.messagebox
import random



root = Tk()

mixer.init()  

# initializing root window characteristics
root.geometry('500x300')
root.title("Harmony")

#creating a statusbar to show muxic being played
statusbar=Label(root,text='Welcome!',relief=SUNKEN,anchor=W)
statusbar.pack(side=BOTTOM,fill=X)

# creating frames for better organization for widgets
leftframe=Frame(root)
leftframe.pack(side=LEFT,padx=30)

rightframe=Frame(root)
rightframe.pack()

topframe=Frame(rightframe)
topframe.pack()

middleframe=Frame(rightframe)
middleframe.pack(pady=10)

bottomframe1=Frame(rightframe)
bottomframe1.pack()

bottomframe2=Frame(rightframe)
bottomframe2.pack()

# function to browse files to be added
def browse_files():
    global f
    global filename_path
    filename_path=filedialog.askopenfilename()
    f=os.path.basename(filename_path)
    add_to_playlist()
    
#function to exit window
def exit_window():
    stop_music()
    root.destroy()
#overriding the functionality of cross button of window
root.protocol('WM_DELETE_WINDOW',exit_window) 

#messagebox for About Us submenu
def about_us():
    tkinter.messagebox.showinfo('About us','Listen to your favourite music whenever you want.')

# creating a menubar for some basic functionality
menubar=Menu(root)
root.config(menu=menubar)
submenu=Menu(menubar,tearoff=0)
#creating basic submenus of File menu
menubar.add_cascade(label='File',menu=submenu)
submenu.add_command(label='Open',command=browse_files)
submenu.add_command(label='Exit',command=exit_window)
#creating submenus for Help menu
submenu=Menu(menubar,tearoff=0)
menubar.add_cascade(label='Help',menu=submenu)
submenu.add_command(label='About us',command=about_us)


# Label to display info
text = Label(topframe, text='Lets make some noise!')
text.pack(pady=10)



plist=[]# list to store path of music files


    
#function to add music to playlist
count=0#to keep track of no. of songs
def add_to_playlist():
    global count
    index=0#to insert at the topmost part of playlist
    playlist.insert(index,f)
    plist.insert(index,filename_path)
    index+=1
    count+=1
    print(plist)
    print(index)
    print(count)
    
#function to remove songs from playlist
def del_song():
    selected_song=playlist.curselection()
    selected_song=selected_song[0]
    playlist.delete(selected_song)
    plist.pop(selected_song)
    print(plist)
    
# buttons to add/remove from playlist
addbtn=Button(leftframe,text="Add.",command=browse_files)
addbtn.pack(side=LEFT)
rmvbtn=Button(leftframe,text="Remove.",command=del_song)
rmvbtn.pack(side=LEFT)



#creating a listbox for holding playlist
playlist=Listbox(leftframe)
playlist.pack()

#function to start/pause/stop music
def stop_music():
    global paused
    paused = False
    mixer.music.stop()
    statusbar['text']="Music stopped."
    
paused=False
shuffled= False
def pause_music():
    global paused
    
    paused=True
    mixer.music.pause()
    statusbar['text']="Music paused."
    
def play_music():
    global paused
    global shuffled
    if paused:
        mixer.music.unpause()
        statusbar['text']="Music resumed."
        paused=False
    else:
        try :
            
            selected_song=playlist.curselection()
            selected_song=int(selected_song[0])
        except :
            selected_song=0
            
        finally:
            try:
                print(selected_song)
                print(len(plist))
                play_it=plist[selected_song]
                mixer.music.load(play_it)
                mixer.music.play()
                statusbar['text']="Playing "+ os.path.basename(play_it)
            except: 
                tkinter.messagebox.showerror('Error','No selected songs in the playlist')
                
def shuffle_music():
    random.shuffle(plist)
    print(plist)
    play_music()
    
# function to control volume
def set_vol(val):
    volume= int(val)/100
    mixer.music.set_volume(volume)
#setiing default volume
scale=Scale(bottomframe2,from_=0,to=100,orient=HORIZONTAL,command=set_vol)
scale.set(70)
mixer.music.set_volume(0.7)
scale.pack(pady=10)
    
#creating all the buttons
playPhoto = PhotoImage(file='touch.png')
playBtn = Button(middleframe, image=playPhoto, command=play_music)
playBtn.pack(side=LEFT,padx=10)

stopPhoto = PhotoImage(file='stop.png')
stopBtn = Button(middleframe, image=stopPhoto, command=stop_music)
stopBtn.pack(side=LEFT,padx=10)

pausePhoto = PhotoImage(file='pause.png')
pauseBtn = Button(middleframe, image=pausePhoto, command=pause_music)
pauseBtn.pack(padx=10)

shufflePhoto = PhotoImage(file='shuffle.png')
shuffleBtn = Button(bottomframe1, image=shufflePhoto,command=shuffle_music)
shuffleBtn.pack(side=LEFT,padx=10)


root.mainloop()