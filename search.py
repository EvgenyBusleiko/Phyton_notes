import easygui
from  easygui import *
import json
from record_new import *


def search_base():

    check = 1
    while check != 3:
        with open("base.json", 'r', encoding='utf-8') as fh:
            base = json.load(fh)
        choices = []
        choices.clear()
        for i in base.keys():

            choices.append(i)
        title = 'Найдены следующие заметки'
        msg = "Выберите нужную заметку"
        choise = easygui.choicebox(msg, title, choices)


        if choise!=None:
                msg = (f'{choise} \n {base.get(choise)}')

                title = "Что вы хотите сделать?"
                button = ['Удалить','Редактировать','Вернуться к списку найденных заметок', 'Вернуться в меню']
                check = indexbox(msg, title, button)
                if check == 0:
                    title = "Вы уверены, что хотите удалить?"
                    button = ['Да', 'Нет']
                    yes_no = ynbox(msg, title, button)
                    if yes_no == 1:
                        base.pop(choise)
                        with open("base.json", 'w', encoding='utf-8') as fh:
                            fh.write(json.dumps(base, ensure_ascii=False))
                        easygui.msgbox(f'Я успешно удалил запись {msg}')
                        choices.remove(choise)
                elif check==1:

                    add_record (choise,base.get(choise))

# search_base()



