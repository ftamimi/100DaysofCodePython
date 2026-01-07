print('''
                               _.--.
                        _.-'_:-'||
                    _.-'_.-::::'||
               _.-:'_.-::::::'  ||
             .'`-.-:::::::'     ||
            /.'`;|:::::::'      ||_
           ||   ||::::::'     _.;._'-._
           ||   ||:::::'  _.-!oo @.!-._'-.
           \'.  ||:::::.-!()oo @!()@.-'_.|
            '.'-;|:.-'.&$@.& ()$%-'o.'\\U||
              `>'-.!@%()@'@_%-'_.-o _.|'||
               ||-._'-.@.-'_.-' _.-o  |'||
               ||=[ '-._.-\\U/.-'    o |'||
               || '-.]=|| |'|      o  |'||
               ||      || |'|        _| ';
               ||      || |'|    _.-'_.-'
               |'-._   || |'|_.-'_.-'
                '-._'-.|| |' `_.-'
                    '-.||_/.-'
     
''')
print("Welcome to Treasure Island")
print("Your mission is to find the treasure")

win = False

response = input("You step out of the wooden hut, the path splits in front of you. Do you turn left or right? ").lower()
if response == "left":
    response = input("The sea looks rough today, will you swim or wait? ").lower()
    if response == "wait":
        response = input("As you waited the weather calmed down, " \
        "a friendly fisherman takes you across to the island. " \
        "\nYou go into the small, smelly hut, which has three doors inside. " \
        "Which door? red, yellow or blue? ").lower()
        if response == "yellow":
            print("You win! You found all the treasure!")
            win = True

if not win:
    print("Game over, more treasure for the others.")   
