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

root.geometry('400x300')
root.title("Harmony")#later

lengthlabel=Label(root,text="Total length- 00:00")
lengthlabel.pack(pady=10)

def show_length():
    a=mixer.Sound(filename_path)
    length=a.get_length()

statusbar=Label(root,text='Welcome!',relief=SUNKEN,anchor=W)
statusbar.pack(side=BOTTOM,fill=X)


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

menubar=Menu(root)
root.config(menu=menubar)

submenu=Menu(menubar,tearoff=0)

plist=[]

def browse_files():
    global f
    global filename_path
    filename_path=filedialog.askopenfilename()
    f=os.path.basename(filename_path)
    add_to_playlist()
    
def add_to_playlist():
    index=0
    playlist.insert(index,f)
    plist.insert(index,filename_path)
    index+=1
    print(plist)
    
def exit_window():#new
    stop_music()#new
    root.destroy()#new

 
    
menubar.add_cascade(label='File',menu=submenu)
submenu.add_command(label='Open',command=browse_files)
submenu.add_command(label='Exit',command=exit_window)#new

root.protocol('WM_DELETE_WINDOW',exit_window)  # root is your root window


    
def about_us():
    tkinter.messagebox.showinfo('About us','Listen to your favourite music whenever you want.')

submenu=Menu(menubar,tearoff=0)
menubar.add_cascade(label='Help',menu=submenu)
submenu.add_command(label='About us',command=about_us)

playlist=Listbox(leftframe
                 )#new
playlist.pack()

addbtn=Button(leftframe,text="Add.",command=browse_files)
addbtn.pack(side=LEFT)

def del_song():
    selected_song=playlist.curselection()
    selected_song=selected_song[0]
    playlist.delete(selected_song)
    plist.pop(selected_song)
    print(plist)

rmvbtn=Button(leftframe,text="Remove.",command=del_song)
rmvbtn.pack(side=LEFT)


text = Label(topframe, text='Lets make some noise!')
text.pack(pady=10)




    
def stop_music():
    global paused
    paused = False#new
    mixer.music.stop()
    statusbar['text']="Music stopped."
    
paused=False
def pause_music():
    global paused
    
    paused=True
    mixer.music.pause()
    statusbar['text']="Music paused."
    
def play_music():
    global paused
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
            
                play_it=plist[selected_song]
                mixer.music.load(play_it)
                mixer.music.play()
                statusbar['text']="Playing "+ os.path.basename(play_it)
            except: 
                tkinter.messagebox.showerror('Error','No selected songs in the playlist')
def shuffle_music():
    random.shuffle(plist)
    print(plist)
    for i in plist:
        #playlist.select_set(i)
        play_it=i
        mixer.music.load(play_it)
        mixer.music.play()
        statusbar['text']="Playing "+ os.path.basename(play_it)
        
        
    

def set_vol(val):
    volume= int(val)/100
    mixer.music.set_volume(volume)
    

    
    


playPhoto = PhotoImage(file='touch.png')
playBtn = Button(middleframe, image=playPhoto, command=play_music)
playBtn.pack(side=LEFT,padx=10)

stopPhoto = PhotoImage(file='stop.png')
stopBtn = Button(middleframe, image=stopPhoto, command=stop_music)
stopBtn.pack(side=LEFT,padx=10)

pausePhoto = PhotoImage(file='pause.png')
pauseBtn = Button(middleframe, image=pausePhoto, command=pause_music)
pauseBtn.pack(padx=10)

shufflePhoto = PhotoImage(file='shuffle.png')#new
shuffleBtn = Button(bottomframe1, image=shufflePhoto,command=shuffle_music)
shuffleBtn.pack(side=LEFT,padx=10)#new

repeatPhoto = PhotoImage(file='repeat.png')
repeatBtn = Button(bottomframe1, image=repeatPhoto)
repeatBtn.pack(padx=10)

scale=Scale(bottomframe2,from_=0,to=100,orient=HORIZONTAL,command=set_vol)
scale.set(70)
mixer.music.set_volume(0.7)
scale.pack(pady=10)

#progress=Scale(bottomframe,from_=0,to=100,orient=HORIZONTAL,command=set_progress)
#mixer.music.set_progress(0.7)
#scale.pack(pady=10)

root.mainloop()