import pytest
from calculator.calculations import Add, Calculation, Subtract


def test_add_attributes():
    op = Add(10, 5)
    assert op.a == 10
    assert op.b == 5


def test_add_execute():
    op = Add(10, 5)
    assert op.execute() == 15


def test_add_negative_execute():
    op = Add(-4, 1)
    assert op.execute() == -3


def test_subtract_execute():
    op = Subtract(20, 7)
    assert op.execute() == 13


def test_subtract_negative_result():
    op = Subtract(3, 5)
    assert op.execute() == -2


def test_polymorphism():
    calculations: list[Calculation] = [Add(10, 5), Subtract(20, 7)]
    results = [calc.execute() for calc in calculations]
    assert results == [15, 13]


def test_calculation_str():
    add_op = Add(10, 5)
    sub_op = Subtract(20, 7)
    assert str(add_op) == "Add: 10, 5 = 15"
    assert str(sub_op) == "Subtract: 20, 7 = 13"


def test_cannot_instantiate_abstract_calculation():
    with pytest.raises(TypeError):
        Calculation(1, 2)