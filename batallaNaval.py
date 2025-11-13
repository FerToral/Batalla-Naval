from typing import Any
from biblioteca import *

## Ejercicio 1


def cantidadDeBarcosDeTamaño(barcos: list[BarcoEnGrilla], tamaño: int) -> int:
    """ 
        Indica si la cantidad de barcos de tamaño *tamaño*

        Pre: La lista barcos contiene solamente barcos validos

        Args: barcos: Lista de Barcos que estan en la grilla (son representados a través de las posiciones que tienen en la grilla)
              tamaño: tamaño/posiciones que tiene un barco en la grilla   
        Return la cantidad de barcos que sean de tamaño *tamaño*


    """

    contador: int = 0
    for barcoEnGrilla in barcos:
        if tamañoBarco(barcoEnGrilla) == tamaño:
            contador+=1

    return contador

## Ejercicio 2

def armadoDeTablero( filas: int, columnas: int) -> Tablero:
    grilla_local = [[VACÍO for _ in range(columnas)] for _ in range(filas)]
    grilla_oponente = [[VACÍO for _ in range(columnas)] for _ in range(filas)]
    
    return (grilla_local, grilla_oponente)

def nuevoJuego(
        cantidadDeFilas: int,
        cantidadDeColumnas: int,
        barcosDisponibles: list[Barco]
    ) -> EstadoJuego:
    """ Agregar docstring acá
    Además de los requiere del tp, asumo que lo siguiente:
            - El tamaño de los barcos no excede de las dimensiones
            - La cantidad de barcos que se puede agregar depende del tamaño y de que no queden juntos (aunque esto puede parecer mas un asegura)

    """
   

    barcos_en_juego: list[Barco] = barcosDisponibles.copy()
    dimension_grilla: Dimensiones = (cantidadDeFilas, cantidadDeColumnas)
    nuevo_tablero_j1: Tablero = armadoDeTablero(cantidadDeFilas, cantidadDeColumnas)
    nuevo_tablero_j2: Tablero = armadoDeTablero(cantidadDeFilas, cantidadDeColumnas)
    jugadores = jugadorQueEmpieza()


    nuevo_juego: EstadoJuego = (
        dimension_grilla, 
        barcos_en_juego, 
        jugadores, 
        nuevo_tablero_j1, 
        nuevo_tablero_j2 
    )

    return nuevo_juego


## Ejercicio 3
def esEstadoDeJuegoVálido(estadoDeJuego: EstadoJuego) -> bool:
    """ Agregar docstring acá
    indica si el estado de juego propuesto es valido o si hay algun error que no permite un desarrollo del juego en condiciones
    pre: {true}
    arg: el resultado es True si todas las funciones (a,b,c,d,e,f,g,h) tienen como resultado True
    arg: el resultado es False si al menos una de las funciones (a,b,c,d,e,f,g,h) tiene como resultado False
    return: True si el estado es valido o False si el estado es invalido
    """
    a = cantidadDeFilasEstadoJuego(estadoDeJuego) >= 1
    b = cantidadDeFilasEstadoJuego(estadoDeJuego) <= 26
    c = cantidadDeColumnasEstadoJuego(estadoDeJuego) > 0
    d = len(estadoDeJuego[2]) == 1
    e = len(barcosDisponibles(estadoDeJuego)) > 0
    f = tableroVálidoEnJuego(tableroDeJugador(estadoDeJuego,UNO),estadoDeJuego)
    g = tableroVálidoEnJuego(tableroDeJugador(estadoDeJuego,DOS),estadoDeJuego)
    h = coincidenPosicionesAtacadas(tableroDeJugador(estadoDeJuego,UNO),tableroDeJugador(estadoDeJuego,DOS))

    return a and b and c and d and e and f and g and h

def tableroVálidoEnJuego(tablero:Tablero,estadoDeJuego:EstadoJuego) -> bool:
    return grillaVálidaEnJuego(grillaLocal(tablero),estadoDeJuego) and grillaVálidaEnJuego(grillaOponente(tablero),estadoDeJuego) and coincidenBarcosEnGrilla(barcosDisponibles(estadoDeJuego),grillaLocal(tablero))

def coincidenBarcosEnGrilla(barcos:list[Barco],grilla:Grilla) -> bool:
    return mismosElementos(barcos,tamaños(barcosEnGrilla(grilla)))


