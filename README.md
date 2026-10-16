# 🚢 Batalla Naval — Trabajo Práctico de Programación Imperativa

## 🧩 Introducción

El objetivo de este **Trabajo Práctico** es aplicar los conceptos de **programación imperativa** vistos en la materia para resolver ejercicios utilizando el lenguaje de programación **Python**.

El trabajo consiste en implementar el clásico juego **Batalla Naval**.  
Para quienes no lo conozcan, es un juego de mesa para dos jugadores, donde cada uno posee una flota de barcos ubicada en un tablero propio.  
El objetivo es **hundir todos los barcos del oponente** antes de que este haga lo mismo.  

En cada turno, un jugador lanza un torpedo a una posición del tablero enemigo, y el oponente debe responder si el disparo **impactó** en alguno de sus barcos o **falló**.

---

## ⚙️ Tecnologí utilizadas

- **Lenguaje:** Python 🐍  
- **Paradigma:** Programación imperativa  
- **Entorno recomendado:** Visual Studio Code / Terminal con Python 3.10+  
- **Control de versiones:** Git y GitLab  

## Estado de la reconstrucción

Esta copia conserva la historia existente del repositorio y publica la versión validada en la rama `version-validada-batalla-naval`. La corrección declara el `TypeVar` utilizado por `batallaNavalCorregido.py`, que impedía importar esa variante histórica.

Validación realizada con Python 3.12 del entorno de trabajo:

- 28/28 tests de `tests_materia.py` pasan.
- `batallaNavalCorregido` importa correctamente.
- La verificación de sintaxis y `git diff --check` pasan.

La rama documenta la versión validada y se mantiene separada de `main` hasta completar su revisión.

---

## 🚀 Ejecución del proyecto

1. Clonar este repositorio:

   ```bash
   git clone https://gitlab.com/dino_code/FerToral-project.git
   cd FerToral-project
