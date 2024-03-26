import tkinter.ttk
import pytube
from pytube import YouTube
from tkinter import *

font = ("Arial", "14", "bold italic")


def downloadVideo():
    quality_value = qualityChoose.get()
    url = str(linkEntry.get())

    download_folder = r"C:\Users\emir_\Desktop\pythonProject\YoutubeTkinter\videos"

    if quality_value == "360p":
        video = YouTube(url).streams.filter(res="360p").first()
        video.download(download_folder)
        Label(text=' VIDEO DOWNLOADED', font='arial 15').grid(row=4, column=0)
    elif quality_value == "480p":
        video = YouTube(url).streams.filter(res="480p").first()
        video.download(download_folder)
        Label(text=' VIDEO DOWNLOADED', font='arial 15').grid(row=4, column=0)
    elif quality_value == "720p":
        video = YouTube(url).streams.filter(res="720p").first()
        video.download(download_folder)
        Label(text=' VIDEO DOWNLOADED', font='arial 15').grid(row=4, column=0)
    elif quality_value == "1080p":
        video = YouTube(url).streams.filter(res="1080p").first()
        video.download(download_folder)
        Label(text=' VIDEO DOWNLOADED', font='arial 15').grid(row=4, column=0)


window = Tk()
window.config(padx=20, pady=20)
window.title("Youtube mp4 downloader")
window.geometry('600x400+50+50')

introLabel = Label()
introLabel.config(text="Please enter the link of the video you want to download", font=font)
introLabel.grid(row=0, column=0, pady=10, padx=10)

linkEntry = Entry()
linkEntry.config(width=50)
linkEntry.grid(row=1, column=0, pady=10, padx=10)

n = StringVar()
qualityChoose = tkinter.ttk.Combobox(window, width=27, textvariable=n)
qualityChoose['values'] = ('360p', '480p', '720p', '1080p')
qualityChoose.grid(row=2, column=0)
qualityChoose.current()

sendButton = Button()
sendButton.config(text="Download", pady=10, padx=10, command=downloadVideo)
sendButton.grid(row=3, column=0, pady=10, padx=10)


window.mainloop()

