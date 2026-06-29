from tkinter import *

root = Tk()
root.geometry("300x300") 

# flat, sunken, raised, grooved etc
# frame = Frame(positioning container, height, width, background color, borderwidth, relief="flat")
frame = Frame(root, height= 60, width= 300, bg='white', borderwidth=5, relief='flat')

lbl1 = Label(frame, text="Full Name", bg="#3B8ABE", fg="white", width=15)
lbl1.place(x=10, y=20)

#frame.pack()
frame.pack(fill="x")

root.mainloop()
