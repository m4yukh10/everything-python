#password_generator(easy)
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
           'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['1','2','3','4','5','6','7','8','9']
symbols = ['!', '#', '$', '&', '(',')', '*','+']
merged = [letters,numbers,symbols]
wanted_letters = int(input("how many letters you want in your password? \n"))
wanted_symbols = int(input("how many symbols would you like in your password? \n"))
wanted_numbers = int(input("how many numbers would you like in your password? \n"))
len_letters = 0
for alpha in letters:
      len_letters+=1
len_nums = 0
for nums in numbers:
      len_nums+=1
len_sym = 0
for sym in symbols:
      len_sym+=1
rand_letter = ""
for i in range(wanted_letters):
      letter_choice = letters[random.randint(0,len_letters-1)]
      rand_letter = rand_letter + letter_choice
rand_number = ""
for j in range(wanted_numbers):
      num_choice = numbers[random.randint(0,len_nums-1)]
      rand_number = rand_number + num_choice
rand_sym = ""      
for k in range(len_sym):
      sym_choice = symbols[random.randint(0,len_sym-1)]
      rand_sym = rand_sym + sym_choice

full_password = rand_letter + rand_number + rand_sym
print(f"Your password is {full_password}")

      
