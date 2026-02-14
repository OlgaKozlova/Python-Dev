

class User:
    def __init__(self, name):
        self.name = name
    
    def greet(self):
        return f'hello, i am {self.name}'

class Admin(User):
    def __init__(self, name, level):
        super().__init__(name)
        self.level = level

    def greet(self):
        base_greet = super().greet()
        return f'{base_greet} Admin level: {self.level}'