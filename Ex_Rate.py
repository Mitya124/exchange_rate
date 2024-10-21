import requests
import json
from tkinter import *
from tkinter import ttk


def generation_list_rates():
    answer = requests.get('https://v6.exchangerate-api.com/v6/daa09e68c25ef3ff1812b017/latest/USD')
    json_info = answer.json()
    list_currency = list(json_info['conversion_rates'].keys())
    return list_currency

def func_exchange():
    code = combo.get()
    if code:
        answer = requests.get('https://v6.exchangerate-api.com/v6/daa09e68c25ef3ff1812b017/latest/USD')
        json_info = answer.json()
        if code in json_info['conversion_rates']:
            rez = json_info['conversion_rates'][code]
            content_l.config(text=f'1 RUB - {rez} {code}')
            content_l.config(bg='green')
        else:
            content_l.config(text='Такого кода валюты не существует')
            content_l.config(bg='red')
    else:
        content_l.config(text='Код валюты не введён')
        content_l.config(bg='red')



window = Tk()
window.title('Курс валют')
window.geometry('400x400')



combo = ttk.Combobox(window, values=generation_list_rates())
combo.pack(pady=[10,10])

content_l = Label(window, text='Выберите код валюты')
content_l.pack(pady=[10,10])

btn = Button(text='Получить курс рубля', command=func_exchange)
btn.pack(pady=[10,10])


window.mainloop()