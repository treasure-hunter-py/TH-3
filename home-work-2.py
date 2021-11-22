'''2. Користувачем вводиться початковий і кінцевий рік. 
Створити цикл, який виведе всі високосні роки в цьому проміжку (границі включно).'''

def year_checker(temp):
    if temp%400 == 0:
        print(temp)
    elif temp%4 == 0 and temp%100 != 0:
        print(temp)

year_in_user_start =  int(input('enter start year '))
year_in_user_end = int(input('enter finish year '))
for i in range(year_in_user_start, year_in_user_end + 1):
    year_checker(i)

