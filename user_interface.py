import easygui
from easygui import *
import json
from search import *
from record_new import *
from change import *


def menu():
    output=''
    while output != "Выход":
        msg = "Выберите пункт меню"
        title = "Меню"
        choices = ["Просмотр списка заметок", "Добавить новую заметку", "Выход"]
        output = easygui.choicebox (msg, title, choices,callback=None)

        if output == "Просмотр списка заметок":
            search_base()


        elif output == "Добавить новую заметку":

            add_record("", "")


        elif output == "Выход":
            exit()


menu()
