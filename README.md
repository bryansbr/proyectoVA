# Proyecto Final - Vida Artificial

**Autores:** Bryan Steven Biojó R. 1529879-2711 & Joel Alexander Ramírez N. 1528879-2711
         
**Descripción:** Proyecto final del curso de Vida Artificial. Fractal de Mandelbrot y sus variaciones.


**INSTRUCCIONES DE EJECUCIÓN.**

1. Descargar **Python** de: https://www.python.org/downloads/ en su versión 3.7.x (no acepta versiones inferiores).

2. Instalar **Anaconda + Jupyter Notebook** de: https://www.anaconda.com/distribution/ (escoger la distribución para el SO correspondiente).

3. Si ya se tiene la distribución Anaconda de Python, ejecutarla a través de **Anaconda Navigator** y abrir **Jupyter Notebook** en **localhost**. El puerto por defecto es el **8888**.
- Cargar el archivo *Mandelbrot.ipynb* en el Jupyter Notebook.
- Recorrer el archivo.

4. Si no se cuenta con lo anterior, cargar el archivo *Mandelbrot.ipynb* en el siguiente Hub: https://mybinder.org/v2/gh/jupyterlab/jupyterlab-demo/try.jupyter.org?urlpath=lab. Es posible editar el archivo como si se tuviese el Jupyter instalado, es decir, se pueden generar nuevos fractales si así se desea.


**EXTRA:** Para ver el código completo, abrir el archivo *mandelbrot.py*. Si se ejecuta lanzará error puesto que está diseñado para utilizarse con Jupyter Notebook.


**FÓRMULAS IMPLEMENTADAS.**

1) z^2+C <- Fórmula original del fractal de Mandelbrot.
2) z^3+C
3) z^5+C
4) z^2+(1/C)
5) z^7+(1/C)
6) z^2+(1/C^2)
7) z^2+C+(1/C)
8) [(z+C^2-1)/C^2]^2 
9) z^2+(1/C) interseccción z^2+C (o eso parece).
10) z^3-z+C

**Nota:** Se pueden modificar o agregar nuevas funciones. Para esto, crear una función mandelbrot, por ejemplo **_def mandelbrot11_** y modificar la fórmula generadora del fractal. Después, modificar en la variable *resultado* el nombre de *mandelbrot<número>* al número correspondiente y ajustar la gráfica en *fila_index* y *columna_index*. Finalmente, se puede cambiar el color de la gráfica en *plt.imshow* en el parámetro *cmap*.

**REFERENCIAS.**

- https://www.youtube.com/watch?v=gECmGwD0DaI <- **Conjunto de Mandelbrot en Python.**
- https://es.wikipedia.org/wiki/Desarrollo_de_fractales_mediante_el_m%C3%A9todo_de_Mandelbrot <- **Desarrollo de fractales mediante el método de Mandelbrot.**
- https://matplotlib.org/3.1.0/tutorials/colors/colormaps.html <- **Mapa de colores (cmap).**
