import unittest
from batallaNaval import *

# Tests
# Tests Ejercicio 1
class cantidadDeBarcosDeTamaño_Test(unittest.TestCase):
    def test_longitud_2_hay_uno_en_el_medio(self): # Un ejemplo de test 
        barcos = [[('H',3), ('H',4), ('H',5)],
                  [('F',4), ('E',4)],
                  [('B',4), ('B',3), ('B',2)]]       
        self.assertEqual(cantidadDeBarcosDeTamaño(barcos,2),1)
        self.assertEqual(barcos, [[('H',3), ('H',4), ('H',5)],
                                  [('F',4), ('E',4)],
                                  [('B',4), ('B',3), ('B',2)]] )
        
# Tests Ejercicio 2
class nuevoJuego_Test(unittest.TestCase):
    def test_2x2_y_un_barco_longitud_2(self): #
        grillaUNO_local = [[VACÍO, VACÍO],
                           [VACÍO, VACÍO]]
        
        grillaUNO_oponente = [[VACÍO, VACÍO],
                              [VACÍO, VACÍO]]
        
        grillaDOS_local = [[VACÍO, VACÍO],
                           [VACÍO, VACÍO]]
        
        grillaDOS_oponente = [[VACÍO, VACÍO],
                              [VACÍO, VACÍO]]
        
        juego = nuevoJuego(2,2,[2])
        
        self.assertEqual(juego[0], (2,2))
        self.assertTrue(juego[1], [2])
        self.assertEqual(juego[2], [UNO])
        self.assertEqual(juego[3], (grillaUNO_local, grillaUNO_oponente))
        self.assertEqual(juego[4], (grillaDOS_local, grillaDOS_oponente))
    
    def test_26x10_y_varios_barcos_de_longitud_x(self): #
        
        filas, columnas = 26, 10
        grillaUNO_local = [[VACÍO for _ in range(columnas)] for _ in range(filas)]
        
        grillaUNO_oponente = [[VACÍO for _ in range(columnas)] for _ in range(filas)]

        grillaDOS_local = [[VACÍO for _ in range(columnas)] for _ in range(filas)]

        grillaDOS_oponente = [[VACÍO for _ in range(columnas)] for _ in range(filas)]

        
        juego = nuevoJuego(26,10,[2,4,6,8,25]) # Respeto que no esten pegados
        
        self.assertEqual(juego[0], (26,10))
        self.assertTrue(juego[1], [2,4,6,8,25])
        self.assertEqual(juego[2], [UNO])
        self.assertEqual(juego[3], (grillaUNO_local, grillaUNO_oponente))
        self.assertEqual(juego[4], (grillaDOS_local, grillaDOS_oponente))
    


