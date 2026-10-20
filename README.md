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

La interfaz es la del ejercicio académico, no todas las reglas comerciales
de Batalla Naval. La revisión evita disparos de la PC después del impacto
ganador, bloquea jugadas tras el cierre y evita repetir ataques.
biblioteca.py permanece intacta.

## Pruebas

```sh
python -m unittest tests_materia test_regresiones test_interfaz -v
```

**51 pruebas pasan:** 28 casos de origen histórico (uno con expectativa
reconciliada y contraste de su resultado anterior), 19 regresiones del núcleo y cuatro
del controlador de interfaz. Estas últimas no abren ventanas: comprueban
disparos únicos, alternancia y cierre de partida con diálogos simulados.
Estas pruebas no sustituyen una revisión visual de Tkinter. Se mantienen las comprobaciones
de últimos ejercicios, inmutabilidad y estados mal dimensionados.

Las regresiones reprodujeron dos excepciones del validador antes de la
corrección. Ahora se valida la estructura antes de comparar posiciones.
El ejercicio 6 sigue la existencia de un impacto por barco del contrato
TN; la GUI conserva una regla separada de barcos hundidos. La expectativa
histórica revisada y su contexto se explican en docs/CONSIGNA.md; no se
presenta como si hubiera permanecido intacta.

Para medir cobertura:

```sh
python -m pip install -r requirements-dev.txt
python -m coverage run --branch --source=batallaNaval -m unittest tests_materia test_regresiones
python -m coverage report
```

Última medición tras separar descubrir/hundir: **172/172 líneas y 62/62
ramas (100 %)** en batallaNaval.py. La cobertura alta no demuestra por sí
sola aprobación docente ni revisión visual del programa.

## Estructura y versiones

- batallaNaval.py: implementación usada por la interfaz y las pruebas.
- batallaNavalCorregido.py: variante histórica, conservada como referencia; no sustituye silenciosamente al archivo activo.
- biblioteca.py e interfaz_batalla_naval.py: auxiliares del trabajo.
- tests_materia.py: casos históricos; una expectativa revisada explícitamente por el contrato TN.
- test_regresiones.py: comprobaciones adicionales de mantenimiento.
- test_interfaz.py: controlador sin ventana ni datos reales.
- docs/CONSIGNA.md: fuente académica, mapa y decisiones de compatibilidad.

Historia original en [GitLab](https://gitlab.com/dino_code/FerToral-project).
La rama de revisión en GitHub preserva sus commits. El contrato de los
seis ejercicios queda revisado respecto del PDF TN recuperado; esto no
es una aprobación docente.

La revisión nativa en Windows comprobó las dos grillas completas, sus
coordenadas, un impacto de UNO, la respuesta de la PC, ambos diálogos y
el retorno a UNO con las marcas actualizadas. El cierre ganador se prueba
automáticamente; no se afirma una partida visual completa ni auditoría de
accesibilidad. [Captura de la interfaz](docs/interfaz-windows.png).
