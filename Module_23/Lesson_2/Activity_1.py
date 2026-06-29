from tkinter import *

# Create Window
root = Tk()
root.title('Dialing Pad')
root.geometry('300x300')

# Number pad layout
# list = [1, 2, 3, 4]
# list1 = [ list2 ]
# list = [[1,2,3],[4,5,6]]
nums = [
    [9, 8, 7], # 0
    [6, 5, 4], # 1
    [3, 2, 1], # 2
    ['#', 0, '*'] # 3
]

# [
# [00, 01, 02]
# [10, 11, 12]
#  [20, 21, 22]
#
#]

# r = 0, c = 0
# nums[r][c] = nums[0][0] = 9

# Create labels in a simple grid
for r in range(4): # rows = 4
    for c in range(3): # cols = 3 
        # lables = 4*3 = 12
        lbl = Label(root, text=nums[r][c], bg="#6cb7dc", relief="solid", width=8, height=2)
        lbl.grid(row=r, column=c, padx=5, pady=5)

# Start the GUI loop
root.mainloop()
