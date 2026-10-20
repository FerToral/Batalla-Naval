"""Controlador de la GUI sin abrir ventanas ni simular una revisión visual."""
import unittest
from unittest.mock import patch, Mock
from interfaz_batalla_naval import InterfazBatallaNaval
from batallaNaval import nuevoJuego
from biblioteca import BARCO, UNO, DOS


def interfaz():
    app = InterfazBatallaNaval.__new__(InterfazBatallaNaval)
    app.estado_juego = nuevoJuego(2,2,[1])
    app.estado_juego[3][0][0][0] = BARCO
    app.estado_juego[4][0][0][0] = BARCO
    app.disparosPC = []
    app.actualizar_interfaz = Mock()
    return app


class ControladorInterfaz(unittest.TestCase):
    def test_pc_no_repite_posiciones_ni_despues_de_dar_vuelta(self):
        app = interfaz()
        with patch("interfaz_batalla_naval.random.choice",return_value=("B",2)):
            tiros = [app.disparoPC() for _ in range(4)]
        self.assertEqual(tiros,[("B",2),("A",1),("A",2),("B",1)])
        self.assertEqual(len(set(tiros)),4)
        with self.assertRaises(ValueError):
            app.disparoPC()

    def test_impacto_final_no_ejecuta_pc_y_click_posterior_no_mutua(self):
        app = interfaz()
        with patch("interfaz_batalla_naval.messagebox.showinfo"):
            app.manejar_disparo(0,0)
            self.assertEqual(app.ganador(),UNO)
            self.assertEqual(app.disparosPC,[])
            turno = app.estado_juego[2][0]
            app.manejar_disparo(1,1)
            self.assertEqual(app.estado_juego[2][0],turno)
            self.assertEqual(app.disparosPC,[])

    def test_jugada_no_terminal_ejecuta_ambos_turnos(self):
        app = interfaz()
        with patch("interfaz_batalla_naval.messagebox.showinfo"), \
             patch("interfaz_batalla_naval.random.choice",return_value=("B",2)):
            app.manejar_disparo(1,1)
        self.assertIsNone(app.ganador())
        self.assertEqual(len(app.disparosPC),1)
        self.assertEqual(app.estado_juego[2][0],UNO)

    def test_ganador_dos_detectado_por_impactos_no_por_perfeccion(self):
        app = interfaz()
        app.estado_juego[4][1][0][0] = BARCO
        self.assertEqual(app.ganador(),DOS)


if __name__ == "__main__":
    unittest.main()
