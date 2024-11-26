#Beginning of the story:
#On your way to Tuesday devotional, you get distracted by  ------ and find yourself wandering aimlessly around the halls of the Snow Building. In an attempt to find your way out of the confusing labyrinth of hallways you open the door to the elevator and click a button. What button do you choose?  
#[choose a button] 
#The elevator whirs to life and you feel yourself moving quickly downwards. It feels like a long time before you feel it stop. As the doors slide open you see a small {insert color} man standing right outside the doors.  
#Option 1) You scream and quickly push a different button on the elevator 
#Outcome: The elevator takes you back upstairs. Lame. 
#Option 2) You step forward and ask him his name 

import time

player = input("What's your name player? ")
time.sleep(1)
print(f"Ah! I knew a {player.capitalize()} once, they were kind of a weirdo.")
time.sleep(1)
height = float(input("And how tall are you? "))

time.sleep(1)
if height <= 5.69:
    print(f"{height} Are you sure you're not a hobbit?")
elif 5.7 <= height <= 5.99:
    print(f"{height}! What a marvelous height!")
if height >= 6.0 >=7.0:
    print(f"{height}!! Oh we have a giant aye?!")
elif height >= 7.01:
    print(f"{height}...Is that even possible?")

time.sleep(1)
gender = ["man", "Man", "boy", "Boy", "male", "Male", "guy", "Guy", "woman", "Woman", "girl", "Girl", "female", "Female"]
gender_input = input("Now, what are you, a man or a woman? ")
while gender_input not in gender:
    time.sleep(1)
    print("Oh... Well... Let's try again. ")
    time.sleep(1)
    gender_input = input("Now, what are you, a man or a woman? ")
time.sleep(1)
print(f"Oh! You're a {gender_input}! Good to know!")

time.sleep(1)
print("Now, let's get this adventure started!")
time.sleep(1)
print("It is another beautiful Tuesday in Rexburg Idaho. Devotional is getting close to starting.") 
time.sleep(2)
print("You better get going! You make your way to the I-center for devotional, as you enter the building you see the elevator is available for use.")
time.sleep(2)
print("You make your way into the elevator and go to select the second floor, but what’s this? An extra button that has never been there before has appeared?")

#Choice 2
time.sleep(3)
print("Stretching before you is a long dirt path. It stretches so far into the horizon that you can’t see where it leads.") 
time.sleep(3)
print("“Where am I?” you wonder, “It’s almost as if I’m not even in Rexburg anymore”")
time.sleep(3)
print(f"You see {player.capitalize()}, there are many unanswered questions. The only way to get the answers you seek is to move forward.")
time.sleep(3)
print("To brave the unknown, and to trust that this elevator has your best interests at heart. Why else would you be here? The elevator hasn’t ever had that button before. It has chosen you.")
time.sleep(3)
print(f"At this time. So what will it be {player.capitalize()}. There is still time to go BACK to devotional. Or you could move FORWARD and accept your fate.")
time.sleep(2)

q2 = input("Go BACK or go FORWARD: ")
time.sleep(2)
if q2 == "back":
    print("You press the button to the second floor and the elevator doors close, a sense of relief washes over you. There is a sense of security in being lame and deciding to go devotional like everybody else. Let’s just hope the speaker doesn’t speak about dirt roads…")
elif q2 == "forward":
    print(f"YES!!! You have no idea how many people decide to turn back. It’s been quite boring. I’m glad there are people like you out there, {player.capitalize()}, we need more adventurers like yourself. ") 
