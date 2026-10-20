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
2. **Descubrir frente a hundir.** Se adopta el contrato formal de Turno Noche: al menos una posición no vacía de cada barco. todosLosBarcosDescubiertos conserva la firma de dos grillas del proyecto y adapta el contrato con barcoDescubiertoEn. La regla anterior queda como todosLosBarcosHundidos para la victoria de la GUI. La variante histórica completa permanece en batallaNavalCorregido.py y en el historial Git.
3. **Pruebas históricas.** Un caso de múltiples barcos usa assertTrue(resultado, esperado), que sólo comprueba que resultado no esté vacío. Otro método no empieza por test y no se descubre automáticamente. Las regresiones nuevas comparan el contenido normalizado y ejecutan ese caso adicional sin modificar el archivo histórico.

Se resuelve la diferencia sobre jugador perfecto siguiendo la especificación
recuperada, no una certificación docente. Un test histórico esperaba False
porque DOS tenía agua, aunque UNO ya había tocado ambos barcos sin agua.
Ahora espera True y verifica también el False de la variante histórica,
para hacer visible el cambio. Su fixture no cumple el balance de ataques
del contrato actual; la nueva regresión usa además un estado válido, con
un impacto por jugador sobre barcos de tamaño dos. Ambos son perfectos
según TN, pero ninguno ganó la partida. No se oculta ese caso fuera de
precondición entre los ejemplos históricos.

También se corrigió un defecto independiente: esEstadoDeJuegoVálido evaluaba
comparaciones de tableros aun cuando sus dimensiones ya eran inválidas,
produciendo IndexError en dos casos reproducibles.

## Otras versiones recuperadas

El enunciado base de 21 páginas tiene SHA-256 7f8514af346c3e0c529f72cfff3f2e5783792ec9193b244f3412392ddeaa107a. La versión de 25 páginas tiene SHA-256 23845f79555c981088a1bac9eadf1a64355d862a9b81d3125ac439bfdfef9ae5 y agrega una jugada maestra con movimiento de barcos. Esa ampliación no coincide con el ejercicio 6 propio y **no se incorpora** por compartir nombre de TP y cuatrimestre.

## Conservación y autoría

Las funciones mantienen sus nombres académicos; las soluciones históricas y
auxiliares permanecen en Git. biblioteca.py no se modifica. La interfaz usa
la regla separada de barcos hundidos y evita turnos posteriores al cierre.

Los porcentajes de cobertura corresponden al archivo activo, no a la
interfaz ni a todos los auxiliares docentes. Cuatro pruebas adicionales
ejecutan el controlador sin abrir ventanas: cierre tras el impacto final,
alternancia, detección del ganador y disparos de PC sin repetición.
Además se abrió la GUI real en Windows: grillas y coordenadas visibles
sin recortes, impacto en A1, respuesta de la PC en B3 y retorno al turno
UNO con ambas marcas. Los diálogos se comprobaron por teclado. La captura
se conserva en interfaz-windows.png; no es una partida visual completa.

El cierre de interfaz usa barcos hundidos; el ejercicio 6 usa barcos
descubiertos. La decisión y el cambio de expectativa quedan explícitos,
sin mezclar la ampliación de otra variante del TP.
