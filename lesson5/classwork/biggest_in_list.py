nums = [9, 10, 4, 1, 3, 17]
print(nums)

# You can use built in shortcuts Python funstions to find the largest and smallest in list
biggest_item = max(nums)
smallest_item = min(nums)

print("The biggest item:", biggest_item)
print("The smallest item:", smallest_item)

print("Our algorithm:")

biggest = nums[0] # Start by assuming the first item is the biggest
for i in range(len(nums)): # Go through each item in our list
    if nums[i] > biggest: # if we find bigger update our guess
        biggest = nums[i]
print("The biggest item is", biggest)
