from tkinter import*
window = Frame ()
window.pack()
Label (window, text='Hello').pack(side=TOP)
Button (window, text='Exit', command=window.quit).pack(side=BOTTOM)
Entry (name = "text1").pack(expand = YES, fill = BOTH)
window.mainloop()
