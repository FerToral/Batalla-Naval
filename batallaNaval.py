from typing import Any
from biblioteca import *

## Ejercicio 1


def cantidadDeBarcosDeTamaño(barcos: list[BarcoEnGrilla], tamaño: int) -> int:
    """
        Devuelve la cantidad de barcos de un tamaño dado dentro de la lista de barcos en una grilla.

        Pre: La lista barcos contiene solamente barcos validos

        Argumentos: barcos: Lista de Barcos que estan en la grilla (son representados a través de las posiciones que tienen en la grilla)
              tamaño: tamaño/posiciones que tiene un barco en la grilla
        Post: Regresa la cantidad de barcos que tienen el tamaño especificado en el paramatro de la función


    """

    cantidadBarcos: int = 0
    for barcoActual in barcos:
        cantidadBarcos += unoSiCeroSiNo(tamañoBarco(barcoActual) == tamaño)

    return cantidadBarcos

## Ejercicio 2

def grillaVacia(filas: int, columnas: int) -> Grilla:
    """
    Devuelve una grilla vacía de las dimensiones dadas,
    cada posición de la misma se inicializa con VACÍO.
    """
    return [[VACÍO for _ in range(columnas)] for _ in range(filas)]

def armadoDeTablero( filas: int, columnas: int) -> Tablero:
    """
    Devuelve un tablero inicial compuesto por dos grillas vacías, una para el jugador local y otra para el oponente
    """

    return (grillaVacia(filas, columnas), grillaVacia(filas, columnas))

def nuevoJuego(
        cantidadDeFilas: int,
        cantidadDeColumnas: int,
        barcosDisponibles: list[Barco]
    ) -> EstadoJuego:
    """
    Crea un nuevo estado de juego listo para comenzar.

    Pre:
        - cantidadDeFilas > 0 y cantidadDeColumnas > 0.
        - Los tamaños de los barcos en `barcosDisponibles` no exceden las dimensiones del tablero.

    Post:
        - Devuelve un EstadoJuego donde ambos tableros están vacíos.
        - La lista de barcos en juego es una copia de `barcosDisponibles`.


    """

    nuevo_juego: EstadoJuego = (
        (cantidadDeFilas, cantidadDeColumnas),
        barcosDisponibles.copy(),
        jugadorQueEmpieza(),
        armadoDeTablero(cantidadDeFilas, cantidadDeColumnas),
        armadoDeTablero(cantidadDeFilas, cantidadDeColumnas)
    )

    return nuevo_juego


## Ejercicio 3
def esEstadoDeJuegoVálido(estadoDeJuego: EstadoJuego) -> bool:
    """
    indica si el estado de juego propuesto es valido o si hay algun error que no permite un desarrollo del juego en condiciones
    requiere: {true}
    asegura: resutado = 1 ≤ cantidad de filas del estado de juego ≤ 26 ∧
             cantidad de columnas del estado de juego > 0 ∧
             tamaño de estado de juego[2] = 1 ∧
             tamaño de estado de juego[1] > 0 ∧
             tablero del jugador UNO Válido ∧
             tablero del jugador DOS Válido ∧
             coinciden las posiciones atacadas en el tablero del jugador UNO y el tablero del jugador DOS
    return: True si el estado es valido o False si el estado es invalido
    """
    cantidad_de_filas_del_estado_de_juego_validas = cantidadDeFilasEstadoJuego(estadoDeJuego) >= 1 and cantidadDeFilasEstadoJuego(estadoDeJuego) <= 26
    cantidad_de_columnas_del_estado_de_juego_validas = cantidadDeColumnasEstadoJuego(estadoDeJuego) > 0
    solo_hay_una_lista_en_turno = len(estadoDeJuego[2]) == 1
    hay_al_menos_un_barco_disponible = len(barcosDisponibles(estadoDeJuego)) > 0
    return (cantidad_de_filas_del_estado_de_juego_validas
            and cantidad_de_columnas_del_estado_de_juego_validas
            and solo_hay_una_lista_en_turno
            and hay_al_menos_un_barco_disponible
            and tableroVálidoEnJuego(tableroDeJugador(estadoDeJuego,UNO),estadoDeJuego)
            and tableroVálidoEnJuego(tableroDeJugador(estadoDeJuego,DOS),estadoDeJuego)
            and coincidenPosicionesAtacadas(tableroDeJugador(estadoDeJuego,UNO),tableroDeJugador(estadoDeJuego,DOS)))

