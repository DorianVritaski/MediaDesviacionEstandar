# Aplicación de Cálculo de Promedio y Desviación Estándar

Esta aplicación permite calcular el **promedio** y la **desviación estándar** de una lista de números. Incluye también un conjunto de **pruebas unitarias** para validar distintos casos de prueba.

## Como ejecutar la aplicación y las pruebas

1. Clona este repositorio en tu máquina local:
   - git clone https://github.com/DorianVritaski/MediaDesviacionEstandar.git

2. Abrir el proyecto en PyCharm:
   - Abrir PyCharm y seleccionar Open en la pantalla de bienvenida.
   - Navega hasta el directorio donde se clonó el repositorio y seleccionar la carpeta del proyecto.

3. Ejecución de la aplicación
   - Para utilizar la aplicación, simplemente importar el módulo y usar las funciones calcularMedia y calcularDesviacionEstandar
  
5. Ejecución delas pruebas
   - Navega al archivo de pruebas tests/PruebasUnitarias.py.
   - Haz clic derecho en cualquier parte del archivo y selecciona Run 'PruebasUnitarias' para ejecutar todas las pruebas.
   - También puedes ejecutar las pruebas haciendo clic en el botón Run en la esquina superior derecha de la ventana de PyCharm.
   - Casos de prueba incluidos:
        - Lista vacía (debe lanzar una excepción).
        - Lista con un solo elemento.
        - Lista con dos elementos.
        - Lista con n elementos positivos.
        - Lista con n elementos donde todos son ceros.
        - Lista con n elementos positivos y negativos.
        - Lista con elementos no numéricos (debe lanzar una excepción TypeError).