# Tests Ejercicio 3
class esEstadoDeJuegoVálido_Test(unittest.TestCase):
    def test_grilla_DOS_local_no_coincide_con_disponibles(self): # la grillaDOSlocal tiene un solo barco de tamaño 3, en lugar de dos de tamaño 2.
        grillaUnoLocal = [[VACÍO, VACÍO, VACÍO, VACÍO],
                          [BARCO, VACÍO, VACÍO, VACÍO],
                          [BARCO, VACÍO, BARCO, VACÍO],
                          [VACÍO, VACÍO, BARCO, VACÍO]]
        
        grillaUnoOponente = [[VACÍO, VACÍO, VACÍO, VACÍO],
                             [VACÍO, VACÍO, VACÍO, VACÍO],
                             [VACÍO, VACÍO, VACÍO, VACÍO],
                             [VACÍO, VACÍO, VACÍO, VACÍO]]
        
        grillaDosLocal = [[VACÍO, VACÍO, VACÍO, VACÍO],
                          [VACÍO, VACÍO, VACÍO, VACÍO],
                          [VACÍO, BARCO, BARCO, BARCO],
                          [VACÍO, VACÍO, VACÍO, VACÍO]]
        
        grillaDosOponente = [[VACÍO, VACÍO, VACÍO, VACÍO],
                             [VACÍO, VACÍO, VACÍO, VACÍO],
                             [VACÍO, VACÍO, VACÍO, VACÍO],
                             [VACÍO, VACÍO, VACÍO, VACÍO]]
        
        estado = ((4,4), [2,2], [DOS], (grillaUnoLocal, grillaUnoOponente), (grillaDosLocal, grillaDosOponente))
        
        self.assertFalse(esEstadoDeJuegoVálido(estado))        
        self.assertEqual(estado, ((4,4), [2,2], [DOS], (grillaUnoLocal, grillaUnoOponente), (grillaDosLocal, grillaDosOponente)))
    
    def test_grilla_UNO_local_no_coincide_con_disponibles(self): 
        grillaUnoLocal = [[VACÍO, VACÍO, VACÍO, VACÍO],
                          [BARCO, VACÍO, VACÍO, VACÍO],
                          [BARCO, VACÍO, VACÍO, VACÍO],
                          [BARCO, VACÍO, VACÍO, VACÍO]]
        
        grillaUnoOponente = [[VACÍO, VACÍO, VACÍO, VACÍO],
                             [VACÍO, VACÍO, VACÍO, VACÍO],
                             [VACÍO, VACÍO, VACÍO, VACÍO],
                             [VACÍO, VACÍO, VACÍO, VACÍO]]
        
        grillaDosLocal = [[VACÍO, VACÍO, VACÍO, VACÍO],
                          [VACÍO, VACÍO, VACÍO, VACÍO],
                          [BARCO, VACÍO, BARCO, BARCO],
                          [BARCO, VACÍO, VACÍO, VACÍO]]
        
        grillaDosOponente = [[VACÍO, VACÍO, VACÍO, VACÍO],
                             [VACÍO, VACÍO, VACÍO, VACÍO],
                             [VACÍO, VACÍO, VACÍO, VACÍO],
                             [VACÍO, VACÍO, VACÍO, VACÍO]]
        
        estado = ((4,4), [2,2], [DOS], (grillaUnoLocal, grillaUnoOponente), (grillaDosLocal, grillaDosOponente))
        
        self.assertFalse(esEstadoDeJuegoVálido(estado))        
        self.assertEqual(estado, ((4,4), [2,2], [DOS], (grillaUnoLocal, grillaUnoOponente), (grillaDosLocal, grillaDosOponente)))
    
    def test_cero_filas(self): 
        grillaUnoLocal = [[VACÍO, VACÍO, VACÍO, VACÍO],
                          [BARCO, VACÍO, VACÍO, VACÍO],
                          [BARCO, VACÍO, VACÍO, VACÍO],
                          [VACÍO, BARCO, BARCO, VACÍO]]
        
        grillaUnoOponente = [[VACÍO, VACÍO, VACÍO, VACÍO],
                             [VACÍO, VACÍO, VACÍO, VACÍO],
                             [VACÍO, VACÍO, VACÍO, VACÍO],
                             [VACÍO, VACÍO, VACÍO, VACÍO]]
        
        grillaDosLocal = [[VACÍO, VACÍO, VACÍO, VACÍO],
                          [VACÍO, VACÍO, VACÍO, VACÍO],
                          [BARCO, VACÍO, BARCO, BARCO],
                          [BARCO, VACÍO, VACÍO, VACÍO]]
        
        grillaDosOponente = [[VACÍO, VACÍO, VACÍO, VACÍO],
                             [VACÍO, VACÍO, VACÍO, VACÍO],
                             [VACÍO, VACÍO, VACÍO, VACÍO],
                             [VACÍO, VACÍO, VACÍO, VACÍO]]
        
        estado = ((0,4), [2,2], [DOS], (grillaUnoLocal, grillaUnoOponente), (grillaDosLocal, grillaDosOponente))
        
        self.assertFalse(esEstadoDeJuegoVálido(estado))        
        self.assertEqual(estado, ((0,4), [2,2], [DOS], (grillaUnoLocal, grillaUnoOponente), (grillaDosLocal, grillaDosOponente)))

    def test_es_valido(self): 
        grillaUnoLocal = [[VACÍO, VACÍO, VACÍO, VACÍO],
                          [BARCO, VACÍO, VACÍO, VACÍO],
                          [BARCO, VACÍO, VACÍO, VACÍO],
                          [VACÍO, BARCO, BARCO, VACÍO]]
        
        grillaUnoOponente = [[VACÍO, VACÍO, VACÍO, VACÍO],
                             [VACÍO, VACÍO, VACÍO, VACÍO],
                             [VACÍO, VACÍO, VACÍO, VACÍO],
                             [VACÍO, VACÍO, VACÍO, VACÍO]]
        
        grillaDosLocal = [[VACÍO, VACÍO, VACÍO, VACÍO],
                          [VACÍO, VACÍO, VACÍO, VACÍO],
                          [BARCO, VACÍO, BARCO, BARCO],
                          [BARCO, VACÍO, VACÍO, VACÍO]]
        
        grillaDosOponente = [[VACÍO, VACÍO, VACÍO, VACÍO],
                             [VACÍO, VACÍO, VACÍO, VACÍO],
                             [VACÍO, VACÍO, VACÍO, VACÍO],
                             [VACÍO, VACÍO, VACÍO, VACÍO]]
        
        estado = ((4,4), [2,2], [DOS], (grillaUnoLocal, grillaUnoOponente), (grillaDosLocal, grillaDosOponente))
        
        self.assertTrue(esEstadoDeJuegoVálido(estado))        
        self.assertEqual(estado, ((4,4), [2,2], [DOS], (grillaUnoLocal, grillaUnoOponente), (grillaDosLocal, grillaDosOponente)))

    def test_muchas_filas(self): 
        grillaUnoLocal = [[VACÍO, VACÍO, VACÍO, VACÍO],
                          [BARCO, VACÍO, VACÍO, VACÍO],
                          [BARCO, VACÍO, VACÍO, VACÍO],
                          [VACÍO, BARCO, BARCO, VACÍO]]
        
        grillaUnoOponente = [[VACÍO, VACÍO, VACÍO, VACÍO],
                             [VACÍO, VACÍO, VACÍO, VACÍO],
                             [VACÍO, VACÍO, VACÍO, VACÍO],
                             [VACÍO, VACÍO, VACÍO, VACÍO]]
        
        grillaDosLocal = [[VACÍO, VACÍO, VACÍO, VACÍO],
                          [VACÍO, VACÍO, VACÍO, VACÍO],
                          [BARCO, VACÍO, BARCO, BARCO],
                          [BARCO, VACÍO, VACÍO, VACÍO]]
        
        grillaDosOponente = [[VACÍO, VACÍO, VACÍO, VACÍO],
                             [VACÍO, VACÍO, VACÍO, VACÍO],
                             [VACÍO, VACÍO, VACÍO, VACÍO],
                             [VACÍO, VACÍO, VACÍO, VACÍO]]
        
        estado = ((70,4), [2,2], [DOS], (grillaUnoLocal, grillaUnoOponente), (grillaDosLocal, grillaDosOponente))
        
        self.assertFalse(esEstadoDeJuegoVálido(estado))        
        self.assertEqual(estado, ((70,4), [2,2], [DOS], (grillaUnoLocal, grillaUnoOponente), (grillaDosLocal, grillaDosOponente)))

    def test_cero_columnas(self): 
        grillaUnoLocal = [[VACÍO, VACÍO, VACÍO, VACÍO],
                          [BARCO, VACÍO, VACÍO, VACÍO],
                          [BARCO, VACÍO, VACÍO, VACÍO],
                          [VACÍO, BARCO, BARCO, VACÍO]]
        
        grillaUnoOponente = [[VACÍO, VACÍO, VACÍO, VACÍO],
                             [VACÍO, VACÍO, VACÍO, VACÍO],
                             [VACÍO, VACÍO, VACÍO, VACÍO],
                             [VACÍO, VACÍO, VACÍO, VACÍO]]
        
        grillaDosLocal = [[VACÍO, VACÍO, VACÍO, VACÍO],
                          [VACÍO, VACÍO, VACÍO, VACÍO],
                          [BARCO, VACÍO, BARCO, BARCO],
                          [BARCO, VACÍO, VACÍO, VACÍO]]
        
        grillaDosOponente = [[VACÍO, VACÍO, VACÍO, VACÍO],
                             [VACÍO, VACÍO, VACÍO, VACÍO],
                             [VACÍO, VACÍO, VACÍO, VACÍO],
                             [VACÍO, VACÍO, VACÍO, VACÍO]]
        
        estado = ((4,0), [2,2], [DOS], (grillaUnoLocal, grillaUnoOponente), (grillaDosLocal, grillaDosOponente))
        
        self.assertFalse(esEstadoDeJuegoVálido(estado))        
        self.assertEqual(estado, ((4,0), [2,2], [DOS], (grillaUnoLocal, grillaUnoOponente), (grillaDosLocal, grillaDosOponente)))

    def test_dos_elementos_en_turno(self): 
        grillaUnoLocal = [[VACÍO, VACÍO, VACÍO, VACÍO],
                          [BARCO, VACÍO, VACÍO, VACÍO],
                          [BARCO, VACÍO, VACÍO, VACÍO],
                          [VACÍO, BARCO, BARCO, VACÍO]]
        
        grillaUnoOponente = [[VACÍO, VACÍO, VACÍO, VACÍO],
                             [VACÍO, VACÍO, VACÍO, VACÍO],
                             [VACÍO, VACÍO, VACÍO, VACÍO],
                             [VACÍO, VACÍO, VACÍO, VACÍO]]
        
        grillaDosLocal = [[VACÍO, VACÍO, VACÍO, VACÍO],
                          [VACÍO, VACÍO, VACÍO, VACÍO],
                          [BARCO, VACÍO, BARCO, BARCO],
                          [BARCO, VACÍO, VACÍO, VACÍO]]
        
        grillaDosOponente = [[VACÍO, VACÍO, VACÍO, VACÍO],
                             [VACÍO, VACÍO, VACÍO, VACÍO],
                             [VACÍO, VACÍO, VACÍO, VACÍO],
                             [VACÍO, VACÍO, VACÍO, VACÍO]]
        
        estado = ((4,4), [2,2], [DOS,UNO], (grillaUnoLocal, grillaUnoOponente), (grillaDosLocal, grillaDosOponente))
        
        self.assertFalse(esEstadoDeJuegoVálido(estado))        
        self.assertEqual(estado, ((4,4), [2,2], [DOS,UNO], (grillaUnoLocal, grillaUnoOponente), (grillaDosLocal, grillaDosOponente)))

    def test_no_hay_barcos_disponibles(self): 
        grillaUnoLocal = [[VACÍO, VACÍO, VACÍO, VACÍO],
                          [BARCO, VACÍO, VACÍO, VACÍO],
                          [BARCO, VACÍO, VACÍO, VACÍO],
                          [VACÍO, BARCO, BARCO, VACÍO]]
        
        grillaUnoOponente = [[VACÍO, VACÍO, VACÍO, VACÍO],
                             [VACÍO, VACÍO, VACÍO, VACÍO],
                             [VACÍO, VACÍO, VACÍO, VACÍO],
                             [VACÍO, VACÍO, VACÍO, VACÍO]]
        
        grillaDosLocal = [[VACÍO, VACÍO, VACÍO, VACÍO],
                          [VACÍO, VACÍO, VACÍO, VACÍO],
                          [BARCO, VACÍO, BARCO, BARCO],
                          [BARCO, VACÍO, VACÍO, VACÍO]]
        
        grillaDosOponente = [[VACÍO, VACÍO, VACÍO, VACÍO],
                             [VACÍO, VACÍO, VACÍO, VACÍO],
                             [VACÍO, VACÍO, VACÍO, VACÍO],
                             [VACÍO, VACÍO, VACÍO, VACÍO]]
        
        estado = ((4,4), [], [DOS], (grillaUnoLocal, grillaUnoOponente), (grillaDosLocal, grillaDosOponente))
        
        self.assertFalse(esEstadoDeJuegoVálido(estado))        
        self.assertEqual(estado, ((4,4), [], [DOS], (grillaUnoLocal, grillaUnoOponente), (grillaDosLocal, grillaDosOponente)))

    def test_es_valido_con_ataques(self): 
        grillaUnoLocal = [[VACÍO, VACÍO, VACÍO, VACÍO],
                          [BARCO, VACÍO, VACÍO, VACÍO],
                          [BARCO, VACÍO, VACÍO, VACÍO],
                          [VACÍO, BARCO, BARCO, VACÍO]]
        
        grillaUnoOponente = [[AGUA, VACÍO, VACÍO, VACÍO],
                             [VACÍO, VACÍO, VACÍO, VACÍO],
                             [VACÍO, VACÍO, VACÍO, VACÍO],
                             [VACÍO, VACÍO, VACÍO, VACÍO]]
        
        grillaDosLocal = [[AGUA, VACÍO, VACÍO, VACÍO],
                          [VACÍO, VACÍO, VACÍO, VACÍO],
                          [BARCO, VACÍO, BARCO, BARCO],
                          [BARCO, VACÍO, VACÍO, VACÍO]]
        
        grillaDosOponente = [[VACÍO, VACÍO, VACÍO, VACÍO],
                             [VACÍO, VACÍO, VACÍO, VACÍO],
                             [BARCO, VACÍO, VACÍO, VACÍO],
                             [VACÍO, VACÍO, VACÍO, VACÍO]]
        
        estado = ((4,4), [2,2], [DOS], (grillaUnoLocal, grillaUnoOponente), (grillaDosLocal, grillaDosOponente))
        
        self.assertTrue(esEstadoDeJuegoVálido(estado))        
        self.assertEqual(estado, ((4,4), [2,2], [DOS], (grillaUnoLocal, grillaUnoOponente), (grillaDosLocal, grillaDosOponente)))

    def test_no_coinciden_posiciones_atacadas_jugador_uno(self): 
        grillaUnoLocal = [[VACÍO, VACÍO, VACÍO, VACÍO],
                          [BARCO, VACÍO, VACÍO, VACÍO],
                          [BARCO, VACÍO, VACÍO, VACÍO],
                          [VACÍO, BARCO, BARCO, VACÍO]]
        
        grillaUnoOponente = [[BARCO, VACÍO, VACÍO, VACÍO],
                             [VACÍO, VACÍO, VACÍO, VACÍO],
                             [VACÍO, VACÍO, VACÍO, VACÍO],
                             [VACÍO, VACÍO, VACÍO, VACÍO]]
        
        grillaDosLocal = [[VACÍO, VACÍO, VACÍO, VACÍO],
                          [VACÍO, VACÍO, VACÍO, VACÍO],
                          [BARCO, VACÍO, BARCO, BARCO],
                          [BARCO, VACÍO, VACÍO, VACÍO]]
        
        grillaDosOponente = [[VACÍO, VACÍO, VACÍO, VACÍO],
                             [BARCO, VACÍO, VACÍO, VACÍO],
                             [VACÍO, VACÍO, VACÍO, VACÍO],
                             [VACÍO, VACÍO, VACÍO, VACÍO]]
        
        estado = ((4,4), [2,2], [DOS], (grillaUnoLocal, grillaUnoOponente), (grillaDosLocal, grillaDosOponente))
        
        self.assertFalse(esEstadoDeJuegoVálido(estado))        
        self.assertEqual(estado, ((4,4), [2,2], [DOS], (grillaUnoLocal, grillaUnoOponente), (grillaDosLocal, grillaDosOponente)))

    def test_no_coinciden_posiciones_atacadas_jugador_dos(self): 
        grillaUnoLocal = [[VACÍO, VACÍO, VACÍO, VACÍO],
                          [BARCO, VACÍO, VACÍO, VACÍO],
                          [BARCO, VACÍO, VACÍO, VACÍO],
                          [VACÍO, BARCO, BARCO, VACÍO]]
        
        grillaUnoOponente = [[VACÍO, VACÍO, VACÍO, VACÍO],
                             [VACÍO, VACÍO, VACÍO, VACÍO],
                             [BARCO, VACÍO, VACÍO, VACÍO],
                             [VACÍO, VACÍO, VACÍO, VACÍO]]
        
        grillaDosLocal = [[VACÍO, VACÍO, VACÍO, VACÍO],
                          [VACÍO, VACÍO, VACÍO, VACÍO],
                          [BARCO, VACÍO, BARCO, BARCO],
                          [BARCO, VACÍO, VACÍO, VACÍO]]
        
        grillaDosOponente = [[VACÍO, VACÍO, VACÍO, VACÍO],
                             [AGUA, VACÍO, VACÍO, VACÍO],
                             [VACÍO, VACÍO, VACÍO, VACÍO],
                             [VACÍO, VACÍO, VACÍO, VACÍO]]
        
        estado = ((4,4), [2,2], [UNO], (grillaUnoLocal, grillaUnoOponente), (grillaDosLocal, grillaDosOponente))
        
        self.assertFalse(esEstadoDeJuegoVálido(estado))        
        self.assertEqual(estado, ((4,4), [2,2], [UNO], (grillaUnoLocal, grillaUnoOponente), (grillaDosLocal, grillaDosOponente)))

    def test_celda_no_es_vacio_ni_barco_grilla_uno(self): 
        grillaUnoLocal = [[AGUA, VACÍO, VACÍO, VACÍO],
                          [BARCO, VACÍO, VACÍO, VACÍO],
                          [BARCO, VACÍO, VACÍO, VACÍO],
                          [VACÍO, BARCO, BARCO, VACÍO]]
        
        grillaUnoOponente = [[VACÍO, VACÍO, VACÍO, VACÍO],
                             [VACÍO, VACÍO, VACÍO, VACÍO],
                             [VACÍO, VACÍO, VACÍO, VACÍO],
                             [VACÍO, VACÍO, VACÍO, VACÍO]]
        
        grillaDosLocal = [[VACÍO, VACÍO, VACÍO, VACÍO],
                          [VACÍO, VACÍO, VACÍO, VACÍO],
                          [BARCO, VACÍO, BARCO, BARCO],
                          [BARCO, VACÍO, VACÍO, VACÍO]]
        
        grillaDosOponente = [[VACÍO, VACÍO, VACÍO, VACÍO],
                             [VACÍO, VACÍO, VACÍO, VACÍO],
                             [VACÍO, VACÍO, VACÍO, VACÍO],
                             [VACÍO, VACÍO, VACÍO, VACÍO]]
        
        estado = ((4,4), [2,2], [UNO], (grillaUnoLocal, grillaUnoOponente), (grillaDosLocal, grillaDosOponente))
        
        self.assertFalse(esEstadoDeJuegoVálido(estado))        
        self.assertEqual(estado, ((4,4), [2,2], [UNO], (grillaUnoLocal, grillaUnoOponente), (grillaDosLocal, grillaDosOponente)))

    def test_celda_no_es_vacio_ni_barco_grilla_dos(self): 
        grillaUnoLocal = [[VACÍO, VACÍO, VACÍO, VACÍO],
                          [BARCO, VACÍO, VACÍO, VACÍO],
                          [BARCO, VACÍO, VACÍO, VACÍO],
                          [VACÍO, BARCO, BARCO, VACÍO]]
        
        grillaUnoOponente = [[VACÍO, VACÍO, VACÍO, VACÍO],
                             [VACÍO, VACÍO, VACÍO, VACÍO],
                             [VACÍO, VACÍO, VACÍO, VACÍO],
                             [VACÍO, VACÍO, VACÍO, VACÍO]]
        
        grillaDosLocal = [[AGUA, VACÍO, VACÍO, VACÍO],
                          [VACÍO, VACÍO, VACÍO, VACÍO],
                          [BARCO, VACÍO, BARCO, BARCO],
                          [BARCO, VACÍO, VACÍO, VACÍO]]
        
        grillaDosOponente = [[VACÍO, VACÍO, VACÍO, VACÍO],
                             [VACÍO, VACÍO, VACÍO, VACÍO],
                             [VACÍO, VACÍO, VACÍO, VACÍO],
                             [VACÍO, VACÍO, VACÍO, VACÍO]]
        
        estado = ((4,4), [2,2], [UNO], (grillaUnoLocal, grillaUnoOponente), (grillaDosLocal, grillaDosOponente))
        
        self.assertFalse(esEstadoDeJuegoVálido(estado))        
        self.assertEqual(estado, ((4,4), [2,2], [UNO], (grillaUnoLocal, grillaUnoOponente), (grillaDosLocal, grillaDosOponente)))


