import time  # We can use time.sleep() for pauses between messages 
import textwrap # To make the paragraphs more readable

print('''Hello and welcome! before you begin to play, we have some information
for you. The CAPITALIZED word will be your options in this game.''')
print(" ")
begin = input("Do you UNDERSTAND or NOT? ").upper()
if begin == "NOT":
    print("Ok well dont play then...")
    time.sleep(1)
    print("You must restart.")
    exit()
elif begin == "UNDERSTAND":
    print("You struck me as a smart individual.")
else:
    print("restart and come back when you can read (or spell).")
    exit()

print(" ")
name = input(str("Please name the player: "))
print(" ")
print (f"ah, I knew a, {name}, once! He was kind of a weirdo.")
print(" ")
color = input(str("What is the players favorite color?: "))
print(" ")
print (f"Care for some {color} eggs and ham?")
print(" ")
favorite_food = input(str("What is the players favorite food?: "))
print(" ")
print("if you insist...")
time.sleep(2)

# the text below is the very beginning of the story before any choices have been presented. 
#I couldn't figure out how to use the wrap text import so fel free to fix it if you want. 
print("It is another beautiful Tuesday in Rexburg Idaho. Devotional is getting close to starting. You better get going!")
print(" ")
print("You make your way to the I-center for devotional, as you enter the building you see the elevator is available for use.")
print("You enter the elevator and go to select the second floor, but what’s this?")
print("An extra button that has never been there before appeared? Which button do you choose?")


def print_wrapped(text, width=80):
    wrapped_paragraph = textwrap.wrap(text, width)
    for line in wrapped_paragraph:
        print(line)

def TIMELOOP():
    print_wrapped("\nTime is looping backwards... It's like déjà vu, but in reverse.\n")
    time.sleep(2)  # Adding a brief pause before restarting
    print_wrapped("Reverting to the start of the journey...\n")
    time.sleep(1)  # Pause before restarting
    ADVENTURE()  # This will call ADVENTURE() again to restart the game.

# \n is for fixing spacing between texts
def FLOOR2():
    print_wrapped("\nReally? Don’t you go to devotional every tuesday? Alright it’s your life. Go and get spiritually stronger, hope you don’t regret not clicking that button. What if it’s not there when you get back?\n")
    time.sleep(2)
    TIMELOOP()
def EXTRA():
    print_wrapped("\nThe elevator begins to descend. “That’s odd” you think to yourself, “I don’t think there is a basement.” the display where the number of the floor is supposed to be is not working. Odd symbols begin to appear. The elevator finally slows and the doors begin to open. \n")
def BACK():
    print_wrapped("\nas you press the button to the second floor and the elevator doors close, a sense of relief washes over you. There is a sense of security in being lame and deciding to go devotional like everybody else. Let’s just hope the speaker doesn’t speak about dirt roads…\n")
    time.sleep(2)
    TIMELOOP()
def FORWARD():
    print_wrapped(f"\nYES!!! You have no idea how many people decide to turn back. It’s been quite boring. I’m glad there are people like you out there, {name}, we need more adventurers like yourself. \n")
def CHECK():
    print_wrapped("\nThe melodies are just too beautiful. It would be a shame if you didn’t see what was going on. Walking through this forest towards the music gives you time to think about the deep and important things in life. Such as “Will I make it back in time for my classes?” and “I hope I have time for lunch.” \n")
    time.sleep(5)
    print_wrapped(f"You start to see something in the near distance. The song intensifies. It truly is the most exquisite song you’ve ever heard. You get close enough to see what it is. A perfectly prepared dish of {favorite_food} . The combination of the music and the food is so overwhelming it becomes hard to think. You just want to eat the dish. But you're still able to muster up one last logical thought before giving into your impulses. “Why would someone leave such a delicious dish out in the open?”\n")
