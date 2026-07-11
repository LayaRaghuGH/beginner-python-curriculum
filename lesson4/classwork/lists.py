colors = ["red", "green", "blue", "yellow"] # Create a list

print(colors)

print("First color:", colors[0])
print("Second color:", colors[1])
print("Third color:", colors[2])
print("Fourth color:", colors[3])

# length of list - 1 or below 

colors.append("orange") # adds element to the end of the list
print("After append", colors[4])

colors.insert(2, "purple") # Inserts into list and pyushes all the others forward
print("After insert at index 2:", colors)

colors.remove("green") # Removes the color
print("After removing green:", colors)

popped_color = colors.pop()
print("Popped color:", popped_color)
print("After pop:", colors)

popped_color_at_index = colors.pop(1)
print("OPopped color at index 1:", popped_color_at_index)
print("After pop at index 1:", colors)

index_of_blue = colors.index("blue")
print("Index of blue:", index_of_blue)

colors.append("blue")
blue_count = colors.count("blue")
print("Count of blue:", blue_count)
print("Current state:", colors)

colors.sort() # alphabetical order
print("After sort:", colors)

colors.reverse()
print("After revers:", colors)

print("Length of the list:", len(colors))
print("Last element:", colors[len(colors) - 1])
