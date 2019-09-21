"""

Nombre del archivo: mandelbrot.py
Fecha de creación: 19/09/2019
Fecha de modificación: 20/09/2019
Autores: Bryan Steven Biojó R.     1529879-2711
         Joel Alexander Ramírez N. 1528879-2711

"""

import numpy # Librería para computación científica.
import matplotlib.pyplot as plt # Librería para graficar.
from numba import jit # Compilador de JIT que mejora la rapidez del código.

# ******************************************* FUNCIÓN 1 *******************************************

@jit
def mandelbrot1(Re, Im, maxIteraciones): # Primera función. Pinta z^2+C
    z = 0.0j
    c = complex(Re, Im)
    
    for i in range(maxIteraciones):
        z = pow(z, 2) + c
        
        if((pow(z.real, 2) + pow(z.imag, 2)) >= 4):
            return i

    return maxIteraciones

# ******************************************* GRÁFICA 1 *******************************************

filas = 2000
columnas = 2000

resultado = numpy.zeros([filas, columnas])
for fila_index, Re in enumerate(numpy.linspace(-2, 1, num = filas)):
    for columna_index, Im in enumerate(numpy.linspace(-1, 1, num = columnas)):
        resultado[fila_index, columna_index] = mandelbrot1(Re, Im, 100)

plt.figure(dpi = 300)
plt.imshow(resultado.T, cmap = 'gray', interpolation = 'bilinear', extent = [-2, 1, -1, 1])
plt.xlabel('Eje Real')
plt.ylabel('Eje Imaginario')
plt.show()

# ******************************************* FUNCIÓN 2 *******************************************

@jit
def mandelbrot2(Re, Im, maxIteraciones): # Segunda función. Pinta z^3+C
    z = 0.0j
    c = complex(Re, Im)
    
    for i in range(maxIteraciones):
        z = pow(z, 3) + c
        
        if((pow(z.real, 2) + pow(z.imag, 2)) >= 4):
            return i

    return maxIteraciones

# ******************************************* GRÁFICA 2 *******************************************

filas = 2000
columnas = 2000

resultado = numpy.zeros([filas, columnas])
for fila_index, Re in enumerate(numpy.linspace(-2, 1, num = filas)):
    for columna_index, Im in enumerate(numpy.linspace(-1.5, 1.5, num = columnas)):
        resultado[fila_index, columna_index] = mandelbrot2(Re, Im, 100)

plt.figure(dpi = 300)
plt.imshow(resultado.T, cmap = 'hot', interpolation = 'bilinear', extent = [-2, 1, -1.5, 1.5])
plt.xlabel('Eje Real')
plt.ylabel('Eje Imaginario')
plt.show()

# ******************************************* FUNCIÓN 3 *******************************************

@jit
def mandelbrot3(Re, Im, maxIteraciones): # Tecera función. Pinta z^5+C
    z = 0.0j
    c = complex(Re, Im)
    
    for i in range(maxIteraciones):
        z = pow(z, 5) + c
        
        if((pow(z.real, 2) + pow(z.imag, 2)) >= 4):
            return i

    return maxIteraciones

# ******************************************* GRÁFICA 3 *******************************************

filas = 2000
columnas = 2000

resultado = numpy.zeros([filas, columnas])
for fila_index, Re in enumerate(numpy.linspace(-2, 1, num = filas)):
    for columna_index, Im in enumerate(numpy.linspace(-1, 1, num = columnas)):
        resultado[fila_index, columna_index] = mandelbrot3(Re, Im, 100)

plt.figure(dpi = 300)
plt.imshow(resultado.T, cmap = 'winter', interpolation = 'bilinear', extent = [-2, 1, -1, 1])
plt.xlabel('Eje Real')
plt.ylabel('Eje Imaginario')
plt.show()

# ******************************************* FUNCIÓN 4 *******************************************

