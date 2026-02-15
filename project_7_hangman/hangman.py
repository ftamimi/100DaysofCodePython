import random
from hangman_art import hangman, title
from hangman_words import word_list

print(title)
lives = len(hangman)

special_word = random.choice(word_list)
# print(f'The chosen word is: {special_word}')

placeholder = ''
for letter in special_word:
    placeholder += '_'

print(placeholder)
correct_guessed = []
guessed = []
game_over = False

while not game_over:
    display = ''
    print(f'\n****** {lives} lives left ******')
    user_choice = input('Pick a letter?\n').lower()

    for i in special_word:
        if i == user_choice:
            display += i
            correct_guessed.append(i)
        elif i in correct_guessed:
            display += i
        else:
            display += '_'

    if user_choice in guessed:
        print(f'You have already guessed {user_choice}')

    else:
        if user_choice not in special_word:
            lives -= 1
            print(hangman[lives])
            print(f'Your guess of "{user_choice}" was not in the word\n You lose a life')

    guessed.append(user_choice)

    print(display)
    if '_' not in display or lives == 0:
        game_over = True

if game_over:
    print('\n')
    if lives == 0:
        print(f'****** You lose! ******\nThe word was {special_word}')
    else:
        print(f'****** You Win! ******\nThe word was {special_word}')