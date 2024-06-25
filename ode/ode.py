# ode/ode.py

def euler(x0, t_final, dt, f):
    """
    Método de Euler
    El método de Euler es un método numérico simple para resolver ODEs.
    Se basa en la aproximación lineal de la derivada en cada paso.

    Args:
        x0 (float): El valor inicial de la variable dependiente.
        t_final (float): El tiempo final hasta el cual se realiza la integración.
        dt (float): El tamaño del paso de integración.
        f (function): La función que describe la ODE (dx/dt = f(x, t)).

    Returns:
        list: Lista de tiempos.
        list: Lista de valores de x en cada paso de tiempo.

    Example:
        >>> def f(x, t):
        >>>     return t - x
        >>> t, x = euler(0, 10, 0.1, f)
        >>> print(t, x)
    """
    lista_t = []
    lista_x = []

    x = x0
    t = 0.0

    while t < t_final + dt:  # Para incluir t_final
        lista_t.append(t)
        lista_x.append(x)

        x += dt * f(x, t)
        t += dt

    return lista_t, lista_x


def rk2(x0, t_final, h, f):
    """
    RK2 mejora la precisión en comparación con el método de Euler al evaluar
    la pendiente en dos puntos dentro del intervalo.

    Args:
        x0 (float): El valor inicial de la variable dependiente.
        t_final (float): El tiempo final hasta el cual se realiza la integración.
        h (float): El tamaño del paso de integración.
        f (function): La función que describe la ODE (dx/dt = f(x, t)).

    Returns:
        list: Lista de tiempos.
        list: Lista de valores de x en cada paso de tiempo.

    Example:
        >>> def f(x, t):
        >>>     return t - x
        >>> t, x = rk2(0, 10, 0.1, f)
        >>> print(t, x)
    """
    lista_t = []
    lista_x = []

    x = x0
    t = 0.0

    while t < t_final + h:  # Para incluir t_final
        lista_t.append(t)
        lista_x.append(x)

        k1 = f(x, t)
        k2 = f(x + 0.5 * h * k1, t + 0.5 * h)

        x += h * k2
        t += h

    return lista_t, lista_x


def rk4(x0, t_final, h, f):
    """
    Método de Runge-Kutta de cuarto orden (RK4) para resolver ODEs.

    RK4 es uno de los métodos más utilizados debido a su precisión y estabilidad.
    Evalúa la pendiente en cuatro puntos dentro del intervalo.

    Args:
        x0 (float): El valor inicial de la variable dependiente.
        t_final (float): El tiempo final hasta el cual se realiza la integración.
        h (float): El tamaño del paso de integración.
        f (function): La función que describe la ODE (dx/dt = f(x, t)).

    Returns:
        list: Lista de tiempos.
        list: Lista de valores de x en cada paso de tiempo.

    Example:
        >>> def f(x, t):
        >>>     return t - x
        >>> t, x = rk4(0, 10, 0.1, f)
        >>> print(t, x)
    """
    lista_t = []
    lista_x = []

    x = x0
    t = 0.0

    while t < t_final + h:  # Para incluir t_final
        lista_t.append(t)
        lista_x.append(x)

        k1 = f(x, t)
        k2 = f(x + 0.5 * h * k1, t + 0.5 * h)
        k3 = f(x + 0.5 * h * k2, t + 0.5 * h)
        k4 = f(x + h * k3, t + h)

        x += h / 6.0 * (k1 + 2.0 * k2 + 2.0 * k3 + k4)
        t += h

    return lista_t, lista_x

