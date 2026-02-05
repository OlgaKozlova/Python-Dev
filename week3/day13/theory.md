# День 13 — Цикл for, range, enumerate, for-else

## 1. for в Python: итерация, а не счётчик

Цикл `for` в Python перебирает **итерируемые объекты**, а не управляет индексом.

```python
for x in [10, 20, 30]:
    print(x)
```

Ближайший аналог в JS — `for (const x of iterable)`.

Важно: основа `for` — **протокол итерации**, а не числовой диапазон.

---

## 2. range — ленивый объект последовательности

```python
range(5)        # 0 1 2 3 4
range(1, 5)     # 1 2 3 4
range(1, 10, 2) # 1 3 5 7 9
```

`range`:

- не список
- не хранит все значения
- вычисляет элементы по запросу

```python
r = range(3)
list(r)  # [0, 1, 2]
```

---

## 3. Антипаттерн range(len(...))

```python
for i in range(len(data)):
    print(data[i])
```

Работает, но:

- завязано на индексы
- хуже читается
- не универсально

Предпочтительно:

```python
for item in data:
    print(item)
```

---

## 4. enumerate — индекс как часть итерации

```python
for i, v in enumerate(data):
    print(i, v)
```

`enumerate(iterable, start=0)`:

- возвращает пары `(index, value)`
- не считает заранее
- работает с любым iterable

Сдвиг индекса:

```python
enumerate(data, start=1)
```

---

## 5. enumerate и словари

```python
for i, key in enumerate(d):
    ...
```

Допустимо, но редко нужно. Индекс ключа словаря обычно не имеет смысла.

---

## 6. for и словари

```python
for key in d:
    ...

for value in d.values():
    ...

for key, value in d.items():
    ...
```

`items()` — самый частый и полезный вариант.

---

## 7. for … else

`else` у цикла выполняется **если не был выполнен break**.

```python
for x in data:
    if x == target:
        break
else:
    print("not found")
```

Это правило **одинаково** для `for` и `while`.

Ключевая формула:

> else = no break

---

## 8. Что НЕ влияет на else

- `continue`
- количество итераций (включая 0)

Влияет только `break` (а также `return`, `raise`).
