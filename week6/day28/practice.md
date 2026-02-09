# День 28 — Практика

## Задача 1

Создай пользовательское исключение `AgeValidationError`.

Требования:

- наследуется от `Exception`
- хранит возраст и сообщение об ошибке

Напиши функцию `validate_age(age)`, которая:

- выбрасывает `AgeValidationError`, если `age < 18`
- ничего не возвращает, если возраст корректный

---

## Задача 2

Есть функция:

```python
def parse_port(value):
    port = int(value)
    if port < 1 or port > 65535:
        raise ValueError("invalid port")
    return port
```

Перепиши её так, чтобы:

- использовалось пользовательское исключение `PortError`
- в исключении хранилось исходное значение `value`

---

## Решения

### Решение задачи 1

```python
class AgeValidationError(Exception):
    def __init__(self, age, message):
        self.age = age
        super().__init__(message)


def validate_age(age):
    if age < 18:
        raise AgeValidationError(age, "Возраст должен быть >= 18")
```

### Решение задачи 2

```python
class PortError(Exception):
    def __init__(self, value, message):
        self.value = value
        super().__init__(message)


def parse_port(value):
    try:
        port = int(value)
    except ValueError:
        raise PortError(value, "Порт не является числом")

    if not (1 <= port <= 65535):
        raise PortError(value, "Порт вне допустимого диапазона")

    return port
```
