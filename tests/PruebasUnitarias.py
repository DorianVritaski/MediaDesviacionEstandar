import unittest
from src.logica.Operaciones import Operaciones, NoSePuedeCalcular

class Pruebas(unittest.TestCase):
    # Pruebas para calcular la media
    def test_media_listaVacia_lanzaExcepcion(self):
        elementos = []
        operacion = Operaciones(elementos)
        with self.assertRaises(NoSePuedeCalcular):
            operacion.calcularMedia()



if __name__ == '__main__':
    unittest.main()
