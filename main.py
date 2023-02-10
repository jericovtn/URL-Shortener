# Name: Jerico James F. Viteño
# Final Project: URL Shortener
# February 18, 2023

import pyperclip
import pyshorteners
from tkinter import *

root = Tk()
root.geometry("400x200")
root.title("URL Shortener")
root.configure(bg="#49A")

url = StringVar()
urlAddress = StringVar()

# URL Shortener Method
def urlShortener():
    urlAddress = url.get()
    urlShort = pyshorteners.Shortener().tinyurl.short(urlAddress)
    urlAddress.set(urlShort)