def EAT():
    print_wrapped("\nJust can’t help it can you? Giving into your deepest and innate impulses all the time isn’t good for you, you know. Don’t you feel even the slightest bit of remorse? What about whoever made this dish? Obviously you are apathetic. All this eating has made you sleepy. The combination of this and the soothing tunes that play around you cause you to fall into a deep sleep.\n")
    time.sleep(5)
    print_wrapped("\nAs you sleep you start to dream. And what’s this? Oh joy, it's the elevator again. Upon your entrance to the elevator it’s different this time. There are no mysterious buttons, heck, there aren’t even any of the other floors buttons either. But the doors still close and the elevator still begins its ascension. “Where are you taking me?!” you shout, but no one can hear you. \n")
    time.sleep(5)
    print_wrapped(f"\nThe elevator's temperature rises, and a stream of sweat drips down your face. It begins to hurt and you start to panic. Your attempts to pry the doors open are in vain. “No.” you think. “This isn’t real.” You close your eyes and pinch yourself to get yourself to wake up. When you open your eyes, there is no elevator in sight. Unfortunately the burning sensation on your skin didn’t end with your dream. As you were asleep. Little {color} creatures tied you up and began cooking you over an open flame. \n")
    time.sleep(5)
    print_wrapped("Your only hope now is that these creatures will put an end to your torment quickly…  ")
    time.sleep(2)
    TIMELOOP()
def LEAVE():
    print_wrapped("\nAre you sure? I mean it’s right there!! How many times has a plate of {favorite food} appeared in front of you ripe for the taking?! In my opinion, this is a missed opportunity on your part. You make your way back to the dirt path. (go to continue after this one)  ")
    time.sleep(2)
    TIMELOOP()
def CONTINUE():
    print_wrapped(f"\nContinuing down the dirt path was the original goal in the first place. It would be wise for you to remember this. It’s often nice to take strolls down serene paths (even if you have a name like {name}. You enjoy breathing in the fresh air, The crunch of the dirt beneath your feet, and the excitement of the unknown path that stretches ahead. Of course there should also be a small sense of fear looming in the back of your head. You know, the little voice that goes over every possible wrong scenario that could happen. The one that tries to use logic and reasoning to help calm you down and carefully make your next move…\n")
    time.sleep(5)
    print_wrapped("The one that reminds you that this dirt path was not your original goal. ")
    time.sleep(5)
    print_wrapped("But who needs all that noise!! ")
    time.sleep(5)
    print_wrapped("\nWe are finally getting somewhere on this path. There is a building off in the distance. It looks large and gray. Almost as if it’s made of cobblestone, and has a faint castle shape that is still a bit hard to make out from here. But alas, before you can get any closer, a fork in the road appears. It seems you have been faced with another choice. Do you dare to travel down yet another unknown road? Or keep heading towards the castle that draws near?\n")
def CASTLE():
    print_wrapped("\nSeems like a sensible option. Why take more risks than you need to in one day? And looky here, you have found yourself standing at the castle gates. They begin to creak open, and you make your way to the front gates. Which are conveniently unlocked. Maybe they knew you were coming? Did the elevator notify the tenants of this land? I guess we can’t really ask it can we. \n")
    time.sleep(5)
    print_wrapped("\nThere is a grand staircase that leads up to an astounding piece of artwork. Its complexity is found in its simplicity. It is a painting of the very dirt road you took to get here with a small gray outline of the cobblestone castle off in the distance. Which reads in a shiny bronze plaque at the bottom “Not all those who wander are lost.” \n")
    time.sleep(5)
    print_wrapped("\n“Maybe I really have been chosen for something” you whisper to yourself. “Something bigger and more important than I could even understand until I get there.”")
    time.sleep(5)
    print_wrapped("\nWell that’s a nice thought but I think it’s time to move on. You're not going to figure it out by standing here. ")
    time.sleep(5)
    print_wrapped("\nThere is another staircase that leads to a higher level of the castle. This castle is cool and all, but it could just be more of the same, dimly lit mumbo jumbo that you’ve already experienced. You know there was that other path outside you decided to pass up the first time.\n")
