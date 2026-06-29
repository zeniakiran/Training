from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfilename
from tkinter import messagebox

# Setup window
window = Tk()
window.title("Codingal's Text Editor")
window.geometry("600x500")

window.rowconfigure(0, weight=1) # row 0 will expand when window resized
window.columnconfigure(1, weight=1) # column 1 will expand when window resized

current_file = None  # Stores the opened file path

# Open file
# other methods include asksaveasfilename, askdirectory, askopenfilenames
def open_file():
    global current_file
    # *.txt
    path = askopenfilename(filetypes=[("Text Files", "*.txt")], title="Open File")
    if not path:
        return
    # handling error
    # catching errors
    try:
        # opening the file in readable mode
        # closes file automatically after reading
        with open(path, "r") as file:

            # setting the text widget editable
            txt_edit.config(state="normal")  

            # Read the file contents and insert them into the text editor.
            # txt.insert(position, "content")
            txt_edit.insert(END, file.read())
    except:
        messagebox.showerror("Error", "Error opening file!")

    current_file = path
    window.title(f"Codingal's Text Editor - {path}")

# Save file
def save_file():
    if current_file is None:
        messagebox.showwarning("No file", "Open a file first before saving.")
        return
    try:
        # r- read
        # w - write to file
        # open(path, 'w')
        with open(current_file, "w") as file:
            file.write(txt_edit.get("1.0", END))
        window.title(f"Text Editor - {current_file}")
    except:
        messagebox.showerror("Error", "Could not save file!")

def exit_app():
    answer = messagebox.askyesno("Exit", "Are you sure you want to exit?")
    if answer:
        window.destroy()

# Widgets
btn_frame = Frame(window, bd=2, relief=RAISED)

# "n" → stick to top
# "ew" → stretches horizontally
# "ns" → stretches vertically
# "nsew" → stretches both horizontally and vertically

btn_frame.grid(row=0, column=0, sticky="ns")

Button(btn_frame, text="Open", command=open_file).pack(padx=5, pady=10, fill="x")
Button(btn_frame, text="Save", command=save_file).pack(padx=5, pady=10, fill="x")
Button(btn_frame, text="Exit", command=exit_app).pack(padx=5, pady=10, fill="x")  # NEW BUTTON

# multi line text
txt_edit = Text(window, state="disabled")
txt_edit.grid(row=0, column=1, sticky="nsew")


window.mainloop()
