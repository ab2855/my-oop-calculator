from calculator.calculations import Add


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