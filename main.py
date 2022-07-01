from tkinter import *
from PIL import ImageTk, Image

GEOMETRY = "1366x768"
MIN_SIZE = (600,600)
MAX_SIZE = (600,600)

root = Tk()

root.title("Monument Detection")
root.geometry("600x600")
root.minsize(1366, 768)
root.maxsize(1366, 768)


image=Image.open("Resources/bg.jpg")
pic= ImageTk.PhotoImage(image)
label=Label(image=pic)
label.pack()


root.mainloop()