@jit
def mandelbrot4(Re, Im, maxIteraciones): # Cuarta función. Pinta z^2+(1/C)
    z = 0.0j
    c = complex(Re, Im)
    
    for i in range(maxIteraciones):
        z = pow(z, 2) + (1 / c)
        
        if((pow(z.real, 2) + pow(z.imag, 2)) >= 4):
            return i

    return maxIteraciones

# ******************************************* GRÁFICA 4 *******************************************

filas = 2000
columnas = 2000

resultado = numpy.zeros([filas, columnas])
for fila_index, Re in enumerate(numpy.linspace(-2, 4, num = filas)):
    for columna_index, Im in enumerate(numpy.linspace(-3, 3, num = columnas)):
        resultado[fila_index, columna_index] = mandelbrot4(Re, Im, 100)

plt.figure(dpi = 300)
plt.imshow(resultado.T, cmap = 'Wistia', interpolation = 'bilinear', extent = [-2, 4, -3, 3])
plt.xlabel('Eje Real')
plt.ylabel('Eje Imaginario')
plt.show()

# ******************************************* FUNCIÓN 5 *******************************************

@jit
def mandelbrot5(Re, Im, maxIteraciones): # Quinta función. Pinta z^7+(1/C)
    z = 0.0j
    c = complex(Re, Im)
    
    for i in range(maxIteraciones):
        z = pow(z, 7) + (1 / c)
        
        if((pow(z.real, 2) + pow(z.imag, 2)) >= 4):
            return i

    return maxIteraciones

# ******************************************* GRÁFICA 5 *******************************************

filas = 2000
columnas = 2000

resultado = numpy.zeros([filas, columnas])
for fila_index, Re in enumerate(numpy.linspace(-2, 2, num = filas)):
    for columna_index, Im in enumerate(numpy.linspace(-2, 2, num = columnas)):
        resultado[fila_index, columna_index] = mandelbrot5(Re, Im, 100)

plt.figure(dpi = 300)
plt.imshow(resultado.T, cmap = 'autumn', interpolation = 'bilinear', extent = [-2, 2, -2, 2])
plt.xlabel('Eje Real')
plt.ylabel('Eje Imaginario')
plt.show()

# ******************************************* FUNCIÓN 6 *******************************************

@jit
def mandelbrot6(Re, Im, maxIteraciones): # Sexta función. Pinta z^2+(1/C^2)
    z = 0.0j
    c = complex(Re, Im)
    
    for i in range(maxIteraciones):
        z = pow(z, 2) + (1 / (c * c))
        
        if((pow(z.real, 2) + pow(z.imag, 2)) >= 4):
            return i

    return maxIteraciones

# ******************************************* GRÁFICA 6 *******************************************

filas = 2000
columnas = 2000

resultado = numpy.zeros([filas, columnas])
for fila_index, Re in enumerate(numpy.linspace(-2, 2, num = filas)):
    for columna_index, Im in enumerate(numpy.linspace(-3, 1.5, num = columnas)):
        resultado[fila_index, columna_index] = mandelbrot6(Re, Im, 100)

plt.figure(dpi = 300)
plt.imshow(resultado.T, cmap = 'bone', interpolation = 'bilinear', extent = [-2, 2, -3, 1.5])
plt.xlabel('Eje Real')
plt.ylabel('Eje Imaginario')
plt.show()

# ******************************************* FUNCIÓN 7 *******************************************

@jit
def mandelbrot7(Re, Im, maxIteraciones): # Séptima función. Pinta z^2+C+(1/C)
    z = 0.0j
    c = complex(Re, Im)
    
    for i in range(maxIteraciones):
        z = pow(z, 2) + c + (1 / c)
        
        if((pow(z.real, 2) + pow(z.imag, 2)) >= 4):
            return i

    return maxIteraciones

# ******************************************* GRÁFICA 7 *******************************************

filas = 2000
columnas = 2000

