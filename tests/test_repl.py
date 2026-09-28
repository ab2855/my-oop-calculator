from calculator.repl import Calculator


def test_repl_exit(monkeypatch, capsys):
    monkeypatch.setattr("builtins.input", lambda _: "exit")
    Calculator().run()
    out, _ = capsys.readouterr()
    assert "Goodbye!" in out


def test_repl_help(monkeypatch, capsys):
    inputs = iter(["help", "exit"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    Calculator().run()
    out, _ = capsys.readouterr()
    assert "Available commands:" in out


def test_repl_add_flow(monkeypatch, capsys):
    inputs = iter(["add", "10", "5", "history", "exit"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    calc = Calculator()
    calc.run()
    out, _ = capsys.readouterr()
    assert "Result: 15" in out
    assert "1. Add: 10.0, 5.0 = 15.0" in out


def test_repl_subtract_flow(monkeypatch, capsys):
    inputs = iter(["subtract", "20", "7", "exit"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    calc = Calculator()
    calc.run()
    out, _ = capsys.readouterr()
    assert "Result: 13" in out


def test_repl_remove_flow(monkeypatch, capsys):
    inputs = iter(["add", "2", "3", "remove", "1", "history", "exit"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    calc = Calculator()
    calc.run()
    out, _ = capsys.readouterr()
    assert "Removed item 1." in out
    assert "History is empty." in out


def test_repl_empty_history(monkeypatch, capsys):
    inputs = iter(["history", "exit"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    Calculator().run()
    out, _ = capsys.readouterr()
    assert "History is empty." in out


def test_repl_unknown_command(monkeypatch, capsys):
    inputs = iter(["foobar", "exit"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    Calculator().run()
    out, _ = capsys.readouterr()
    assert "Unknown command: foobar" in out


def test_repl_blank_input(monkeypatch, capsys):
    inputs = iter(["", "exit"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    Calculator().run()
    out, _ = capsys.readouterr()
    assert "Goodbye!" in out


def test_repl_eof_interrupt(monkeypatch, capsys):
    def mock_input(_):
        raise EOFError

    monkeypatch.setattr("builtins.input", mock_input)
    Calculator().run()
    out, _ = capsys.readouterr()
    assert "Goodbye!" in out


def test_repl_keyboard_interrupt(monkeypatch, capsys):
    def mock_input(_):
        raise KeyboardInterrupt

    monkeypatch.setattr("builtins.input", mock_input)
    Calculator().run()
    out, _ = capsys.readouterr()
    assert "Goodbye!" in out


def test_repl_invalid_numbers(monkeypatch, capsys):
    inputs = iter(["add", "abc", "exit"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    calc = Calculator()
    calc.run()
    out, _ = capsys.readouterr()
    assert "Invalid input: Please enter numeric values." in out
    assert calc.history.count() == 0


def test_repl_non_finite_numbers(monkeypatch, capsys):
    inputs = iter(["add", "inf", "5", "exit"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    calc = Calculator()
    calc.run()
    out, _ = capsys.readouterr()
    assert "Invalid input: Please enter numeric values." in out
    assert calc.history.count() == 0


def test_repl_float_result(monkeypatch, capsys):
    inputs = iter(["add", "2.5", "3.2", "exit"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    calc = Calculator()
    calc.run()
    out, _ = capsys.readouterr()
    assert "Result: 5.7" in out


def test_repl_remove_invalid_entries(monkeypatch, capsys):
    inputs = iter(["remove", "not_a_number", "remove", "99", "exit"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    calc = Calculator()
    calc.run()
    out, _ = capsys.readouterr()
    assert "Invalid history entry." in out


def test_main_execution(monkeypatch):
    import runpy
    monkeypatch.setattr("builtins.input", lambda _: "exit")
    runpy.run_module("calculator.__main__", run_name="__main__")