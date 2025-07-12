def regla_trapecio(f, a, b, n):
    """
    Calcula la integral definida de f en [a, b] usando la regla del trapecio con n subintervalos.
    
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
        Aproximación de la integral definida usando la regla del trapecio.
    """
    # Paso 1: Calcular el ancho de cada subintervalo
    h = (b - a) / n
    print(f"Ancho de cada subintervalo (h): {h}")
    # Paso 2: Calcular los extremos
    suma = f(a) + f(b)
    print(f"f(a) = {f(a)}, f(b) = {f(b)}")
    # Paso 3: Sumar los valores de f en los puntos internos
    for i in range(1, n):
        x = a + i * h
        fx = f(x)
        suma += 2 * fx
        print(f"Punto interno x_{i} = {x}, f(x_{i}) = {fx}")
    # Paso 4: Multiplicar por h/2
    resultado = (h / 2) * suma
    print(f"Suma total: {suma}")
    print(f"Resultado final: {resultado}")
    return resultado
