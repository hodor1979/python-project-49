import prompt
from random import randint   ### числа для игры будут генерироваться случайно

print('Answer "yes" if the number is even, otherwise answer "no".')
for i in range(0, 3):
  x = randint(1, 100)
  if x % 2 == 0:
   correct_answer = "yes"
  else:
    correct_answer = "no"
  print('Question: ',x)
  user_answer = prompt.string('Your answer: ')
  if user_answer == correct_answer:
      print('Correct!')
      if i ==2:
          print(f'Congratulations, {name}!')
      continue
  else:
    print(f"'{user_answer}' is wrong answer /;(./ Correct answer was {correct_answer}.")
    print(f"Let's try again, {name}!")  
    break
