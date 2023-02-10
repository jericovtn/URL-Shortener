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

# Copy URL Method
def copyURL():
    urlShort = urlAddress.get()
    pyperclip.copy(urlShort)

# Set GUI
Label(root, text="My URL Shortener", font="poppins").pack(pady=10)
Entry(root, textvariable=url).pack(pady=5)
Button(root, text="Generate Short URL", command=urlShortener).pack(pady=7)
Entry(root, textvariable=urlAddress).pack(pady=5)
Button(root, text="Copy URL", command=copyURL).pack(pady=5)

