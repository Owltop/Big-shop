from PyQt5 import QtCore
from lib.window import ShopWindow

import pytest


@pytest.fixture
def data():
    return {1: 100}


def test_buttons_start(qtbot, data):
    print('data', data)
    window = ShopWindow(data=data)
    assert len(window.buttons) == len(window.data)

    for i, button in enumerate(window.buttons):
        assert 'Купить товар номер {}\n доступно: {}'.format(i+1, window.data[i+1]) == button.text()

    # кликаем по левой кнопке мыши (LeftButton)
    qtbot.mouseClick(window.buttons[0], QtCore.Qt.LeftButton)
    qtbot.mouseClick(window.buttons[0], QtCore.Qt.LeftButton)

    for i, button in enumerate(window.buttons):
        print(button.text())

    assert 'Товар номер 1\n доступно: 98' == window.buttons[0].text()