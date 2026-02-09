# День 27 — Практика

## Задача 1

Есть функция:

```python
def parse(value):
    try:
        return int(value)
    except Exception:
        return None
```

1. Объясни, **почему это плохая обработка ошибок**.
2. Перепиши функцию корректно.

---

## Задача 2

Что вернёт функция и почему:

```python
def f():
    try:
        return "try"
    finally:
        return "finally"
```

Ответ обоснуй через порядок выполнения.

---

## Задача 3

Перепиши код так, чтобы:

- исключения не подавлялись
- ресурс закрывался гарантированно

```python
def read_file(path):
    try:
        f = open(path)
        return f.read()
    except IOError:
        return None
```

---

## Решения (проверь себя)

### Задача 1

Плохо потому что:

- ловится `Exception` без понимания причины
- подавляются неожиданные ошибки
- функция врёт о результате

Корректно:

```python
def parse(value):
    try:
        return int(value)
    except ValueError:
        return None
```

---

### Задача 2

Вернётся `"finally"`, потому что `return` в `finally` выполняется последним и перекрывает `return` из `try`.

---

### Задача 3

```python
def read_file(path):
    f = None
    try:
        f = open(path)
        return f.read()
    finally:
        if f:
            f.close()
```

(Позже это будет заменено на `with`.)
