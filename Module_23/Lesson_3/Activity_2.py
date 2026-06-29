# Import necessary libraries
from tkinter import *
from tkinter import messagebox

# Setup Tkinter Window
root = Tk()
root.geometry("300x300")

# Function for Displaying Warning Message
# This will be called once the button is clicked
def msg():
    #result = messagebox.askyesno("Delete", "Are you sure.?")
    #print("REsult", result)
    result = messagebox.askyesno("Warning", "Viruses detected!") # true or false 
    if result == True:
        print("True")
    elif result == False:
        print("False")

# Adding Button Widget to Window
button = Button(root, text="Scan for Virus", command=msg)
button.place(x=40, y=80)

# Entering main event loop
root.mainloop()
