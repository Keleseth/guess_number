from random import randint
print('Угадайте число от 1 до 100')
a = randint(1, 100)
while True:
    int_input_guess = int(input())
    if int_input_guess > a:
        print('«Ваше число больше того, что загадано»')
    elif int_input_guess < a:
        print('«Ваше число меньше того, что загадано»')
    else:
        print('Отличная интуиция! Вы угадали число :)')
        break
    