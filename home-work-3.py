'''3. Написати функцiю season, яка приймає один аргумент — номер мiсяця (вiд 1 до 12), яка буде повертати пору року, 
якiй цей мiсяць належить (зима, весна, лiто або осiнь)'''

def season(numb_mans):
    temp_position = ''
    if numb_mans in [1, 2, 12]:
        temp_position = 'зима'
    elif numb_mans in [3, 4, 5]:
        temp_position = 'весна'
    elif numb_mans in [6, 7, 8]:
        temp_position = 'літо'
    elif numb_mans in [9, 10, 11]:
        temp_position = 'осінь'
    return temp_position

#print(str(season(int(input('номер місяця - '))))) не знаю где грань между можно и нельзя так что розпишу
num = int(input('номер місяця - '))
num_res = season(num)
print(num_res)



