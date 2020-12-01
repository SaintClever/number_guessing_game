from ascii_art import art
from random import randint
random_num = randint(1, 101)


print(f'{art}\nWelcome to the Number Guessing Game!\n')


def difficulty_level():
  ''' Set difficulty level '''
  easy_or_hard = input("Choose a difficulty. Type 'easy' or 'hard': ")
  if easy_or_hard == 'easy':
    chances = 9
  elif easy_or_hard == 'hard':
    chances = 4
  return chances

    
def user_numbers(chances):
  ''' chances user_num and random_num '''
  user_num = int(input("I'm thinking of a number between 1 and 100: "))
  while chances > 0:
    if user_num > random_num:
      print(f'\nToo high. Guess again. You have {chances} attempt(s) remaining to guess the number.')
      user_num = int(input('Make a guess: '))
    elif user_num < random_num:
      print(f'\nToo low. Guess again. You have {chances} attempt(s) remaining to guess the number.')
      user_num = int(input('Make a guess: '))
    if user_num == random_num:
      return f'\nYou got it! The answer was {random_num}\n'
    chances -= 1
    
    
    ''' Results based on chances '''
    if chances == 0 and user_num != random_num:
      return f"\nYou've ran out of guesses, you lose. The answer was {random_num}\n"
    elif chances == 0 and user_num == random_num:
      return f'\nYou got it! The answer was {random_num}\n'
  
  
print(user_numbers(difficulty_level()))