from ascii_art import art
import random
random_num = random.randint(1, 101)


print(f'{art}\nWelcome to the Number Guessing Game!\n')

def game():
  difficulty_level = input("Choose a difficulty. Type 'easy' or 'hard': ")
  user_num = int(input("I'm thinking of a number between 1 and 100: "))

  ''' Set difficulty level '''
  if difficulty_level == 'easy':
    chances = 9
  elif difficulty_level == 'hard':
    chances = 4
    
  ''' chances user_num and random_num '''
  while chances > 0:
    if user_num == random_num:
      return f'\nYou got it! The answer was {random_num}\n'
    elif user_num > random_num:
      print(f'\nToo high. Guess again. You have {chances} attempt(s) remaining to guess the number.')
      user_num = int(input('Make a guess: '))
    elif user_num < random_num:
      print(f'\nToo low. Guess again. You have {chances} attempt(s) remaining to guess the number.')
      user_num = int(input('Make a guess: '))
    chances -= 1
    
    ''' Results based on chances '''
    if chances == 0 and user_num != random_num:
      return f"\nYou've ran out of guesses, you lose. The answer was {random_num}\n"
    elif chances == 0 and user_num == random_num:
      return f'\nYou got it! The answer was {random_num}\n'
  
print(game())