def UNKNOWN():
    print_wrapped(f"\nI commend the bravery. It’s one thing to brave one unfamiliar road in a day. But TWO? Some may even call it a little stupid. This path leads you out of the trees. And at the end of it, a sword with a {color} hilt lies cemented into stone. Engraved into the front of the great boulder it reads: “Sometimes the detours are the path.” \n")
    time.sleep(5)
    print_wrapped("\nAmazing, simply amazing! Look like you have found where you were always meant to end up. I mean it says it right there. Go ahead, pick up the sword and claim your prize.\n")
    time.sleep(5)
    print_wrapped("\nYou step onto the rock and pull with all your might. The sword immediately slips out and you wield it high above your head. Almost at that exact moment. An earth shattering rumbling begins all around you. This is it, your big moment. The very reason you’re here.\n")
    time.sleep(5)
    print_wrapped("\nA giant arm formed from large boulders emerges from the ground. Then another, then a leg, face, and entire body. A huge golem made from pebbles, boulders, and stones stands directly in front of you. Towering your small frame. \n")
    time.sleep(5)
    print_wrapped("\nAn epic battle ensues. You dodge its attacks, slicing boulders in half as they are slung towards you. But it’s no match for you. You run up one of its arms and with one great swing of your sword kindly relieve the monstrosity of its own head. I guess this is what you were chosen for. To protect this land from this hardened monster. Some questions still lie unanswered of course. Such as “who sent this mysterious elevator”, “Why was I needed to slay this beast’, “Where in the world am I”, or even… “Who has been narrating this story?”.\n")
    time.sleep(5)
    print_wrapped("\nBut alas, I’m afraid that some answers are better left to the imagination. For better or for worse. The only thing that you should be concerned about now is if the elevator is still there… \n")
def STAIRCASE():
    print_wrapped("\nNo I don't want you to do that...\n")
    print_wrapped("\nUmmmm...\n")
    print_wrapped("\nYou die of dysentery...\n")
    time.sleep(2)
    TIMELOOP()
def UMBRELLA():
    print_wrapped("You seem to have forgotten your umbrella... and now the sky has fallen on your head")
def VICTORIOUS():
    print_wrapped("\nYou Win?\n")
    print_wrapped("\nGAME OVER\n")
    TIMELOOP()
def UNLIKELY():
    time.sleep(1)
    print("\nWhat? just what did you do?")
    time.sleep(1)
    print("\nWHY DID THAT WORK?")
    time.sleep(1)
    print("\nYou win... please don't come back\n.")
    time.sleep(2)
    TIMELOOP()

def QUIT():
    # Function to handle the quit condition
    print("\nGAME OVER")
    print("\nThanks for playing!\n")
    exit()

def REPLAY():
    Replay = input(str("\nWould you like to play again? ")).upper()
    if Replay == "YES":
        ADVENTURE()
    if Replay == "NO":
        exit()

def FIRST_CHOICE():
        Answer1 = ["FLOOR", "EXTRA", "QUIT", "I WIN"]
        Choice1 = "none"
        while Choice1 not in Answer1:
            Choice1 = input(str("\nFLOOR or EXTRA button? (type QUIT to quit) ")).upper()
            if Choice1 == "FLOOR":
                FLOOR2()
            elif Choice1 == "EXTRA":
                EXTRA()
                SECOND_CHOICE()
            elif Choice1 == "QUIT":
                QUIT()
            elif Choice1 == "I WIN":
                VICTORIOUS()
            else:
                print("Thats not a viable answer...")
   
def SECOND_CHOICE():
        Answer2 = ["BACK", "FORWARD", "QUIT", "UP", "DOWN"]
        Choice2 = "none"
        while Choice2 not in Answer2:
            Choice2 = input(str("\nGo BACK or move FORWARD? (type QUIT to quit) ")).upper()
            if Choice2 == "BACK":
                BACK()
            elif Choice2 == "FORWARD":
                FORWARD()
                THIRD_CHOICE()        
            elif Choice2 == "QUIT":
                QUIT()
            elif Choice2 == "UP":
                UNLIKELY()
            elif Choice2 == "DOWN":
                UNLIKELY()
            else:
                print("Thats not a viable answer...")
   
        
