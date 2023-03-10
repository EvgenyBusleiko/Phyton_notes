import easygui
from easygui import *
import json


def add_record(name,text):


    name_old = name


    msg = "Введите текст заметки"
    title = "Добавление новой заметки"

    type_vvod = multenterbox(msg, title, fields=["Название заметки", "Текст заметки"],values=[name,text])
    name = type_vvod[0]
    text = type_vvod[1]


    title = "Вы хотите сохранить заметку?"
    button = ['Да', 'Нет']
    yes_no = ynbox(name + "\n" + text, title, button)

    if yes_no == 1:
        with open("base.json", 'r', encoding='utf-8') as fh:
            base = json.load(fh)
        if name_old != '':
            base.pop (name_old)
        base.update({name: text})

        with open("base.json", 'w', encoding='utf-8') as fh:
            fh.write(json.dumps(base, ensure_ascii=False))

        msgbox('Я успешно записал в файл информацию: ' + "\n" + name + "\n" + text)



# add_record("","")
