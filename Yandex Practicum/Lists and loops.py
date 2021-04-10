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


print("Автоматизация для списков")
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