def tamaños(barcos:list[BarcoEnGrilla]) -> list[int]:
            res = []
            for i in range (2,6):
                cant = cantidadDeBarcosDeTamaño(barcos,i)
                while cant > 0:
                    res = res + [i]
                    cant = cant - 1
            return res
def mismosElementos(lista1: list[str],lista2: list[str]) -> bool:
    res = True
    for i in range (len(losElementosDeLaPrimeraAparecenEnLaSegunda(lista1,lista2))):
        res = res and losElementosDeLaPrimeraAparecenEnLaSegunda(lista1,lista2)[i]
    return res

def losElementosDeLaPrimeraAparecenEnLaSegunda(lista1:list[str],lista2:list[str]) -> list[bool]:
    res = [cantidadDeApariciones(elemento,lista1) == cantidadDeApariciones(elemento,lista2) for elemento in lista1 for elemento in lista2]
    return res

def coincidenPosicionesAtacadas(tablero:Tablero,tableroOponente:Tablero) -> bool:
    res = True
    for fila in range (len(tablero[1])):
        for posicion in range (len(tablero[1][fila])):
            if tablero[1][fila][posicion] != VACÍO:
              if tableroOponente[0][fila][posicion] == tablero[1][fila][posicion]:
                res = res and True
              else:
                res = res and False
            else:
              if tableroOponente[0][fila][posicion] == VACÍO or tableroOponente[0][fila][posicion] == BARCO:
                res = res and True
              else:
                res = res and False
    for fila in range (len(tableroOponente[1])):
        for posicion in range (len(tableroOponente[1][fila])):
            if tableroOponente[1][fila][posicion] != VACÍO:
              if tablero[0][fila][posicion] == tableroOponente[1][fila][posicion]:
                res = res and True
              else:
                res = res and False
            else:
              if tablero[0][fila][posicion] == VACÍO or tablero[0][fila][posicion] == BARCO:
                res = res and True
              else:
                res = res and False
    return res

estadoDeJuego = (((2,2),[2],[UNO],
([[BARCO, VACÍO], [BARCO, VACÍO]],
[[VACÍO,VACÍO], [VACÍO, VACÍO]]),   
([[BARCO, BARCO], [VACÍO, VACÍO]],
[[VACÍO, VACÍO], [VACÍO, VACÍO]])))

## Ejercicio 4

def dispararEnPosición(estado_juego: EstadoJuego, posición: Posición) -> ResultadoDisparo:
    """ Agregar docstring acá
    Indica si el disparo fue a un barco o fue al agua
    pre:el estado de juego es valido
    pre:la posicion de ataque esta dentro de la grilla
    pre:no se ataco previamente a esa posicion
    arg:modifica el estado de juego segun el disparo
    arg:solo modifica la celda disparada
    arg:si se dispara a un barco la celda con esa posicion en la grilla del oponente se reemplaza por Barco
    arg:si se dispara al agua la celda con esa posicion en la grilla del oponente se reemplaza por agua
    arg:si se dispara al agua la celda con esa posicion en la grilla local del contrincante se reemplaza por agua
    return: devuelve TOCADO si se dispara a un BARCO o devuelve NADA si se dispara a un VACÍO
    """
    if turno(estado_juego) == UNO:
        t2 = DOS
    if turno(estado_juego) == DOS:
        t2 = UNO
    if celdaEnPosición(grillaLocal((tableroDeJugador(estado_juego, t2))), posición) == VACÍO:
        disparoHaceAgua(estado_juego,posición)
        res = NADA
    if celdaEnPosición(grillaLocal((tableroDeJugador(estado_juego, t2))), posición) == BARCO:
        disparoAlBarco(estado_juego,posición)
        res = TOCADO
    return res # TODO: Implementame

def disparoHaceAgua(estado_juego:EstadoJuego,posición: Posición) -> ResultadoDisparo:
    if turno(estado_juego) == UNO:
        t2 = DOS
    if turno(estado_juego) == DOS:
        t2 = UNO
    cambiarCeldaGrilla(grillaLocal(tableroDeJugador(estado_juego, t2)), posición, AGUA)
    cambiarCeldaGrilla(grillaOponente(tableroDeJugador(estado_juego, turno(estado_juego))), posición, AGUA)
    cambiarTurno(estado_juego)
    return estado_juego
    
def disparoAlBarco(estado_juego:EstadoJuego,posición: Posición) -> ResultadoDisparo:
    if turno(estado_juego) == UNO:
        t2 = DOS
    if turno(estado_juego) == DOS:
        t2 = UNO
    cambiarCeldaGrilla(grillaOponente(tableroDeJugador(estado_juego, turno(estado_juego))), posición, BARCO)
    cambiarTurno(estado_juego)
    return estado_juego

