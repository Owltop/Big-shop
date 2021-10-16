from PyQt5 import QtCore
from lib.window import ShopWindow
import yaml

import pytest


@pytest.fixture
def data():
    with open('data/data.yml', 'r', encoding='utf-8') as file:
        return yaml.safe_load(file)


def test_buttons_start(qtbot, data):
    window = ShopWindow(data=data)

    assert 'Товар {}'.format(1) == window.button.text()

    # кликаем по левой кнопке мыши (LeftButton)
    qtbot.mouseClick(window.button, QtCore.Qt.LeftButton)
    qtbot.mouseClick(window.button, QtCore.Qt.LeftButton)

    assert 8 == data[1]
