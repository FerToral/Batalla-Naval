# Consigna y alcance del TP

**UBA Exactas · Introducción a la Programación · 2C2025.** El [campus de la materia](https://campus.exactas.uba.ar/course/view.php?id=674) contiene el enunciado y los auxiliares. Puede requerir la cuenta institucional.

Se recuperó localmente **EnunciadoTN.pdf**, 23 páginas, identificado como Turno Noche. SHA-256:

```text
778940f233379178d963375261b5d2f7b24810ecaeba4dcbdcafcb9c44f618b2
```

Se conserva el PDF original en el respaldo privado del curso. No se copia al repositorio público porque no se acreditó permiso de redistribución. El enlace del campus y la huella permiten mantener el vínculo sin atribuir el material docente al autor de las soluciones.

## Mapa de lectura

| Ejercicios | Páginas del PDF recuperado | Alcance |
|---|---|---|
| 1–2 | 16–17 | Conteo y construcción del juego |
| 3 | 17–18 | Estado válido, flotas y consistencia entre grillas |
| 4 | 18–19 | Efectos del disparo y alternancia de turno |
| 5 | 19–21 | Posiciones y agrupación de barcos |
| 6 | 21–23 | Predicado de jugador perfecto y auxiliares |

## Diferencias de versión que no se deben ocultar

El PDF y las soluciones/pruebas históricas coinciden en materia, edición y ejercicios, pero se detectaron diferencias sustantivas. No basta que las pruebas pasen para decidir que son equivalentes.

1. **Balance de ataques.** El PDF agrega una condición de diferencia de cero o uno entre los disparos de los dos jugadores. Se confirmó también en las otras dos versiones recuperadas del mismo TP (21 y 25 páginas). El validador histórico aceptaba dos ataques de diferencia: se incorporó la condición común a las tres fuentes y se agregó una regresión, conservando los 28 tests históricos.
2. **Descubrir frente a hundir.** En la página 22, el auxiliar formal de barco descubierto usa existencia de una posición marcada. El código histórico exige que estén descubiertas todas las posiciones. En un barco de tamaño dos con un solo impacto, sin agua, ambas interpretaciones difieren. No se convirtió una interpretación en corrección silenciosa.
3. **Pruebas históricas.** Un caso de múltiples barcos usa assertTrue(resultado, esperado), que sólo comprueba que resultado no esté vacío. Otro método no empieza por test y no se descubre automáticamente. Las regresiones nuevas comparan el contenido normalizado y ejecutan ese caso adicional sin modificar el archivo histórico.

La diferencia restante sobre jugador perfecto impide presentar la revisión como cierre formal del TP. Sí se corrigió un defecto independiente: esEstadoDeJuegoVálido evaluaba comparaciones de tableros aun cuando sus dimensiones ya eran inválidas, produciendo IndexError en dos casos reproducibles.

## Otras versiones recuperadas

El enunciado base de 21 páginas tiene SHA-256 7f8514af346c3e0c529f72cfff3f2e5783792ec9193b244f3412392ddeaa107a. La versión de 25 páginas tiene SHA-256 23845f79555c981088a1bac9eadf1a64355d862a9b81d3125ac439bfdfef9ae5 y agrega una jugada maestra con movimiento de barcos. Esa ampliación no coincide con el ejercicio 6 propio y **no se incorpora** por compartir nombre de TP y cuatrimestre.

## Conservación y autoría

Las funciones mantienen sus nombres académicos, las soluciones históricas y auxiliares permanecen en Git. La revisión agrega pruebas y una validación por cortocircuito; no reescribe el ejercicio con herramientas ajenas a su nivel. biblioteca.py y la interfaz no se modificaron.

Los porcentajes de cobertura corresponden al archivo activo, no a la
interfaz ni a todos los auxiliares docentes. Cuatro pruebas adicionales
ejecutan el controlador sin abrir ventanas: cierre tras el impacto final,
alternancia, detección del ganador y disparos de PC sin repetición.
La GUI aún necesita una revisión visual interactiva específica.

El cierre de interfaz usa barcos hundidos; no cambia el contrato del
ejercicio 6 sobre jugador perfecto. La discrepancia descubrir/hundir
sigue explícita, sin mezclar la ampliación de otra variante del TP.
