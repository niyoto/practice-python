print("Welcome to the Quiz game")

response = input("Do you want to play?: ")

if response.lower() != "yes":
    quit()
print("Let's play :)")

count = 0
answer = input("What does CPU stand for?: ")
if answer.lower() == "central processing unit":
    print("Correct!")
    count += 1
else:
    print("Incorrect!")

answer = input("What does GPU stand for?: ")
if answer.lower() == "graphics processing unit":
    print("Correct!")
    count += 1
else:
    print("Incorrect!")

answer = input("What does PSU stand for?: ")
if answer.lower() == "power supply":
    print("Correct!")
    count += 1
else:
    print("Incorrect!")

print(f"you got {count} ({(count/3 * 100)}%) correct!")

