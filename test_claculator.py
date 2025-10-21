import unittest
import timeit
from calculator import Calculator

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    # Prueba unitaria: Verificar que la suma sea correcta
    def test_add(self):
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(0, 0), 0)

    # Caso de prueba de integración: Operaciones encadenadas
    def test_chained_operation(self):
        # Prueba una expresión encadenada simple
        result = self.calc.chained_operation("2 + 3 * 4")
        self.assertEqual(result, 14)  # 2 + (3*4) = 14
        result = self.calc.chained_operation("10 - 2 / 2")
        self.assertEqual(result, 9)  # 10 - (2/2) = 9
        with self.assertRaises(ValueError):
            self.calc.chained_operation("invalid expression")

    # Propuesta de prueba de rendimiento: Repetir una operación miles de veces
    def test_performance(self):
        # Mide el tiempo para sumar 1 + 1 repetido 10,000 veces
        code_to_test = "calc.add(1, 1)"
        setup = "from calculator import Calculator; calc = Calculator()"
        time_taken = timeit.timeit(code_to_test, setup=setup, number=10000)
        print(f"Tiempo para 10,000 sumas: {time_taken:.4f} segundos")
        # No hay aserción estricta; solo imprime el tiempo. En un entorno real, podrías comparar con un umbral.
        self.assertLess(time_taken, 1.0)  # Ejemplo: Debe ser menor a 1 segundo (ajusta según tu máquina)

if __name__ == '__main__':
    unittest.main()