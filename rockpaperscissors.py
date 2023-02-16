#a sinple-player rock paper scissors game made by me..
import random
n = int(input("What do you choose? Type 0 for Rock, 1 for Paper and 2 for scissors: "))
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
comp_choice = random.randint(0,2)
if n == 0:
      print(f"you chose:\n{rock}")
      if comp_choice == 2:
            print(f"the computer chose:\n{scissors}")
            print("You win")
      if comp_choice == 1:
            print(f"the computer chose:\n{paper}")
            print("The computer wins!")
elif n == 1:
      print(f"you chose:\n{paper}")
      if comp_choice == 0:
            print(f"the computer chose:\n{rock}")
            print("You win!")
      if comp_choice == 2:
             print(f"the computer chose:\n{scissors}")
             print("The computer wins") 
elif n == 2:
      print(f"you chose:\n{scissors}")
      if comp_choice == 0:
            print(f"the computer chose:\n{rock}")
            print("The computer wins!")
      if comp_choice == 1:
            print(f"the computer chose:\n{paper}")
            print("You win!")                                                     
