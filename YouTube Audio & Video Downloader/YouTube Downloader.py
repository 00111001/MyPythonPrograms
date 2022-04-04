# -----------------------------------------------
# Author: Nick V.
# YouTube Downloader
# Version: 0.9
# creation date: 30.03.2022
# -----------------------------------------------
# 03.04.2022 Added Button to download WebM
# 03.04.2022 Automated convert from Webm to Mp3
# 04.04 2022 Added Checkboxes for Audio and MP4
# -----------------------------------------------

# Import tkinter fot the graphic Overlay
# Where soon will be added new features
from tkinter import *
# Lib for downloading Videos and Audios
from pytube import YouTube
# For some Operating system feats. like getcwd and scandir
import os


# Function for Checking Value of RadioMenu
def scan_option():
    # Var1 is instanced with int, so we check if he is selected with 1
    if audio.get() == 1:
        # Calling Audio Mp3 download function
        download_audio()
    # Var2 is instanced with int, so we check if he is selected with 1
    if video.get() == 1:
        # Calling High Res MP4 download
        download_mp4()


# Function for downloading the MP4
def download_mp4():
    # Referencing our link to url
    url = YouTube(str(link.get()))
    # Download the highest Resolution
    video = url.streams.get_highest_resolution()
    # Start download
    video.download()
    # Message when Download is finished


def convert_data():
    # Actual directory where the .py is
    path_folder = os.getcwd()
    # for converting extensions
    old_extension = '.webm'
    new_extension = '.mp3'

    # to get an iterator
    with os.scandir(path_folder) as files_and_folders:
        # For File or Folder in Files_and_folders
        for element in files_and_folders:
            # If element is a file and not a folder
            if element.is_file():

                tuple_root_ext = os.path.splitext(element.path)
                root = tuple_root_ext[0]
                ext = tuple_root_ext[1]

                root, ext = os.path.splitext(element.path)
                if ext == old_extension:
                    new_path = root + new_extension
                    os.rename(element.path, new_path)


def download_audio():
    # Referencing our link to url
    url = YouTube(str(link.get()))
    # Download only Audio data
    audio_file = url.streams.filter(only_audio=True, subtype='webm', abr='160kbps').first()
    # Start download
    audio_file.download()
    # Calling the Convert Data function
    convert_data()


# Initializing Pgm and
# referencing it to Program
Program = Tk()
# Referencing StringVar() to link
link = StringVar()
# Storing int values to choose download Option
audio = IntVar()
video = IntVar()

# Graphical
# Set Program Size (x, y)
Program.geometry('360x120')
# Set Program resizeable or not
Program.resizable(0, 0)
# Setting Program title to YouDownLoad?
Program.title("YouDownLoad?")
# Creating a Label which is the Headline of the Pgm and reference it to title
title = Label(Program, text='YouDownLoad', font='arial 20 bold').pack()
# Creating a Label which is the Headline of the Link Input field
Label(Program, text='Link: ', font='arial 15 bold').place(x=10, y=35)
# Creating an Input field for entering the Link
link_enter = Entry(Program, width=46, textvariable=link).place(x=70, y=40)
# Creating Check buttons which get checked on download
Checkbutton(Program, text="Audio", variable=audio).place(x=10, y=70)
Checkbutton(Program, text="Video", variable=video).place(x=10, y=90)
# Creating a Button for the download process  which triggers the DownloadMp4 func
Button(Program, text='Download Data', font='arial 15 bold',
       bg='pale violet red', padx=2, command=scan_option).place(x=80, y=71)
# Creating a Button to exit the PGM look at the command doesn't require sys or smth
Button(Program, text='EXIT', font='arial 15 bold',
       bg='pale violet red', padx=2, command=Program.quit).place(x=250, y=70)

# Calling main and therefor the Program
if __name__ == '__main__':
    Program.mainloop()
