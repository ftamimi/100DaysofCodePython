import random, sys

rock = '''

     .-.___
----/ \\ )__)
  (  (/()___)
        ()__)
----(___()_)
'''

paper = '''
      .-.
     / /_______
----/   )______)
  (    ()_______)
        ()_____)
----(___()____)
'''

scissors = '''

    .-.________
----/ \\ )______)
  (  ( ()_______)
        ()__)
----(___()_)
'''

choice = int(input('What do you choose? Type 0 for Rock, 1 for Paper and 2 for Scissors\n'))
options = [rock, paper, scissors]

if choice >= 0 and choice <=2:
    print(options[choice])
else:
    print('Invalid choice!')
    sys.exit()


ai_choice = random.randint(0, 2)

print('\nI Chose\n')

print(options[ai_choice])

if (choice == 0 and ai_choice == 2) or (choice == 1 and ai_choice == 0) or (choice == 2 and ai_choice == 1):
    print('\nYou Win!')
elif choice == ai_choice:
    print('\nDraw!')
else:
    print('\nI Win!')