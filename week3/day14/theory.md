# День 14 — Comprehensions (list / dict / set)

## Общая идея

Comprehension — это выражение языка Python для построения **нового контейнера** на основе итерируемого объекта.

Ментальная модель:

> пройтись → преобразовать → (опционально) отфильтровать → собрать

Comprehension **не заменяет** `for`, а является его сжатием без изменения логики.

---

## List comprehension

Базовая форма:

```python
[expression for x in iterable]
```

Эквивалент через `for`:

```python
result = []
for x in iterable:
    result.append(expression)
```

### Фильтрация (аналог `.filter()`)

```python
[expression for x in iterable if condition]
```

Важно:

- `if` **после for** — это фильтр

### Условное выражение (аналог `cond ? a : b`)

```python
[a if condition else b for x in iterable]
```

Важно:

- `if/else` **до for** — это условное значение
- элементы **не отбрасываются**, количество сохраняется

---

## Связь с мышлением JS-разработчика

| JS                     | Python                        |
| ---------------------- | ----------------------------- |
| `arr.map(g)`           | `g(x)`                        |
| `arr.filter(f)`        | `if f(x)`                     |
| `arr.filter(f).map(g)` | `[g(x) for x in arr if f(x)]` |

Python deliberately не использует цепочки методов для трансформации списков.
Трансформация задаётся **выражением**, а не методом контейнера.

---

## Dict comprehension

Форма:

```python
{key_expr: value_expr for x in iterable}
```

Эквивалент через `for`:

```python
result = {}
for x in iterable:
    result[key_expr] = value_expr
```

Принципиальное отличие от list comprehension:

- явно конструируется связь **ключ → значение**
- важна семантика соответствия, а не порядок

---

## Set comprehension

Форма:

```python
{expression for x in iterable}
```

Особенности:

- дубликаты удаляются автоматически
- порядок не гарантирован

---

## Когда не стоит использовать comprehension

Лучше использовать обычный `for`, если:

- больше 1–2 условий
- сложная логика
- вложенность больше 2 уровней

Python предпочитает **читаемость**, а не максимальную компактность.
