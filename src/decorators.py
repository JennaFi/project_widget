from functools import wraps
from typing import Callable, Any


def log(filename: Any = None) -> Callable:
    """Функция, реализующая запись информации в лог"""

    def decorator(function: Callable) -> Callable:

        @wraps(function)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            try:
                function(*args, **kwargs)
                log_msg = f"{function.__name__} ok"
            except Exception as e:
                log_msg = f"{function.__name__} error: {e}. Inputs: {args} and {kwargs}"
            if filename:
                with open(filename, "w", encoding="utf-8") as file:
                    file.write(log_msg)

            else:
                print(log_msg)

        return wrapper

    return decorator
