# Name: Jerico James F. Viteño
# Final Project: URL Shortener
# February 18, 2023

import pyperclip
import pyshorteners
from tkinter import *

root = Tk()
root.geometry("400x210")
root.title("URL Shortener")
root.configure(bg="#d4ebf2")

url = StringVar()
url_address = StringVar()

# URL Shortener Method
def urlShortener():
    urlAddress = url.get()
    urlShort = pyshorteners.Shortener().tinyurl.short(urlAddress)
    url_address.set(urlShort)

# Copy URL Method
def copyURL():
    urlShort = url_address.get()
    pyperclip.copy(urlShort)

# Set GUI
Label(root, text="URL Shortener", font="poppins", background="#d4ebf2").pack(pady=8)
Entry(root, textvariable=url, width=50, justify="center").pack(pady=10)
Button(root, text="Generate Short URL", command=urlShortener).pack(pady=7)
Entry(root, textvariable=url_address, width=50, justify="center", fg="#ff0000").pack(pady=5)
Button(root, text="Copy URL", command=copyURL).pack(pady=5)

root.mainloop()