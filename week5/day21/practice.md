# День 21 — Практика

## Задача

Даны файлы:

```python
# utils.py
print("utils loaded")

def add(a, b):
    return a + b

def main():
    print(add(2, 3))

if __name__ == "__main__":
    main()
```

```python
# app.py
from utils import add

print("app loaded")
print(add(10, 20))
```

**Вопросы:**

1. Вывод `python app.py` (строго по порядку)
2. Вывод `python utils.py`
3. Почему `main()` вызывается только в одном случае

---

## Решение

### `python app.py`

```
utils loaded
app loaded
30
```

### `python utils.py`

```
utils loaded
5
```

### Пояснение

При импорте `utils` его `__name__ == "utils"`, поэтому условие `if __name__ == "__main__"` ложно и `main()` не вызывается.

При прямом запуске `utils.py` значение `__name__ == "__main__"`, поэтому `main()` выполняется.
