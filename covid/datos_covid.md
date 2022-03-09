
# Datos covid

El [Instituto de salud Carlos III](https://www.isciii.es/) recoge los [datos](https://cnecovid.isciii.es/covid19/) sobre la COVID-19 en España.
Concretamente, hacen públicas unas [tablas de datos](https://cnecovid.isciii.es/covid19/#documentaci%C3%B3n-y-datos) en ficheros [csv](https://es.wikipedia.org/wiki/Valores_separados_por_comas).

Este curso lo vamos a organizar alrededor del análisis de la tabla [casos_hosp_uci_def_sexo_edad_provres.csv](https://cnecovid.isciii.es/covid19/resources/casos_hosp_uci_def_sexo_edad_provres.csv) que incluye:

  - Número de hospitalizaciones,
  - número de ingresos en UCI
  - número de defunciones y
  - número de casos detectados
  
Todos estos datos están divididos en la tabla por sexo, edad, provincia de residencia y día.

| provincia_iso | sexo | grupo_edad | fecha | num_casos | num_hosp | num_uci | num_def |
| --- | --- | --- | --- | --- | --- | --- | --- |
| M | H | 0-9 | 2020-03-23 | 6 | 3 | 1 | 0 |
| M | H | 10-19 | 2020-03-23 | 5 | 1 | 1 | 0 |
| M | H | 20-29 | 2020-03-23 | 58 | 18 | 0 | 0 |
| M | H | 30-39 | 2020-03-23 | 136 | 58 | 3 | 0 |
| M | H | 40-49 | 2020-03-23 | 218 | 128 | 14 | 1 |
| M | H | 50-59 | 2020-03-23 | 292 | 248 | 20 | 4 |
| M | H | 60-69 | 2020-03-23 | 243 | 248 | 30 | 21 |
| M | H | 70-79 | 2020-03-23 | 277 | 269 | 25 | 74 |
| M | H | 80+ | 2020-03-23 | 183 | 175 | 2 | 77 |
| M | H | NC | 2020-03-23 | 0 | 0 | 0 | 0 |
| M | M | 0-9 | 2020-03-23 | 4 | 2 | 0 | 0 |
| M | M | 10-19 | 2020-03-23 | 1 | 1 | 1 | 0 |
| M | M | 20-29 | 2020-03-23 | 113 | 18 | 0 | 0 |
| M | M | 30-39 | 2020-03-23 | 204 | 51 | 4 | 0 |

El análisis lo haremos utilizando [Jupyter Notebooks](https://docs.jupyter.org/) y, también, creando un programa tradicional de Python.
