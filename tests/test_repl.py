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