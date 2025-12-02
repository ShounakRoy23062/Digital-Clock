import tkinter as tk
import time
from tkinter import PhotoImage
from tkinter import font

#Title
root = tk.Tk()
root.title("Digital Clock")

bg_image = PhotoImage(file=r"C:\Users\Shounak\Downloads\desktop-wallpaper-i-made-high-sierra-dark-dynamic-macos-dark.png") #Background pic

#Image size
W = bg_image.width() 
H = bg_image.height()

#Window size
root.geometry(f"{W}x{H}") 

#Canvas interface
canvas = tk.Canvas(root, width=W, height=H, highlightthickness=0, bd=0)
canvas.pack(fill="both", expand=True) #Put the canvas in the window

#Image cover the window
canvas.create_image(0, 0, anchor="nw", image=bg_image)

#Text and Alignment
text_item = canvas.create_text(
    W // 2,
    H // 2,
    text="",
    fill="white",
    font=("Lucida Fax", 38, "bold"),
    anchor="center",
    justify="center"
)

#Clock update
def update_time():
    current_time = time.strftime("%H:%M:%S\n%A, %B %d, %Y")
    canvas.itemconfig(text_item, text=current_time)
    root.after(1000, update_time)

update_time()
root.mainloop()
