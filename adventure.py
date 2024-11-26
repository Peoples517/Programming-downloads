print('Welcome to this awesome adventure game!!!')
print('')
print('''You are a 17 year old oprhan. When you were 8 years old, your parents died in a car wreck. You were
then put into a orphanage and lived there for 6 years. At 14 years old, you decided that you couldn't take living
at the orphanage anymore. You left the orphanage and started your life on the street. You survived for 3 years scrounnging
anything you could get your hands on. One day a meteor crashed into your city. When scrounging for food, you dound a piece from
the meteor. As you picked it up, you started to feel weird. You passed out. When you woke up you discovered you now have super speed.''')

print('')

invalid_response = "You entered a invalid response. I'm sorry, but you are going to have to start over."

choice_one = input('Do you want to start fighting CRIME, HIDE your abilites, or SEEK a mentor? ').upper()

if choice_one == 'CRIME':
    print('''You decide to fight crime. You come across a dude stealing from a gas station. Using your super speed you easily defeat him.
You realize that was very easy since no one can do things anywhere near as fast as you.''')
    print('')
    crime_one = input('Do you decide to find more CRIMINALS to beat up or decide that fighting crime is too EASY and boring? ').upper()
    if crime_one == 'CRIMINALS':
        print('''You decide to keep fighting crime. You don't know your strength and speed that you accidentally kill one of the criminals. You realize
that you like the power you have.''')
        print('')
        criminals_one = input('Do you want to keep KILLING people or CONTROL yourself and not give in to your power? ').upper()
        if criminals_one == 'KILLING':
            print('You decide to keep killing criminals. You completely lose control and become a monster. Congragulations! You are a terrible person.')
        elif criminals_one == 'CONTROL':
            print('You are able to control yourself. Congratulations! You become a great hero.')
        else:
            print(invalid_response)
    elif crime_one == 'EASY':
        print('''You decide fighting crime is too easy. While you are saving everbody easily, you realize you
are so powerful that you can practically do whatever you want.''')
        print('')
        easy_one = input("Do you want to take over the WORLD or DROWN yourself so you can't ruin the world? " ).upper()
        if easy_one == 'WORLD':
            print('You use your power to take over world. Congratulations! You are a tyrant.')
        elif easy_one == 'DROWN':
            print('''You go to drown yourself but while you are doing it you can not bring yourself to do it. You go live in a cabin in the
mountains for the rest of your life. Enjoy your exsistence!''')
        else:
            print(invalid_response)
    else:
        print(invalid_response)
elif choice_one == 'HIDE':
    print('''You don't want to be more different than you already are so you decide to hide your new abilities. You decide you want to
make something of your life. You go to get a job.''')
    print('')
    hide_one = input('Do you want to get a NORMAL job or become a CRIMINAL? ').upper()
    if hide_one == 'NORMAL':
        print('''You get a job at a local juice stand. Throughout the years of your life you go from the bottom to the manager of the now juice store.
You end up inheritng the store fromm the owner, who has become a father figure to you.''')
        print('')
        normal = input('Do you want to RUN the business until your old age or SELL it? ').upper()
        if normal == 'RUN':
            print('You run this business until you are an old man. You never got married and never had a family. Congratualtions! You die a sad old man.')
        elif normal == 'SELL':
            print('You sell the bussiness and make a millions of dollars. Congratulations! You are alone and rich.')
        else:
            print(invalid_response)
    elif hide_one == 'CRIMINAL':
        print('You decide you might as well follow the other street kids and join organized crime.')
        print('')
        bad_guy = input('Do you want to become a drug DEALER or STEAL? ').upper()
        if bad_guy == 'DEALER':
            print('''You become a drug dealer. You are caught and about to be thrown in jail but then use your powers to get away.
Congratulations! You are a horrible person and are on the run.''')
        elif bad_guy == 'STEAL':
            print('''You decide to steal coins from a wishing fountian. It is not a very lucrative business. You decide to actual get a real job.
Congratualtions! You are a valuable member of society.''')
        else:
            print(invalid_response)
    else:
        print(invalid_response)
elif choice_one == 'SEEK':
    print('''You decide to find a mentor to help you through your new predicament. The only ever person you ever heard of that had
super speed was a here from the 90's called Velocity. The problem is no one has seem him this century.''')
    print('')
    seek_one = input('Do you try to FIND Velocity or GIVE up and accept he will never be seen again? ').upper()
    if seek_one == 'FIND':
        print('''You decide to search for Velocity. Since you have super speed, you run all around the Earth trying to find him but you never did.
A little while later a random dude shows up at you house saying that Velcity is in space and he can bring you to him.''')
        print('')
        find_one = input('Do you want go to SPACE or choose NOT to go to space? ' ).upper()
        if find_one == 'SPACE':
            print('You choose to go to space to find Velocity. After all your searching you never find him. Congratualtions! You are lost in space for forever.0')
        elif find_one == 'NOT':
            print('You choose to go the safe route and not go to space. Congratulations! You are a mediocre human being.')
        else:
            print(invalid_response)
    elif seek_one == 'GIVE':
        print('You give up on finding Velocity. You decide to put your energy into becoming a dart throwing champion.')
        print('')
        give = input('Do you want to use your POWERS in dart throwing or be a NORMAL person? ').upper()
        if give == 'POWERS':
            print('''You use your powers to become the dart throwing champion. The goverment catches you using your powers, kidnaps you, and uses you as a
test subject. Contragulation! You live the rest of your life in captivity as a lab rat.''')
        elif give == 'NORMAL':
            print("You follow the rules and don't use your powers. You become the dart throwing champion legally. Congratulations!. You are a good person.")
        else:
            print(invalid_response)
    else:
        print(invalid_response)
else: 
    print(invalid_response)