# Tests Ejercicio 4
class DispararEnPosición_Test(unittest.TestCase):
    def test_disparo_en_posicion_vacia_turno_uno(self):
        estado = ((5,5), [3, 2], [UNO],
            ([[BARCO, VACÍO, VACÍO, VACÍO, VACÍO], [BARCO, VACÍO, VACÍO, VACÍO, VACÍO],
             [BARCO, VACÍO, VACÍO, VACÍO, VACÍO], [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO],
             [VACÍO, VACÍO, VACÍO, BARCO, BARCO]],
            [[VACÍO, VACÍO, VACÍO, VACÍO, VACÍO], [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO],
             [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO], [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO],
             [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO]]),
            ([[VACÍO, VACÍO, VACÍO, VACÍO, VACÍO], [BARCO, BARCO, BARCO, VACÍO, VACÍO],
             [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO], [VACÍO, VACÍO, VACÍO, BARCO, BARCO],
             [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO]],
            [[VACÍO, VACÍO, VACÍO, VACÍO, VACÍO], [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO],
             [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO], [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO],
             [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO]])
        )
        
        estado_esperado = ((5,5), [3, 2], [DOS],
            ([[BARCO, VACÍO, VACÍO, VACÍO, VACÍO], [BARCO, VACÍO, VACÍO, VACÍO, VACÍO],
             [BARCO, VACÍO, VACÍO, VACÍO, VACÍO], [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO],
             [VACÍO, VACÍO, VACÍO, BARCO, BARCO]],
            [[AGUA, VACÍO, VACÍO, VACÍO, VACÍO], [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO],
             [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO], [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO],
             [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO]]),
            ([[AGUA, VACÍO, VACÍO, VACÍO, VACÍO], [BARCO, BARCO, BARCO, VACÍO, VACÍO],
             [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO], [VACÍO, VACÍO, VACÍO, BARCO, BARCO],
             [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO]],
            [[VACÍO, VACÍO, VACÍO, VACÍO, VACÍO], [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO],
             [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO], [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO],
             [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO]])
        )
        resultado = dispararEnPosición(estado, ("A", 1))
        self.assertEqual(resultado, NADA)
        self.assertEqual(estado, estado_esperado)
        
    def test_disparo_en_posicion_barco_turno_dos(self):
        estado = ((5,5), [3, 2], [DOS],
            
            ([[VACÍO, VACÍO, VACÍO, VACÍO, VACÍO], [BARCO, BARCO, BARCO, VACÍO, VACÍO],
             [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO], [VACÍO, VACÍO, VACÍO, BARCO, BARCO],
             [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO]],
            [[VACÍO, VACÍO, VACÍO, VACÍO, VACÍO], [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO],
             [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO], [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO],
             [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO]]),([[BARCO, VACÍO, VACÍO, VACÍO, VACÍO], [BARCO, VACÍO, VACÍO, VACÍO, VACÍO],
             [BARCO, VACÍO, VACÍO, VACÍO, VACÍO], [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO],
             [VACÍO, VACÍO, VACÍO, BARCO, BARCO]],
            [[VACÍO, VACÍO, VACÍO, VACÍO, VACÍO], [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO],
             [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO], [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO],
             [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO]])
        )
        
        estado_esperado = ((5,5), [3, 2], [UNO],
            
            ([[VACÍO, VACÍO, VACÍO, VACÍO, VACÍO], [BARCO, BARCO, BARCO, VACÍO, VACÍO],
             [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO], [VACÍO, VACÍO, VACÍO, BARCO, BARCO],
             [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO]],
            [[VACÍO, VACÍO, VACÍO, VACÍO, VACÍO], [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO],
             [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO], [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO],
             [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO]]),([[BARCO, VACÍO, VACÍO, VACÍO, VACÍO], [BARCO, VACÍO, VACÍO, VACÍO, VACÍO],
             [BARCO, VACÍO, VACÍO, VACÍO, VACÍO], [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO],
             [VACÍO, VACÍO, VACÍO, BARCO, BARCO]],
            [[VACÍO, VACÍO, VACÍO, VACÍO, VACÍO], [BARCO, VACÍO, VACÍO, VACÍO, VACÍO],
             [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO], [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO],
             [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO]])
        )
        resultado = dispararEnPosición(estado, ("B", 1))
        self.assertEqual(resultado, TOCADO)
        self.assertEqual(estado, estado_esperado)

    def test_disparo_en_posicion_vacia_turno_dos(self):
        estado = ((5,5), [3, 2], [DOS],
            
            ([[VACÍO, VACÍO, VACÍO, VACÍO, VACÍO], [BARCO, BARCO, BARCO, VACÍO, VACÍO],
             [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO], [VACÍO, VACÍO, VACÍO, BARCO, BARCO],
             [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO]],
            [[VACÍO, VACÍO, VACÍO, VACÍO, VACÍO], [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO],
             [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO], [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO],
             [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO]]),([[BARCO, VACÍO, VACÍO, VACÍO, VACÍO], [BARCO, VACÍO, VACÍO, VACÍO, VACÍO],
             [BARCO, VACÍO, VACÍO, VACÍO, VACÍO], [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO],
             [VACÍO, VACÍO, VACÍO, BARCO, BARCO]],
            [[VACÍO, VACÍO, VACÍO, VACÍO, VACÍO], [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO],
             [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO], [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO],
             [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO]])
        )
        
        estado_esperado = ((5,5), [3, 2], [UNO],
            
            ([[AGUA, VACÍO, VACÍO, VACÍO, VACÍO], [BARCO, BARCO, BARCO, VACÍO, VACÍO],
             [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO], [VACÍO, VACÍO, VACÍO, BARCO, BARCO],
             [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO]],
            [[VACÍO, VACÍO, VACÍO, VACÍO, VACÍO], [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO],
             [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO], [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO],
             [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO]]),([[BARCO, VACÍO, VACÍO, VACÍO, VACÍO], [BARCO, VACÍO, VACÍO, VACÍO, VACÍO],
             [BARCO, VACÍO, VACÍO, VACÍO, VACÍO], [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO],
             [VACÍO, VACÍO, VACÍO, BARCO, BARCO]],
            [[AGUA, VACÍO, VACÍO, VACÍO, VACÍO], [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO],
             [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO], [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO],
             [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO]])
        )
        resultado = dispararEnPosición(estado, ("A", 1))
        self.assertEqual(resultado, NADA)
        self.assertEqual(estado, estado_esperado)

    def test_disparo_en_posicion_barco_turno_uno(self):
        estado = ((5,5), [3, 2], [UNO],
            
            ([[VACÍO, VACÍO, VACÍO, VACÍO, VACÍO], [BARCO, BARCO, BARCO, VACÍO, VACÍO],
             [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO], [VACÍO, VACÍO, VACÍO, BARCO, BARCO],
             [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO]],
            [[VACÍO, VACÍO, VACÍO, VACÍO, VACÍO], [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO],
             [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO], [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO],
             [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO]]),([[BARCO, VACÍO, VACÍO, VACÍO, VACÍO], [BARCO, VACÍO, VACÍO, VACÍO, VACÍO],
             [BARCO, VACÍO, VACÍO, VACÍO, VACÍO], [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO],
             [VACÍO, VACÍO, VACÍO, BARCO, BARCO]],
            [[VACÍO, VACÍO, VACÍO, VACÍO, VACÍO], [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO],
             [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO], [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO],
             [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO]])
        )
        
        estado_esperado = ((5,5), [3, 2], [DOS],
            
           ([[VACÍO, VACÍO, VACÍO, VACÍO, VACÍO], [BARCO, BARCO, BARCO, VACÍO, VACÍO],
             [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO], [VACÍO, VACÍO, VACÍO, BARCO, BARCO],
             [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO]],
            [[VACÍO, VACÍO, VACÍO, VACÍO, VACÍO], [BARCO, VACÍO, VACÍO, VACÍO, VACÍO],
             [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO], [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO],
             [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO]]),([[BARCO, VACÍO, VACÍO, VACÍO, VACÍO], [BARCO, VACÍO, VACÍO, VACÍO, VACÍO],
             [BARCO, VACÍO, VACÍO, VACÍO, VACÍO], [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO],
             [VACÍO, VACÍO, VACÍO, BARCO, BARCO]],
            [[VACÍO, VACÍO, VACÍO, VACÍO, VACÍO], [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO],
             [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO], [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO],
             [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO]])
        )
        resultado = dispararEnPosición(estado, ("B", 1))
        self.assertEqual(resultado, TOCADO)
        self.assertEqual(estado, estado_esperado)

