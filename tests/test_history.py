import pytest
from calculator.calculations import Add, Subtract
from calculator.history import History


def test_history_starts_empty():
    history = History()
    assert history.count() == 0
    assert history.all() == []


def test_history_add_and_count():
    history = History()
    history.add(Add(10, 5))
    history.add(Subtract(20, 7))
    assert history.count() == 2
    assert len(history.all()) == 2


def test_history_encapsulation():
    history = History()
    history.add(Add(2, 3))
    records = history.all()
    records.append(Add(9, 9))
    assert history.count() == 1


def test_history_clear():
    history = History()
    history.add(Add(1, 1))
    history.clear()
    assert history.count() == 0
    assert history.all() == []


def test_history_remove():
    history = History()
    op1 = Add(10, 5)
    op2 = Subtract(20, 7)
    history.add(op1)
    history.add(op2)

    removed = history.remove(1)
    assert removed == op1
    assert history.count() == 1
    assert history.all() == [op2]


def test_history_remove_invalid_index():
    history = History()
    history.add(Add(1, 2))
    with pytest.raises(IndexError):
        history.remove(0)
    with pytest.raises(IndexError):
        history.remove(2)