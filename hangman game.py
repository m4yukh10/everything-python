import random
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''']
word_list = ["ardvark", "baboon", "camel","hello", "meow", "web3", "Drake"]
word_choice = word_list[random.randint(0,len(word_list) - 1)]
open_list = []
correct_list = []
game_end = False
for i in word_choice:
    open_list.append("_")
print(open_list)
guess_limit = 6
for j in word_choice:
    correct_list.append(j)
stage_index = len(stages)
while guess_limit>0:
    index_m = 0
    a = input("guess the letter: ").lower()
    for j in word_choice:
        if a == j:
            open_list[index_m] = a
        index_m+=1
    print(open_list)
    if a not in word_choice:
        stage_index -= 1
        print("You guessed the wrong alphabet! You lose 1 life..")
        print(stages[stage_index - 1])
    else:
        print(stages[stage_index - 1])      
    guess_limit -= 1       
    if open_list == correct_list and guess_limit >= 0:
        game_end = True
        break
if game_end == True:
    print("You Win!")
else:
    print("You Lose!")    

                   
