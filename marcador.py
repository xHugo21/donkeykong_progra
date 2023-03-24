class Marcador:
    def __init__(self, puntos: int, vidas: int):
        self.puntos = puntos
        self.vidas = vidas

    @property
    def puntos(self):
        return self.__puntos

    @puntos.setter
    def puntos(self, puntos):
        if puntos>=0:
            self.__puntos = puntos
        else:
            self.__puntos = 0

    @property
    def vidas(self):
        return self.__vidas

    @vidas.setter
    def vidas(self, vidas):
        if 0<=vidas<=3:
            self.__vidas = vidas
        else:
            self.__vidas = 3

    def puntossalto(self):
        self.puntos += 100

    def perdervidas(self):
        self.vidas -= 1

    def __str__(self):
        '''Método que devuelve la puntuación para imprimirla en pantalla'''
        if len(str(self.puntos)) == 1:
            return str("00000") + str(self.puntos)
        elif len(str(self.puntos)) == 2:
            return str("0000") + str(self.puntos)
        elif len(str(self.puntos)) == 3:
            return str("000") + str(self.puntos)
        elif len(str(self.puntos)) == 4:
            return str("00") + str(self.puntos)
        elif len(str(self.puntos)) == 5:
            return str("0") + str(self.puntos)
        elif len(str(self.puntos)) == 2:
            return str(self.puntos)

