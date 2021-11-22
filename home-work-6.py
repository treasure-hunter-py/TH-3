'''6. Маємо рядок --> "f98neroi4nr0c3n30irn03ien3c0rfekdno400wenwkowe00koijn35pijnp46ij7k5j78p3kj546p465jnpoj35po6j345" -> просто потицяв по клавi
   Створіть ф-цiю, яка буде отримувати рядки на зразок цього, яка оброблює наступні випадки:
-  якщо довжина рядка в діапазонi 30-50 -> прiнтує довжину, кiлькiсть букв та цифр
-  якщо довжина менше 30 -> прiнтує суму всiх чисел та окремо рядок без цифр (лише з буквами)
-  якщо довжина бульше 50 - > ваша фантазiя'''
def trash_calc(temp_str):
    if len(temp_str) < 30:
        sum_num = 0
        sum_str = ''
        for item_num in range(len(temp_str)):
            if temp_str[item_num].isdigit() == True:
                sum_num += int(temp_str[item_num])
        print(sum_num)
        for item_str in range(len(temp_str)):
            if temp_str[item_str].isalpha() == True:
                sum_str += temp_str[item_str]
        print(sum_str)
    elif 30 <= len(temp_str) <= 50:
        kol_num_items = 0
        kol_str_items = 0
        for item_num in range(len(temp_str)):
            if temp_str[item_num].isdigit() == True:
                kol_num_items += 1
        print(kol_num_items)
        for item_str in range(len(temp_str)):
            if temp_str[item_str].isalpha() == True:
                kol_str_items += 1
        print(kol_str_items)
    elif len(temp_str) > 50:
        print(temp_str[::-1])


#                                              hardCode test

#magisters_work = "f98neroi4nr0c3n30irnf98neroi4nr0c3n30irnf98neroi4nr0c3n30irnf98neroi4nr0c3n30irnf98neroi4nr0c3n30irnf98neroi4nr0c3n30irnf98neroi4nr0c3n30irnf98neroi4nr0c3n30irn"
#magisters_work = 'f98neroi4nr0cf98neroi4nr0cf98neroi4nr0c'
#magisters_work = 'f98neroi4nr0c'

magisters_work = input('pls dropped your face in keyboard   x _ X  ')
trash_calc(magisters_work)

