# День 34 — Практика

## Задача 1

Есть классы:

```python
class EmailSender:
    def send(self, message):
        print(f"Email: {message}")

class SMSSender:
    def send(self, message):
        print(f"SMS: {message}")
```

1. Напиши функцию notify(sender, message), которая вызывает метод send.
2. Проверь, что она работает для обоих классов.
3. Что произойдёт, если передать объект без метода send?

---

## Задача 2

Сделай пример композиции:

1. Класс CPU с методом compute().
2. Класс Computer, который содержит CPU.
3. Метод run() у Computer должен делегировать вызов compute().

Ответь:

- Почему это композиция?
- Было бы логично делать Computer наследником CPU?

---

# Решения

## Решение 1

```python
def notify(sender, message):
    sender.send(message)

notify(EmailSender(), "Hello")
notify(SMSSender(), "Hello")
```

Если передать объект без send(), будет AttributeError во время выполнения.

---

## Решение 2

```python
class CPU:
    def compute(self):
        return "Computing"

class Computer:
    def __init__(self):
        self.cpu = CPU()

    def run(self):
        return self.cpu.compute()
```

Это композиция, потому что Computer содержит CPU (has-a).

Наследование было бы нелогичным: Computer не является CPU.
