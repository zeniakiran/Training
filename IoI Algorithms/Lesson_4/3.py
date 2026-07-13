# Python program to calculate the sum of the first 20 natural numbers using a while loop

total_sum = 0
num = 1

while num <= 20:
    total_sum += num
    num += 1

print(f"The sum of the numbers : {total_sum}")