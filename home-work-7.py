'''7. Ну і традиційно -> калькулятор :) повинна бути 1 ф-цiя яка б приймала 3 аргументи - один з яких операцiя,
 яку зробити!'''

def my_calc(calc_data):
    if '+' in calc_data:
        x_and_y = calc_data.split(' + ')
        x_and_y = float(x_and_y[0]) + float(x_and_y[1])
        print(x_and_y)
    elif '-' in calc_data:
        x_and_y = calc_data.split(' - ')
        x_and_y = float(x_and_y[0]) - float(x_and_y[1])
        print(x_and_y)
    elif '*' in calc_data:
        x_and_y = calc_data.split(' * ')
        x_and_y = float(x_and_y[0]) * float(x_and_y[1])
        print(x_and_y)
    elif '/' in calc_data:
        x_and_y = calc_data.split(' / ')
        try:
            x_and_y = float(x_and_y[0]) / float(x_and_y[1])
            print(x_and_y)
        except ZeroDivisionError:
            print(' ERRORR X\0 =  ? --> 8')
data_user = input( '123 + 222, { - + * / }  x" "*" "y       ' )
my_calc(data_user)
