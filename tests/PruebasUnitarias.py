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

    def test_media_elementosPositivos(self):
        elementos = [1, 2, 3, 4, 5]
        resultadoEsperado = 3
        operacion = Operaciones(elementos)
        resultadoActual = operacion.calcularMedia()
        self.assertEqual(resultadoEsperado, resultadoActual)

    def test_media_todosCeros(self):
        elementos = [0, 0, 0, 0, 0]
        resultadoEsperado = 0
        operacion = Operaciones(elementos)
        resultadoActual = operacion.calcularMedia()
        self.assertEqual(resultadoEsperado, resultadoActual)

    def test_media_elementosPositivosYNegativos(self):
        elementos = [-1, 2, -3, 4]
        resultadoEsperado = 0.5
        operacion = Operaciones(elementos)
        resultadoActual = operacion.calcularMedia()
        self.assertEqual(resultadoEsperado, resultadoActual)

    def test_media_elementosNoNumericos_lanzaExcepcion(self):
        elementos = [1, 'a', 3]
        operacion = Operaciones(elementos)
        with self.assertRaises(TypeError):
            operacion.calcularMedia()

    # Pruebas para calcular la desviación estándar
    def test_desviacion_listaVacia_lanzaExcepcion(self):
        elementos = []
        operacion = Operaciones(elementos)
        with self.assertRaises(NoSePuedeCalcular):
            operacion.calcularDesviacionEstandar()

    def test_desviacion_unElemento(self):
        elementos = [5]
        resultadoEsperado = 0
        operacion = Operaciones(elementos)
        resultadoActual = operacion.calcularDesviacionEstandar()
        self.assertEqual(resultadoEsperado, resultadoActual)

    def test_desviacion_dosElementos(self):
        elementos = [2, 4]
        resultadoEsperado = 1
        operacion = Operaciones(elementos)
        resultadoActual = operacion.calcularDesviacionEstandar()
        self.assertEqual(resultadoEsperado, resultadoActual)

    def test_desviacion_elementosPositivos(self):
        elementos = [2, 4, 4, 4, 5, 5, 7, 9]
        resultadoEsperado = 2
        operacion = Operaciones(elementos)
        resultadoActual = operacion.calcularDesviacionEstandar()
        self.assertAlmostEqual(resultadoEsperado, resultadoActual, places=2)

    def test_desviacion_todosCeros(self):
        elementos = [0, 0, 0, 0, 0]
        resultadoEsperado = 0
        operacion = Operaciones(elementos)
        resultadoActual = operacion.calcularDesviacionEstandar()
        self.assertEqual(resultadoEsperado, resultadoActual)

    def test_desviacion_elementosPositivosYNegativos(self):
        elementos = [-2, -1, 0, 1, 2]
        resultadoEsperado = 1.4142
        operacion = Operaciones(elementos)
        resultadoActual = operacion.calcularDesviacionEstandar()
        self.assertAlmostEqual(resultadoEsperado, resultadoActual, places=2)

    def test_desviacion_elementosNoNumericos_lanzaExcepcion(self):
        elementos = [1, 'a', 3]
        operacion = Operaciones(elementos)
        with self.assertRaises(TypeError):
            operacion.calcularDesviacionEstandar()

if __name__ == '__main__':
    unittest.main()
