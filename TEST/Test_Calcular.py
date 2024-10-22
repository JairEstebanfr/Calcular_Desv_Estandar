import unittest
from SRC.Calcular import CalculosEstadisticos

class TestCalcular(unittest.TestCase):
    def setUp(self):
        self.calcular = CalculosEstadisticos()

    def tearDown(self):
        self.calcular = None
    def test_calcular_media(self):
        # Arrange
        num = [1, 2, 3, 4, 5]
        resultado_final = 3.0
        # Do
        resultado_actual = self.calcular.calcular_media(num)
        # Assert
        self.assertEqual(resultado_final, resultado_actual)
        # Caso adicional
        num = [10, 20, 30, 40, 50]
        resultado_final = 30.0
        resultado_actual = self.calcular.calcular_media(num)
        self.assertEqual(resultado_final, resultado_actual)
    def test_calcular_desviacion_estandar(self):
        # Arrange
        num = [1, 2, 3, 4, 5]
        resultado_esperado = 1.58
        # Do
        resultado_actual = self.calcular.calcular_desviacion_estandar(num)
        # Assert
        self.assertAlmostEqual(resultado_esperado, resultado_actual, places=2)
        # Casos adicionales
        num = [10, 20, 30, 40, 50]
        resultado_esperado = 15.81
        resultado_actual = self.calcular.calcular_desviacion_estandar(num)
        self.assertAlmostEqual(resultado_esperado, resultado_actual, places=2)
        # Caso para lista vacía
        num = []
        resultado_actual = self.calcular.calcular_desviacion_estandar(num)
        self.assertIsNone(resultado_actual)
if __name__ == '_main_':
    unittest.main()