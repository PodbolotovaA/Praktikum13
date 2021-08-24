tickets = int(input('Введите количество билетов, кторое вы хотите приобрести:\nПри покупке более 3х билетов предоставляется скидка 10%\n '))
result = 0
count = 0
for i in range(tickets):
    age = int(input('Введите возраст:\n'))
    if 0 <= age < 18:
        print('До 18 лет вход бесплатно')
        result += 0
        count += 1
    elif 18 <= age < 25:
        print('Стоимость одного билета 990 руб.')
        result += 990
        count += 1
    elif 25 <= age < 999:
        print('Стоимость одного билета 1390 руб.')
        result += 1390
        count += 1
    else:
        print('Введите возраст')
if count < 3:
    print('Общая стоимость приобретаемых билетов (', count, '), составляет', result, 'руб. ')
else:
    count > 3
    result=int(result-(result*0.1))
    print('Общая стоимость приобретаемых билетов (', count, '), составляет', result, 'руб. ')