# Tests Ejercicio 5
class barcosEnGrilla_Test(unittest.TestCase):

    def test_un_barco_pequeño_en_grilla_pequeña(self):
        grilla: Grilla = [
            [BARCO]
        ]
        esperado: list[BarcoEnGrilla] = [
            [('A',1)]
        ]
        self.assertCountEqual(barcosEnGrilla(grilla), esperado)
    def test_barcos_en_bordes_horizontal(self):
        grilla: Grilla = [[BARCO, BARCO, VACÍO],
                          [VACÍO, VACÍO, VACÍO],
                          [VACÍO, BARCO, BARCO]]
        esperado: list[BarcoEnGrilla] = [
            [('A', 1), ('A', 2)],
            [('C', 2), ('C', 3)]
        ]
        self.assertCountEqual(barcosEnGrilla(grilla), esperado)
    
    def test_barcos_en_bordes_vertical(self):
        grilla: Grilla = [[BARCO, VACÍO, BARCO],
                          [BARCO, VACÍO, BARCO],
                          [BARCO, VACÍO, BARCO]]
        esperado: list[BarcoEnGrilla] = [
            [('A', 1), ('B', 1), ('C', 1)],
            [('A', 3), ('B', 3), ('C', 3)]
        ]
        self.assertCountEqual(barcosEnGrilla(grilla), esperado)
    

    def test_varios_barcos_distintos_tamanios(self): # Varios barcos de distintos tamaños en una grilla con varios barcos de distintos tamaños
        grilla: Grilla = [[VACÍO, VACÍO, VACÍO, VACÍO, VACÍO, VACÍO, VACÍO],
                          [BARCO, VACÍO, VACÍO, BARCO, BARCO, BARCO, VACÍO],
                          [BARCO, VACÍO, VACÍO, VACÍO, VACÍO, VACÍO, VACÍO],
                          [BARCO, VACÍO, BARCO, BARCO, VACÍO, BARCO, VACÍO],
                          [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO, BARCO, VACÍO]]
        
        barcosEsperados: list[BarcoEnGrilla] = [[('D',3), ('D',4)],
                                                [('B',6), ('B',5), ('B',4)],
                                                [('D',6), ('E',6)],
                                                [('D',1),('C',1), ('B',1)]]
        
        # Pensar! qué pasa si el orden de los barcos en la lista no es el mismo? respeta la especificación?
        self.assertTrue(barcosEnGrilla(grilla), barcosEsperados)
        self.assertEqual(grilla, [[VACÍO, VACÍO, VACÍO, VACÍO, VACÍO, VACÍO, VACÍO],
                                  [BARCO, VACÍO, VACÍO, BARCO, BARCO, BARCO, VACÍO],
                                  [BARCO, VACÍO, VACÍO, VACÍO, VACÍO, VACÍO, VACÍO],
                                  [BARCO, VACÍO, BARCO, BARCO, VACÍO, BARCO, VACÍO],
                                  [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO, BARCO, VACÍO]])


