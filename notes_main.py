#начни тут создавать приложение с умными заметками
from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

import json

notes = {
    'Добро пожаловать !' : {
        'текст' : "Это самое лучшие приложение для заметок в мире !",
        'теги' : ['добро', 'инструкция']
    },
    'Создатель' : {
        'текст' : "Алхимов Ростислав Амборцумович, является создателем этой программы.",
        'теги' : ['програмист', 'алгоритмика']
    },
    'Поддержка' : {
        'текст' : "Если вы хотите поддержать меня или ускорить разработку проэкта.\nВот ссылка:https://www.donationalerts.com/r/romanjo020",
        'теги' : ['пж', 'спс']
    }
}
"""
with open("notes_data.json", 'w', encoding='utf-8') as file:
    json.dump(notes, file, ensure_ascii=False, indent=4)
"""
app = QApplication([])
ui = uic.loadUi('untitled1.html')
ui.show()

def show_note():
    key = ui.zamet.selectedItems() [0].text()
    print(key)
    ui.textEdit.setText(notes[key]['текст'])
    ui.teg.clear()
    ui.teg.addItems(notes[key]['теги'])

def add_note():
    note_name,ok = QInputDialog.getText(ui, 'Добавить заметку', 'Название заметки:')
    if ok and note_name != "":
        notes[note_name] = {'текст' : "" ,'теги' : []}
        ui.zamet.addItem(note_name)
        ui.teg.addItems(notes[note_name]['теги'])
        print(notes)

def save_note():
    if ui.zamet.selectedItems():
        key = ui.zamet.selectedItems()[0].text()
        notes[key]['текст'] = ui.textEdit.toPlainText()
        with open("notes_data.json", 'w', encoding='utf-8') as file:
            json.dump(notes, file, ensure_ascii=False, indent=4)
        print(notes)
    else:
        print('Заметка для сохранений не выбранна!')

def del_note():
    if ui.zamet.selectedItems():
        key = ui.zamet.selectedItems()[0].text()
        del notes[key]
        ui.zamet.clear()
        ui.teg.clear()
        ui.textEdit.clear()
        ui.zamet.addItems(notes)
        with open("notes_data.json", 'w', encoding='utf-8') as file:
            json.dump(notes, file, ensure_ascii=False, indent=4)
        print(notes)
    else:
        print('Заметка для удаления не выбрана!')

def add_tag():
    if ui.zamet.selectedItems():
        key = ui.zamet.selectedItems()[0].text()
        tag = ui.poisk.text()
        if not tag in notes[key]['теги']:
            notes[key]['теги'].append(tag)
            ui.teg.addItem(tag)
            ui.textEdit.clear()
        with open("notes_data.json", 'w', encoding='utf-8') as file:
            json.dump(notes, file, ensure_ascii=False, indent=4)
        print(notes)
    else:
        print('Заметка для добавления тега не выбрана!')

def del_tag():
    if ui.teg.selectedItems():
        key = ui.zamet.selectedItems()[0].text()
        tag = ui.teg.selectedItems()[0].text()
        notes[key]['теги'].remove(tag)
        ui.teg.clear()
        ui.teg.addItems(notes[key]['теги'])
        with open("notes_data.json", 'w', encoding='utf-8') as file:
            json.dump(notes, file, ensure_ascii=False, indent=4)
    else:
        print('Тег для удаления не выбран!')



ui.otkrp.clicked.connect(del_tag)
ui.dob.clicked.connect(add_tag)        
ui.udal.clicked.connect(del_note)
ui.sohr.clicked.connect(save_note)
ui.zamet.itemClicked.connect(show_note)
ui.sozd.clicked.connect(add_note)
with open('notes_data.json', 'r', encoding='utf-8') as file:
    notes = json.load(file)
ui.zamet.addItems(notes)

app.exec_()