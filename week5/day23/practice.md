# День 23 — Практика (пакеты)

## Задача 1

Дана структура:

```
app/
    main.py
    utils/
        helpers.py
```

1. Почему `import utils.helpers` не работает?
2. Что нужно добавить, чтобы заработало?
3. Какой импорт будет корректным из `main.py`?

---

## Задача 2

Есть структура:

```
service/
    __init__.py
    api/
        __init__.py
        users.py
```

1. Напиши импорт функции `get_user` из `users.py` **двумя способами**:
   - через полный путь
   - через re-export в `api/__init__.py`

---

## Задача 3

Почему это плохая идея?

```python
# pkg/__init__.py
connect_to_db()
start_worker()
```

Опиши минимум **две проблемы**, которые это создаёт.

---

## Решения

### Задача 1

1. `utils` — просто папка, не пакет
2. Нужно добавить `utils/__init__.py`
3. `import utils.helpers` или `from utils import helpers`

---

### Задача 2

Полный путь:

```python
from service.api.users import get_user
```

Через `api/__init__.py`:

```python
# service/api/__init__.py
from .users import get_user
```

Использование:

```python
from service.api import get_user
```

---

### Задача 3

Проблемы:

- побочные эффекты при импорте
- импорт становится небезопасным
- ломается тестирование
- возможны циклические импорты
