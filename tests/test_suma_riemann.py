import unittest
from suma_riemann import suma_riemann

class TestSumaRiemann(unittest.TestCase):
    def test_integral_lineal(self):
        # f(x) = x en [0, 1], integral exacta = 0.5
        def f(x):
            return x
        resultado = suma_riemann(f, 0, 1, 1000)
        self.assertAlmostEqual(resultado, 0.5, places=3)

    def test_integral_constante(self):
        # f(x) = 2 en [0, 3], integral exacta = 6
        def f(x):
            return 2
        resultado = suma_riemann(f, 0, 3, 1000)
        self.assertAlmostEqual(resultado, 6.0, places=3)

    def test_integral_cuadratica(self):
        # f(x) = x^2 en [0, 1], integral exacta = 1/3
        def f(x):
            return x**2
        resultado = suma_riemann(f, 0, 1, 10000)
        self.assertAlmostEqual(resultado, 1/3, places=3)

if __name__ == "__main__":
    unittest.main()
