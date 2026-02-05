# День 14 — Практика (Comprehensions)

## Задача 1 — list comprehension

Дано:

```python
nums = [1, 2, 3, 4, 5, 6]
```

Получить список квадратов **чётных** чисел.

### Решение через for

```python
result = []
for num in nums:
    if num % 2 == 0:
        result.append(num * num)
```

### Решение через comprehension

```python
[num * num for num in nums if num % 2 == 0]
```

---

## Задача 2 — условное выражение

Дано:

```python
nums = [1, 2, 3, 4]
```

Получить список:

- квадрат, если число чётное
- `0`, если нечётное

### Решение через for

```python
result = []
for x in nums:
    if x % 2 == 0:
        result.append(x * x)
    else:
        result.append(0)
```

### Решение через comprehension

```python
[x * x if x % 2 == 0 else 0 for x in nums]
```

---

## Задача 3 — dict comprehension

Дано:

```python
words = ["apple", "banana", "pear", "plum"]
```

Построить словарь: слово → длина слова.

### Решение через for

```python
result = {}
for w in words:
    result[w] = len(w)
```

### Решение через dict comprehension

```python
{w: len(w) for w in words}
```

---

## Контрольные правила

- `if` после `for` → фильтрация
- `if/else` до `for` → условное значение
- comprehension всегда можно получить механическим сжатием `for`

Если comprehension читается хуже, чем `for` — используй `for`.
