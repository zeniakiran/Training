#Input a word or sentence
string = input("Please enter text : ")

reversed = ('')
#loop for printing in reverse 
for i in string:
    reversed = i + reversed
    
print("\nThe Original Text = ", string)
print("The Reversed Text = ", reversed)
