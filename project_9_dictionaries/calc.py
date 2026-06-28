from art import calc

def question_1():
    response = input('What is the first number? ')
    return response

def question_2():
    for symbol in operations.keys():
        print(symbol)
    response = input('Pick an operation: ')
    return response

def question_3():
    response = input('What is the second number? ')
    return response

def add(first_number, second_number):
    return first_number + second_number

def subtract(first_number, second_number):
    return first_number - second_number

def multiply(first_number, second_number):
    return first_number * second_number

def divide(first_number, second_number):
    return first_number / second_number

def operation(first_number, operation, second_number):
    result = operations[operation](first_number, second_number)
    print(f'{float(first_number)} {operation} {float(second_number)} = {float(result)}')
    return result

operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide
}



def main(starting_number):
    print(calc)

    if starting_number == 0.0:
        starting_number = float(question_1())
    operation_symbol = question_2()
    second_number = float(question_3())

    total = operation(starting_number, operation_symbol, second_number)
    carry_on = input(f'Type "y" to continue calculating with {float(total)} or type "n" to start with a new calculation: ')
    if carry_on.lower() == 'y':
        main(total)
    else:
        main(0.0)
    

        
        

if __name__ == '__main__':
    starting_number = 0.0  
    main(starting_number)
    