# Tests Ejercicio 6
class hayJugadorPerfecto_Test(unittest.TestCase):
    def test_jugador_uno_es_jugador_perfecto(self):
        
        grillaUnoLocal = [[VACÍO, VACÍO, VACÍO, VACÍO],
                          [BARCO, VACÍO, VACÍO, VACÍO],
                          [BARCO, VACÍO, VACÍO, VACÍO],
                          [VACÍO, BARCO, BARCO, VACÍO]]
        
        grillaUnoOponente = [[VACÍO, VACÍO, VACÍO, VACÍO],
                             [VACÍO, VACÍO, VACÍO, VACÍO],
                             [BARCO, VACÍO, BARCO, BARCO],
                             [BARCO, VACÍO, VACÍO, VACÍO]]
        
        grillaDosLocal = [[VACÍO, VACÍO, VACÍO, VACÍO],
                          [VACÍO, VACÍO, VACÍO, VACÍO],
                          [BARCO, VACÍO, BARCO, BARCO],
                          [BARCO, VACÍO, VACÍO, VACÍO]]
        
        grillaDosOponente = [[VACÍO, VACÍO, VACÍO, VACÍO],
                             [VACÍO, VACÍO, VACÍO, VACÍO],
                             [VACÍO, VACÍO, VACÍO, VACÍO],
                             [VACÍO, VACÍO, VACÍO, VACÍO]]
        estadoDeJuego: EstadoJuego = ((4,4), [2,2], [DOS], (grillaUnoLocal, grillaUnoOponente), (grillaDosLocal, grillaDosOponente))
        self.assertTrue(hayJugadorPerfecto(estadoDeJuego))

    def test_jugador_dos_es_jugador_perfecto(self):
        
        grillaUnoLocal = [[VACÍO, VACÍO, VACÍO, VACÍO],
                          [BARCO, VACÍO, VACÍO, VACÍO],
                          [BARCO, VACÍO, VACÍO, VACÍO],
                          [VACÍO, BARCO, BARCO, VACÍO]]
        
        grillaUnoOponente = [[VACÍO, VACÍO, VACÍO, VACÍO],
                             [VACÍO, VACÍO, VACÍO, VACÍO],
                             [BARCO, VACÍO, VACÍO, BARCO],
                             [BARCO, VACÍO, VACÍO, VACÍO]]
        
        grillaDosLocal = [[VACÍO, VACÍO, VACÍO, VACÍO],
                          [VACÍO, VACÍO, VACÍO, VACÍO],
                          [BARCO, VACÍO, BARCO, BARCO],
                          [BARCO, VACÍO, VACÍO, VACÍO]]
        
        grillaDosOponente = [[VACÍO, VACÍO, VACÍO, VACÍO],
                             [BARCO, VACÍO, VACÍO, VACÍO],
                             [BARCO, VACÍO, VACÍO, VACÍO],
                             [VACÍO, BARCO, BARCO, VACÍO]]
        estadoDeJuego: EstadoJuego = ((4,4), [2,2], [DOS], (grillaUnoLocal, grillaUnoOponente), (grillaDosLocal, grillaDosOponente))
        self.assertTrue(hayJugadorPerfecto(estadoDeJuego))

    def test_jugador_dos_tiene_agua(self):
        
        grillaUnoLocal = [[VACÍO, VACÍO, VACÍO, VACÍO],
                          [BARCO, VACÍO, VACÍO, VACÍO],
                          [BARCO, VACÍO, VACÍO, VACÍO],
                          [VACÍO, BARCO, BARCO, AGUA]]
        
        grillaUnoOponente = [[VACÍO, VACÍO, VACÍO, VACÍO],
                             [VACÍO, VACÍO, VACÍO, VACÍO],
                             [BARCO, VACÍO, VACÍO, BARCO],
                             [BARCO, VACÍO, VACÍO, VACÍO]]
        
        grillaDosLocal = [[VACÍO, VACÍO, VACÍO, VACÍO],
                          [VACÍO, VACÍO, VACÍO, VACÍO],
                          [BARCO, VACÍO, BARCO, BARCO],
                          [BARCO, VACÍO, VACÍO, VACÍO]]
        
        grillaDosOponente = [[VACÍO, VACÍO, VACÍO, VACÍO],
                             [BARCO, VACÍO, VACÍO, VACÍO],
                             [BARCO, VACÍO, VACÍO, VACÍO],
                             [VACÍO, BARCO, BARCO, AGUA]]
        estadoDeJuego: EstadoJuego = ((4,4), [2,2], [DOS], (grillaUnoLocal, grillaUnoOponente), (grillaDosLocal, grillaDosOponente))
        self.assertFalse(hayJugadorPerfecto(estadoDeJuego))

    def test_jugador_uno_tiene_agua(self):
        
        grillaUnoLocal = [[VACÍO, VACÍO, VACÍO, VACÍO],
                          [BARCO, VACÍO, VACÍO, VACÍO],
                          [BARCO, VACÍO, VACÍO, VACÍO],
                          [VACÍO, BARCO, BARCO, VACÍO]]
        
        grillaUnoOponente = [[VACÍO, VACÍO, VACÍO, VACÍO],
                             [VACÍO, VACÍO, VACÍO, VACÍO],
                             [BARCO, VACÍO, BARCO, BARCO],
                             [BARCO, VACÍO, AGUA, VACÍO]]
        
        grillaDosLocal = [[VACÍO, VACÍO, VACÍO, VACÍO],
                          [VACÍO, VACÍO, VACÍO, VACÍO],
                          [BARCO, VACÍO, BARCO, BARCO],
                          [BARCO, VACÍO, VACÍO, VACÍO]]
        
        grillaDosOponente = [[VACÍO, VACÍO, VACÍO, VACÍO],
                             [VACÍO, VACÍO, VACÍO, VACÍO],
                             [VACÍO, VACÍO, VACÍO, VACÍO],
                             [VACÍO, VACÍO, VACÍO, VACÍO]]
        estadoDeJuego: EstadoJuego = ((4,4), [2,2], [DOS], (grillaUnoLocal, grillaUnoOponente), (grillaDosLocal, grillaDosOponente))
        self.assertFalse(hayJugadorPerfecto(estadoDeJuego))

    def no_hay_jugador_perfecto(self):
        
        grillaUnoLocal = [[VACÍO, VACÍO, VACÍO, VACÍO],
                          [BARCO, VACÍO, VACÍO, VACÍO],
                          [BARCO, VACÍO, VACÍO, VACÍO],
                          [VACÍO, BARCO, BARCO, VACÍO]]
        
        grillaUnoOponente = [[VACÍO, VACÍO, VACÍO, VACÍO],
                             [VACÍO, VACÍO, VACÍO, VACÍO],
                             [VACÍO, VACÍO, VACÍO, VACÍO],
                             [VACÍO, VACÍO, VACÍO, VACÍO]]
        
        grillaDosLocal = [[VACÍO, VACÍO, VACÍO, VACÍO],
                          [VACÍO, VACÍO, VACÍO, VACÍO],
                          [BARCO, VACÍO, BARCO, BARCO],
                          [BARCO, VACÍO, VACÍO, VACÍO]]
        
        grillaDosOponente = [[VACÍO, VACÍO, VACÍO, VACÍO],
                             [VACÍO, VACÍO, VACÍO, VACÍO],
                             [VACÍO, VACÍO, VACÍO, VACÍO],
                             [VACÍO, VACÍO, VACÍO, VACÍO]]
        estadoDeJuego: EstadoJuego = ((4,4), [2,2], [DOS], (grillaUnoLocal, grillaUnoOponente), (grillaDosLocal, grillaDosOponente))
        self.assertFalse(hayJugadorPerfecto(estadoDeJuego))





if __name__ == '__main__':
    unittest.main(verbosity=1)
