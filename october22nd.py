# while loops are good for conditions
"""
magic_number = 7
guess = 0

while guess != magic_number:
    guess = int(input("What's your guess, 1 through 10? "))
    if guess > magic_number: print("Too large!")
    elif guess < magic_number: print("Too small!")
    else: print("Congrats!")
"""
"""
keep_converting = "yes"

while keep_converting.lower() == "yes":
    fahrenheit = float(input("Enter temperature in Fahrenheit: "))

    celsius = (fahrenheit - 32) * 5/9

    if celsius > 30:
        weather = "Hot!"
    elif celsius < 10:
        weather = "Cold!"
    else:
        weather = "Nice!"
    print(f"{fahrenheit}F is {celsius:.1f}C - {weather}")

    keep_converting = input("Want to convert another temperature? ")
print("Thanks for using this code!")
"""

secret_password = "YourMom"
necessary_evil = 0

while necessary_evil != secret_password:
    necessary_evil = input("What's the password? ")
    if necessary_evil != secret_password:
        print("Nope! Try again!")
print("Congrats! You got it!")