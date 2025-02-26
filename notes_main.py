from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QTextEdit, QLineEdit, QListWidget, QInputDialog
import json

'''notes_list = {
    'Добро пожаловать!':
    {
        'текст':'В этом приложении можно создавать заметки с тегами',
        'теги':['умные заметки', 'инструкция']
        
    }
}

with open('notes_data.json', 'w', encoding = 'utf-8') as file:
    json.dump(notes_list, file)
'''
app = QApplication([]) #виджет приложение


main_win = QWidget() #виджет главное окно

notes = QTextEdit() #виджет для текста заметки
search_tags = QLineEdit() #виджет для ввода поиска по тегам и добавление тега
create_notes = QPushButton('Создать заметку')
delete_notes = QPushButton('Удалить заметку')
saves_notes = QPushButton('Сохранить заметку')
add_to_a_notes = QPushButton('Добавить к заметке')
detach_from_the_note = QPushButton('Открепить от заметки')
search_for_notes_by_tag = QPushButton('Искать заметки по тегу')
list_tags = QListWidget() #виджет для списка тегов
list_notes = QListWidget() #виджет для списка заметок
text_tags = QLabel('Список тегов')
text_notes = QLabel('Список заметок')
main_horizontal = QHBoxLayout()
horizontal2 = QHBoxLayout()
horizontal3 = QHBoxLayout()
horizontal4 = QHBoxLayout()
horizontal5 = QHBoxLayout()
horizontal6 = QHBoxLayout()
horizontal7 = QHBoxLayout()
horizontal8 = QHBoxLayout()
horizontal9 = QHBoxLayout()
horizontal10 = QHBoxLayout()

vertical1 = QVBoxLayout()
vertical2 = QVBoxLayout()

vertical1.addWidget(notes)
horizontal2.addWidget(text_notes)
horizontal3.addWidget(list_notes)
horizontal4.addWidget(create_notes)
horizontal4.addWidget(delete_notes)
horizontal5.addWidget(saves_notes)
horizontal6.addWidget(text_tags)
horizontal7.addWidget(list_tags)
horizontal8.addWidget(search_tags)
horizontal9.addWidget(add_to_a_notes)
horizontal9.addWidget(detach_from_the_note)
horizontal10.addWidget(search_for_notes_by_tag)
vertical2.addLayout(horizontal2)
vertical2.addLayout(horizontal3)
vertical2.addLayout(horizontal3)
vertical2.addLayout(horizontal4)
vertical2.addLayout(horizontal5)
vertical2.addLayout(horizontal6)
vertical2.addLayout(horizontal7)
vertical2.addLayout(horizontal8)
vertical2.addLayout(horizontal9)
vertical2.addLayout(horizontal10)
main_horizontal.addLayout(vertical1)
main_horizontal.addLayout(vertical2)

main_win.setLayout(main_horizontal)

def show_note():
    name = list_notes.selectedItems()[0].text()
    notes.setText(notes_list[name]['текст'])
    list_tags.clear()
    list_tags.addItems(notes_list[name]['теги'])

def add_note():
    note_name, ok = QInputDialog.getText(
        main_win, 'Добавить заметку', 'Название заметки: '
    )
    if ok and note_name != '':
        notes_list[note_name] = {'текст' : '', 'теги' : []}
        list_notes.addItem(note_name)

def del_note():
    if list_notes.selectedItems():
        save_name = list_notes.selectedItems()[0].text()
        del notes_list[save_name] #удаление заметки из словаря
        with open('notes_data.json', 'w', encoding = 'utf-8')as file:
            json.dump(notes_list, file)
        list_notes.clear()
        list_tags.clear()
        notes.clear()
        list_notes.addItems(notes_list)

def save_note():
    if list_notes.selectedItems():
        key = list_notes.selectedItems()[0].text()
        notes_list[key]['текст'] = notes.toPlainText()
        with open('notes_data.json', 'w', encoding ='utf-8') as file:
            json.dump(notes_list, file, sort_keys=True, ensure_ascii=False)
        print(notes_list)
    else:
        print('Заметка для сохранения не выбрана!')


def add_tag():
    if list_notes.selectedItems():
        key = list_notes.selectedItems()[0].text()
        tag = search_tags.text()
        if not tag in notes_list[key]['теги']:
            notes_list[key]['теги'].append(tag)
            list_tags.addItem(tag)
            search_tags.clear()
        with open('notes_data.json', 'w', encoding = 'utf-8') as file:
            json.dump(notes_list, file, sort_keys=True)
    else:
        print('Заметка для добавления тега не выбрана!')

def del_tag():
    if list_notes.selectedItems():
        key = list_notes.selectedItems()[0].text()
        tag = list_tags.selectedItems()[0].text()
        notes_list[key]['теги'].remove(tag)
        list_tags.clear()
        list_tags.addItems(notes_list[key]['теги'])
        with open('notes_data.json', 'w', encoding = 'utf-8')as file:
            json.dump(notes_list, file, sort_keys=True, ensure_ascii=False)
        
def search_tag():
    tag = search_tags.text()
    if search_for_notes_by_tag.text() == 'Искать заметки по тегу' and tag:
        notes_filtered = {} #тут будут заметки с выделенным тегом
        for note in notes_list:
            if tag in notes_list[note]['теги']:
                notes_filtered[note]=notes_list[note]
        search_for_notes_by_tag.setText('Сбросить поиск')
        list_notes.clear()
        list_tags.clear()
        list_notes.addItems(notes_filtered)
    elif search_for_notes_by_tag.text() == 'Сбросить поиск':
        search_tags.clear()
        list_notes.clear()
        list_tags.clear()
        list_notes.addItems(notes_list)
        search_for_notes_by_tag.setText('Искать заметки по тегу')
 



with open('notes_data.json', 'r', encoding = 'utf-8') as file:
    notes_list = json.load(file)
print(notes_list)
list_notes.addItems(notes_list)
list_notes.itemClicked.connect(show_note)
create_notes.clicked.connect(add_note)
delete_notes.clicked.connect(del_note)
saves_notes.clicked.connect(save_note)
add_to_a_notes.clicked.connect(add_tag)
detach_from_the_note.clicked.connect(del_tag)
search_for_notes_by_tag.clicked.connect(search_tag)
main_win.show()
app.exec_()
