# День 18 — Практика

## Задача 1

Что выведет код и почему:

```python
def f(x, data=[]):
    data.append(x)
    return data

print(f(10))
print(f(20))
print(f(30, []))
print(f(40))
```

Опиши:

- сколько объектов списков существует
- какой из них используется в каждом вызове

---

## Задача 2

Что выведет код при запуске **в одном процессе**:

```python
def g(x, acc=[]):
    acc.append(x)
    return acc

print(g(1))
g.__defaults__[0].append(99)
print(g(2))
```

---

## Задача 3

Найди логическую ошибку и исправь:

```python
def log(message, history=[]):
    history.append(message)
    return history
```

Перепиши функцию так, чтобы:

- история была независима между вызовами
- поведение было предсказуемым

---

## Решения (смотри после попытки решить самостоятельно)

<details>
<summary>Показать решения</summary>

### Задача 1

Используется один default-список, который накапливает `[10, 20, 40]`. Вызов с `[]` создаёт отдельный временный список `[30]`.

### Задача 2

```text
[1]
[1, 99, 2]
```

`__defaults__` содержит ссылку на тот же объект.

### Задача 3

```python
def log(message, history=None):
    if history is None:
        history = []
    history.append(message)
    return history
```

</details>