def tableroVálidoEnJuego(tablero:Tablero,estadoDeJuego:EstadoJuego) -> bool:
    return grillaVálidaEnJuego(grillaLocal(tablero),estadoDeJuego) and grillaVálidaEnJuego(grillaOponente(tablero),estadoDeJuego) and coincidenBarcosEnGrilla(barcosDisponibles(estadoDeJuego),grillaLocal(tablero))

def coincidenBarcosEnGrilla(barcos:list[Barco],grilla:Grilla) -> bool:
    return mismosElementos(barcos,tamaños(barcosEnGrilla(grilla)))

def tamaños(barcos:list[BarcoEnGrilla]) -> list[int]:
            tamañosPorAhora = []
            for i in range (len(barcos)):
              tamañosPorAhora = tamañosPorAhora + [tamañoBarco(barcos[i])]
            return tamañosPorAhora
def mismosElementos(lista1: list[str],lista2: list[str]) -> bool:
    return losElementosDeLaPrimeraAparecenEnLaSegunda(lista1,lista2) and losElementosDeLaSegundaAparecenEnLaPrimera(lista1,lista2)

def losElementosDeLaPrimeraAparecenEnLaSegunda(lista1:list[str],lista2:list[str]) -> list[bool]:
    res = True
    for elemento in lista1:
        res = res and cantidadDeApariciones(elemento,lista1) == cantidadDeApariciones(elemento,lista2)
    return res
def losElementosDeLaSegundaAparecenEnLaPrimera(lista1:list[str],lista2:list[str]) -> list[bool]:
    res = True
    for elemento in lista2:
        res = res and cantidadDeApariciones(elemento,lista1) == cantidadDeApariciones(elemento,lista2)
    return res

def coincidenPosicionesAtacadas(tablero:Tablero,tableroOponente:Tablero) -> bool:
    res = True
    for fila in range (len(tablero[1])):
        res = res and coincidenPosicionesAtacadasEnCadaFila(tablero,tableroOponente,fila)
    for fila in range (len(tableroOponente[1])):
        res = res and coincidenPosicionesAtacadasEnCadaFila(tableroOponente,tablero,fila)
    diferencia_de_ataques: int = cantidadDePosicionesAtacadas(grillaOponente(tablero)) - cantidadDePosicionesAtacadas(grillaOponente(tableroOponente))
    return res and 0 <= diferencia_de_ataques <= 1


def cantidadDePosicionesAtacadas(grilla: Grilla) -> int:
    """Cuenta las celdas marcadas por disparos en una grilla válida."""
    cantidad: int = 0
    for fila in grilla:
        for celda in fila:
            cantidad += unoSiCeroSiNo(celda != VACÍO)
    return cantidad

def coincidenPosicionesAtacadasEnCadaFila(tablero:Tablero,tableroOponente:Tablero,fila) -> bool:
    res = True
    for posicion in range (len(tablero[1][fila])):
            if tablero[1][fila][posicion] != VACÍO:
              res = res and posicionEnTableroOponenteEsPosicionEnTablero(tablero,tableroOponente,fila,posicion)
            else:
              res = res and posicionEnTableroOponenteEsVacioOBarco(tableroOponente,fila,posicion)
              if tableroOponente[0][fila][posicion] == VACÍO or tableroOponente[0][fila][posicion] == BARCO:
                res = res and True
              else:
                res = res and False
    return res

def posicionEnTableroOponenteEsPosicionEnTablero(tablero:Tablero,tableroOponente:Tablero,fila,posicion) -> bool:
    res = True
    if tableroOponente[0][fila][posicion] == tablero[1][fila][posicion]:
        res = res and True
    else:
        res = res and False
    return res

def posicionEnTableroOponenteEsVacioOBarco(tableroOponente:Tablero,fila,posicion) -> bool:
    res = True
    if tableroOponente[0][fila][posicion] == VACÍO or tableroOponente[0][fila][posicion] == BARCO:
        res = res and True
    else:
        res = res and False
    return res

## Ejercicio 4

