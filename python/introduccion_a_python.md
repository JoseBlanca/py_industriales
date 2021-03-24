# Introducción a Python

## ¿Por qué Python?

### Sencillo

[Python](https://es.wikipedia.org/wiki/Python) es un lenguaje de programación potente, pero diseñado para ser sencillo.

Java es un lenguaje alternativo a Python, que es incluso más utilizado en muchos ámbitos, pero resulta mucho más complejo de aprender, especialmente para un 
estudiante sin experiencia en programación orientada a objetos.

### Hola mundo

Podemos comenzar a familiarizarnos con Python imprimiendo "Hola mundo".

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

Alternativamente, en java para imprimir "Hola mundo" deberíamos escribir:

```
    class HolaMundo
    {
        public static void main(String[] args)
        {
            System.out.println("Hola Mundo");
        }
    }
```

### Propósito general

A pesar de su sencillez Python es un lenguaje multipropósito que puede ser utilizado para resolver una gran diversidad de taréas informáticas.
Python es utilizado ampliamente en la industria, por ejemplo en aplicaciones tan comunes como Dropbox o Youtube.

La otra gran alternativa para hacer análisis de datos es [R](https://www.r-project.org/).
R es un paquete estadístico que no puede ser utilizado como lenguaje de propósito general.

### Multiparadigma

Python es un lenguaje [multiparadigma](https://es.wikipedia.org/wiki/Lenguaje_de_programaci%C3%B3n_multiparadigma), está diseñado para permitir la programación [orientada a objetos](https://es.wikipedia.org/wiki/Programaci%C3%B3n_orientada_a_objetos), programación [estructurada](https://es.wikipedia.org/wiki/Programaci%C3%B3n_estructurada) y programación [funcional](https://es.wikipedia.org/wiki/Programaci%C3%B3n_funcional).

### Libre

Python se distribuye bajo una licencia libre por lo que podemos descargarlo y utilizarlo sin prácticamente ninguna restricción.

### Pilas incluidas

Python tiene un gran ecosistema de desarrolladores y librerías.

### Dinámico

No hace falta definir el tipo de las variables antes de utilizarlas. Aunque ahora, opcionalmente, sí pueden definirse los [tipos](https://docs.python.org/3/library/typing.html).

### Interpretado

El intérprete compila el código de forma transparente sin que tengamos que preocuparnos por hacerlo nosotros.

### Manejo de la memoria automático

No es necesario que reservemos memoria antes de utilizarla o que la liberemos al final, Python lo hace por nosotros.

### Gran adopción en análisis de datos

Python era, y sigue siendo, muy popular en desarrollo web y entre los administradores de sistemas y actualmente uno de los lenguajes con un mayor [crecimiento](https://stackoverflow.blog/2017/09/06/incredible-growth-python/).
Además, Python se está convirtiendo en el estándar en ciencia de datos.

Python es además un lenguaje ampliamente utilizado en genral, puedes consultar los resultados de la última [encuesta](https://insights.stackoverflow.com/survey/2020) a los usuarios de Stackoverflow.

### Limitaciones

Al ser dinámico, interpretado y de manejo de memoria automático los programas escritos en Python puro no son tan eficientes como los que podamos llegar a escribir en un lenguaje de bajo nivel como C.
Aunque esto no suele ser una limitación relevante ya que es muy fácil escribir en C o en Cython las partes limitantes de la computación e integrarlas en Python.
De hecho, así es como funcionan muchas de las librerías que utiliza Python que están realmente escritas en C. Aunque es cierto que esta aproximación nos obliga a utilizar otras tecnologías que carecen de la sencillez de Python.

La computación multihilo no es el fuerte de Python debido al [Gobal Interpreter Lock](https://wiki.python.org/moin/GlobalInterpreterLock).
A pesar de esto, Python se utiliza para procesar datos en paralelo porque esta limitación suele ser superada por las librerías de análisis de datos.

Por el momento no es el lenguaje ideal para escribir aplicaciones con una rica interfaz de usuario ya que no suele utilizarse para esta tarea.

No se puede ejecutar directamente en un navegador web, para este propósito Javascript es la mejor alternativa.

## Python actual y antiguo

Las versiones de la serie 2 de Python están obsoletas a pesar de que todavía hay mucha documentación en la web dedicadas a ellas.

Las versiones de Python actuales son las de la serie 3.

## Instalando Python

Python está preinstalado en los sistemas Linux y MacOS y podríamos utilizarlo directamente, pero para homogeneizar el entorno de todos los estudiantes en este curso asumiremos que hemos instalado la distribución [Anaconda](https://www.anaconda.com/distribution/) para Python3.

Esta distribución está orientada al análisis de datos e incluye, además del intérprete, numerosas librerías, así como otras utilidades para facilitar la edición de código en Python y su ejecución interactiva.

En Real Python tienen un muy buen tutorial de [instalación](https://realpython.com/installing-python/) de Python en distintas plataformas.