
# icon display for rock, paper and scissors
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

import random
option = ['rock', 'paper', 'scissors']

# user input 
your_option = int(input("What do you chose? Type 0 for Rock, 1 for Paper or 2 for Scissors: "))
your_selection = option[your_option]
print()

# To print the icon (rock, paper and scissors) as per user input
if your_selection == 'paper':
    print(paper)
elif your_selection == 'scissors':
    print(scissors)
else:
    print(rock)

print("Computer chose:")
computer_option = random.randint(0, len(option)-1)
computer_selection = option[computer_option]
print()

# To print the icon (rock, paper and scissors) randomly selected by computer
if computer_selection == 'paper':
    print(paper)
elif computer_selection == 'scissors':
    print(scissors)
else:
    print(rock)


# RULES OF THE GAME
# ---------------------
#Rock wins against scissors.
#Scissors win against paper.
#Paper wins against rock.

if (your_selection == 'rock') and (computer_selection == 'scissors'):
    print("You Win")
elif (your_selection == 'scissors') and (computer_selection == 'paper'):
    print("You Win")
elif (your_selection == 'paper') and (computer_selection== 'rock'):
    print("You Win")
elif your_selection == computer_selection:
    print("Draw")
else:
    print("You lose")


