# Imports random module to use later in script
import random

# Declaring variables for use in if statement below
name = "Pudgers"
question = "Will we win the HGTV Dream Home?"
answer = ""
random_number = random.randint(1, 9)

# If statement to determine answer from Magic 8 Ball
if random_number == 1:
  answer = "Yes - definitely."
elif random_number == 2:
  answer = "It is decidedly so."
elif random_number == 3:
  answer = "Without a doubt."
elif random_number == 4:
  answer = "Reply hazy, try again."
elif random_number == 5:
  answer = "Ask again later."
elif random_number == 6:
  answer = "Better not tell you now."
elif random_number == 7:
  answer = "My sources say no."
elif random_number == 8:
  answer = "Outlook not so good."
elif random_number == 9:
  answer = "Very doubtful."
else:
  answer = "Error"

# Prints results of submission and answer
print(name + " asks: " + question)
print("Magic 8-Ball's answer: " + answer)