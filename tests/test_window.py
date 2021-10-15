from PyQt5 import QtCore
from lib.window import ShopWindow

import pytest


@pytest.fixture
def data():
    return {1: 100}


def test_buttons_start(qtbot, data):
    window = ShopWindow(data=data)

    assert 'Товар {}'.format(1) == window.button.text()

    # кликаем по левой кнопке мыши (LeftButton)
    qtbot.mouseClick(window.button, QtCore.Qt.LeftButton)
    qtbot.mouseClick(window.button, QtCore.Qt.LeftButton)

    assert 98 == data[1]
