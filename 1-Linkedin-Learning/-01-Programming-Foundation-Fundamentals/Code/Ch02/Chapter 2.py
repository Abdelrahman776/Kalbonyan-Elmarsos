# Make the user read "Hi, what's your name? " then he can write his name
name = input("Hi, what's your name? ")
# the same but here for the age
age = int(input("How old are you? "))
# check the age by using if 
if (age < 13):
    print("You're too young to register", name)
else:
    print("Feel free to join", name)    