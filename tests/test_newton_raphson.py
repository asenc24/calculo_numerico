import unittest
import math
from newton_raphson import newton_raphson

class TestNewtonRaphson(unittest.TestCase):
    def test_raiz_cuadrada_de_2(self):
        # f(x) = x^2 - 2, raíz esperada: sqrt(2)
        def f(x):
            return x**2 - 2
        def df(x):
            return 2*x
        x0 = 1.0
        raiz, iteraciones = newton_raphson(f, df, x0)
        self.assertAlmostEqual(raiz, math.sqrt(2), places=6)
        self.assertLessEqual(iteraciones, 10)

    def test_derivada_cero(self):
        # f(x) = x^3, df(x) = 3x^2, x0 = 0, la derivada es cero en x=0
        def f(x):
            return x**3
        def df(x):
            return 3*x**2
        x0 = 0.0
        with self.assertRaises(ValueError):
            newton_raphson(f, df, x0)

if __name__ == "__main__":
    unittest.main()
