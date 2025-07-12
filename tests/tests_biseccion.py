import unittest
import math
from biseccion import biseccion

class TestBiseccion(unittest.TestCase):
    def test_raiz_cuadrada_de_2(self):
        # f(x) = x^2 - 2, raíz esperada: sqrt(2)
        def f(x):
            return x**2 - 2
        a, b = 1, 2
        raiz = biseccion(f, a, b)
        self.assertAlmostEqual(raiz, math.sqrt(2), places=6)

    def test_intervalo_invalido(self):
        # f(x) = x^2 + 1 no tiene raíz real en [0, 1]
        def f(x):
            return x**2 + 1
        a, b = 0, 1
        with self.assertRaises(ValueError):
            biseccion(f, a, b)

    def test_tolerancia(self):
        # f(x) = x - 0.5, raíz esperada: 0.5
        def f(x):
            return x - 0.5
        a, b = 0, 1
        raiz = biseccion(f, a, b, tol=1e-2)
        self.assertAlmostEqual(raiz, 0.5, places=2)

if __name__ == "__main__":
    unittest.main()
