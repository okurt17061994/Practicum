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



