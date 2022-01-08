import random

answer = int(input("guess number between 1 and 200: "))
# if answer.isdigit():
#     if 0 >= answer >= 200:
#         print("Please type a number between 0 and 200")
#         quit()
# #elif int(float(answer)).isdigit:
#  #   if 0 >= answer >= 200:
#   #      print("Please type a number between 0 and 200")
#    #     quit()
# else:
#     print("Please type a number next time")
#     quit()

random_number = random.randrange(1,5)

while random_number != answer:
    answer = input("guess number between 1 and 200: ")
    continue

    


# if random_number != answer:
#     print("Correct!")
# elif random_number > answer:
#     print("The number guessed is lower")
#     print(f"The correct number is {random_number}")
# else:
#     print("The number guessed is higher")
#     print(f"The correct number is {random_number}")
    

# import random

# top_of_range = input("Type a number: ")

# if top_of_range.isdigit():
#     top_of_range = int(top_of_range)

#     if top_of_range <= 0:
#         print('Please type a number larger than 0 next time.')
#         quit()
# else:
#     print('Please type a number next time.')
#     quit()

# random_number = random.randint(0, top_of_range)
# guesses = 0

# while True:
#     guesses += 1
#     user_guess = input("Make a guess: ")
#     if user_guess.isdigit():
#         user_guess = int(user_guess)
#     else:
#         print('Please type a number next time.')
#         continue

#     if user_guess == random_number:
#         print("You got it!")
#         break
#     elif user_guess > random_number:
#         print("You were above the number!")
#     else:
#         print("You were below the number!")

# print("You got it in", guesses, "guesses")