import random
from hangman import hangmans, words

word = words[random.randint(0,2)]
display = []
lives = 6
print(word)
for letter in word:
  display.append('_')

while ('_' in display) and lives > 0:
  users_letter = input('Give me a letter:\n\t').lower()
  if (users_letter in word) and (not users_letter in display):
    print('Your Letter is in the hidden word.')
    for i in range(len(word)):
      if users_letter == word[i]:
        display[i] = users_letter
  elif users_letter in display:
    print('You have already tried this letter.')
  else:
    lives -= 1
    print('Your Letter is not in the hidden word.')
  print(hangmans[lives])
  print(display)
else:
  if (not '_' in display):
    print('You win')
  else:
    print(hangmans[lives])
    print('You are out of lives.\nYou lose.')