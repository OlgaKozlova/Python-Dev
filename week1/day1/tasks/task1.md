### Что будет выведено и почему
```
def f():
    print("inside f")

print("before")

def g():
    f()
    print("inside g")

print("after")
```
### Ответ
```
before
after
```
