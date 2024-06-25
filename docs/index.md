# Introducción
 
A continuaciòn se muestra la documentaciòn de tres funciones que se utilizan para resolver ecuaciones diferenciales ordinarias (ODEs): el método de Euler, el método de Runge-Kutta de segundo orden (RK2) y el método de Runge-Kutta de cuarto orden (RK4).
 
## Método de Euler

La fórmula del método de Euler se expresa como:

$$ y_{n+1} = y_{n} + h \cdot f(t_{n}, y_{n}) $$

## Método de Runge-Kutta de segundo orden (RK2)

Para RK2 se tiene:

$$ k_{1} = f(t_{n}, y_{n}) $$

$$ k_{2} = f \left( t_{n} + \frac{h}{2}, y_{n} + \frac{h}{2} k_{1} \right) $$

$$ y_{n+1} = y_{n} + h \cdot k_{2} $$

## Método de Runge-Kutta de cuarto orden (RK4)

El método de Runge-Kutta de cuarto orden (RK4) utiliza las siguientes ecuaciones:

$$ k_{1} = f(t_{n}, y_{n}) $$

$$ k_{2} = f \left( t_{n} + \frac{h}{2}, y_{n} + \frac{h}{2} k_{1} \right) $$

$$ k_{3} = f \left( t_{n} + \frac{h}{2}, y_{n} + \frac{h}{2} k_{2} \right) $$

$$ k_{4} = f(t_{n} + h, y_{n} + h \cdot k_{3}) $$

$$ y_{n+1} = y_{n} + \frac{h}{6} \left( k_{1} + 2k_{2} + 2k_{3} + k_{4} \right) $$


#### Welcome to MkDocs

For full documentation visit [mkdocs.org](https://www.mkdocs.org).

#### Commands

* `mkdocs new [dir-name]` - Create a new project.
* `mkdocs serve` - Start the live-reloading docs server.
* `mkdocs build` - Build the documentation site.
* `mkdocs -h` - Print help message and exit.

#### Project layout

    mkdocs.yml    # The configuration file.
    docs/
        index.md  # The documentation homepage.
        ...       # Other markdown pages, images and other files.
