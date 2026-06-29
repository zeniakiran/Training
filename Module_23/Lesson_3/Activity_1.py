# Import necessary libraries
from tkinter import *

# Create window
window = Tk()
window.title("Event Handler")
window.geometry("300x300")

# Event Handler for Keypress
def handle_keypress(event):
    print("Some key is pressed!")
    #Print the character associated to the key pressed
    print(event.char) # a, b, c

# Bind keypress event to handle_keypress()
window.bind("<Key>", handle_keypress)

# Event handler for button click
def handle_click(event):
    print("\nThe button was clicked!")

button = Button(text="Click me!") # clciking mouse and pressing enter
button.pack()

# Bind click event to handle_click()
button.bind("<Button-1>", handle_click)

# Start the GUI event loop
window.mainloop()
