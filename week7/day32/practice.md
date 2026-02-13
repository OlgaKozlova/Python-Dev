# День 32 — Практика

## Задача 1

Написать класс `Counter`.

Требования:

1. У каждого экземпляра своё значение счётчика.
2. Класс хранит общее количество созданных экземпляров.
3. Метод `increment()` увеличивает значение конкретного экземпляра.
4. Метод `get_total_created()` возвращает общее количество созданных объектов.

---

## Задача 2

Создать класс `User`:

1. Атрибут класса `role = "guest"`.
2. В `__init__` передаётся `name`.
3. Метод `change_role(new_role)` меняет роль только конкретного экземпляра.
4. Проверить, что изменение роли одного пользователя не влияет на других.

---

## Задача 3

Создать класс `TagStorage`:

1. Атрибут класса `tags = []`.
2. Метод `add_tag(tag)` добавляет тег.
3. Создать два экземпляра и продемонстрировать, что список общий.
4. Затем изменить поведение так, чтобы у каждого экземпляра был свой список.

---

# Решения

## Решение 1

```python
class Counter:
    total_created = 0

    def __init__(self):
        self.value = 0
        type(self).total_created += 1

    def increment(self):
        self.value += 1

    @classmethod
    def get_total_created(cls):
        return cls.total_created
```

---

## Решение 2

```python
class User:
    role = "guest"

    def __init__(self, name):
        self.name = name

    def change_role(self, new_role):
        self.role = new_role
```

Присваивание создаёт атрибут экземпляра, перекрывающий атрибут класса.

---

## Решение 3

Общий список:

```python
class TagStorage:
    tags = []

    def add_tag(self, tag):
        self.tags.append(tag)
```

Индивидуальный список:

```python
class TagStorage:
    def __init__(self):
        self.tags = []

    def add_tag(self, tag):
        self.tags.append(tag)
```

В первом случае список один на всех.
Во втором — у каждого экземпляра свой.
