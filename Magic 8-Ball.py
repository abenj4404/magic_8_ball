# define variables
name = input("What is your name, traveler?")
print("Why hello, " + name + ".")
question = input("I sense you seek my knowledge. What would you like to know?")
print("Let me look into the ether.")
print("Hmm...")
answer = ""



# print(random_number)
import random
random_number = random.randint(1, 10)



# Set up possible responses
if random_number == 1:
    print("Yes, most definitely.")
elif random_number == 2:
    print("It shall be so.")
elif random_number == 3:
    print("Without a doubt, yes.")
elif random_number == 4:
    print("My vision isn't clear, ask again.")
elif random_number == 5:
    print("My sources say ask again later.")
elif random_number == 6:
    print("Better not to tell you.")
elif random_number == 7:
    print("My sources say probably not.")
elif random_number == 8:
    print("The outlook is not so good.")
elif random_number == 9:
    print("Very doubtful, my friend.")
elif random_number == 10:
    print("The answer is quite ominous, so perhaps I should not say...")
else:
    print("Something is not right. You must go immediately and come back later.")

