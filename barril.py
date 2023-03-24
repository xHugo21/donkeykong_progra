import constantes


class Barril:
    def __init__(self, posX, posY, tipo):
        self.posX = posX
        self.posY = posY
        self.sobreplataforma = True
        self.bajaescaleras = False
        # Barril estático
        if tipo == 0:
            self.sprite = (1, 36, 240, 12, 16)
        # Barril en movimiento
        if tipo == 1:
            self.sprite = (1, 57, 241, 14, 14)
        # Barril cayendo
        if tipo == 2:
            self.sprite = (1, 79, 242, 18, 12)

    @property
    def posX(self):
        return self.__posX

    @posX.setter
    def posX(self, posX):
        if 0 <= posX <= 234:
            self.__posX = posX

    @property
    def posY(self):
        return self.__posY

    @posY.setter
    def posY(self, posY):
        if 0 <= posY <= 240:
            self.__posY = posY

    def rightX(self, x):
        self.posX += x

    def leftX(self, x):
        self.posX -= x

    def downY(self, y):
        self.sprite = (1, 79, 242, 18, 12)
        self.posY += y

    def movimientoBarril(self):
        if self.sobreplataforma:
            self.sprite = (1, 57, 241, 14, 14)
            # Sexta, cuarta y segunda plataforma
            if self.posY in range(0, 51) or self.posY in range(114, 125) or self.posY in range(184, 196):
                self.rightX(constantes.VELOCIDADBARRIL)
            # Quinta, tercera y primera plataforma
            if self.posY in range(77, 88) or self.posY in range(146, 159) or self.posY in range(224, 230):
                self.leftX(constantes.VELOCIDADBARRIL)

        if not self.sobreplataforma:
            self.downY(constantes.VELOCIDADBARRILBAJANDO)
