class Calculator:
    def add(self, a, b):
        self._validate_numbers(a, b)
        return a + b

    def divide(self, a, b):
        self._validate_numbers(a, b)
        if b == 0:
            raise ValueError("Division by zero is not allowed")
        return a / b

    def _validate_numbers(self, a, b):
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise TypeError("Inputs must be a number")
