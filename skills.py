import json
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
from vosk import KaldiRecognizer
from app import model, main
import fuzzywuzzy







def browser():
	'''Открывает браузер заданнный по уполчанию в системе с url указанным здесь'''

	webbrowser.open('https://www.google.com/webhp?hl=ru&sa=X&ved=0ahUKEwjIgqfw0cb6AhXPmosKHRV8AbcQPAgI', new=2)



def game():	
	exec(open('main.py').read())

        


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

import pyaudio
rec = KaldiRecognizer(model, 16000)
p = pyaudio.PyAudio()
stream =  p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8000)
stream.start_stream()


def listen():
	while True:
		data = stream.read(4000, exception_on_overflow=False)
		if (rec.AcceptWaveform(data)) and (len(data) > 0):
			answer = json.loads(rec.Result())
			if answer['text']:
				return answer['text']




def search():

	webbrowser.open_new_tab('https://www.google.com/search?q='+str(listen()))


def spotify():

	webbrowser.open('https://open.spotify.com/', new=2)




def bloknot():



	with open('spisok.txt', 'a', encoding="utf-8") as file:
		file.write(f'!{listen()}\n')

	return f'Задача {listen()} добавлена:)'