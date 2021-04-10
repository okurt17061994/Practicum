print(" ")
# - ПРИМЕРЫ ПРОСТЫХ ВЫЧИСЛЕНИЙ
# - пример простых вычислительных операций

print("ПРИМЕРЫ ПРОСТЫХ ВЫЧИСЛЕНИЙ")
print(2 + 5 * 4 / 2 - 8 + 3 * (3 + 2))
print(" ")

print(" ")
print("Возведение в степень = 2 ** 2 = ")
print(2 ** 2) # - возведение в степень
print(" ")
print(" ")


# - ПЕРЕМЕННЫЕ И ОПЕРАЦИИ С НИМИ
# число носителей английского
english_native = 378.2
# число говорящих на английском
english_speakers = 1121
# число носителей русского
russian_native = 153.9
# число говорящих на русском
russian_speakers = 264.3

# число выучивших язык как второй
english_second = english_speakers - english_native
russian_second = russian_speakers - russian_native

# конкатенация для вывода результата с описанием
print("english_second / russian_second = " + str(english_second / russian_second))

# - ИСПОЛЬЗОВАНИЕ ПЕРЕМЕННЫХ
print("ИСПОЛЬЗОВАНИЕ ПЕРЕМЕННЫХ")
english = 378.2
russian = 153.9
german = 76.0
chinese = 908.7
top3_total =(english + russian + german)
print("top3_total = " + str(chinese - top3_total))
print(" ")
print(" ")

# - ТИПЫ ДАННЫХ
print(type(english))  # - будет выдан результат - <class 'int'>
# - дробные числа имеют другой тип данных — float
german_web_percent = 6
print(type(german_web_percent))
german_web_percent_2 = 6.0
print(type(german_web_percent_2))
print(" ")
print(" ")

russian_web_part = 0.061
web_popular = 10000000
russian_web_popular = russian_web_part * web_popular

print("russian_web_popular и его тип")
print(russian_web_popular)
print(type(russian_web_popular))
print(" ")
print(" ")

#ПРЕОБРАЗОВАНИЕ ТИПОВ
russian_native_millions = 153.9
russian_native = int(russian_native_millions * 1000000)
print("russian_native = ")
print(russian_native)
#Преобразовать тип данных из float в integer - перевод типа данных из float в integer следующим способом

#print(int(russian_native_millions * 1000000))

print(" ")
print(" ")
print("Языки в онлайне и оффлайне ")
total_web = 10
total_speakers = 7539

chinese_speakers = 1107
chinese_web_part = 0.017
print("chinese_web_part = " + str(chinese_web_part))

english_speakers = 1121
english_web_part = 0.539
print(english_web_part)

russian_speakers = 264.3
russian_web_part = 0.061
print(russian_web_part)
print(" ")
print(" ")

#ПЕЧАТЬ НА ОДНОЙ СТРОКЕ
print("Печать на одной строке")
total_web = 10
total_speakers = 7539

chinese_speakers = 1107
chinese_web_part = 0.017

chinese_speakers_part = chinese_speakers / total_speakers
print('Доля людей, говорящих на китайском:', chinese_speakers_part)

english_speakers = 1121
english_web_part = 0.539

english_speakers_part = english_speakers / total_speakers
print('Доля людей, говорящих на английском:', english_speakers_part)

russian_speakers = 264.3
russian_web_part = 0.061

russian_speakers_part = russian_speakers / total_speakers
print('Доля людей, говорящих на русском:', russian_speakers_part)
print(" ")
print(" ")

print("Функция format()")

chinese_speakers = 1107
print('Число людей, говорящих на китайском: {} млн'.format(chinese_speakers))

total_web = 10
total_speakers = 7539

chinese_speakers = 1107
chinese_web_part = 0.017

english_speakers = 1121
english_web_part = 0.539

russian_speakers = 264.3
russian_web_part = 0.061

chinese_speakers_part = chinese_speakers / total_speakers
print('Доля людей, говорящих на китайском: {:.1%}'.format(chinese_speakers_part))

english_speakers_part = english_speakers / total_speakers
print('Доля людей, говорящих на английском: {:.2%}'.format(english_speakers_part))

russian_speakers_part = russian_speakers / total_speakers
print('Доля людей, говорящих на русском: {:.3%}'.format(russian_speakers_part))
print(" ")
print(" ")

print("Оформление текста")
total_web = 10
total_speakers = 7539

chinese_speakers = 1107
chinese_web_part = 0.017

english_speakers = 1121
english_web_part = 0.539

russian_speakers = 264.3
russian_web_part = 0.061

chinese_speakers_part = chinese_speakers / total_speakers
print('--- Китайский язык ---')
print('Доля говорящих на языке: {:.1%}'.format(chinese_speakers_part))
print()
english_speakers_part = english_speakers / total_speakers
print('--- Английский язык ---')
print('Доля говорящих на языке: {:.1%}'.format(english_speakers_part))
print()
russian_speakers_part = russian_speakers / total_speakers
print('--- Русский язык ---')
print('Доля говорящих на языке: {:.1%}'.format(russian_speakers_part))
print(" ")
print(" ")

print("Языки в офлайне и в онлайне: завершение")
total_web = 10
total_speakers = 7539

chinese_speakers = 1107
chinese_web_part = 0.017

english_speakers = 1121
english_web_part = 0.539

russian_speakers = 264.3
russian_web_part = 0.061

chinese_speakers_part = chinese_speakers / total_speakers
chinese_web_sites = chinese_web_part * total_web
chinese_index = 1000 * chinese_web_sites / chinese_speakers
print('--- Китайский язык ---')
print('Доля говорящих на языке: {:.1%}'.format(chinese_speakers_part))
print('Доля сайтов с языком: {:.1%}'.format(chinese_web_part))
print('Индекс проникновения в интернет: {:.2f}'.format(chinese_index))
print()

english_speakers_part = english_speakers / total_speakers
english_web_sites = english_web_part * total_web
english_index = 1000 * english_web_sites / english_speakers
print('--- Английский язык ---')
print('Доля говорящих на языке: {:.1%}'.format(english_speakers_part))
print('Доля сайтов с языком: {:.1%}'.format(english_web_part))
print('Индекс проникновения в интернет: {:.2f}'.format(english_index))
print()

russian_speakers_part = russian_speakers / total_speakers
russian_web_sites = russian_web_part * total_web
russian_index = 1000 * russian_web_sites / russian_speakers
print('--- Русский язык ---')
print('Доля говорящих на языке: {:.1%}'.format(russian_speakers_part))
print('Доля сайтов с языком: {:.1%}'.format(russian_web_part))
print('Индекс проникновения в интернет: {:.2f}'.format(russian_index))
print()
