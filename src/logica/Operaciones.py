class NoSePuedeCalcular(Exception):
    pass


class Operaciones:
    def __init__(self, elementos):
        self.elementos = elementos

    def calcularMedia(self):
        if not self.elementos:
            raise NoSePuedeCalcular("La lista de elementos está vacía.")

        for elemento in self.elementos:
            if not isinstance(elemento, (int, float)):
                raise TypeError(f"{elemento} no es un número.")

        return sum(self.elementos) / len(self.elementos)

    def calcularDesviacionEstandar(self):
        if not self.elementos:
            raise NoSePuedeCalcular("La lista de elementos está vacía.")

        media = self.calcularMedia()
        varianza = sum((x - media) ** 2 for x in self.elementos) / len(self.elementos)
        return varianza ** 0.5
