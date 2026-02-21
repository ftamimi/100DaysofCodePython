from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(logo)



def ceasar():
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    original_text = input("Type your message:\n").lower()
    shift_amount = int(input("Type the shift number:\n"))

    shifted = ''
    if direction == 'decode':
        shift_amount *= -1

    for letter in original_text:
        if letter in alphabet:
            index = alphabet.index(letter)
            # print(f'letter: {letter}')
            # if direction == 'encode':
            #     new_index = index + shift_amount
            # elif direction == 'decode':
            #     new_index = index - shift_amount

            # better option is to minus if decoding by * -1, shown above

            new_index = index + shift_amount
            new_index = new_index % len(alphabet)

            shifted += alphabet[new_index]
        else:
            shifted += letter
    print(f'Here is the {direction}d result: {shifted}')
    again = input('Do you want to go again? (yes or no) ')
    if again == 'yes':
        ceasar()

    return shifted


ceasar()
