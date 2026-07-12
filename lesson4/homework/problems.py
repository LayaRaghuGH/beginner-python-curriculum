import random

# Problem 1
# Create a list of 3 operating systems.
# Print the last one using len().
# Then reverse the list and print it.
operating_systems = ["Windows", "Apple", "Mac"]
print("Last element:", operating_systems[len(operating_systems) - 1])
operating_systems.reverse()
print("After reverse:", operating_systems)


# Problem 2
# Create a list of 4 school subjects.
# Print the second subject.
# Then sort them alphabetically and print the result.
subjects = ["Math", "English", "Science", "Social Studies"]
print("Second subject:", subjects[1])
subjects.sort
print("After sort:", subjects)

# Problem 3 
# Create a list of 5 error codes.
# Print how many there are.
# Then use a for loop to print each error code.
error = [404, 500, 1064, "0x7B", 403]
print(len(error))
for i in range(len(error)):
    print(error[i])


# Problem 4 
# Create a list of 2 programming languages.
# Print a random one.
# Then append another language and print the list.
lang = ["Javascript", "Python"]
length = len(lang)

random_index = random.randint(0, length - 1) # 

random_lang = lang[random_index]
print("Random lang:", random_lang)
lang.append("C++")
print("Current state:", lang)


# Problem 5
# Create a list of 6 passwords.
# Print the one in the middle using len().
# Then remove the first password in the list and print it.
passwords = []