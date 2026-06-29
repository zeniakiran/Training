import tkinter as tk
from datetime import date

# Create Window
root = tk.Tk()
root.title("Simple App")
root.geometry("300x200")

# tk.Label(window, text, bg, fg).
# fill x stretches your text horizontally accross the window
tk.Label(root, text="Full Name", bg="#3895D3").pack(fill="x")

# Widgets
tk.Label(root, text="Enter your name:").pack()

# input field 
# user will be allowed to enter single line text
# name_entry = Maheen
name_entry = tk.Entry(root)
name_entry.pack()


# display the text
output_box = tk.Text(root, height=4)
output_box.pack()

def display():
    name = name_entry.get() # get the entry value 

    # clearing the text field 
    # 1.0 -> 1 line 1 of box
    # End end of the text
    # 1 to last
    # 1.0 start from line 1 character 0 till end 
    output_box.delete("1.0", tk.END)  # Clear previous text

    # output_box.insert(position, text)
    # tk.END put the line at the bottom, after everything.
    # string literals
    # line 
    # line 
    # Hello Zenia
    # outputBoxx.insert("1.0", hello)
    # outputBox.insert("2.0", Welcome)

    output_box.insert(tk.END, f"Hello {name}!\n")
    output_box.insert(tk.END, "Welcome to the Application!\n")
    output_box.insert(tk.END, f"Today's date is: {date.today()}")

    # CLEAR the input field 
    
    name_entry.delete(0, tk.END)


# tk.Button(window, text= label of the button, command= function name)
tk.Button(root, text="Begin", command=display).pack()

root.mainloop()
