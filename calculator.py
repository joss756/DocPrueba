class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ValueError("No se puede dividir por cero")
        return a / b

    def chained_operation(self, expression):
        # Evalúa una expresión simple encadenada, como "2 + 3 * 4"
        # Nota: Esto es básico y no maneja paréntesis complejos; usa eval() con precaución en producción.
        try:
            return eval(expression)
        except Exception as e:
            raise ValueError(f"Expresión inválida: {e}")
