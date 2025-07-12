def suma_riemann(f, a, b, n):
    """
    Calcula la suma de Riemann para la función f en el intervalo [a, b] usando n subintervalos.
    
    Parámetros:
    f : función
        Función a integrar.
    a : float
        Extremo izquierdo del intervalo.
    b : float
        Extremo derecho del intervalo.
    n : int
        Número de subintervalos.
    
    Retorna:
    float
        Aproximación de la integral definida por suma de Riemann (puntos izquierdos).
    """
    dx = (b - a) / n
    suma = 0.0
    for i in range(n):
        x = a + i * dx
        suma += f(x) * dx
    return suma
