# Batalla Naval · Introducción a la Programación

Trabajo práctico de programación imperativa de **UBA Exactas, segundo cuatrimestre de 2025**. Implementación en Python, con biblioteca e interfaz Tkinter provistas para el ejercicio y soluciones históricas conservadas.

## Recorrido del TP

| Ejercicio | Tema | Archivo activo |
|---|---|---|
| 1 | Cantidad de barcos según tamaño | batallaNaval.py |
| 2 | Construcción de un juego y sus grillas | batallaNaval.py |
| 3 | Validez y consistencia de un estado | batallaNaval.py |
| 4 | Disparo y cambio de turno | batallaNaval.py |
| 5 | Reconocimiento de barcos en una grilla | batallaNaval.py |
| 6 | Jugador perfecto | batallaNaval.py |

La [consigna y sus diferencias de versión](docs/CONSIGNA.md) contextualizan los ejercicios. No se incluyen copias docentes sin permiso de redistribución.

## Ejecutar

Python 3.10 o posterior; comprobado con Python 3.12. La interfaz requiere Tkinter:

```sh
python interfaz_batalla_naval.py
```

La interfaz es la del ejercicio académico, no una implementación completa de todas las reglas comerciales de Batalla Naval. No se modificaron biblioteca.py ni la interfaz en esta revisión.

## Pruebas

```sh
python -m unittest tests_materia test_regresiones -v
```

**45 pruebas pasan:** 28 históricas y 17 regresiones nuevas. Se comprueban los últimos ejercicios, inmutabilidad, independencia de grillas, posiciones límite, resultado exacto de múltiples barcos y validación de estados mal dimensionados.

Las nuevas regresiones reprodujeron dos excepciones del validador antes de la corrección. Ahora se valida la estructura antes de comparar posiciones entre tableros. No se alteraron las expectativas del archivo histórico para hacer pasar el código.

Para medir cobertura:

```sh
python -m pip install -r requirements-dev.txt
python -m coverage run --branch --source=batallaNaval -m unittest tests_materia test_regresiones
python -m coverage report
```

Última medición: **162/162 líneas ejecutables (100 %) y 54/54 ramas (100 %)** en batallaNaval.py. La cobertura alta no demuestra por sí sola concordancia completa con la especificación.

## Estructura y versiones

- batallaNaval.py: implementación usada por la interfaz y las pruebas.
- batallaNavalCorregido.py: variante histórica, conservada como referencia; no sustituye silenciosamente al archivo activo.
- biblioteca.py e interfaz_batalla_naval.py: auxiliares del trabajo.
- tests_materia.py: pruebas históricas conservadas.
- test_regresiones.py: comprobaciones adicionales de mantenimiento.
- docs/CONSIGNA.md: fuente académica, mapa y discrepancias pendientes.

Historia original en [GitLab](https://gitlab.com/dino_code/FerToral-project). La rama de revisión en GitHub preserva sus commits. No se considera aprobación docente ni cierre completo mientras la diferencia de contrato del último ejercicio no estén reconciliadas.
