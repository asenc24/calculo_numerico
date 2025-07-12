def biseccion(f, a, b, tol=1e-6, max_iter=100):
    """
    Método de Bisección para encontrar una raíz de la función f en el intervalo [a, b].

    Parámetros:
    - f: función continua
    - a, b: extremos del intervalo (f(a)*f(b) < 0)
    - tol: tolerancia para el error
    - max_iter: número máximo de iteraciones

    Retorna:
    - raíz aproximada
    """
    if f(a) * f(b) >= 0:
        raise ValueError("La función debe cambiar de signo en el intervalo [a, b].")

    for i in range(max_iter):
        c = (a + b) / 2
        if abs(f(c)) < tol or (b - a) / 2 < tol:
            return c
        if f(a) * f(c) < 0:
            b = c
        else:
            a = c
    return (a + b) / 2