# День 26 — Практика

## Задача 1

Дан код:

```python
values = ["10", "20", "x", "30"]
result = 0

for v in values:
    result += int(v)
```

1. Код падает. Почему?
2. Исправь код так, чтобы:
   - корректные числа суммировались
   - некорректные значения игнорировались

---

## Задача 2

Напиши функцию `safe_div(a, b)`, которая:

- возвращает результат деления `a / b`
- если деление невозможно — возвращает `None`

Требования:

- использовать `try / except`
- не ловить `Exception`

---

## Задача 3

Есть функция:

```python
def load_user(data, key):
    return data[key]
```

Требуется:

- обработать ситуацию отсутствия ключа
- **не** использовать `if key in data`

Подсказка: это как раз тот случай, где исключение оправдано.

---

## Решения

### Решение 1

```python
values = ["10", "20", "x", "30"]
result = 0

for v in values:
    try:
        result += int(v)
    except ValueError:
        pass
```

Исключение `ValueError` возникает при попытке преобразовать `"x"` в число.

---

### Решение 2

```python
def safe_div(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return None
```

Ловим конкретный тип ошибки — деление на ноль.

---

### Решение 3

```python
def load_user(data, key):
    try:
        return data[key]
    except KeyError:
        return None
```

Здесь исключение — нормальный способ работы с API словаря.
