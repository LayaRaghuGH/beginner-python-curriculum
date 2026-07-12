numbers = [5, -8, 35, -3, 6, 2]
print(numbers)

total = sum(numbers) # shorcut to find sum
print("The sum of these numbers is:", total)

print("Our algorithm:")
total = 0
for i in range(len(numbers)): # Go through each index in the  list
    item = numbers[i] # Get the numbers at this index
    total = total + item # Add it to the running total
print("The sum is:", total)


# Find the sum of only positive numbers
total = 0
for i in range(len(numbers)): # Go through each index in our list
    item = numbers[i] # Get the number at this index
    if item > 0: # Postitive means > 0
        total = total + item # Add it  to the running total
        
