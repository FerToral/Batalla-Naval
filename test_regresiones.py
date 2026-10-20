"""Regresiones nuevas: preservan los tests históricos y no alteran biblioteca.py."""
import copy
import unittest
import batallaNaval as juego
from biblioteca import VACÍO, BARCO, AGUA, UNO, DOS, NADA, TOCADO


def estado_inicial():
    estado = juego.nuevoJuego(2, 2, [1])
    estado[3][0][0][0] = BARCO
    estado[4][0][1][1] = BARCO
    return estado


def canonico(barcos):
    return sorted(sorted(barco) for barco in barcos)


class ContratosIniciales(unittest.TestCase):
    def test_lista_de_barcos_vacia_y_tamano_ausente(self):
        self.assertEqual(juego.cantidadDeBarcosDeTamaño([], 2), 0)
        self.assertEqual(juego.cantidadDeBarcosDeTamaño([[("A", 1)]], 2), 0)

    def test_nuevo_juego_no_comparte_filas_grillas_o_flota(self):
        barcos = [1, 2]
        estado = juego.nuevoJuego(3, 3, barcos)
        estado[3][0][0][0] = BARCO
        barcos.append(3)
        self.assertEqual(estado[1], [1, 2])
        self.assertEqual(estado[3][0][1][0], VACÍO)
        self.assertEqual(estado[3][1][0][0], VACÍO)
        self.assertEqual(estado[4][0][0][0], VACÍO)

    def test_estado_con_dimensiones_cruzadas_es_falso_no_excepcion(self):
        estado = estado_inicial()
        estado = (estado[0], estado[1], estado[2], estado[3], ([[BARCO]], estado[4][1]))
        self.assertFalse(juego.esEstadoDeJuegoVálido(estado))

    def test_estado_con_grilla_irregular_es_falso_no_excepcion(self):
        estado = estado_inicial()
        estado = (estado[0], estado[1], estado[2], ([[BARCO], []], estado[3][1]), estado[4])
        self.assertFalse(juego.esEstadoDeJuegoVálido(estado))

    def test_limites_de_dimensiones_turno_y_flota(self):
        for dimensiones, barcos, turno in [((0, 2), [1], [UNO]), ((27, 2), [1], [UNO]),
                                           ((2, 0), [1], [UNO]), ((2, 2), [], [UNO]),
                                           ((2, 2), [1], []), ((2, 2), [1], [UNO, DOS])]:
            estado = estado_inicial()
            candidato = (dimensiones, barcos, turno, estado[3], estado[4])
            with self.subTest(dimensiones=dimensiones, barcos=barcos, turno=turno):
                self.assertFalse(juego.esEstadoDeJuegoVálido(candidato))


