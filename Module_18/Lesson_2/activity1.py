#input an integer value 
number = int(input("Enter the number to find its sum: "))
sum=0

#Iterates for n+1 times: i=1 to n+1
for i in range(1, number+1): 
  sum = sum+i
  print("\nSum =", sum)
