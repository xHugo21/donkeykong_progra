class Mario:
    def __init__(self, posX, posY):
        self.posX = posX
        self.posY = posY
        self.sprite = (0, 96, 0, 16, 16)
        self.estadosubiendo = False
        self.estadosalto = False
        # Atributos para el salto
        self.velocidadsalto = 0
        self.posInicialY = 0

    @property
    def posX(self):
        return self.__posX

    @posX.setter
    def posX(self, posX):
        '''Evita que mario se salga de la pantalla'''
        if 0<=posX<=240:
            self.__posX = posX

    @property
    def posY(self):
        return self.__posY

    @posY.setter
    def posY(self, posY):
        '''Evita que mario se salga de la pantalla'''
        if 0<=posY<=240:
            self.__posY = posY

    def rightX(self, x):
        self.sprite = (0, 96, 0, 16, 16)
        self.posX += x

    def leftX(self, x):
        self.sprite = (0, 80, 0, 16, 15)
        self.posX -= x

    def upY(self, y):
        self.posY -= y

    def downY(self, y):
        self.posY += y

    def gravedad(self, posXplataforma, posYplataforma, widthPlataforma):
        if self.posX+8 in range(posXplataforma, posXplataforma+widthPlataforma) and self.posY in range(posYplataforma-46, posYplataforma-5):
            if self.posY < posYplataforma-16:
                self.downY(2)
            if self.posY > posYplataforma-16:
                self.upY(2)
