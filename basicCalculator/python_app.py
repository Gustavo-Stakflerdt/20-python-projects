def add(a, b):
    answer = a + b
    print(f'{str(a)} + {str(b)} = {str(answer)}')


def sub(a, b):
    answer = a - b
    print(f'{str(a)} - {str(b)} = {str(answer)}')


def mul(a, b):
    answer = a * b
    print(f'{str(a)} x {str(b)} = {str(answer)}')


def div(a, b):
    answer = a / b
    print(f'{str(a)} / {str(b)} = {str(answer)}')


while True:
    print('-=' * 20)
    print('A. Addition')
    print('B. Subtraction')
    print('C. Multiplication')
    print('D. Division')
    print('Or press any other key to exit')
    print('-=' * 20)

    choice = input('Enter your choice: ')

    match choice.lower():
        case 'a':
            print('Addition')
            a = int(input('Enter the first number: '))
            b = int(input('Enter the second number: '))
            add(a, b)
        case 'b':
            print('Subtraction')
            a = int(input('Enter the first number: '))
            b = int(input('Enter the second number: '))
            sub(a, b)
        case 'c':
            print('Multiplication')
            a = int(input('Enter the first number: '))
            b = int(input('Enter the second number: '))
            mul(a, b)
        case 'd':
            print('Division')
            a = int(input('Enter the first number: '))
            b = int(input('Enter the second number: '))
            div(a, b)
        case _:
            print('See you later!')
            break
