# День 5 — Практика

## Задача 1 — strip + isalnum

```python
s = "  123 abc  "

if s.strip().isalnum():
    print("A")
else:
    print("B")
```

### Ответ

```text
B
```

### Пояснение

- `strip()` → "123 abc" (пробел внутри остаётся)
- `isalnum()` требует только буквы и цифры
- пробел → `False`

---

## Задача 2 — split + replace + join

```python
s = "  one,,two, three ,four  "

parts = s.strip().split(",", 2)
result = ",".join(p.strip().replace("o", "0") for p in parts)

print(result)
```

### Ответ

```text
0ne,,tw0, three ,f0ur
```

### Пояснение

- `split(',', 2)` даёт `['one', '', 'two, three ,four']`
- генератор проходит по каждому элементу списка
- `replace('o', '0')` заменяет **букву** на **цифру**, не меняя регистр
- пустая строка сохраняется → двойная запятая

---

## Задача 3 — порядок вызовов методов

```python
s = "  Hello World  "

a = s.strip().lower().replace(" ", "_")
b = s.replace(" ", "_").strip().lower()

print(a)
print(b)
```

### Ответ

```text
hello_world
__hello_world__
```

### Пояснение

- В `b` пробелы заменены **до** `strip`
- `strip` не удаляет подчёркивания
- порядок методов меняет результат

---

## Задача 4 — форматирование

```python
name = "Bob"
score = 7.5

s = f"|{name:^6}|{score:05.1f}|"
print(s)
```

### Ответ

```text
| Bob  |007.5|
```

### Пояснение

- `^6` — центрирование строки шириной 6
- `05.1f` — ширина 5, заполнение нулями, 1 знак после точки
- ширина всегда минимальная, обрезки нет