def dispararEnPosición(estado_juego: EstadoJuego, posición: Posición) -> ResultadoDisparo:
    """
    Indica si el disparo fue a un barco o fue al agua
    Requiere:el estado de juego es valido
    Requiere:la posicion de ataque esta dentro de la grilla
    Requiere:no se ataco previamente a esa posicion
    Asegura:modifica el estado de juego segun el disparo
    Asegura:solo modifica la celda disparada
    Asegura:si se dispara a un barco la celda con esa posicion en la grilla del oponente se reemplaza por Barco
    Asegura:si se dispara al agua la celda con esa posicion en la grilla del oponente se reemplaza por agua
    Asegura:si se dispara al agua la celda con esa posicion en la grilla local del contrincante se reemplaza por agua
    return: devuelve TOCADO si se dispara a un BARCO o devuelve NADA si se dispara a un VACÍO
    """
    if celdaEnPosición(grillaLocal((tableroDeJugador(estado_juego, contrario(turno(estado_juego))))), posición) == VACÍO:
        nuevoEstadoDeJuegoSiDisparoHaceAgua(estado_juego,posición)
        res = NADA
    else:
        nuevoEstadoDeJuegoSiDisparoAlBarco(estado_juego,posición)
        res = TOCADO
    return res

def nuevoEstadoDeJuegoSiDisparoHaceAgua(estado_juego:EstadoJuego,posición: Posición) -> ResultadoDisparo:
    cambiarCeldaGrilla(grillaLocal(tableroDeJugador(estado_juego, contrario(turno(estado_juego)))), posición, AGUA)
    cambiarCeldaGrilla(grillaOponente(tableroDeJugador(estado_juego, turno(estado_juego))), posición, AGUA)
    cambiarTurno(estado_juego)
    return estado_juego

def nuevoEstadoDeJuegoSiDisparoAlBarco(estado_juego:EstadoJuego,posición: Posición) -> ResultadoDisparo:
    cambiarCeldaGrilla(grillaOponente(tableroDeJugador(estado_juego, turno(estado_juego))), posición, BARCO)
    cambiarTurno(estado_juego)
    return estado_juego

def contrario (jugador:Jugador) -> Jugador:
    jugadorContrario = DOS if jugador == UNO else UNO
    return jugadorContrario
## Ejercicio 5

def indiceAPosicion(fila: int, columna: int) -> Posición:
    """
    Devuelve la posición correspondiente a los índices dados.
    """
    return (chr(fila + ord('A')), columna+1)

def agregarBarcoEn(grilla: Grilla, desde: Posición, direccion: Dirección,
                     barco_actual: list[Posición]) -> None:

    posicion_actual: Posición = desde

    while hayBarcoAl(grilla, posicion_actual, direccion):
        posicion_actual = posiciónAdyacenteAl(grilla, posicion_actual, direccion)
        barco_actual.append(posicion_actual)


def  barcoDesdePosicion(grilla: Grilla, inicio: Posición) -> list[Posición]:

    barco_actual: list[Posición] = []
    barco_actual.append(inicio)

    if hayBarcoAl(grilla, inicio, DERECHA):
        agregarBarcoEn(grilla, inicio, DERECHA, barco_actual)
    elif hayBarcoAl(grilla, inicio, ARRIBA):
        agregarBarcoEn(grilla, inicio, ARRIBA, barco_actual)


    return barco_actual

def esUnBarcoNoVisitado(grilla, posicionActual, visitadas) -> bool:
    return celdaEnPosición(grilla, posicionActual) == BARCO and posicionActual not in visitadas


def barcosEnGrilla(grilla: Grilla) -> list[BarcoEnGrilla]:
    """
    Identifica y devuelve una lista de barcos presentes en la grilla

    Recorre la grilla celda por celdad y agrupa las celdas marcadas como BARCO en barcos.

    Cada barco es a su vez una lista de posiciones contiguas, que pueden ser horizontal o vertical.
    Se asume que no haya formaciones como cruces, apiladas, etc.

    Pre:
        - *grilla* es una Grilla válida y todas sus filas tienen la misma longitud.
        - Las celdas pertenecen al conjunto {VACIO, BARCO, AGUA}
        - Se asume que los barcos son rectos
    Post:
        - Devuelve una lista de BarcoEnGrilla, donde cada BarcoEnGrilla es una lista de Posición
          que representa las celdas que ocupa un barco en la *grilla*.

        - La unión de todas las posiciones devueltas es exactamente el conjunto de posiciones de
          la grilla cuya celda es BARCO
        - No hay solapamiento (ninguna posición aparece en más de un barco)
        - Cada barco contiene posiciones contiguas y ordenadas en la dirección del barco (direcciones rectas arriba, abajo, derecha e izquierda)

    """

    visitadas: list[Posición] = []
    barcos_por_ahora: list[BarcoEnGrilla] = []


    posicion_actual: Posición = primeraPosiciónEnGrilla(grilla)
    quedan_posiciones_por_recorrer: bool =  True

    while quedan_posiciones_por_recorrer:
        if esUnBarcoNoVisitado(grilla, posicion_actual, visitadas):
            barco_en_grilla: list[Posición] = barcoDesdePosicion(grilla, posicion_actual)
            barcos_por_ahora.append(barco_en_grilla)
            visitadas+=barco_en_grilla

        if esLaÚltimaPosiciónEnGrilla(posicion_actual, grilla):
            quedan_posiciones_por_recorrer = False
        else:
            posicion_actual = posiciónSiguienteEnGrilla(posicion_actual, grilla)


    return barcos_por_ahora

    #Ejercicio 6
