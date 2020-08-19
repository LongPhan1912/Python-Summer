## Create a Python project of a Magic 8 Ball (fortune-telling or seeking advice).
# Allow the user to input their question.
# Show an in progress message.
# Create 10/20 responses, and show a random response. (Imma create 5)
# Allow the user to ask another question/advice or quit the game.
import time, sys, random
def magic_8_ball():
    question = input('Ask me anything! ')
    bank = dict()
    responses = ["Not just no, hell no!",
                 "I know, right?",
                 "Don't count on it.",
                 "The Universe says maybe.",
                 "I don't see why not.",
                 "Keep doing what you're doing and it'll happen.",
                 "Someday, but not today.",
                 "Pretty, pretty, pretty good!",
                 "Not so bad yourself.",
                 "Go with your guts.",
                 "Now is the wrong time to ask this question.",
                 "The answer is unknown.",
                 "Hang on, let me Google it.",
                 "Congratulations!",
                 "Yes, I believe that is the problem",
                 "Yes, that is true. All of it.",
                 "Go for it!",
                 "It is truly a mystery.",
                 "42. The answer is always 42.",
                 "Dew it!",
                 "Are you an angel?",
                 "Uh! So uncivilized!",
                 "Always two there are, no more, no less.",
                 "I don’t understand.",
                 "Please don't swear. Ask nicely.",
                 "You kiss your mama with that mouth?"
                 "STOP THIS MADNESS, IN THE NAME OF YOUR KING!",
                 "Fat? Fat, is it? Is that how you speak to your king? "
                 "Ah, damn you, Ned, why are you always right?",
                 "The Gods Mock The Prayers Of Kings And Cowards Alike.",
                 "How Long Can Hate Hold A Thing Together?"
                 ]
    for i in range(len(responses)): bank[i] = responses[i]
    STOP_POINT = 5
    while (STOP_POINT > 0):
        STOP_POINT -= 1
        # random_ans = bank[random.randint(0, len(responses))]
        # this will cause a key error (happens when a key is not in the dictionary)
        # instead use randrange (takes from a to b - 1 instead of a to b)
        random_ans = bank[random.randrange(0, len(responses))]

        # you could instead use:
        # random_ans = random.choice(bank)

        print(random_ans)
        onwards = input('Do you wish to continue? Please type Yes or No: ')
        if onwards.lower() == 'no' or onwards.lower() == 'n':
            print('\n\tThank you for playing Magic 8-Ball. Come again!\n')
            break
        elif onwards.lower() == 'yes' or onwards.lower() == 'y':
            question = input('Ask me something else! ')
            if STOP_POINT == 0:
                 time.sleep(1)
                 print('\n\tCooling down! Thinking...\n')
                 STOP_POINT = 5
            continue
        else:
            print("Please enter Y or Yes if you wish to continue; if not, type N or No")
            onwards = input('Do you wish to continue? Please type correctly this time: ')
            question = input('Ask me something else! ')

# Run the program:
magic_8_ball()
