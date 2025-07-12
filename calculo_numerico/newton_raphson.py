
def newton_raphson(f, df, x0, tol=1e-6, max_iter=100):
    """
    Método de Newton-Raphson para encontrar raíces de una función.
    
    Parámetros:
    f : función
        Función de la cual se busca la raíz.
    df : función
        Derivada de la función f.
    x0 : float
        Valor inicial para la iteración.
    tol : float, opcional
        Tolerancia para el criterio de parada (por defecto 1e-6).
    max_iter : int, opcional
        Número máximo de iteraciones (por defecto 100).
    
    Retorna:
    x : float
        Aproximación de la raíz.
    n_iter : int
        Número de iteraciones realizadas.
    
    Levanta:
    ValueError si la derivada es cero en algún punto.
    """
    x = x0
    for n_iter in range(1, max_iter + 1):
        fx = f(x)
        dfx = df(x)
        # Verificar que la derivada no sea cero
        if dfx == 0:
            raise ValueError(f"La derivada es cero en x = {x}. No se puede continuar.")
        # Calcular el siguiente valor usando la fórmula de Newton-Raphson
        x_new = x - fx / dfx
        # Documentar el paso
        print(f"Iteración {n_iter}: x = {x}, f(x) = {fx}, f'(x) = {dfx}, x_new = {x_new}")
        # Verificar criterio de parada
        if abs(x_new - x) < tol:
            return x_new, n_iter
        x = x_new
    # Si no converge, retornar el último valor
    print("Advertencia: No se alcanzó la tolerancia en el número máximo de iteraciones.")
    return x, max_iter

# Ejemplo de prueba
if __name__ == "__main__":
    # Buscar la raíz de f(x) = x^2 - 2 (raíz esperada: sqrt(2))
    def f(x):
        return x**2 - 2
    def df(x):
        return 2*x
    x0 = 1.0
    raiz, iteraciones = newton_raphson(f, df, x0)
    print(f"\nRaíz aproximada: {raiz}")
    print(f"Iteraciones: {iteraciones}")
    print(f"Error absoluto: {abs(raiz - 2**0.5)}")
