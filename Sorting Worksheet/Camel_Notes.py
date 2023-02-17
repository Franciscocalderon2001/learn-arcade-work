# # Variables used in the example ``if`` statements
# a = 4
# b = 5
#
# # Basic comparisons
# if a < b:
#     print("a is less than b")
#
# if a > b:
#     print("a is greater than b")
#
# print("Done")
#
# if a == 1:
#     print("If a is one, this will print.")
#     print("So will this.")
#
# print("This will always print because it is not indented.")
# print("This will generate an error. Why it is indented?")

# done = False
#
# while not done:
#     x=input("What do you want boss?").lower()
#     if x == 'quit':
#         print("I quit")
#         done = True
#     elif x=='lunch':
#         print("Great. I'm famished.")
#     elif x=='work':
#         print("no thanks")
#         break
#     print("Thanks a lot")

# # Get input from the user
# temperature = input("What is the temperature in Fahrenheit? ")
#
# # Convert the input to an integer
# temperature = int(temperature)
#
# # Do our comparison
# if temperature > 90:
#     print("It is hot outside.")

# # or you can re-write like this...
# # Get input from the user
# temperature = int(input("What is the temperature in Fahrenheit? "))
#
# # Do our comparison
# if temperature > 90:
#     print("It is hot outside.")

# temperature = int(input("What is the temperature in Fahrenheit? "))
# if temperature > 90:
#     print("It is hot outside")
# elif temperature < 30:
#     print("It is cold outside")
# else:
#     print("It is not hot outside")
# print("Done")

# temperature = int(input("What is the temperature in Fahrenheit? "))
# if temperature > 110:
#     print("Oh man, you could fry eggs on the pavement!")
# elif temperature > 90:
#     print("It is hot outside")
# elif temperature < 30:
#     print("It is cold outside")
# else:
#     print("It is ok outside")
# print("Done")

user_name = input("What is your name? ")
if user_name == "Paul":
    print("You have a nice name.")
else:
    print("Your name is ok.")

