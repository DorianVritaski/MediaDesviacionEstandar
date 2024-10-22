import unittest
from src.logica.Operaciones import Operaciones, NoSePuedeCalcular

class Pruebas(unittest.TestCase):

    def crear_operacion(self, elementos):
        return Operaciones(elementos)

    def test_media_listaVacia_lanzaExcepcion(self):
        operacion = self.crear_operacion([])
        with self.assertRaises(NoSePuedeCalcular):
            operacion.calcularMedia()

    def test_media_unElemento_retornaElemento(self):
        resultadoEsperado = 3.5
        operacion = self.crear_operacion([3.5])
        resultadoActual = operacion.calcularMedia()
        self.assertEqual(resultadoEsperado, resultadoActual)

    def test_media_dosElementos(self):
        resultadoEsperado = 5
        operacion = self.crear_operacion([3, 7])
        resultadoActual = operacion.calcularMedia()
        self.assertEqual(resultadoEsperado, resultadoActual)

    def test_media_elementosPositivos(self):
        resultadoEsperado = 3
        operacion = self.crear_operacion([1, 2, 3, 4, 5])
        resultadoActual = operacion.calcularMedia()
        self.assertEqual(resultadoEsperado, resultadoActual)

    def test_media_todosCeros(self):
        resultadoEsperado = 0
        operacion = self.crear_operacion([0, 0, 0, 0, 0])
        resultadoActual = operacion.calcularMedia()
        self.assertEqual(resultadoEsperado, resultadoActual)

    def test_media_elementosPositivosYNegativos(self):
        resultadoEsperado = 0.5
        operacion = self.crear_operacion([-1, 2, -3, 4])
        resultadoActual = operacion.calcularMedia()
        self.assertEqual(resultadoEsperado, resultadoActual)

    def test_media_elementosNoNumericos_lanzaExcepcion(self):
        operacion = self.crear_operacion([1, 'a', 3])
        with self.assertRaises(TypeError):
            operacion.calcularMedia()

    # Pruebas para calcular la desviación estándar
    def test_desviacion_listaVacia_lanzaExcepcion(self):
        operacion = self.crear_operacion([])
        with self.assertRaises(NoSePuedeCalcular):
            operacion.calcularDesviacionEstandar()

    def test_desviacion_unElemento(self):
        resultadoEsperado = 0
        operacion = self.crear_operacion([5])
        resultadoActual = operacion.calcularDesviacionEstandar()
        self.assertEqual(resultadoEsperado, resultadoActual)

    def test_desviacion_dosElementos(self):
        resultadoEsperado = 1
        operacion = self.crear_operacion([2, 4])
        resultadoActual = operacion.calcularDesviacionEstandar()
        self.assertEqual(resultadoEsperado, resultadoActual)

    def test_desviacion_elementosPositivos(self):
        resultadoEsperado = 2
        operacion = self.crear_operacion([2, 4, 4, 4, 5, 5, 7, 9])
        resultadoActual = operacion.calcularDesviacionEstandar()
        self.assertAlmostEqual(resultadoEsperado, resultadoActual, places=2)

    def test_desviacion_todosCeros(self):
        resultadoEsperado = 0
        operacion = self.crear_operacion([0, 0, 0, 0, 0])
        resultadoActual = operacion.calcularDesviacionEstandar()
        self.assertEqual(resultadoEsperado, resultadoActual)

    def test_desviacion_elementosPositivosYNegativos(self):
        resultadoEsperado = 1.4142
        operacion = self.crear_operacion([-2, -1, 0, 1, 2])
        resultadoActual = operacion.calcularDesviacionEstandar()
        self.assertAlmostEqual(resultadoEsperado, resultadoActual, places=2)

    def test_desviacion_elementosNoNumericos_lanzaExcepcion(self):
        operacion = self.crear_operacion([1, 'a', 3])
        with self.assertRaises(TypeError):
            operacion.calcularDesviacionEstandar()

if __name__ == '__main__':
    unittest.main()
