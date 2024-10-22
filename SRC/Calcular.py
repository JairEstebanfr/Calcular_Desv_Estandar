import math

class CalculosEstadisticos:

    def calcular_media(self, num):
        """Calcula la media de una lista de números"""
        if not num:
            return None
        return sum(num) / len(num)
    def calcular_desviacion_estandar(self, num):
        """Calcula la desviación estándar muestral de una lista de números"""
        if not num:
            return None
        media = self.calcular_media(num)
        # Dividimos por (n-1) en lugar de n para desviación estándar muestral
        varianza = sum((x - media) ** 2 for x in num) / (len(num) - 1)
        return math.sqrt(varianza)