import pytest
from main import add  # замените на имя вашего файла и функции


def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0


def test_add_zero():
    assert add(0, 0) == 0


def test_add_invalid_type():
    with pytest.raises(TypeError):
        add("2", 3)
