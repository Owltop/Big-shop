from PyQt5 import QtCore
from lib.window import ShopWindow
from PyQt5.QtWidgets import QPushButton

import pytest


@pytest.fixture
def data():
    return {
        'Морковь': 10,
        'Квартира в Медведково': 200,
        'Кухонная плита': 12,
        'Стул': 11,
        'Яхта Абрамовича': 1
    }


def test_buttons_start(qtbot, data):
    window = ShopWindow(data=data)
    assert len(window.findChildren(QPushButton)) == len(data)  # кол-во кнопок == len(data)
    assert 'Морковь'.format(1) == window.button_1.text()  # в кнопках нужный текст
    assert 'Стул'.format(1) == window.button_4.text()  # в кнопках нужный текст
    assert window.name_of_window == 'Ozon'  # правильное название окна
    assert window.label.width() == 700  # label нужной длины
    qtbot.mouseClick(window.button_1, QtCore.Qt.LeftButton)
    qtbot.mouseClick(window.button_1, QtCore.Qt.LeftButton)
    assert 8 == data['Морковь']  # кнопки работают
    qtbot.mouseClick(window.button_5, QtCore.Qt.LeftButton)
    assert 0 == data['Яхта Абрамовича']  # кнопки работают
    '''как проверить остутвие кнопки? если вмето deletelater использовать close(), то с помощью isVisiable() 
    это можно проверить, но это работает только в window.py. здесь всегда выдает false'''
    # assert not(window.button_1.isVisible())
    qtbot.mouseClick(window.button_5, QtCore.Qt.LeftButton)
    assert 0 == data['Яхта Абрамовича']  # нажатие на товар, который закончился, не меняет data
