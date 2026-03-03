# День 41 — Практика

## Задача 1

Реализовать функцию `dispatch(op)`, которая:

- возвращает функцию сложения при `"add"`
- возвращает функцию умножения при `"mul"`
- бросает `ValueError("unknown op")` для неизвестной операции

Проверка:

```python
dispatch("add")(2, 3)  # 5
dispatch("mul")(2, 3)  # 6
```

---

## Задача 2

Написать функцию `apply_all(funcs, value)`, которая:

- принимает список функций одного аргумента
- возвращает список результатов применения этих функций к `value`

Пример:

```python
def square(x): return x * x
def double(x): return x * 2

apply_all([square, double], 3)
# [9, 6]
```

---

## Задача 3 (мышление)

Объяснить устно или письменно:

Почему в Python нет hoisting, и чем это принципиально отличается от JavaScript?

---

# Решения

## Решение 1

```python
def dispatch(op: str):
    def add(a: int, b: int):
        return a + b

    def mul(a: int, b: int):
        return a * b

    ops = {
        "add": add,
        "mul": mul,
    }

    try:
        return ops[op]
    except KeyError:
        raise ValueError("unknown op")
```

---

## Решение 2

```python
def apply_all(funcs, value):
    result = []
    for f in funcs:
        result.append(f(value))
    return result
```

---

## Комментарии

- Функции являются объектами, поэтому могут храниться в списках и словарях.
- Передача функции отличается от её вызова.
- В Python имена связываются во время выполнения кода, поэтому использовать функцию до её определения нельзя.
