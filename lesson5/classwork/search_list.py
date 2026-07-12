fruits = ["banana", "apple", "cherry", "orange"]

flag = False # assume there is no apple in our list
for i in range(len(fruits)): # Go through each index in out=r list
    if fruits[i] == "apple": # If the cureent item is aplle
        flag = True # Update our guess to true
        break # Exit the loop after finding
print(flag)

if "apple" in fruits: # Python shortcut
    print("Found apple")
else:
    print("No apples found")

