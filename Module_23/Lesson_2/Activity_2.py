from tkinter import *

# Create Window
root = Tk()
root.title('Login App')
root.geometry('400x400')

# Create a Frame for grouping widgets
# Frame is a container used to group other widgets.
frame = Frame(root, bg="#d0efff")
frame.place(x=20, y=10, width=360, height=220)

# Labels
lbl1 = Label(frame, text="Full Name", bg="#3895D3", fg="white", width=15)
lbl2 = Label(frame, text="Email Id", bg="#3895D3", fg="white", width=15)
lbl3 = Label(frame, text="Enter Password", bg="#3895D3", fg="white", width=15)

# Entry Fields
name_entry = Entry(frame, bg="#B1CCDD", fg="black")
email_entry = Entry(frame, bg="#B1CCDD", fg="black")
pass_entry = Entry(frame, bg="#B1CCDD", fg="black", show="*")

# Function to display message
def display():
    name = name_entry.get().strip() 
    email = email_entry.get().strip()
    password = pass_entry.get().strip()

    # Clear previous messages
    textbox.delete("1.0", END)

    # Validation
    if name == "" or email == "" or password == "":
        textbox.insert(END, "Error: All fields are required!\n")
        return

    # Success message
    greet = "Hey " + name + "\n"
    message = "Congratulations for your new account!\n"
    textbox.insert(END, greet)
    textbox.insert(END, message)

    # Clear text fields after success
    name_entry.delete(0, END)
    email_entry.delete(0, END)
    pass_entry.delete(0, END)

# Textbox to show output
textbox = Text(root, bg="#BEBEBE", fg="black", height=5)

# Button
#btn = Button(root, text="Create Account", command=display, bg="#D33838", fg="white")

# Place widgets inside frame
lbl1.place(x=10, y=20)
name_entry.place(x=150, y=20, width=180)

lbl2.place(x=10, y=80)
email_entry.place(x=150, y=80, width=180)

lbl3.place(x=10, y=140)
pass_entry.place(x=150, y=140, width=180)


btn =Button(root, text="Create Account", bg="red", command=display)

# Place button and textbox in main window
btn.place(x=130, y=240)
textbox.place(x=20, y=280, width=360, height=100)

# Start loop
root.mainloop()
