from tkinter import*

root = Tk()
root.title('Learn To Code Game')
#root.iconbitmap(' ')

button_quit = Button(root, text="Exit Program", command=root.destroy)
button_quit.pack()

root.mainloop()
