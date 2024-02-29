import pytest
from app import App

def test_app_add_command(capfd, monkeypatch):
    """Test that the REPL correctly handles the 'add' command."""
    inputs = iter(['add 1 2', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    app = App()
    with pytest.raises(SystemExit):  # Expect the application to exit
        app.start()

    out, _ = capfd.readouterr()
    assert "3" in out, "The add command did not produce the expected output"

def test_add_command_non_numeric_arguments(capfd, monkeypatch):
    inputs = iter(['add one two', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    app = App()
    with pytest.raises(SystemExit):
        app.start()

    out, _ = capfd.readouterr()
    assert "Error: All arguments must be numeric" in out, "The add command should validate numeric arguments"

def test_add_command_failure(capfd, monkeypatch):
    inputs = iter(['add 3', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    app = App()
    with pytest.raises(SystemExit):  # Expect the application to exit
        app.start()
    
    out, _ = capfd.readouterr()
    assert "Require exact two arguments" in out, "The add command failure did not produce the expected output"

def test_app_subtract_command(capfd, monkeypatch):
    """Test that the REPL correctly handles the 'sub' command."""
    inputs = iter(['sub 5 2', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    app = App()
    with pytest.raises(SystemExit):  # Expect the application to exit
        app.start()
    
    out, _ = capfd.readouterr()
    assert "3" in out, "The subtract command did not produce the expected output"

def test_subtract_command_failure(capfd, monkeypatch):
    inputs = iter(['sub 10', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    app = App()
    with pytest.raises(SystemExit):  # Expect the application to exit
        app.start()
    
    out, _ = capfd.readouterr()
    assert "Require exact two arguments" in out, "The subtract command failure did not produce the expected output"

def test_app_multiply_command(capfd, monkeypatch):
    """Test that the REPL correctly handles the 'multi' command."""
    inputs = iter(['multi 3 4', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    app = App()
    with pytest.raises(SystemExit):  # Expect the application to exit
        app.start()
    
    out, _ = capfd.readouterr()
    assert "12" in out, "The multiply command did not produce the expected output"

def test_multiply_command_failure(capfd, monkeypatch):
    inputs = iter(['multi 4', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    app = App()
    with pytest.raises(SystemExit):  # Expect the application to exit
        app.start()
    
    out, _ = capfd.readouterr()
    assert "Require exact two arguments" in out, "The multiply command failure did not produce the expected output"

def test_app_divide_command(capfd, monkeypatch):
    """Test that the REPL correctly handles the 'div' command."""
    inputs = iter(['div 8 2', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    app = App()
    with pytest.raises(SystemExit):  # Expect the application to exit
        app.start()
    
    out, _ = capfd.readouterr()
    assert "4" in out, "The divide command did not produce the expected output"

def test_divide_command_div_by_zero(capfd, monkeypatch):
    inputs = iter(['div 20 0', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    app = App()
    with pytest.raises(SystemExit):  # Expect the application to exit
        app.start()
    
    out, _ = capfd.readouterr()
    assert "Can't division by zero" in out, "Divide by zero did not produce the expected output"

def test_divide_command_failure(capfd, monkeypatch):
    inputs = iter(['div 20', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    app = App()
    with pytest.raises(SystemExit):  # Expect the application to exit
        app.start()
    
    out, _ = capfd.readouterr()
    assert "Require exact two arguments" in out, "The divide command failure did not produce the expected output"
