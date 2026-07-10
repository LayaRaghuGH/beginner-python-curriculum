age = int(input("How old are you: "))
if age >= 18:
    print("You can vote!")
print("Vote check complete!")

temp = int(input("What's the temperature outside: "))

if temp < 70:
    print("It's cold, wear a jacket.")
else:
    print("No jacket needed")
print("Weather check complete!")

day = input("What day of the week is it: ")

score = int(input("What is your score out of 100: "))

if score >= 60:
    print("You passed!")
    if score >= 90:
        print("You got an A!")
else: 
    print("You did not pass :( ")
print("Grading check complete")
    
