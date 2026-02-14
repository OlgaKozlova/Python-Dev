# День 33 — Практика

## Задача 1 — Базовое наследование

Реализовать:

- Класс User
  - **init**(self, name)
  - метод get_role() → возвращает "user"

- Класс Admin(User)
  - переопределить get_role() → "admin"
  - добавить метод ban()

Проверить полиморфизм через список объектов.

---

## Задача 2 — super() и расширение поведения

Реализовать:

- Класс User
  - **init**(self, name)
  - greet() → возвращает строку

- Класс Admin(User)
  - добавить level
  - переопределить greet(), используя super()
  - не использовать print внутри метода

Проверить, что возвращается единая строка.

---

## Задача 3 — Контракт метода

Создать базовый класс Shape с методом area(),
который выбрасывает NotImplementedError.

Создать классы:

- Rectangle
- Circle

Реализовать area() корректно.

Проверить, что базовый класс нельзя использовать напрямую.

---

# Решения

## Решение 1

```python
class User:
    def __init__(self, name):
        self.name = name

    def get_role(self):
        return "user"


class Admin(User):
    def get_role(self):
        return "admin"

    def ban(self):
        print(f"{self.name} banned")
```

---

## Решение 2

```python
class User:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"Hello, I am {self.name}"


class Admin(User):
    def __init__(self, name, level):
        super().__init__(name)
        self.level = level

    def greet(self):
        base = super().greet()
        return f"{base}\nAdmin level: {self.level}"
```

---

## Решение 3

```python
class Shape:
    def area(self):
        raise NotImplementedError


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        import math
        return math.pi * self.radius ** 2
```

Попытка вызвать Shape().area() приведёт к ошибке — это ожидаемое поведение.
