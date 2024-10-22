import unittest
from src.logica.Operaciones import Operaciones, NoSePuedeCalcular

class Pruebas(unittest.TestCase):
    # Pruebas para calcular la media
    def test_media_listaVacia_lanzaExcepcion(self):
        elementos = []
        operacion = Operaciones(elementos)
        with self.assertRaises(NoSePuedeCalcular):
            operacion.calcularMedia()

    def test_media_unElemento_retornaElemento(self):
        elementos = [3.5]
        resultadoEsperado = 3.5
        operacion = Operaciones(elementos)
        resultadoActual = operacion.calcularMedia()
        self.assertEqual(resultadoEsperado, resultadoActual)

    def test_media_dosElementos(self):
        elementos = [3, 7]
        resultadoEsperado = 5
        operacion = Operaciones(elementos)
        resultadoActual = operacion.calcularMedia()
        self.assertEqual(resultadoEsperado, resultadoActual)


if __name__ == '__main__':
    unittest.main()
