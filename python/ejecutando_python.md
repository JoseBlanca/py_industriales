
# Ejecutando Python

## El interprete

Python dispone de un intérpretre interactivo en la línea de comandos que puede ejecutarse con el comando python3.
Una vez en el intérprete podremos ejecutar cualquier comando de Python.

```
    jose@sagan:~$ python3
    Python 3.7.3 (default, Jul 25 2020, 13:03:44) 
    [GCC 8.3.0] on linux
    Type "help", "copyright", "credits" or "license" for more information.
    >>> print('Hola')
    Hola
    >>> 2 + 2
    4
    >>>
```

El intérprete suele utilizarse para ejecutar pequeños fragmentos de código.

## Ficheros de código

Lo más común es escribir un script o un programa en uno o varios ficheros de texto y ejecutar el programa utilizando el comando Python.

```
    jose@sagan:~$ python3 hola_mundo.py
    Hola
   
```

Los ficheros con código de Python, por convención, suelen tener tener la extensión *.py*.

Python es un lenguaje interpretado, no es necesario compilar previamente los ficheros con código fuente, el intérprete lo hará por nosotros.

Para editar Python es recomendable utilizar un editor de código. En la actualidad uno de los más populares es [Visual Studio Code](https://code.visualstudio.com/) junto a la [extensión para Python](https://code.visualstudio.com/docs/languages/python).

## Jupyter Notebooks

Otra forma alternativa de utilizar Python es utilizar [Jupyter Notebooks](https://jupyter.org/).
Son documentos que incluyen código Python, resultados de la ejecución y fragmentos [markdown](https://es.wikipedia.org/wiki/Markdown) y que se editan y se visualizan en el navegador web.

JupyterLab es un entorno de creación de Notebooks. Tanto JupyterLab como Notebook se incluyen en la distribución Anaconda.

