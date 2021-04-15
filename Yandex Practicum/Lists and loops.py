print(" ")
print(" ")

print("**Структурирование и автоматизация** | Сбор данных | Формирование исходной таблицы")
print(" ")
print(" ")


print("Строки ")
heart = '❤️'
fire = '🔥'
shrug = '🤷'

print(heart)
print(fire)
print(shrug)
print(" ")
print(" ")


print("Строки")
grinning_row = ["Ухмыляюсь", "Grinning", 2.26, 1.02, 87.3]
print(grinning_row)

emojixpress = [2.26, 19.1, 25.6, 233.0, 15.2, 22.7, 64.6, 87.5, 6.81, 6.0]
# - у каждого значения в строке есть индекс, начинается индексация с 0
total = emojixpress[0]+emojixpress[1]+emojixpress[2]+emojixpress[3]+emojixpress[4]

print('{:.2f}'.format(total))
print(" ")
print(" ")


print("Автоматизация для списков - ниже идут циклы и прочее")
#Автоматизация для списков делается через циклы, присваивание со сложением, суммирование в цикле
print(" ")
print(" ")

print("Циклы")
print(" ")
twitter = [87.3, 150.0, 0.0, 2270.0, 264.0, 565.0, 834.0, 432.0, 0.0, 478.0]

print('Твиттер, млн')
print('------------')
for element in twitter:
    print(element)
print(" ")

emojixpress = [2.26, 19.1, 25.6, 233.0, 15.2, 22.7, 64.6, 87.5, 6.81, 6.0]

# количество всех эмодзи в миллионах
emojixpress_total = 1720

print('Доли эмодзи:')
# объявляем цикл
for element in emojixpress:
    part = element / emojixpress_total

    print('{:.1%}'.format(part))  # вставьте переменную part вместо многоточия

print()
print('Всего эмодзи: 1.72 млрд')

print(" ")
print(" ")

print("Присваивание со сложением")
#Присваивание со сложением осущетвляется через комбинацию +=.
#-= ; *= ; /= -
print(" ")
total_hands = 0

# эмодзи "Поцелуй"
total_hands += 0

# эмодзи "Класс"
total_hands += 1

# эмодзи "Катаюсь от смеха"
total_hands += 0

# эмодзи "Подмигиваю"
total_hands += 0

# эмодзи "Задумчивость"
total_hands += 1

# эмодзи "Пожимаю плечами"
total_hands += 2

print(total_hands)




emojixpress = [2.26, 19.1, 25.6, 233.0, 15.2]

# приравняйте переменную total к нулю
total = 0

# прибавьте значение с индексом 0
total += 2.26

# прибавьте значение с индексом 1
total += 19.1

# прибавьте значение с индексом 2
total += 25.6

# прибавьте значение с индексом 3
total += 233.0

# прибавьте значение с индексом 4
total += 15.2

print("total")
print('{:.2f}'.format(total))
print(" ")
print(" ")

print("Суммирование в цикле")
#Пр

emojixpress = [2.26, 19.1, 25.6, 233.0, 15.2]

total = 0
total += emojixpress[0]
total += emojixpress[1]
total += emojixpress[2]
total += emojixpress[3]
total += emojixpress[4]
print("total in format")
print('{:.2f}'.format(total))

print(" ")
print(" ")

emojixpress = [
    2.26,
    19.1,
    25.6,
    233.0,
    15.2,
    22.7,
    64.6,
    87.5,
    6.81,
    6.0,
    4.72,
    24.7,
    21.7,
    10.0,
    118.0,
    3.31,
    23.1,
    1.74,
    4.5,
    0.0333,
]
emojixpress_total = 1720

# Переменная для хранения суммы
# selected_total (англ. selected total, "сумма выбранного").
selected_total = 0
for count in emojixpress:
    selected_total += count

# Переменная для хранения доли
# selected_part (англ. selected part, "доля выбранного").
selected_part = selected_total / emojixpress_total
print('Доля выбранных эмодзи в EmojiXpress: {:.1%}'.format(selected_part))

print(" ")
print(" ")
twitter = [
    87.3,
    150,
    0.0,
    2270.0,
    264.0,
    565.0,
    834.0,
    432.0,
    0.0,
    478.0,
    198.0,
    654.0,
    98.7,
    445.0,
    1080.0,
    697.0,
    227.0,
    0.0,
    150.0,
    932.0,
]
twitter_total = 24500

selected_total = 0

for twitter_em in twitter:
    selected_total += twitter_em
selected_part = selected_total / twitter_total
print('Доля выбранных эмодзи в Твиттере: {:.1%}'.format(selected_part))
print(" ")
print(" ")



print("Списки списков")

# Выведение списка
data = [
    ['Ухмыляюсь', 2.26, 1.02, 87.3],
    ['Сияю от радости', 19.1, 1.69, 150.0],
    ['Катаюсь от смеха', 25.6, 0.774, 0.0],
    ['Слёзы радости', 233, 7.31, 2270.0],
    ['Подмигиваю', 15.2, 2.36, 264.0]
]
print(data)


# Вычислеие места числа в списке со списком

data = [
    ['Ухмыляюсь', 2.26, 1.02, 87.3],
    ['Сияю от радости', 19.1, 1.69, 150.0],
    ['Катаюсь от смеха', 25.6, 0.774, 0.0],
    ['Слёзы радости', 233.0, 7.31, 2270.0],
    ['Подмигиваю', 15.2, 2.36, 264.0]
]

print(data[3][2])

print(" ")
print(" ")