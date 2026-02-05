# День 17 — Практика: области видимости

## Задача 1 — замыкание и UnboundLocalError

```python
counter = 0

def make_counter():
    counter = 0

    def inc():
        counter += 1
        return counter

    return inc
```

**Вопросы:**

1. Какая ошибка возникает и где?
2. Почему Python не берёт `counter` из внешней функции?
3. Исправь код минимально.

### Решение

Ошибка:

```
UnboundLocalError: local variable 'counter' referenced before assignment
```

Причина:

- `counter += 1` содержит присваивание
- имя `counter` считается local в `inc`
- чтение происходит до инициализации

Исправление:

```python
def make_counter():
    counter = 0
    def inc():
        nonlocal counter
        counter += 1
        return counter
    return inc
```

---

## Задача 2 — global и затенение

```python
value = 100

def f():
    print(value)
    value = 200

f()
```

**Вопросы:**

1. Что произойдёт?
2. Почему не печатается 100?
3. Исправь двумя способами.

### Решение

Ошибка:

```
UnboundLocalError: local variable 'value' referenced before assignment
```

Причина:

- присваивание делает `value` локальной
- чтение происходит раньше

**Вариант A — с global:**

```python
value = 100

def f():
    global value
    print(value)
    value = 200
```

**Вариант B — без global:**

```python
value = 100

def f(v):
    print(v)
    return 200

value = f(value)
```

Рекомендация:

- второй вариант предпочтительнее в реальном коде
