from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

# Setting up Main Window
root = Tk()
root.title('Denomination Counter')
root.configure(bg='light blue')
root.geometry('650x400')

# Adding Image and Labels in the Main Window
upload = Image.open("calculator.png")
# Resize the image using resize() method
upload = upload.resize((300, 300))
image = ImageTk.PhotoImage(upload)
label = Label(root, image=image, bg='light blue')
label.place(x=180, y=20)

label1 = Label(
    root,
    text="Hey User! Welcome to Denomination Counter Application.",
    bg='light blue'
)

# relative 0.0, 0.5, 1.0
label1.place(relx=0.5, y=340, anchor=CENTER)

# Function to display a messagebox and proceed if OK is clicked
def msg():
    topwin()

# Adding Buttons to the main window
button1 = Button(
    root,
    text="Let's get started!",
    command=msg,
    bg='brown',
    fg='white'
)
button1.place(x=260, y=360)
# Function for opening new/top window
def topwin():
    # top level widget
    top = Toplevel()
    top.title("Denominations Calculator")
    top.configure(bg='light grey')
    top.geometry("600x400")

    label = Label(top, text="Enter total amount", bg='light grey')
    entry = Entry(top)

    lbl = Label(top, 
                text="Here are number of notes for each denomination", 
                bg='light grey')

    l1 = Label(top, text="2000", bg='light grey')
    l2 = Label(top, text="500", bg='light grey')
    l3 = Label(top, text="100", bg='light grey')

    t1 = Entry(top) # 2
    t2 = Entry(top)
    t3 = Entry(top)

    def calculator():
        try:
            note2000, note500, note100, amount = 0, 0, 0, 0
            amount = int(entry.get())

            # no of notes needed
            # integer division
            # no of notes
            note2000 = amount // 2000 

            # remaining amount
            # modulus division
            amount %= 2000 # 1600

            if amount > 0: 
                note500 = amount // 500
                amount %= 500
                note100 = amount // 100

            # deletes previous entries
            t1.delete(0,END)
            t2.delete(0, END)
            t3.delete(0, END)

            # insert values
            t1.insert(0, str(note2000)) # 2
            t2.insert(0, str(note500))# 3
            t3.insert(0, str(note100))# 1


        except ValueError:
            messagebox.showerror("Error", "Please enter valid amount")

    btn = Button(top, text="Calculate", command=calculator, bg="brown", fg="white")
    label.place(x=230, y=50)
    entry.place(x=200, y=80)
    btn.place(x=240, y=120)
    lbl.place(x=140, y=170)

    l1.place(x=180, y=200)
    l2.place(x=180, y=230)
    l3.place(x=180, y=260)

    t1.place(x=270, y=200)
    t2.place(x=270, y=230)
    t3.place(x=270, y=260)

    #top.mainloop()

root.mainloop()
