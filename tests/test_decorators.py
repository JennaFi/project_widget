from src.decorators import log


def test_log_correct():
    @log(filename="test_msg.txt")
    def my_function(x, y):
        return x + y

    my_function(1, 2)

    with open("test_msg.txt", "r", encoding="utf-8") as file:
        file.read()

    assert "my_function ok"


def test_log_incorrect():
    @log(filename="test_msg.txt")
    def error_function():
        raise ValueError("There's been an issue")

    error_function()

    with open("test_msg.txt", "r", encoding="utf-8") as file:
        file.read()

    assert "error_function error: There's been an issue. Inputs: () and {}"


def test_log_console_correct(capsys):
    @log()
    def my_function(x, y):
        return x + y

    my_function(1, 2)
    captured = capsys.readouterr()

    assert "my_function ok\n" in captured.out


def test_log_console_incorrect(capsys):
    @log()
    def error_function():
        raise ValueError("There's been an issue")

    error_function()
    captured = capsys.readouterr()

    assert "error_function error: There's been an issue. Inputs: () and {}\n" in captured.out
