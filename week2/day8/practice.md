# Словари (dict) — практика

## Задача 1. get и falsy значения

Что выведет код и почему:

```python
d = {"a": 0}

if d.get("a"):
    print("YES")
else:
    print("NO")
```

---

## Задача 2. Проверка наличия ключа

```python
d = {"a": 0}

if "a" in d:
    print("YES")
else:
    print("NO")
```

---

## Задача 3. View и мутация

```python
d = {"a": 1, "b": 2}
vals = d.values()

d["c"] = 3
print(list(vals))
```

---

## Задача 4. Опасный паттерн

```python
d = {}

value = d.get("a", []).append(1)

print(d)
print(value)
```

---

## Задача 5. defaultdict

```python
from collections import defaultdict

d = defaultdict(int)

print(d["x"])
print(d)
```

---

# Ответы и пояснения

## Ответ 1

Вывод:

```
NO
```

`d.get("a")` возвращает `0`, а `0` — falsy значение.

---

## Ответ 2

Вывод:

```
YES
```

`in` проверяет наличие ключа, значение не имеет значения.

---

## Ответ 3

Вывод:

```
[1, 2, 3]
```

`values()` возвращает view, отражающий текущее состояние словаря.

---

## Ответ 4

Вывод:

```
{}
None
```

`append` мутирует временный список и возвращает `None`. Словарь не меняется.

---

## Ответ 5

Вывод:

```
0
defaultdict(<class 'int'>, {'x': 0})
```

`int()` используется как фабрика значений по умолчанию.
