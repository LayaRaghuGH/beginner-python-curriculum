import random

# Problem 1
# Create a list of 4 car brands.
# Print the first and last.
# Then add another brand using append() and print the updated list.
brands = ["BMW", "Tesla", "Toyota","Lambhorgini"]
print("First car brand:", brands[0])
print("Second car brand:", brands[1])
brands.append("Ford")
print("After append", brands)

# Problem 2
# Create a list of 5 numbers.
# Print the number at index 2.
# Then insert a new number at index 2 and print the updated list.
numbers = [2. 3. 72, 10, 8]
print(numbers[2])
numbers.insert(2, 5) 
print("After insert at index 2:", numbers)


# Problem 3
# Create a list of 3 cities.
# Print the length of the list.
# Then use a for loop to print each city.
cities = ["Tokyo", "Paris", "New York"]

print("Length of the city list:", len(cities))

for city in cities:
    print(city)


# Problem 4
# Create a list of 6 file extensions.
# Print a random one.
# Then pop one at index 3 and print the updated list.
extensions = ["pdf", "docx", "pptx", "xlsx", "jpg", "mpg"]

random_ext = random.choice(extensions)
print("Random extension:", random_ext)

extensions.pop(3)
print("Updated extension list:", extensions)


# Problem 5
# Create a list of 8 names.
# Print the one at the middle index using len().
# Then use a for loop to print all the names.

names = ["Alice", "Bob", "Charlie", "David", "Emma", "Frank", "Grace", "Henry"]

print("Name at the middle index:", names[len(names) // 2])

for name in names:
    print(name)