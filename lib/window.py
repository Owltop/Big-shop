import yaml
from PyQt5.QtWidgets import QLabel,  QMainWindow, QPushButton
import requests


class ShopWindow(QMainWindow):

    def __init__(self, data=None):
        super().__init__()

        self.setWindowTitle('Интернет-магазин')

        self.button = QPushButton('Товар 1', self)
        self.button.setGeometry(200, 150, 200, 80)

        # считываем данные с сервера (по-хорошему, их надо считывать раз в сколько-то секунд)
        # это псевдокод
        data_stats = requests.get('http://127.0.0.1:8080/api/stats')

        if data is not None:
            self.data = data
        else:
            with open('data/data.yml', 'r') as file:
                self.data = yaml.safe_load(file)

        print('Our data', self.data)

        self.label = QLabel(
            'Бронирование товаров в магазине\n {}'.format(self.data), self
        )
        # # это константа
        self.label.setGeometry(10, -100, 300, 300)

        self.button.clicked.connect(self.on_click)

        # это тоже константа
        self.resize(1000, 300)

    def on_click(self):
        requests.post('http://127.0.0.1:8080/api/reserve')
        # посылаем данные на сервер
        self.data[1] -= 1

        print('Our data', self.data)
        self.label.setText(
            'Бронирование товаров в магазине\n {}'.format(self.data)
        )

