'''operations performed under different test cases'''
import pytest
from app import App

def test_app_get_environment_variable():
    '''Test how the REPL handles the command.'''
    app = App()
#   Retrieve the current environment setting
    current_env = app.get_environment_variable('ENVIRONMENT')
    # Assert that the current environment is what you expect
    assert current_env in ['DEVELOPMENT', 'TESTING', 'PRODUCTION'], f"Invalid ENVIRONMENT: {current_env}"



def test_app_start_exit_command(capfd, monkeypatch):
    """Test that the REPL exits correctly on 'exit' command."""
    # Simulate user entering 'exit'
    monkeypatch.setattr('builtins.input', lambda _: 'exit')
    app = App()
    with pytest.raises(SystemExit) as e:
        app.start()
    assert e.type == SystemExit

def test_app_start_unknown_command(capfd, monkeypatch):
    """Test how the REPL handles an unknown command before exiting."""
    # Simulate user entering an unknown command followed by 'exit'
    inputs = iter(['unknown_command', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    app = App()
    with pytest.raises(SystemExit):
        app.start()
    # Optionally, check for specific exit code or message
    # assert excinfo.value.code == expected_exit_code
    # Verify that the unknown command was handled as expected
    captured = capfd.readouterr()
    assert "No such command: unknown_command" in captured.out

def test_app_start_add(capfd, monkeypatch):
    """Test how the REPL handles an add command before exiting."""
    # Simulate user entering an unknown command followed by 'exit'
    inputs = iter(['add', '14', '5', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    app = App()
    with pytest.raises(SystemExit):
        app.start()
    captured = capfd.readouterr()
    assert "19" in captured.out, "The addition command did not produce the expected output."


def test_app_start_subtract(capfd, monkeypatch):
    """Test how the REPL handles an sub command before exiting."""
    # Simulate user entering an unknown command followed by 'exit'
    inputs = iter(['subtract', '10', '2', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    app = App()
    with pytest.raises(SystemExit):
        app.start()

    captured = capfd.readouterr()
    assert "8" in captured.out, "The subract command did not produce the expected output."

def test_app_start_multiply(capfd, monkeypatch):
    """Test how the REPL handles a 'multiply' command before exiting."""
    inputs = iter(['multiply', '4', '4', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    app = App()
    with pytest.raises(SystemExit):
        app.start()

    captured = capfd.readouterr()
    assert "16" in captured.out, "The multiplication command did not produce the expected output."

def test_app_start_divide(capfd, monkeypatch):
    """Test how the REPL handles a 'divide' command before exiting."""
    inputs = iter(['divide', '10', '2', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    app = App()
    with pytest.raises(SystemExit):
        app.start()

    captured = capfd.readouterr()
    assert "5" in captured.out, "The division command did not produce the expected output."

def test_app_start_divide_by_zero(capfd, monkeypatch):
    """Test how the REPL handles a 'divide' command with division by zero before exiting."""
    inputs = iter(['divide', '6', '0', 'exit'])  # Correct command and simulate division by zero
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    app = App()

    with pytest.raises(SystemExit):
        app.start()

    captured = capfd.readouterr()
    # Ensure the expected error message for division by zero is in the output
    assert "Cannot divide by zero." in captured.out, "The divide command did not handle division by zero as expected."


def test_app_start_load(capfd, monkeypatch):
    """Test how the REPL handles an fetch command before exiting."""
    # Simulate user entering an unknown command followed by 'exit'
    inputs = iter(['load', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    app = App()

    with pytest.raises(SystemExit) :
        app.start()

    captured = capfd.readouterr()
    assert "Operation history of calculator:" in captured.out

def test_app_start_delete(capfd, monkeypatch):
    """Test how the REPL handles an delete command before exiting."""
    # Simulate user entering an unknown command followed by 'exit'
    inputs = iter(['delete', 2, 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    app = App()

    with pytest.raises(SystemExit) :
        app.start()

    captured = capfd.readouterr()
    assert "Operation history of calculator after deletion:" in captured.out

def test_app_start_clear(capfd, monkeypatch):
    """Test how the REPL handles an clear command before exiting."""
    # Simulate user entering an unknown command followed by 'exit'
    inputs = iter(['clear', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    app = App()

    with pytest.raises(SystemExit) :
        app.start()

    captured = capfd.readouterr()
    assert "History has been cleared!" in captured.out

def test_app_start_menu(capfd, monkeypatch):
    """Test how the REPL handles an menu command before exiting."""
    # Simulate user entering an unknown command followed by 'exit'
    inputs = iter(['menu', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    app = App()

    with pytest.raises(SystemExit) :
        app.start()

    captured = capfd.readouterr()
    assert "menu" in captured.out
