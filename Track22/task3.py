# Создайте класс с базовым исключением и дочерние классыисключения:
# ○ ошибка уровня,
# ○ ошибка доступа.

class MyBaseException(Exception):
    """Базовый класс для исключений."""

class LevelError(MyBaseException):
    """Исключение для ошибок уровня."""

class AccessError(MyBaseException):
    """Исключение для ошибок доступа."""

try:
    # Генерируем исключение ошибки уровня
    raise LevelError("Ошибка уровня: уровень 2")

except LevelError as le:
    print(f"Поймано исключение уровня: {le}")

except AccessError as ae:
    print(f"Поймано исключение доступа: {ae}")

except MyBaseException as be:
    print(f"Поймано базовое исключение: {be}")
