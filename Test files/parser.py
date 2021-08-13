# Вызываем библиотеки BeautifulSoup и Selenium
# По Selenium выходит ошибка. Решение - https://qna.habr.com/q/519260
from bs4 import BeautifulSoup
import requests
import csv
import time

#header = {'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36 OPR/76.0.4017.177'}

# Сохраняем URL в переменную
url= "https://11letopita.ru/katalog/kuxni-na-zakaz/"
#url= "https://e-mebel.net.ua/kuhni/"

# отправляем запрос к странице
page = requests.get(url)
# думаю нужно запустить цикл чтобы он по пагинационным страницам
# гулял и собирал ссылки?
#for page in range(1, 5000):
    #pagination = f'?page={page}'
    #url = small_url + pagination
    #html = get_html(url)
    #time.sleep(2)

#создадим список - думаю туда запихать урлы кухонь
#all_kuhni_url = []
#print(page.status_code)

#скармливаем ему наш page, указав в кавычках как он нам поможет 'html.parcer':
soup = BeautifulSoup(page.text, "html.parser")

# указываем тег, который нужно собрать со страници
all_kuhni_url = soup.findAll('div', class_='category-title')
#all_kuhni_url = soup.findAll('div', class_='product-layout product-grid col-lg-4 col-md-4 col-sm-6 col-xs-12')

for data in all_kuhni_url:
    print(data)

#def pars_content(small_url):
    #root = 'https://11letopita.ru/katalog/kuxni-na-zakaz/'

    #for page in range(1, 5000):
        #pagination = f'?page={page}'
        #url = small_url + pagination



#responce = requests.get(link, headers = header).txt
#soup = BeautifulSoup(responce, 'lxml')
#blok = soup.find_all('???')

# Check js
#check_js = blok.finde('div, id = 'javascript_check')
#status_js = check_js.find_all('span')[1].text
#result_js = f'javascript: {status_js}

# Check flash
#check_flash = blok.finde('div, id = 'flash_version')
#status_flash = check_flash.find_all('span')[1].text
#result_flash = f'javascript: {status_flash}

# Check flash
#check_user = blok.finde('div, id = 'user_agent').text

#rint(check_user)