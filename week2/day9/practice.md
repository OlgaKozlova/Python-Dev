# День 9 — Практика (словари)

## Задача 1 — Агрегация логов

Дан список логов:

```python
logs = [
    "INFO user=alice action=login",
    "ERROR user=bob action=pay",
    "INFO user=alice action=view",
    "INFO user=bob action=login",
    "ERROR user=alice action=pay",
]
```

Нужно получить:

```python
{
    "alice": {"INFO": 2, "ERROR": 1},
    "bob":   {"INFO": 1, "ERROR": 1},
}
```

### Решение

```python
result = {}

for log in logs:
    level, user_part, _ = log.split()
    user = user_part.split("=")[1]

    if user not in result:
        result[user] = {}

    result[user][level] = result[user].get(level, 0) + 1
```

---

## Задача 2 — Группировка по тегам

Дан список событий:

```python
events = [
    {"id": 1, "tags": ["work", "urgent"]},
    {"id": 2, "tags": ["home"]},
    {"id": 3, "tags": ["work"]},
    {"id": 4, "tags": ["home", "urgent"]},
]
```

Нужно получить:

```python
{
    "work": [1, 3],
    "urgent": [1, 4],
    "home": [2, 4],
}
```

### Решение

```python
result = {}

for event in events:
    event_id = event["id"]
    for tag in event["tags"]:
        if tag not in result:
            result[tag] = []
        result[tag].append(event_id)
```

---

## Контрольные вопросы

1. Почему опасно использовать:

```python
lst = d.get(key, [])
lst.append(x)
```

без присваивания обратно?

2. Почему в Python доступ к данным в словаре сделан через `[]`, а не через `.`?

Ответы на эти вопросы означают, что модель словарей усвоена корректно.
