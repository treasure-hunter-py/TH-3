'''1. Створити цикл від 0 до ... (вводиться користувачем). В циклі створити умову, 
яка буде виводити поточне значення, якщо остача від ділення на 17 дорівнює 0.'''
num_user = int(input('0,...N '))
for i in range(num_user):
    if i%17 == 0:
        print(i)