def THIRD_CHOICE():
        Answer3 = ["CHECK", "CONTINUE", "QUIT"]
        Choice3 = "none"
        while Choice3 not in Answer3:
            Choice3 = input(str("\nCHECK or CONTINUE? (type QUIT to quit) ")).upper()
            if Choice3 == "CHECK":
                CHECK()
                THIRD_CHOICE_ONE()        
            elif Choice3 == "CONTINUE":
                CONTINUE()
                FOURTH_CHOICE()
            elif Choice3 == "QUIT":
                QUIT()
            else:
                print("Thats not a viable answer...")
   

def FOURTH_CHOICE():
        Answer4 = ["UNKNOWN", "CASTLE", "QUIT"]
        Choice4 = "none"
        while Choice4 not in Answer4:
            Choice4 = input(str("\nUNKNOWN or CASTLE? (type QUIT to quit) ")).upper()
            if Choice4 == "UNKNOWN":
                UNKNOWN()
            elif Choice4 == "CASTLE":
                CASTLE()
                FOURTH_CHOICE_ONE()
            elif Choice4 == "QUIT":
                QUIT()
            else:
                print("Thats not a viable answer...")
   

def FIFTH_CHOICE():
        Answer5 = ["STAIRCASE", "UNKNOWN", "QUIT"]
        Choice5 = "none"
        while Choice5 not in Answer5:
            Choice5 = input(str("\nSTAIRCASE or UNKNOWN? (type QUIT to quit) ")).upper()
            if Choice5 == "STAIRCASE":
                STAIRCASE()
            elif Choice5 == "UNKNOWN":
                UNKNOWN()
            elif Choice5 == "QUIT":
                QUIT()
            else:
                print("Thats not a viable answer...")
   
        
def THIRD_CHOICE_ONE():
        Answer3_1 = ["I FORGOT MY UMBRELLA", "EAT", "LEAVE", "QUIT"]
        Choice3_1 = "none"
        while Choice3_1 not in Answer3_1:        
            Choice3_1 = input(str("\nThe choice is yours. DO you want to EAT the dish or LEAVE it be? (type QUIT to quit) ")).upper()
            if Choice3_1 == "I FORGOT MY UMBRELLA":
                UMBRELLA()
            if Choice3_1 == "EAT":
                EAT()
            elif Choice3_1 == "LEAVE":
                LEAVE()
            elif Choice3_1 == "QUIT":
                QUIT()
            else:
                print("Thats not a viable answer...")
   

def FOURTH_CHOICE_ONE():
        Answer4_1 = ["UNKNOWN", "STAIRCASE", "QUIT"]
        Choice4_1 = "none"
        while Choice4_1 not in Answer4_1:
            Choice4_1 = input(str("\nWould you like to go to the UNKNOWN path or go up the STAIRCASE? (if you select unknown go to it) [type QUIT to quit]")).upper()
            if Choice4_1 == "UNKNOWN":
                UNKNOWN()
            elif Choice4_1 == "STAIRCASE":
                STAIRCASE()
            elif Choice4_1 == "QUIT":
                QUIT()
            else:
                print("Thats not a viable answer...")
   

# Run the game
def ADVENTURE(): # I did this just in case so that the order of the code wouldn't make the code wonky
     while True:
        FIRST_CHOICE()

ADVENTURE()
print("Thanks for playing!\n ")
time.sleep(5)
REPLAY()
 

print("Now that you have completed our game, please take a moment to give us some feedback.")
print(f"Your feedback is valued and important to us, {name}, so please be honest. ")

desired_answer = "none"
while desired_answer != "10":
    interview = input("Please rate this game out of 10. ")
    if interview == "10":
        print("\nYour response has been submitted. :\n)")
        exit()
    elif interview != "10":
        print("\nNo\n")