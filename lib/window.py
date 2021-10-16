import yaml
from PyQt5.QtWidgets import QLabel, QMainWindow, QPushButton
import requests


class ShopWindow(QMainWindow):

    def __init__(self, data=None):
        super().__init__()

        self.setWindowTitle('Ozon')

        self.button_1 = QPushButton('Морковь', self)
        self.button_2 = QPushButton('Квартира в Медвеково', self)
        self.button_3 = QPushButton('Кухонная плита', self)
        self.button_4 = QPushButton('Стул', self)
        self.button_5 = QPushButton('Яхта Абрамовича', self)

        self.button_1.name = 'Морковь'
        self.button_2.name = 'Квартира в Медведково'
        self.button_3.name = 'Кухонная плита'
        self.button_4.name = 'Стул'
        self.button_5.name = 'Яхта Абрамовича'

        self.button_1.setGeometry(100, 150, 150, 80)
        self.button_2.setGeometry(260, 150, 150, 80)
        self.button_3.setGeometry(420, 150, 150, 80)
        self.button_4.setGeometry(580, 150, 150, 80)
        self.button_5.setGeometry(740, 150, 150, 80)

        # считываем данные с сервера (по-хорошему, их надо считывать раз в сколько-то секунд)
        # это псевдокод
        # data_stats = requests.get('http://127.0.0.1:8080/api/stats')

        if data is not None:
            self.data = data
        else:
            with open('data/data.yml', 'r', encoding='utf-8') as file:
                self.data = yaml.safe_load(file)

        # print(self.data)

        self.label = QLabel('Осталось на складе\n {}'.format(self.data), self)
        self.label.setGeometry(150, -100, 700, 300)
        self.button_1.clicked.connect(self.on_click_1)
        self.button_2.clicked.connect(self.on_click_2)
        self.button_3.clicked.connect(self.on_click_3)
        self.button_4.clicked.connect(self.on_click_4)
        self.button_5.clicked.connect(self.on_click_5)
        self.resize(1000, 300)

    def on_click_1(self):
        name = 'Морковь' # я пытался не копировать код и передавать name при вызове функции но что-то пошло не так
        self.data[name] -= 1
        self.label.setText('Бронирование товаров в магазине\n {}'.format(self.data))
        if self.data[name] <= 0:
            self.button_1.deleteLater()

    def on_click_2(self):
        name = 'Квартира в Медведково'
        self.data[name] -= 1
        self.label.setText('Бронирование товаров в магазине\n {}'.format(self.data))
        if self.data[name] <= 0:
            self.button_2.deleteLater()

    def on_click_3(self):
        name = 'Кухонная плита'
        self.data[name] -= 1
        self.label.setText('Бронирование товаров в магазине\n {}'.format(self.data))
        if self.data[name] <= 0:
            self.button_3.deleteLater()

    def on_click_4(self):
        name = 'Стул'
        self.data[name] -= 1
        self.label.setText('Бронирование товаров в магазине\n {}'.format(self.data))
        if self.data[name] <= 0:
            self.button_4.deleteLater()

    def on_click_5(self):
        name = 'Яхта Абрамовича'
        self.data[name] -= 1
        self.label.setText('Бронирование товаров в магазине\n {}'.format(self.data))
        if self.data[name] <= 0:
            self.button_5.deleteLater()

    '''def on_click(self, button):
        # requests.post('http://127.0.0.1:8080/api/reserve')
        # посылаем данные на сервер
        self.data[button] -= 1

        # print('Our data', self.data)
        self.label.setText(
            'Бронирование товаров в магазине\n {}'.format(self.data)
        )'''