def agregarPosiciones(listaPosiciones: list[Posición], barco_en_grilla: BarcoEnGrilla):
    """
    Agrega las posiciones de un barco a una lista dada.
    """
    for posicion_actual in barco_en_grilla:
        listaPosiciones.append(posicion_actual)

def posicionesDeBarcos(barcos: list[BarcoEnGrilla]) -> list[Posición]:
    """
    Devuelve una lista con todas las posiciones ocupadas por barcos.
    """
    posiciones_con_barco_por_ahora: list[Posición] = []

    for barco_actual in barcos:
        agregarPosiciones(posiciones_con_barco_por_ahora, barco_actual)

    return posiciones_con_barco_por_ahora


def todosLosBarcosDescubiertos(grillaJugadorOponente: Grilla, grillaOponenteLocal: Grilla) -> bool:
    """
    Indica si todos los barcos de una grilla fueron descubiertos en otra.
    """

    todos_descubiertos_por_ahora = True
    barcos_acertados: list[BarcoEnGrilla] = barcosEnGrilla(grillaJugadorOponente)
    barcos_totales: list[BarcoEnGrilla] = barcosEnGrilla(grillaOponenteLocal)

    posiciones_de_barcos_acertados: list[Posición] = posicionesDeBarcos(barcos_acertados)
    posiciones_de_barcos_totales: list[Posición] = posicionesDeBarcos(barcos_totales)


    for posicion_actual in posiciones_de_barcos_totales:
        if posicion_actual not in posiciones_de_barcos_acertados:
            todos_descubiertos_por_ahora = False

    return todos_descubiertos_por_ahora


def hayAgua(grillaLocalOponente: Grilla) -> bool:
    """
    Realiza un recorrido por la grilla del oponente para verificar si alguno de los tiros haya dado en AGUA.
    """
    hay_agua_por_ahora: bool = False
    posicion_actual: Posición = primeraPosiciónEnGrilla(grillaLocalOponente)
    quedan_posiciones_por_recorrer: bool = True

    while quedan_posiciones_por_recorrer and not hay_agua_por_ahora:
        if celdaEnPosición(grillaLocalOponente, posicion_actual) == AGUA:
            hay_agua_por_ahora = True

        if esLaÚltimaPosiciónEnGrilla(posicion_actual, grillaLocalOponente):
            quedan_posiciones_por_recorrer = False
        else:
            posicion_actual = posiciónSiguienteEnGrilla(posicion_actual, grillaLocalOponente)

    return hay_agua_por_ahora

def jugadorOponente(jugador: Jugador) -> Jugador:
    """Devuelve el jugador oponente al jugador dado."""
    return UNO if jugador == DOS else DOS

def esJugadorPerfecto(estadoDeJuego: EstadoJuego, jugador: Jugador) -> bool:

    """"
    Indica si un jugador realizó una partida perfecta.
    Un jugador es perfecto si:
        - Descubrió todos los barcos del oponente.
        - No hizo ningún disparo que haya dado en AGUA.
    """

    return todosLosBarcosDescubiertos(
        grillaOponente(tableroDeJugador(estadoDeJuego,jugador)),
        grillaLocal(tableroDeJugador(estadoDeJuego,jugadorOponente(jugador)))
    ) and not hayAgua(grillaOponente(tableroDeJugador(estadoDeJuego,jugador)))


def hayJugadorPerfecto(estadoDeJuego: EstadoJuego) -> bool:
    """
    Indica si algún jugador realizó una partida perfecta.

    Pre:
        - estadoDeJuego es válido.
    Post:
        - Devuelve True si el jugador UNO o el jugador DOS realizaron una partida perfecta.
        - Devuelve False si ninguno lo logró.
    """

    return esJugadorPerfecto(estadoDeJuego,UNO) or esJugadorPerfecto(estadoDeJuego, DOS)

