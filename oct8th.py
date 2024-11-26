import time



print("Hello! Welcome to Python Cafe!")
name = input("What is your name? ")

if name == "Ben":
    print("Get out Evil Ben!!")
    exit()
else:
    print(f"Hello {name}! How can I help you today?")
time.sleep(2)
print("We have coffee, tea, hot chocolate, pastries, pretty much anything you'd expect from a cafe.")


x = int(input("Pick a random number between 1 through 10: "))
if x == 7:
    print("Boring answer")
elif x == 4:
    print("Now that's an answer.")
else:
    print(f"Interesting, didn't think you'd pick {x}")


if int(input("What number is bigger than 3? ")) > 3:
    print("Yup, it's true!!")
    time.sleep(1)
    print("Still true!")
else:
    print("Nope, very much not true.")