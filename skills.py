import os
import webbrowser
import sys
import subprocess
from apikey import API_TOKEN
import voice
import requests		
from bs4 import BeautifulSoup as b
import random
import re


def browser():
	'''Открывает браузер заданнный по уполчанию в системе с url указанным здесь'''

	webbrowser.open('https://www.google.com/webhp?hl=ru&sa=X&ved=0ahUKEwjIgqfw0cb6AhXPmosKHRV8AbcQPAgI', new=2)


# def game():
# 	'''Нужно разместить путь к exe файлу любого вашего приложения'''
# 	try:
# 		open.r(main.py)
# 	except:
# 		voice.speaker('Путь к файлу не найден, проверьте, правильный ли он')


def offpc():
	#Эта команда отключает ПК под управлением Windows

	os.system('shutdown \s')
	print('пк был бы выключен, но команде # в коде мешает;)))')


def weather():
	'''Для работы этого кода нужно зарегистрироваться на сайте
	https://openweathermap.org или переделать на ваше усмотрение под что-то другое'''
	# try:
	params = {'q': 'Bishkek', 'units': 'metric', 'lang': 'ru', 'appid': 'd99fdfe2133e692f8c1e41f784b47a90'}
	response = requests.get(f'https://api.openweathermap.org/data/2.5/weather', params=params)
		# if not response:
		# 	raise
	w = response.json()
	voice.speaker(f"На улице {w['weather'][0]['description']} {round(w['main']['temp'])} градусов")
		
	# except:
	# 	voice.speaker('Произошла ошибка при попытке запроса к ресурсу API, проверь код')


def offBot():
	'''Отключает бота'''
	sys.exit()


def passive():
	'''Функция заглушка при простом диалоге с ботом'''
	pass


# URL = 'https://www.anekdot.ru/last/good/'


# def pas():
# 	r = requests.get(url)
# 	soup = b(r.text, 'html.parser')
# 	response = requests.get(soup.find_all('div', class_='text'))
# list_of_jokes = pas(URL)
# random.shuffle(list_of_jokes)
#     # return [c.text for c in  response]
 
#     voice.speaker(str(pas)) 

# # list_of_jokes = pas_anekdots(URL)
# # random.shuffle(list_of_jokes)
def search():
    call = input('Введите ссылку или запрос: ')
    if re.search(r'\.', call):
        webbrowser.open_new_tab('https://' + call)
    elif re.search(r'\ ', call):
        webbrowser.open_new_tab('https://yandex.ru/search/?text='+call)
    else:
        webbrowser.open_new_tab('https://yandex.ru/search/?text=' + call) 

