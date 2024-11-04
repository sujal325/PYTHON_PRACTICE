class modular:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def calculation(self):
        return self.a % self.b


result = modular(1002, 7)
print(result.calculation())
