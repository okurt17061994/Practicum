emojixpress = [2.26, 19.1, 25.6, 233.0, 15.2, 22.7, 64.6, 87.5, 6.81, 6.0]

# количество всех эмодзи в миллионах
emojixpress_total = 1720

print('Доли эмодзи:')
# объявляем цикл
for element in emojixpress:
    part = element / emojixpress_total

    print('{:.2%}'.format(part))  # вставьте переменную part вместо многоточия

print()
print('Всего эмодзи: 1.72 млрд')