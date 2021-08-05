import random
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
game_images = [rock, paper, scissors] # list of variable rock paper and scissors 
user_choice = int(input("Enter 0 for rock , 1 for paper and 2 for scissors. "))
print(game_images[user_choice])
# random number between 0 to 2 chose by computer 
computer_chose = random.randint(0, 2)
print('computer chose: ')
print(game_images[computer_chose])

if user_choice>=3 or user_choice<0:  # if user enter invalid number 
    print('You typed invalid number, you lose!\U0001F611 \U0001F611 \U0001F611') # ascii code for emoji is used 
elif user_choice==0 and computer_chose== 2: # first check for scissors 
    print('You Win! \U0001F929')
elif user_choice==2 and computer_chose== 0:
    print("you lose. \U0001F44E")
elif computer_chose>user_choice:   # paper is lose by scissors and rock is lose by paper 
    print("You lose. \U0001F44E")
elif computer_chose == user_choice: #if both chose same then it's draw 
    print("It's a draw.\U0001F91D")



