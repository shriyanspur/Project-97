import random

print()
print('NUMBER GUESSING GAME')
print()
print('Guess the number (between 1 and 10)')
print()

answer = random.randint(1, 10)
chances = 5
guess = int(input('Enter your guess: '))

while chances <= 5:
  chances = chances - 1

  if guess == answer:
    print('Congratulations, You Guessed it Right !!!!')
    break

  if not guess == answer:
    print()
    print("Try Again, the number wasn't ", guess)

    if chances >= 2:
      print(chances, ' chances left')
    elif chances == 1:
      print(chances, ' chance left')

    print()
    print()
    guess = int(input('Enter your guess: '))

    if chances <= 0:
      print('You Failed to Guess the Number, You Lose !!!')
      print('The Number was: ', answer)
      break