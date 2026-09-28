from abc import ABC, abstractmethod


class Calculation(ABC):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    @abstractmethod
    def execute(self):
        """Execute the calculation and return the result."""
        pass  # pragma: no cover

    def __str__(self):
        return f"{self.__class__.__name__}: {self.a}, {self.b} = {self.execute()}"


class Add(Calculation):
    def execute(self):
        return self.a + self.b


class Subtract(Calculation):
    def execute(self):
        return self.a - self.b