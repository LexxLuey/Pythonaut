from tkinter import *

root = Tk()
root.geometry("600x400")

def key_response(event):
    label2['text'] += event.char
    if label2['text'] in ["Nothing"]:
        label['Exact']

label = Label(text="What?")
label.pack()

label2 = Label(text="")
label2.pack()

root.bind("<Key>", key_response)

root.mainloop()