class UltimosEjercicios(unittest.TestCase):
    def test_descubrir_no_es_hundir_y_requiere_cada_barco(self):
        local = [[BARCO,BARCO,VACÍO],[VACÍO,VACÍO,VACÍO],[BARCO,BARCO,VACÍO]]
        parcial = [[BARCO,VACÍO,VACÍO],[VACÍO,VACÍO,VACÍO],[BARCO,VACÍO,VACÍO]]
        self.assertTrue(juego.todosLosBarcosDescubiertos(parcial,local))
        self.assertFalse(juego.todosLosBarcosHundidos(parcial,local))
        parcial[2][0] = VACÍO
        self.assertFalse(juego.todosLosBarcosDescubiertos(parcial,local))
        self.assertTrue(juego.todosLosBarcosHundidos(local,local))

    def test_jugador_perfecto_con_un_impacto_por_barco_y_sin_agua(self):
        local_uno = [[BARCO,BARCO,VACÍO],[VACÍO,VACÍO,VACÍO],[VACÍO,VACÍO,VACÍO]]
        local_dos = [[VACÍO,VACÍO,VACÍO],[VACÍO,VACÍO,VACÍO],[BARCO,BARCO,VACÍO]]
        oponente_uno = [[VACÍO,VACÍO,VACÍO],[VACÍO,VACÍO,VACÍO],[BARCO,VACÍO,VACÍO]]
        oponente_dos = [[BARCO,VACÍO,VACÍO],[VACÍO,VACÍO,VACÍO],[VACÍO,VACÍO,VACÍO]]
        estado = ((3,3),[2],[UNO],(local_uno,oponente_uno),(local_dos,oponente_dos))
        self.assertTrue(juego.esEstadoDeJuegoVálido(estado))
        self.assertTrue(juego.esJugadorPerfecto(estado,UNO))
        self.assertTrue(juego.esJugadorPerfecto(estado,DOS))
        from interfaz_batalla_naval import InterfazBatallaNaval
        interfaz = InterfazBatallaNaval.__new__(InterfazBatallaNaval)
        interfaz.estado_juego = estado
        self.assertIsNone(interfaz.ganador())

    def test_balance_no_permite_dos_ataques_de_diferencia_ni_mas_del_segundo(self):
        estado = estado_inicial()
        estado[3][1][0][1] = AGUA
        estado[3][1][1][0] = AGUA
        estado[4][0][0][1] = AGUA
        estado[4][0][1][0] = AGUA
        self.assertFalse(juego.esEstadoDeJuegoVálido(estado))
        invertido = (estado[0], estado[1], estado[2], estado[4], estado[3])
        self.assertFalse(juego.esEstadoDeJuegoVálido(invertido))

    def test_conversion_de_indices_en_ambos_extremos(self):
        self.assertEqual(juego.indiceAPosicion(0, 0), ("A", 1))
        self.assertEqual(juego.indiceAPosicion(25, 9), ("Z", 10))

    def test_disparo_al_barco_solo_cambia_marca_y_turno(self):
        estado = estado_inicial()
        esperado = copy.deepcopy(estado)
        esperado[3][1][1][1] = BARCO
        esperado[2][0] = DOS
        self.assertEqual(juego.dispararEnPosición(estado, ("B", 2)), TOCADO)
        self.assertEqual(estado, esperado)

    def test_disparo_al_agua_actualiza_solo_las_dos_celdas_y_turno(self):
        estado = estado_inicial()
        esperado = copy.deepcopy(estado)
        esperado[3][1][0][1] = AGUA
        esperado[4][0][0][1] = AGUA
        esperado[2][0] = DOS
        self.assertEqual(juego.dispararEnPosición(estado, ("A", 2)), NADA)
        self.assertEqual(estado, esperado)

    def test_barcos_vacios_y_borde_inferior_derecho(self):
        self.assertEqual(juego.barcosEnGrilla([[VACÍO, AGUA]]), [])
        self.assertEqual(juego.barcosEnGrilla([[VACÍO, VACÍO], [VACÍO, BARCO]]), [[("B", 2)]])

    def test_barco_vertical_de_26_filas_sin_mutar_entrada(self):
        grilla = [[BARCO] for _ in range(26)]
        original = copy.deepcopy(grilla)
        self.assertEqual(juego.barcosEnGrilla(grilla), [[(chr(65 + fila), 1) for fila in range(26)]])
        self.assertEqual(grilla, original)

    def test_varios_barcos_compara_contenido_no_solo_lista_no_vacia(self):
        grilla = [[VACÍO, VACÍO, VACÍO, VACÍO, VACÍO, VACÍO, VACÍO],
                  [BARCO, VACÍO, VACÍO, BARCO, BARCO, BARCO, VACÍO],
                  [BARCO, VACÍO, VACÍO, VACÍO, VACÍO, VACÍO, VACÍO],
                  [BARCO, VACÍO, BARCO, BARCO, VACÍO, BARCO, VACÍO],
                  [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO, BARCO, VACÍO]]
        esperado = [[("D", 3), ("D", 4)], [("B", 4), ("B", 5), ("B", 6)],
                    [("D", 6), ("E", 6)], [("B", 1), ("C", 1), ("D", 1)]]
        original = copy.deepcopy(grilla)
        resultado = juego.barcosEnGrilla(grilla)
        self.assertEqual(canonico(resultado), canonico(esperado))
        posiciones = [posicion for barco in resultado for posicion in barco]
        self.assertEqual(len(posiciones), len(set(posiciones)))
        self.assertEqual(grilla, original)

    def test_sin_ataques_no_hay_jugador_perfecto(self):
        self.assertFalse(juego.hayJugadorPerfecto(estado_inicial()))

    def test_ultimo_ejercicio_con_barco_unitario_descubierto(self):
        estado = estado_inicial()
        juego.dispararEnPosición(estado, ("B", 2))
        self.assertTrue(juego.hayJugadorPerfecto(estado))
        self.assertFalse(juego.esJugadorPerfecto(estado, DOS))

    def test_agua_impide_perfeccion_aunque_se_descubra_el_barco(self):
        estado = estado_inicial()
        estado[3][1][0][1] = AGUA
        estado[4][0][0][1] = AGUA
        estado[3][1][1][1] = BARCO
        estado[4][1][1][0] = AGUA
        estado[3][0][1][0] = AGUA
        self.assertFalse(juego.hayJugadorPerfecto(estado))

    def test_activar_caso_historico_que_no_tenia_prefijo_test(self):
        from tests_materia import hayJugadorPerfecto_Test
        hayJugadorPerfecto_Test().no_hay_jugador_perfecto()

    def test_no_hay_agua_en_ultima_celda_no_oculta_agua_anterior(self):
        self.assertTrue(juego.hayAgua([[AGUA, VACÍO], [VACÍO, VACÍO]]))
        self.assertTrue(juego.hayAgua([[VACÍO, VACÍO], [VACÍO, AGUA]]))
        self.assertFalse(juego.hayAgua([[BARCO, VACÍO], [VACÍO, BARCO]]))


if __name__ == "__main__":
    unittest.main()
