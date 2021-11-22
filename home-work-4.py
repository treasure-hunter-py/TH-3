'''4. Створiть 3 рiзних функцiї (на ваш вибiр). Кожна з цих функцiй повинна повертати якийсь результат. 
Також створiть четверу ф-цiю, яка в тiлi викликає 3 попереднi, 
обробляє повернутий ними результат та також повертає результат. 
Таким чином ми будемо викликати 1 функцiю, а вона в своєму тiлi ще 3'''

def pow_two(x):
    return x ** 2

def pow_three(x):
    return x ** 3

def pow_four(x):
    return x ** 4

def my_pow_function(temp):
    print(pow_two(temp))
    print(pow_three(temp))
    print(pow_four(temp))

my_pow_function(int(input('число буде піднесено у степінь 2, 3, 4  = ')))