resultado = numpy.zeros([filas, columnas])
for fila_index, Re in enumerate(numpy.linspace(-2, 2, num = filas)):
    for columna_index, Im in enumerate(numpy.linspace(-3, 2, num = columnas)):
        resultado[fila_index, columna_index] = mandelbrot7(Re, Im, 100)

plt.figure(dpi = 300)
plt.imshow(resultado.T, cmap = 'magma', interpolation = 'bilinear', extent = [-2, 2, -3, 2])
plt.xlabel('Eje Real')
plt.ylabel('Eje Imaginario')
plt.show()

# ******************************************* FUNCIÓN 8 *******************************************

@jit
def mandelbrot8(Re, Im, maxIteraciones): # Octava función. Pinta [(z+C^2-1)/C^2]^2 
    z = 0.0j
    c = complex(Re, Im)
    
    for i in range(maxIteraciones):
        z = pow(((z + (c * c) - 1) / (c * c)), 2)
        
        if((pow(z.real, 2) + pow(z.imag, 2)) >= 4):
            return i

    return maxIteraciones

# ******************************************* GRÁFICA 8 *******************************************

filas = 2000
columnas = 2000

resultado = numpy.zeros([filas, columnas])
for fila_index, Re in enumerate(numpy.linspace(-2, 2, num = filas)):
    for columna_index, Im in enumerate(numpy.linspace(-2, 2, num = columnas)):
        resultado[fila_index, columna_index] = mandelbrot8(Re, Im, 100)

plt.figure(dpi = 300)
plt.imshow(resultado.T, cmap = 'binary', interpolation = 'bilinear', extent = [-2, 2, -2, 2])
plt.xlabel('Eje Real')
plt.ylabel('Eje Imaginario')
plt.show()

# ******************************************* FUNCIÓN 9 *******************************************

@jit
def mandelbrot9(Re, Im, maxIteraciones): # Novena función. Pinta [z^2+(1/C) interseccción z^2+C (o eso parece).
    z = 0.0j
    c = complex(Re, Im)
    
    for i in range(maxIteraciones):
        z = pow(z, 2) + (1 / c)
        z = pow(z, 2) + c
        
        if((pow(z.real, 2) + pow(z.imag, 2)) >= 4):
            return i

    return maxIteraciones

# ******************************************* GRÁFICA 9 *******************************************

filas = 2000
columnas = 2000

resultado = numpy.zeros([filas, columnas])
for fila_index, Re in enumerate(numpy.linspace(-2, 2, num = filas)):
    for columna_index, Im in enumerate(numpy.linspace(-2, 2, num = columnas)):
        resultado[fila_index, columna_index] = mandelbrot9(Re, Im, 100)

plt.figure(dpi = 300)
plt.imshow(resultado.T, cmap = 'Greens', interpolation = 'bilinear', extent = [-2, 2, -2, 2])
plt.xlabel('Eje Real')
plt.ylabel('Eje Imaginario')
plt.show()

# ******************************************* FUNCIÓN 10 ******************************************

@jit
def mandelbrot10(Re, Im, maxIteraciones): # Décima función. Pinta z^3-z+C
    z = 0.0j
    c = complex(Re, Im)
    
    for i in range(maxIteraciones):
        z = pow(z, 3) - z + c
        
        if((pow(z.real, 2) + pow(z.imag, 2)) >= 4):
            return i

    return maxIteraciones

# ******************************************* GRÁFICA 10 ******************************************

filas = 2000
columnas = 2000

resultado = numpy.zeros([filas, columnas])
for fila_index, Re in enumerate(numpy.linspace(-2, 2, num = filas)):
    for columna_index, Im in enumerate(numpy.linspace(-1, 1, num = columnas)):
        resultado[fila_index, columna_index] = mandelbrot10(Re, Im, 100)

plt.figure(dpi = 300)
plt.imshow(resultado.T, cmap = 'YlOrBr', interpolation = 'bilinear', extent = [-2, 1, -1, 1])
plt.xlabel('Eje Real')
plt.ylabel('Eje Imaginario')
plt.show()