## Ejercicio 5

def indiceAPosicion(fila: int, columna: int) -> Posición:
    letra = chr(fila + ord('A'))
    return (letra, columna+1)

def  construirBarcoDesdePosicion(grilla: Grilla, inicio: Posición, visitadas:list[Posición]) -> list[Posición]:
    
    
    barco: list[Posición] = []
    barco.append(inicio)
    visitadas.append(inicio)
    direccion_de_construccion: Dirección = DERECHA if hayBarcoAl(grilla, inicio, DERECHA) else ARRIBA

    posicion_siguiente: Posición = inicio

    while hayBarcoAl(grilla, posicion_siguiente, direccion_de_construccion):
        posicion_siguiente: Posición = posiciónAdyacenteAl(grilla, posicion_siguiente, direccion_de_construccion)
        barco.append(posicion_siguiente)
        visitadas.append(posicion_siguiente)
    

    return barco


def barcosEnGrilla(grilla: Grilla) -> list[BarcoEnGrilla]:
    """ Agregar docstring acá
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

    filas: int = len(grilla)
    columnas: int = len(grilla[0])

    visitadas: list[Posición] = []
    res: list[BarcoEnGrilla] = []

    for f in range(filas):
        for c in range(columnas):
            posicion: Posición = indiceAPosicion(f,c) 
            if celdaEnPosición(grilla, posicion) == BARCO and posicion not in visitadas:
                barco: list[Posición] = construirBarcoDesdePosicion(grilla, posicion, visitadas)
                res.append(barco)


    return res

    #Ejercicio 6

def posicionesDeBarcos(barcos: list[BarcoEnGrilla]) -> list[Posición]:
    posiciones: list[Posición] = []

    for barco in barcos:
        for pos in barco:
            posiciones.append(pos)
    
    return posiciones


def todosLosBarcosDescubiertos(grillaJugadorOponente: Grilla, grillaOponenteLocal: Grilla) -> bool:

    res = True
    barcos_acertados: list[BarcoEnGrilla] = barcosEnGrilla(grillaJugadorOponente)
    barcos_totales: list[BarcoEnGrilla] = barcosEnGrilla(grillaOponenteLocal)

    posiciones_de_barcos_acertados: list[Posición] = posicionesDeBarcos(barcos_acertados)
    posiciones_de_barcos_totales: list[Posición] = posicionesDeBarcos(barcos_totales)

    
    for pos_de_total in posiciones_de_barcos_totales:
        if pos_de_total not in posiciones_de_barcos_acertados:
            res = False
    
    return res

 
def hayAgua(grillaLocalOponente: Grilla) -> bool:
    res: bool = False
    dimensiones_grilla: Dimensiones = dimensionesGrilla(grillaLocalOponente)
    for fila in range(dimensiones_grilla[0]):
        for colum in range(dimensiones_grilla[1]):
            if grillaLocalOponente[fila][colum] == AGUA:
                res = True

    return res        

def esJugadorPerfecto(estadoDeJuego: EstadoJuego, jugador: Jugador) -> bool:
    tablero_jugador_UNO: Tablero = estadoDeJuego[3]
    tablero_jugador_DOS: Tablero = estadoDeJuego[4]
  

    """"
    Para que sea jugador PERFECT, cumple:
    si es jugador UNO, la grilla local está intacta, la grilla del oponente esta destruida
    """
    if jugador == UNO:
       a: bool = todosLosBarcosDescubiertos(tablero_jugador_UNO[1], tablero_jugador_DOS[0])
       b: bool = hayAgua(tablero_jugador_UNO[1])
    if jugador == DOS:
       a: bool = todosLosBarcosDescubiertos(tablero_jugador_DOS[1], tablero_jugador_UNO[0])
       b: bool = hayAgua(tablero_jugador_DOS[1])

    return a and not b

def hayJugadorPerfecto(estadoDeJuego: EstadoJuego) -> bool:
    """
    indica si algun jugador encontro todos los barcos rivales sin hacer ningun disparo a la nada
    pre:el estado de juego es valido
    arg: un booleano = el jugador UNO o el jugador DOS hizo una partida perfecta
    return True si hubo jugador perfecto False si no hubo
    """

    return esJugadorPerfecto(estadoDeJuego,UNO) or esJugadorPerfecto(estadoDeJuego, DOS)

