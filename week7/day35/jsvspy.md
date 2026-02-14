# Python vs JavaScript — сравнение через одинаковые примеры

Документ построен как «одна задача — два языка».

---

# 1. Ссылки и мутация

## Задача: две переменные указывают на один массив/список

### Python

```python
a = [1, 2]
b = a

a.append(3)
print(b)  # [1, 2, 3]
```

### JavaScript

```javascript
const a = [1, 2];
const b = a;

a.push(3);
console.log(b); // [1, 2, 3]
```

В обоих случаях мутируется один объект.

---

# 2. `+=` и создание нового объекта

## Задача: число и копия

### Python

```python
a = 1
b = a

a += 1
print(a, b)  # 2 1
```

`int` immutable → создаётся новый объект.

### JavaScript

```javascript
let a = 1;
let b = a;

a += 1;
console.log(a, b); // 2 1
```

Поведение совпадает.

---

# 3. `+=` для списка

### Python

```python
a = [1]
b = a

a += [2]
print(b)  # [1, 2]
```

`+=` вызывает `__iadd__` → мутация.

### JavaScript

```javascript
const a = [1];
const b = a;

a.push(2);
console.log(b); // [1, 2]
```

В JS нет перегрузки операторов — мутация всегда через методы.

---

# 4. Значения по умолчанию

## Задача: накопление состояния

### Python

```python
def f(x, acc=[]):
    acc.append(x)
    return acc

print(f(1))
print(f(2))  # [1, 2]
```

Default вычисляется один раз.

### JavaScript

```javascript
function f(x, acc = []) {
  acc.push(x);
  return acc;
}

console.log(f(1));
console.log(f(2)); // [2]
```

Default вычисляется при каждом вызове.

---

# 5. Атрибут класса / static поле

## Задача: общий список для всех экземпляров

### Python

```python
class A:
    xs = []
    def add(self, x):
        self.xs.append(x)


a1 = A()
a2 = A()
a1.add(1)
a2.add(2)

print(A.xs)  # [1, 2]
```

### JavaScript

```javascript
class A {
  static xs = [];
  add(x) {
    A.xs.push(x);
  }
}

const a1 = new A();
const a2 = new A();
a1.add(1);
a2.add(2);

console.log(A.xs); // [1, 2]
```

В Python поиск атрибута идёт: instance → class.

---

# 6. Переназначение вместо мутации

## Задача: изменение числа в классе

### Python

```python
class B:
    n = 0
    def inc(self):
        self.n += 1

b1 = B()
b2 = B()
b1.inc()
b2.inc()

print(b1.n, b2.n, B.n)  # 1 1 0
```

`int` immutable → создаётся атрибут экземпляра.

### JavaScript

```javascript
class B {
  static n = 0;
  inc() {
    this.n += 1;
  }
}

const b1 = new B();
const b2 = new B();
b1.inc();
b2.inc();

console.log(b1.n, b2.n, B.n);
```

В JS поведение будет зависеть от того, существует ли поле в экземпляре.

---

# 7. `self` vs `this`

### Python

```python
class C:
    def show(self):
        print(self)
```

`self` — обычный аргумент.

### JavaScript

```javascript
class C {
  show() {
    console.log(this);
  }
}

const c = new C();
const f = c.show;
f(); // потеря контекста
```

В JS `this` зависит от способа вызова.

---

# Итоговое различие

Python:

- единая модель объектов
- важна мутация и разделяемое состояние
- строгий поиск атрибутов

JavaScript:

- важен контекст вызова
- прототипная цепочка
- нет перегрузки операторов
