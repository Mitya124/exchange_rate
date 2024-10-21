import requests
import json
from tkinter import *
from tkinter import ttk


def generation_list_rates():
    answer = requests.get(f'https://v6.exchangerate-api.com/v6/daa09e68c25ef3ff1812b017/latest/RUB')
    json_info = answer.json()
    list_currency = list(json_info['conversion_rates'].keys())
    return list_currency

def func_exchange():
    code_target = combo_to.get()
    code_base = combo_from.get()
    if code_target and code_base:
        answer = requests.get(f'https://v6.exchangerate-api.com/v6/daa09e68c25ef3ff1812b017/latest/{code_base}')
        json_info = answer.json()
        if code_target in json_info['conversion_rates']:
            rez = json_info['conversion_rates'][code_target]
            content_l.config(text=f'1 {code_base} - {rez} {code_target}')
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

combo_from = ttk.Combobox(window, values=generation_list_rates())
combo_from.pack(pady=[10,10])

content_l = Label(window, text='Выберите код базовой валюты')
content_l.pack(pady=[10,10])

combo_to = ttk.Combobox(window, values=generation_list_rates())
combo_to.pack(pady=[10,10])

content_l_to = Label(window, text='Выберите код конечной валюты')
content_l_to.pack(pady=[10,10])

btn = Button(text='Конвертировать', command=func_exchange)
btn.pack(pady=[10,10])


window.mainloop()