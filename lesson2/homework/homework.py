# Homework Problem 1
# Ask the user for two numbers.
# Print their quotient and remainder on separate lines.
num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))
print(num1 // num2)
print(num1 % num2)

# Homework Problem 2
# Ask the user for their favorite animal and favorite color.
# Print a sentence combining them like: "A blue tiger would be awesome!"
animal = input("What is your favourite animal: ")
color = input("What is your favorite color: ")
print("A", color, animal, "would be awesome!")


# Homework Problem 3
# Use a for loop to print all the even numbers from 0 to 10 (including 10).
for i in range(0, 11):
    print(i)


# Homework Problem 4
# Ask the user how many push-ups they can do.
# Multiply it by 7 and print how many they could do in a week.
pushups = int(input("How many push-ups can you do: "))
print("You can do", pushups * 7, "a week")



# Homework Problem 5
# Use a for loop to print the square of each number from 1 to 6.
# (Example: 1*1=1, 2*2=4, etc.)
for i in range(1, 7):
    print(i * i)
